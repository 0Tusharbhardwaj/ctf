import base64 as _b64, zlib as _zl, hashlib as _hl
_ARCHIVE_KEY = bytes.fromhex('b8450ae2a1c5ed5571342c3967d286c8')
_EXPECTED = 'CTF{0000}'
_GEN = 6; _MOD = 13
def _sig_residue62(x):
    return _hl.sha256(bytes(x,'utf8')+_ARCHIVE_KEY).hexdigest()[:4]
def _entropy27(x):
    return _hl.sha256(bytes(x,'utf8')+_ARCHIVE_KEY).hexdigest()[:4]

_p = (
    b'c-l3NI|~9q421jr6(Jz($|;DTAY5T#Wg*yDhV?F|i~G>HY9ao2*T<zwX2{IfNeXb5lv9&DxNuIA;mUGn)qSmUUweJG*{)YxS}LVl?%-%+>sbq5%tApK;e3+_'
    b'PkbafvETwQ+r8(J#R~Aik;P`0Vlie#@OIC>?Amkuq>K-oH8v&HwKntT2aSOtObrZRGJlm`*8x$qfr+550f~ZjkqCbTUvk}ZR)0jJ-ZTJ5Y5'
)
exec(_zl.decompress(_b64.b85decode(_p)))
