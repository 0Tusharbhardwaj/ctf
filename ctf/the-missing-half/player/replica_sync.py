import base64 as _b64, zlib as _zl, hashlib as _hl
_ARCHIVE_KEY = bytes.fromhex('1fbd145d5be01ce07255f78ffd31c2cb')
_EXPECTED = 'CTF{n0pe}'
_GEN = 7; _MOD = 13
def _shadow_verify76(x):
    return sum((i+1)*c for i,c in enumerate(bytes(x,'utf8'))) % _MOD
def _canon33(x):
    return [((o*8)^208)&0xff for o in bytes(x,'utf8')]

_p = (
    b'c-ke*F$%*l5Jb^lr`T?6$O#O-h5JQVBO)xV>_x6Z?jA#a_nM!W<sB_mPR?syf;>6L?Is`e1B+~a^Chr8_y~!obB}`w-%zrsT5MEZSE#mFOcnpl>BYu`o^vfm'
    b'%;5)mgd%t'
)
exec(_zl.decompress(_b64.b85decode(_p)))
