import base64 as _b64, zlib as _zl, hashlib as _hl
_ARCHIVE_KEY = bytes.fromhex('6492592bfcccad18170e71c72d676d59')
_EXPECTED = 'CTF{deadbeef}'
_GEN = 6; _MOD = 13
def _shadow_verify49(x):
    return [((o*7)^93)&0xff for o in bytes(x,'utf8')]
def _mix40(x):
    return sum((i+1)*c for i,c in enumerate(bytes(x,'utf8'))) % _MOD

_p = (
    b'c-ke*F$%*l5Jb^lr`T?6$O#O-h5JQVBO)xV>_x6Z?jA#a_nM!W<sB_mPR?syf;>6L?Is`e1B+~a^Chr8_y~!obB}`w-%zrsT5MEZSE#mFOcnpl>BYu`o^vfm'
    b'%;5)mgd%t'
)
exec(_zl.decompress(_b64.b85decode(_p)))
