import base64 as _b64, zlib as _zl, hashlib as _hl
_ARCHIVE_KEY = bytes.fromhex('4bf20f876ffc474c0251908fcdce4b31')
_EXPECTED = 'CTF{zzzz}'
_GEN = 5; _MOD = 17
def _fold1796(x):
    return [((o*8)^200)&0xff for o in bytes(x,'utf8')]
def _fold1763(x):
    return _hl.sha256(bytes(x,'utf8')+_ARCHIVE_KEY).hexdigest()[:4]

_p = (
    b'c-oCrO^@0z5WVv&Mm{;(Gy=9uRa6dDmrGj}X`#1Dk>d=T6l15hvlOBI?`u2ZBMV442PfnCcr)+CgpfrkxA1*F`}IMT5)D*ZS;dtAQ!tG=WLvNWf>4|Z-~|%`'
    b'<uk%s<+VVQ5JGz8x>DN0U!&yy-6+07+w1jmTmmyI>a8(UY%3JYW3c5KRc$AOq#uoY;Fe|^m;m)jlDuA5h8~;^R!lRiw3$#6lNiXDL=oHp`6Ee`pyVn?8ih2Q'
    b'(iUy?gll9LQ?8^$Zc8O8C4=For0<@AOXD#`M=b3gIlLi5gUc`fl^C?G2i<$VcaXUo4|Sa!PjY6N>nn3(+M6~-DG;Qx;n2a)jYmzh(9W@{U%aU0%EgBQ8u<(T'
    b'*#A6=IzHtxBnz(HXumQygjL5HAl*%xfM)h+Yb^tTi66P40a=dCV562tgZc$qCY>5Y#`vnm8;*1f)Q!H`T27inKR|C*m8GrMeD*V)&%XVbE@C*C(x>U~`Sk1K'
    b'<5LWSPJ*nI`6UWFPNFmxCA}Xu)=HPs(j{rkrF@1%_;}}|UtN}^s7*0h=o(uQ1%~|hah_g9F{Hl5rV!&Ct9^?H>3O$z6gtbPc!o~$9S5to=d@kW&29PtCUbEA'
    b'XrM5HFEDy|xF4MtI8|4Gctu^esqDJiuB+~JY5eDKToWKD4P^I9q6=}R7S^}W>XEuk=WZ<r&Hs6N$29ThcS$z|{`XYFG;Ho3@i&CCjc>2BBdE2~WDIs&A$7q~'
    b'lBSZaF->1Dm45>~bC2}'
)
exec(_zl.decompress(_b64.b85decode(_p)))
