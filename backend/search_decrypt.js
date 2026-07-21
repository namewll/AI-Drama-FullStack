function get_param(query,pn,pc){
    const timestamp=(new Date).toISOString().replace(/\.\d{3}Z/, "Z")

    function genUUID4() {
        var e = Math.random
          , p = "0000000"
          , t = 4294967296
          , a = (e() * t >>> 0).toString(16)
          , b = ((e() * t & 4294922239 | 16384) >>> 0).toString(16)
          , n = ((e() * t & 3221225471 | 2147483648) >>> 0).toString(16)
          , r = (e() * t >>> 0).toString(16);
        return a.length < 8 && (a = (p + a).slice(-8)),
        b.length < 8 && (b = (p + b).slice(-8)),
        n.length < 8 && (n = (p + n).slice(-8)),
        r.length < 8 && (r = (p + r).slice(-8)),
        [a, b.slice(0, 4), b.slice(4), n.slice(0, 4), n.slice(4) + r].join("-")
    }
    const signNonce=genUUID4().replaceAll("-", "")

    var r = 0
    var o = 8;
    function f(a, b, t, e, n, s, r) {
        return d(b & e | t & ~e, a, b, n, s, r)
    }
    function m(a, b, t, e, n, s, r) {
        return d(b ^ t ^ e, a, b, n, s, r)
    }
    function v(a, b, t, e, n, s, r) {
        return d(t ^ (b | ~e), a, b, n, s, r)
    }
    function y_(t, e) {
        var n = (65535 & t) + (65535 & e);
        return (t >> 16) + (e >> 16) + (n >> 16) << 16 | 65535 & n
    }
    function d(q, a, b, t, s, e) {
        return y_((n = y_(y_(a, q), y_(t, e))) << (r = s) | n >>> 32 - r, b);
        var n, r
    }
    function h(a, b, t, e, n, s, r) {
        return d(b & t | ~b & e, a, b, n, s, r)
    }
    function O(t) {
        for (var e = r ? "0123456789ABCDEF" : "0123456789abcdef", n = "", i = 0; i < 4 * t.length; i++)
            n += e.charAt(t[i >> 2] >> i % 4 * o + 4 & 15) + e.charAt(t[i >> 2] >> i % 4 * o & 15);
        return n
    }
    function w(t) {
        for (var e = Array(), mask = (1 << o) - 1, i = 0; i < t.length * o; i += o)
            e[i >> 5] |= (t.charCodeAt(i / o) & mask) << i % 32;
        return e
    }
    function l(t, e) {
        t[e >> 5] |= 128 << e % 32,
        t[14 + (e + 64 >>> 9 << 4)] = e;
        for (var a = 1732584193, b = -271733879, n = -1732584194, r = 271733878, i = 0; i < t.length; i += 16) {
            var o = a
              , c = b
              , l = n
              , d = r;
            a = h(a, b, n, r, t[i + 0], 7, -680876936),
            r = h(r, a, b, n, t[i + 1], 12, -389564586),
            n = h(n, r, a, b, t[i + 2], 17, 606105819),
            b = h(b, n, r, a, t[i + 3], 22, -1044525330),
            a = h(a, b, n, r, t[i + 4], 7, -176418897),
            r = h(r, a, b, n, t[i + 5], 12, 1200080426),
            n = h(n, r, a, b, t[i + 6], 17, -1473231341),
            b = h(b, n, r, a, t[i + 7], 22, -45705983),
            a = h(a, b, n, r, t[i + 8], 7, 1770035416),
            r = h(r, a, b, n, t[i + 9], 12, -1958414417),
            n = h(n, r, a, b, t[i + 10], 17, -42063),
            b = h(b, n, r, a, t[i + 11], 22, -1990404162),
            a = h(a, b, n, r, t[i + 12], 7, 1804603682),
            r = h(r, a, b, n, t[i + 13], 12, -40341101),
            n = h(n, r, a, b, t[i + 14], 17, -1502002290),
            a = f(a, b = h(b, n, r, a, t[i + 15], 22, 1236535329), n, r, t[i + 1], 5, -165796510),
            r = f(r, a, b, n, t[i + 6], 9, -1069501632),
            n = f(n, r, a, b, t[i + 11], 14, 643717713),
            b = f(b, n, r, a, t[i + 0], 20, -373897302),
            a = f(a, b, n, r, t[i + 5], 5, -701558691),
            r = f(r, a, b, n, t[i + 10], 9, 38016083),
            n = f(n, r, a, b, t[i + 15], 14, -660478335),
            b = f(b, n, r, a, t[i + 4], 20, -405537848),
            a = f(a, b, n, r, t[i + 9], 5, 568446438),
            r = f(r, a, b, n, t[i + 14], 9, -1019803690),
            n = f(n, r, a, b, t[i + 3], 14, -187363961),
            b = f(b, n, r, a, t[i + 8], 20, 1163531501),
            a = f(a, b, n, r, t[i + 13], 5, -1444681467),
            r = f(r, a, b, n, t[i + 2], 9, -51403784),
            n = f(n, r, a, b, t[i + 7], 14, 1735328473),
            a = m(a, b = f(b, n, r, a, t[i + 12], 20, -1926607734), n, r, t[i + 5], 4, -378558),
            r = m(r, a, b, n, t[i + 8], 11, -2022574463),
            n = m(n, r, a, b, t[i + 11], 16, 1839030562),
            b = m(b, n, r, a, t[i + 14], 23, -35309556),
            a = m(a, b, n, r, t[i + 1], 4, -1530992060),
            r = m(r, a, b, n, t[i + 4], 11, 1272893353),
            n = m(n, r, a, b, t[i + 7], 16, -155497632),
            b = m(b, n, r, a, t[i + 10], 23, -1094730640),
            a = m(a, b, n, r, t[i + 13], 4, 681279174),
            r = m(r, a, b, n, t[i + 0], 11, -358537222),
            n = m(n, r, a, b, t[i + 3], 16, -722521979),
            b = m(b, n, r, a, t[i + 6], 23, 76029189),
            a = m(a, b, n, r, t[i + 9], 4, -640364487),
            r = m(r, a, b, n, t[i + 12], 11, -421815835),
            n = m(n, r, a, b, t[i + 15], 16, 530742520),
            a = v(a, b = m(b, n, r, a, t[i + 2], 23, -995338651), n, r, t[i + 0], 6, -198630844),
            r = v(r, a, b, n, t[i + 7], 10, 1126891415),
            n = v(n, r, a, b, t[i + 14], 15, -1416354905),
            b = v(b, n, r, a, t[i + 5], 21, -57434055),
            a = v(a, b, n, r, t[i + 12], 6, 1700485571),
            r = v(r, a, b, n, t[i + 3], 10, -1894986606),
            n = v(n, r, a, b, t[i + 10], 15, -1051523),
            b = v(b, n, r, a, t[i + 1], 21, -2054922799),
            a = v(a, b, n, r, t[i + 8], 6, 1873313359),
            r = v(r, a, b, n, t[i + 15], 10, -30611744),
            n = v(n, r, a, b, t[i + 6], 15, -1560198380),
            b = v(b, n, r, a, t[i + 13], 21, 1309151649),
            a = v(a, b, n, r, t[i + 4], 6, -145523070),
            r = v(r, a, b, n, t[i + 11], 10, -1120210379),
            n = v(n, r, a, b, t[i + 2], 15, 718787259),
            b = v(b, n, r, a, t[i + 9], 21, -343485551),
            a = y_(a, o),
            b = y_(b, c),
            n = y_(n, l),
            r = y_(r, d)
        }
        return Array(a, b, n, r)
    }
    function c(s) {
        return O(l(w(s), s.length * o))
    }

    var l_e=`_support=10000000&allowedRC=1&corr=1&did=70ae7094-37cb-4741-84aa-943fa13dca36&pc=${pc}&pn=${pn}&q=${encodeURIComponent(query)}&signNonce=${signNonce}&signVersion=1&src=mgtv&timestamp=${timestamp}`
    var l_y='xHAa3YZflWLogZUOzl'
    var l_n = "".concat(l_y).concat(l_e).concat(l_y)
    const signature=c(l_n)
    console.log(l_n)
    return [timestamp,signNonce,signature]
}

result=get_param("家",'1',"10")
console.log(result)
