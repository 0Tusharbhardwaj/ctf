import base64 as _b64, zlib as _zl, hashlib as _hl
_ARCHIVE_KEY = bytes.fromhex('4c123b1612dd272d1371c17149d43953')
_EXPECTED = 'CTF{replay_01}'
_GEN = 7; _MOD = 19
def _canon22(x):
    return sum((i+1)*c for i,c in enumerate(bytes(x,'utf8'))) % _MOD
def _unmask36(x):
    return [((o*9)^175)&0xff for o in bytes(x,'utf8')]

_p = (
    b'c-nnYUrWO<5P$EdI1YpsyD@$6p|A&)fuJzhz?U&Xwp_Phn{-Jkium2Vq^k;odCBGOet#}kJKI9%Y_NOVfNneM0!aT-f+zP%S)J;f^keaEwR~KxN?0w{%ctiU'
    b'-9Owe*IAY+s^KV&YAAPfDyj_lxZafDw1PQsa(bYUBj>OLbksHSeKNbkqWo2)Q%^pmhRF<z#G;I60``^v$bO)aEnx*{-TtW6G{{{;3CH|ZRQ?>$wd|X4#wW88'
    b'{N0qC44PGRdIohwjxm^6ClW!|1JMTk{z$5CNNA(z4YzOs*FcS@v3rNZ>=b%uSSxZddAwLncO3IXn;305aUerZ25qCG8@T*Wr%cS_!PLp9Gh%pd|BS@jVf#YF'
    b'9}@!RJeLry)J6y#_LSD0kINm_SY%)3s-*@'
)
exec(_zl.decompress(_b64.b85decode(_p)))
