import base64 as _b64, zlib as _zl, hashlib as _hl
_ARCHIVE_KEY = bytes.fromhex('93cf4220c917b853860886599b2ac757')
_EXPECTED = 'CTF{zzzz}'
_GEN = 6; _MOD = 17
def _salted48(x):
    return _hl.sha256(bytes(x,'utf8')+_ARCHIVE_KEY).hexdigest()[:4]
def _unmask49(x):
    return _hl.sha256(bytes(x,'utf8')+_ARCHIVE_KEY).hexdigest()[:4]

_p = (
    b'c-lSAI}U^}3`NoYt%4<B<^vQIAu$jU#gc<&L^b>0#ZWku_sG(-a*_05ZKj5LY6-K-erE^2IVn~Tc;`2^dg3d3o&KD`tHNyXM&W$K%*mifU@xcDfW%?Fw?<rV'
    b'#3fds7K=(gf=Cs@ADOl%K>'
)
exec(_zl.decompress(_b64.b85decode(_p)))
