import base64 as _b64, zlib as _zl, hashlib as _hl
_ARCHIVE_KEY = bytes.fromhex('bc4612476c0efecf6c2f708dfc3832cc')
_EXPECTED = 'CTF{zzzz}'
_GEN = 5; _MOD = 19
def _canon40(x):
    return [((o*3)^128)&0xff for o in bytes(x,'utf8')]
def _salted36(x):
    return sum((i+1)*c for i,c in enumerate(bytes(x,'utf8'))) % _MOD

_p = (
    b'c-m!9%WA_g5WMRvhJ}Ju+>n-*fWd_l3dy0T^e#lab_}+ZN^&oy|K7EdoVtf)AH(d<bTLdg$B@G@j2NbKh#86FH><9!q))f`_HDa+S4y?q;pBWfvX1;^Y6Xcn'
    b'v}hpxs^_dpikVZU3KSpKWD3UhEEt{UNeg_%{uo-;#^4?sgF8GwUZ^<F(c_0wc6m-zgLeB*!q63lS3Ir3V`9+9{%}}M$XHO4t3q%K>e+L2c?e$CFaHTP%X`;P'
    b'>qWw^$P<*c-c4*Rng(R;<OXjoU4#~Qbn&9P+F;ZlXl`F6'
)
exec(_zl.decompress(_b64.b85decode(_p)))
