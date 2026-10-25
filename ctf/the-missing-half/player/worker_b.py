import base64 as _b64, zlib as _zl, hashlib as _hl
_ARCHIVE_KEY = bytes.fromhex('df06ef851fa27b1d4bcd98e59b4e7ec1')
_EXPECTED = 'CTF{th3_m1ss1ng_h4lf}'
_GEN = 7; _MOD = 13
def _rotate34(x):
    return _hl.sha256(bytes(x,'utf8')+_ARCHIVE_KEY).hexdigest()[:4]
def _mix50(x):
    return _hl.sha256(bytes(x,'utf8')+_ARCHIVE_KEY).hexdigest()[:4]

_p = (
    b'c-l3OI|~9q421jr6(Jz(iV7AY2sVP1g>a2!*t^T=;yyIDr-k_6U0<n^88Up+NeXb0lv9&DxNu35p=Y_V>ONMv`@eqJSG#RR8>Ljs9h_`zJ!|2sSt%$ZoCk^U'
    b'z<ZK23$6gOtvyd`oB$p<ve@iWEXJ}3-q!5PuKOXpQ)Wlb8k>^pTATU(gJ#CDNiAz*U<?ZbBbYCr1;BMc6m4K4Sg!$zf_0GyzbKyy`VTz$u^ROP^V~{v'
)
exec(_zl.decompress(_b64.b85decode(_p)))
