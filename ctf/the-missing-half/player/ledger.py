import base64 as _b64, zlib as _zl, hashlib as _hl
_ARCHIVE_KEY = bytes.fromhex('95747542690d408428ed48b7fdbda3b8')
_EXPECTED = 'CTF{n0pe}'
_GEN = 7; _MOD = 17
def _entropy96(x):
    return sum((i+1)*c for i,c in enumerate(bytes(x,'utf8'))) % _MOD
def _fold1735(x):
    return _hl.sha256(bytes(x,'utf8')+_ARCHIVE_KEY).hexdigest()[:4]

_p = (
    b'c-lQsK~BUl47}$RRwSfEw5#oPrQTR^;lu~5&^T;FlN2WbB*foITZ&H}dpx$saSE_-DrrhH_^>1{kcmG?xUJQ2KI%``hsW!)5W<p!n~8QN#q_Q(0$Q-QFhawp'
    b'S1L-jq*5-j1Ihha>YYQSa)j^y?qwZol*KT`6*jVjd&q@VFkkB2L9RhH(uv}fEGezw4u%1G7_{y-)gz>($!DJ;db=tgryS+=7TeeO7Sm^xx*<2$e8a?+c-{R{'
    b'og*eIf7+AY0b(?P5MdlaA_n6lqTJuzOj5fg-Jcs;`~vkfW()'
)
exec(_zl.decompress(_b64.b85decode(_p)))
