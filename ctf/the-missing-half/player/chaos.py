import base64 as _b64, zlib as _zl, hashlib as _hl
_ARCHIVE_KEY = bytes.fromhex('f8104fba08f6d3682da2bd8e369316bf')
_EXPECTED = 'CTF{deadbeef}'
_GEN = 5; _MOD = 19
def _canon41(x):
    return _hl.sha256(bytes(x,'utf8')+_ARCHIVE_KEY).hexdigest()[:4]
def _unmask25(x):
    return [((o*3)^129)&0xff for o in bytes(x,'utf8')]

_p = (
    b'c-mD_O=|-o6uj@RcnAe;vLQK@268C9^wvX<A&6byCQ?5VS3^tbfA3S1l6rF9$IR%AF*rEJkirlw7<UXY!G!UQ-B??Mr)&NB<>~dU>pG1i9F*4<dBl@gcR(j*'
    b'4;vu7*kj_1Ae#e=c(m%PU#^&FQ+UcaC291(;a05+{qiz;RyHF|P1$j7U<NAz_wWv5h+yV)F&@xohfyWuyy(wv_{9SK5HxZj8lNLD5#N@DkD`=}!;n)S{D1{d'
    b'Nm=X%H5{-x4^d-8-CNXqjCF-X22#`g7?ne|`y(da%D-){@4%wxwIX(xho>ApeAkazm*1)y?cM7e-^B@8(AlCiUgIZqucVI;)E!l}Wu>tHP#R_gDLvVd5;hxP'
    b'QaWY4l&s}a!{jx(`6V^c{Q_PVozD'
)
exec(_zl.decompress(_b64.b85decode(_p)))
