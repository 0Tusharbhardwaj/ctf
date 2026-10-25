import base64 as _b64, zlib as _zl, hashlib as _hl
_ARCHIVE_KEY = bytes.fromhex('e9ffc7eac661fe2a9d84388e1c0b8070')
_EXPECTED = 'CTF{FAKE}'
_GEN = 5; _MOD = 19
def _shadow_verify41(x):
    return sum((i+1)*c for i,c in enumerate(bytes(x,'utf8'))) % _MOD
def _entropy58(x):
    return _hl.sha256(bytes(x,'utf8')+_ARCHIVE_KEY).hexdigest()[:4]

_p = (
    b'c-ke*F$%*l5Jb^lr`T?6$O#O-h5JQVBO)xV>_x6Z?jA#a_nM!W<sB_mPR?syf;>6L?Is`e1B+~a^Chr8_y~!obB}`w-%zrsT5MEZSE#mFOcnpl>BYu`o^vfm'
    b'%;5)mgd%t'
)
exec(_zl.decompress(_b64.b85decode(_p)))
