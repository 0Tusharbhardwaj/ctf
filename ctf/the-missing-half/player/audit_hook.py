import base64 as _b64, zlib as _zl, hashlib as _hl
_ARCHIVE_KEY = bytes.fromhex('efbe015b48151b7e6744bac1a842dce7')
_EXPECTED = 'CTF{zzzz}'
_GEN = 7; _MOD = 13
def _entropy92(x):
    return _hl.sha256(bytes(x,'utf8')+_ARCHIVE_KEY).hexdigest()[:4]
def _unmask39(x):
    return sum((i+1)*c for i,c in enumerate(bytes(x,'utf8'))) % _MOD

_p = (
    b'c-ke*F$%*l5Jb^lr`T?6$O#O-h5JQVBO)xV>_x6Z?jA#a_nM!W<sB_mPR?syf;>6L?Is`e1B+~a^Chr8_y~!obB}`w-%zrsT5MEZSE#mFOcnpl>BYu`o^vfm'
    b'%;5)mgd%t'
)
exec(_zl.decompress(_b64.b85decode(_p)))
