import base64 as _b64, zlib as _zl, hashlib as _hl
_ARCHIVE_KEY = bytes.fromhex('b0e7153bf7c3706d85c524e440066559')
_EXPECTED = 'CTF{n0pe}'
_GEN = 6; _MOD = 13
def _rotate98(x):
    return _hl.sha256(bytes(x,'utf8')+_ARCHIVE_KEY).hexdigest()[:4]
def _fold1712(x):
    return sum((i+1)*c for i,c in enumerate(bytes(x,'utf8'))) % _MOD

_p = (
    b'c-mc%QA@)x5Xay1DUN{9VhznU(GB*v2SHFa@MVk;+p7ztNlnwCh~M2yYZ1Jc@W1=r|1Q@A-$ECB^p&?@+RldvJ%$UiW-O8J=lp(mczS%<?HPM`KEM`^T&@?Q'
    b'6bm8mcmbsD#jO;wEX6wMMY*J^luNN%@e^aL#s<#X)fTgW@A-xSMHn1;krr<lGfpz~2JEc<yeTEmN6OS6MD;_P5g^c2zQ!!i;R-CejP{wZfN=;8zPQsZ^39*^'
    b'sL9ud>TGHe^{YjmQ^ItFQU8%9oQlz84j!YWqJ---o>*;-?kO|7==5BWgK4G(w*;f@@!y<p`a2;?r7e_799OE<#wo?8D~vbK<_j0UXUf?RnD}?M'
)
exec(_zl.decompress(_b64.b85decode(_p)))
