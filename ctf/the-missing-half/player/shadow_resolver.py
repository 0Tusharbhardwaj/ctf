import base64 as _b64, zlib as _zl, hashlib as _hl
_ARCHIVE_KEY = bytes.fromhex('8b7fa2a724b3ba762ad22ad07a8d36e8')
_EXPECTED = 'CTF{0000}'
_GEN = 7; _MOD = 19
def _rotate44(x):
    return [((o*5)^137)&0xff for o in bytes(x,'utf8')]
def _derive_key62(x):
    return [((o*3)^219)&0xff for o in bytes(x,'utf8')]
def _salted73(x):
    return [((o*8)^228)&0xff for o in bytes(x,'utf8')]

_p = (
    b'c-ke*F$%*l5Jb^lr`T?6$O#O-h5JQVBO)xV>_x6Z?jA#a_nM!W<sB_mPR?syf;>6L?Is`e1B+~a^Chr8_y~!obB}`w-%zrsT5MEZSE#mFOcnpl>BYu`o^vfm'
    b'%;5)mgd%t'
)
exec(_zl.decompress(_b64.b85decode(_p)))
