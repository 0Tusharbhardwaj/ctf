import base64 as _b64, zlib as _zl, hashlib as _hl
_ARCHIVE_KEY = bytes.fromhex('22b598615dcbe810beacd557705a54b5')
_EXPECTED = 'CTF{th3_m1ss1ng_h4lf}'
_GEN = 6; _MOD = 17
def _unmask55(x):
    return _hl.sha256(bytes(x,'utf8')+_ARCHIVE_KEY).hexdigest()[:4]
def _rotate61(x):
    return [((o*9)^168)&0xff for o in bytes(x,'utf8')]
def _mix72(x):
    return _hl.sha256(bytes(x,'utf8')+_ARCHIVE_KEY).hexdigest()[:4]

_p = (
    b'c-oCq$!^;)5WVXwrtC!m9J@(wg6&Hdw3iBSb2AKq62~<giDbCAG1B~dN0ckuO<;r<f^Rr)-fW*gO@gzNN~#H}Ets9(Xmy>))@bYDm(wa)Tit@O+Ur_3u(xpc'
    b'xHr(t{X_2;#rKEXqF5wJB5(~YmnzNj1n3wml}}l*xcU0+7RXn55L(+Y+~~IDO1K=nHoDP2ckl<Kat3P;ON&ndoxhM`MX(E1D?LnWa*%?1oD)dmwg^)`hiTQl'
    b'H`o}uo`Uo&i@|?yWP|Wv1NLIN<L&P7hzfa^%8WvrKuWc(H&V=jWn<^9G%4Mtkv`1^FMO`ic(^O>@2u7Kl&-SK9|uIPL22K|IQ>^sC8P>CfORWKMf|z^vN~qy'
    b'EK)(rVrnB`_}ry<E-sai$X;087n$W9$?N~5vl*~`#Tn2yXi%k5K?ZZUJPkmUOSW$dTMbe#4^pu?;_X}ZLE53OA0Uoxe~0(#JnyJS98%%MahUvib!Ir?_;w31'
    b'7NIpRr42}jd5@ggh?*l%`Po(WW=4u1aYSfwI^;d>H9IT?1jV;pHoR&uhZpjArAbZ_%DyZWZ?P<63Cgltv9e@6VZU$5U&@jhtN'
)
exec(_zl.decompress(_b64.b85decode(_p)))
