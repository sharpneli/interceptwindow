/* dc-lite: a small stand-in for the claude.ai Design canvas runtime, so the
 * .dc.html mockups in this folder open straight from disk in a browser.
 * It supports what these mockups use: {{holes}}, <sc-for>, <sc-if>,
 * <dc-import> (as an iframe), <helmet>, event and ref attributes, and the
 * DCLogic class with setState and the mount/unmount lifecycle.
 * It also serves canvas asset URLs (/_blob/<id>) from dc-data.js.
 * Rendering uses Preact (vendor/preact.min.js, MIT licence), loaded below. */
(function () {
  'use strict';
  var P, h, render, PC;
  document.write('<style>x-dc{display:none!important}</style>');
  document.write('<script src="./vendor/preact.min.js"><\/script>');
  document.write('<script src="./dc-data.js"><\/script>');

  // Canvas assets: /_blob/<id> answered from window.DC_ASSETS when present.
  var realFetch = window.fetch ? window.fetch.bind(window) : null;
  window.fetch = function (u, o) {
    var m = typeof u === 'string' && u.match(/^\/_blob\/([0-9a-f]{32})/);
    if (m && window.DC_ASSETS && window.DC_ASSETS[m[1]] !== undefined) {
      return Promise.resolve(new Response(JSON.stringify(window.DC_ASSETS[m[1]]), { headers: { 'Content-Type': 'application/json' } }));
    }
    return realFetch ? realFetch(u, o) : Promise.reject(new Error('fetch unavailable'));
  };

  function DCLogic(props) { this.props = props || {}; this.state = undefined; }
  DCLogic.prototype.setState = function (o, cb) {
    var next = typeof o === 'function' ? o(this.state || {}, this.props) : o;
    this.state = Object.assign({}, this.state || {}, next);
    this._schedule(); if (cb) Promise.resolve().then(cb);
  };
  DCLogic.prototype.forceUpdate = function () { this._schedule(); };
  DCLogic.prototype._schedule = function () {
    var self = this; if (self._pending || !self.__host) return; self._pending = true;
    Promise.resolve().then(function () { self._pending = false; if (self.__host) self.__host.forceUpdate(); });
  };
  DCLogic.prototype.renderVals = function () { return {}; };
  window.DCLogic = DCLogic;

  var HOLE = /\{\{\s*([^}]+?)\s*\}\}/g, WHOLE = /^\{\{\s*([^}]+?)\s*\}\}$/;
  function lookup(path, scopes) {
    if (path === 'true') return true; if (path === 'false') return false; if (path === 'null') return null;
    if (/^-?\d+(\.\d+)?$/.test(path)) return Number(path);
    if (/^(['"]).*\1$/.test(path)) return path.slice(1, -1);
    var parts = path.split('.'), head = parts[0], v;
    for (var i = scopes.length - 1; i >= 0; i--) { var s = scopes[i]; if (s != null && head in Object(s)) { v = s[head]; break; } }
    for (var k = 1; k < parts.length; k++) { if (v == null) return undefined; v = v[parts[k]]; }
    return v;
  }
  function interp(str, scopes) { return str.replace(HOLE, function (_, p) { var v = lookup(p, scopes); return v == null ? '' : String(v); }); }
  var EVT = { ondoubleclick: 'ondblclick' };
  function propsOf(el, scopes) {
    var props = {}, tag = el.localName, type = (el.getAttribute('type') || 'text').toLowerCase();
    for (var i = 0; i < el.attributes.length; i++) {
      var a = el.attributes[i], name = a.name, raw = a.value;
      if (name.indexOf('hint-') === 0) continue;
      var whole = raw.match(WHOLE), val = whole ? lookup(whole[1], scopes) : interp(raw, scopes);
      var ln = name.toLowerCase();
      if (ln.indexOf('on') === 0 && ln.length > 2) {
        if (ln === 'onchange' && tag === 'input' && type !== 'checkbox' && type !== 'radio') ln = 'oninput';
        props[EVT[ln] || ln] = typeof val === 'function' ? val : undefined; continue;
      }
      if (ln === 'ref') { props.ref = typeof val === 'function' ? val : undefined; continue; }
      if (ln === 'tabindex') { props.tabIndex = val; continue; }
      if (ln === 'checked' || ln === 'disabled' || ln === 'selected') { props[ln] = whole ? !!val : true; continue; }
      if (ln === 'value' && (tag === 'input' || tag === 'textarea')) { props.value = val == null ? '' : val; continue; }
      props[name] = val;
    }
    return props;
  }
  function build(nodes, scopes) {
    var out = [];
    for (var i = 0; i < nodes.length; i++) {
      var n = nodes[i];
      if (n.nodeType === 3) {
        var t = n.nodeValue; if (/^\s*$/.test(t) && t.indexOf('\n') >= 0) continue;
        out.push(interp(t, scopes)); continue;
      }
      if (n.nodeType !== 1) continue;
      var tag = n.localName;
      if (tag === 'helmet' || tag === 'script') continue;
      if (tag === 'sc-for') {
        var list = lookup((n.getAttribute('list') || '').replace(/^\{\{\s*|\s*\}\}$/g, ''), scopes) || [], as = n.getAttribute('as') || 'item';
        for (var j = 0; j < list.length; j++) {
          var sc = {}; sc[as] = list[j]; sc.$index = j;
          var kids = build(n.childNodes, scopes.concat([sc])), item = list[j];
          var key = item && typeof item === 'object' && item.id != null ? item.id : j;
          var els = kids.filter(function (k) { return k && typeof k === 'object'; });
          if (els.length === 1) els[0].key = key;
          out.push.apply(out, kids);
        }
        continue;
      }
      if (tag === 'sc-if') {
        var v = lookup((n.getAttribute('value') || '').replace(/^\{\{\s*|\s*\}\}$/g, ''), scopes);
        if (v) out.push.apply(out, build(n.childNodes, scopes));
        continue;
      }
      if (tag === 'dc-import') {
        var nm = n.getAttribute('name'), qs = [], size = (n.getAttribute('hint-size') || '100%,100%').split(',');
        for (var a = 0; a < n.attributes.length; a++) { var at = n.attributes[a]; if (at.name === 'name' || at.name.indexOf('hint-') === 0) continue; qs.push(encodeURIComponent(at.name) + '=' + encodeURIComponent(interp(at.value, scopes))); }
        out.push(h('iframe', { src: './' + nm + '.dc.html' + (qs.length ? '?' + qs.join('&') : ''), title: nm, style: 'display:block;border:0;width:' + size[0].trim() + ';height:' + (size[1] || size[0]).trim(), key: 'imp-' + nm }));
        continue;
      }
      out.push(h(tag, propsOf(n, scopes), build(n.childNodes, scopes)));
    }
    return out;
  }

  function boot() {
    P = window.preact; h = P.h; render = P.render; PC = P.Component;
    var x = document.querySelector('x-dc'); if (!x) return;
    var helmet = x.querySelector('helmet');
    if (helmet) Array.prototype.slice.call(helmet.children).forEach(function (c) { document.head.appendChild(c.cloneNode(true)); });
    var tpl = Array.prototype.slice.call(x.childNodes).filter(function (n) { return !(n.nodeType === 1 && n.localName === 'helmet'); });
    var sEl = document.querySelector('script[type="text/x-dc"]');
    var Comp = sEl ? new Function('DCLogic', sEl.textContent + '\n;return typeof Component !== "undefined" ? Component : null;')(DCLogic) : null;
    if (!Comp) Comp = DCLogic;
    var props = {};
    new URLSearchParams(location.search).forEach(function (v, k) { if (k === 'fit') return; props[k.replace(/-([a-z])/g, function (_, c) { return c.toUpperCase(); })] = v; });
    function Host(p) { PC.call(this, p); this.inst = new Comp(props); this.inst.props = props; this.inst.__host = this; }
    Host.prototype = Object.create(PC.prototype); Host.prototype.constructor = Host;
    Host.prototype.componentDidMount = function () { if (this.inst.componentDidMount) this.inst.componentDidMount(); };
    Host.prototype.componentWillUnmount = function () { if (this.inst.componentWillUnmount) this.inst.componentWillUnmount(); this.inst.__host = null; };
    Host.prototype.render = function () { var vals = this.inst.renderVals() || {}; var kids = build(tpl, [vals]); return kids.length === 1 ? kids[0] : h(P.Fragment, null, kids); };
    var mount = document.createElement('div'); mount.id = 'dc-root'; document.body.appendChild(mount); x.remove();
    // Standalone and smaller than the design: scale the board to fit the window.
    var pre = sEl && sEl.getAttribute('data-props'), size = null; try { size = JSON.parse(pre || '{}').$preview; } catch (e) { }
    if (window.top === window.self && size && new URLSearchParams(location.search).get('fit') !== '0') {
      var fit = function () { var s = Math.min(1, window.innerWidth / size.width, window.innerHeight / size.height); mount.style.width = size.width + 'px'; mount.style.height = size.height + 'px'; mount.style.transformOrigin = '0 0'; mount.style.transform = 'scale(' + s + ')'; document.body.style.overflow = s < 1 ? 'hidden' : ''; };
      fit(); window.addEventListener('resize', fit);
    }
    render(h(Host, null), mount);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot); else boot();
})();
