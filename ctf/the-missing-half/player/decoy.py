import base64 as _b64, zlib as _zl, hashlib as _hl
_ARCHIVE_KEY = bytes.fromhex('8b4c0bf8e704eb5a6162ac20172de3d4')
_EXPECTED = 'CTF{0000}'
_GEN = 7; _MOD = 17
def _sig_residue81(x):
    return sum((i+1)*c for i,c in enumerate(bytes(x,'utf8'))) % _MOD
def _shadow_verify87(x):
    return [((o*8)^172)&0xff for o in bytes(x,'utf8')]

_p = (
    b'c-lRXL2JV>42AFh6~Zuxp$l0z7%Ak`b=O^X8KoG{mKQ@}wYF1MO8)y?udPmgPvVpHY@iYLff8vNz>Rwf2_l9gGFw_%$D9AQS$}*n#td5Ml{W)c0S{uuAeZjR'
    b'X^hapmajkG&#hkK%ok8Z(=@Ml@r`Kj;%WK(GV@(QIB)Pb1L8DZ!1WKNis#3KF<s`vW5Y#_UX#H}2zY=2eRW+d3L;>df`>EL%9D3m4SaR`+P3g_8KlWuXEF$L'
    b'x2fAUdumEO1(#0Q;>sLdq;TSMKG#{0(yI}rgsuZF<*1yOlK&rG(yB@}i)$=`{Q)yfYYG'
)
exec(_zl.decompress(_b64.b85decode(_p)))
