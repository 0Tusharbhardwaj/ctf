import base64 as _b64, zlib as _zl, hashlib as _hl
_ARCHIVE_KEY = bytes.fromhex('283fefc63f0cd0e873a0000c6d07ef7b')
_EXPECTED = 'CTF{FAKE}'
_GEN = 5; _MOD = 19
def _entropy47(x):
    return [((o*2)^107)&0xff for o in bytes(x,'utf8')]
def _derive_key33(x):
    return [((o*6)^31)&0xff for o in bytes(x,'utf8')]

_p = (
    b'c-nnc-*e(N5PtVxp}H@2%bAdCnl>p<Ii_WL7czl+x?w!RUO<g3X(Sm!Z|;BZO0ta!^x$FjV|TUt?YHY6e;C$A4_8bKLF|Y+*sT=rqd1P|mTF6=D2b^R=p8da'
    b'>=p=@1?6P+{P5TG12OKR08+`a=3p|ki&&*3T1wNd4BH6GyPYgvz;?TOrL-)-9JLSK(y|Jo=y^6<kTLqp6t&x|WLnS)l6Fs5#>phl*Nj7+r)l(Q_Tlr#$sCQo'
    b'#2Sp`JJ6Xr!~+r+Tj~t`dZp#d@q!jxXx4kF@gk>w8<FF$y;(Ji283k-c(W~`kcVc?q1<%NH`KzO`m1I1G<#n7*haUbtI>cs@ji&_AbttrCWv2yxDDdBAb$5^'
    b'G+IW*mhn=9a2}UY6qT?h#!8j^l&5z-__fr;flQbn8W0NuWzw28I_}5TUM*9S^CTtAkVh%tt`9&^u%Ig@FsCFvd!Y4uG_(3}!N;C5o45kY+K#W&P61vEP<>ux'
    b'i=Z@lRZK&9!PN_M@%nR39Zly4W1*V7;tN-414%`hNSb6ZQ6X)|D0pSYnvPKaNYr$s!@?n0Y|TKwE2M@v?SXan(y6XPuVTh9vAM@C0kWzQ7X-*yT^E)~VH{dn'
    b'Hk5ip1^XBDa6bF^c`=<mW>p!7bWWhdTvvcq4h@tAk))^h8Fq4+B=P9_HoL<A2<dl~zEvu?G;Q%3z-RM`)>ubs+{t(HT*qMoEFPYkPz<4%a4qPLGEP?<?#Ng4'
    b'@vTWBw0{;v((LBbKc|m~uw&}?)fSWIPklW{wlHoSfK96(<8AquQKbN(=n?5j;z{xa2Mm@RirTtZ2joKCga33nAjQ5MyR!zu5@^Y><FO2myICcXNK&u@`{ieH'
    b'<8|D#Saw$_tdH;ZV7$lBpu2XH^~}c~-3!Nze0RBVi0Rr|aYz~$>1i*V^_hQ@*=@_1LId_}UPvLpQ}7K>+#~6Lv`vYJ>AAyRhM9&+?l2r@ccOU8sdFca;=J#V'
    b'o#60IJ`Nni0aSt!-W&_yCY=hf^e2vY)Ei!|#oYi~wmt7{oz>gd{J0GMm1Y8ax%s>Wrkk2sz{yF=1EH35klpzSd`}*%=I<VemEI8ox#qRmju*Oy3vC=&;4c3+'
    b'-O(wU7&;Y)<Wg?uC|oF6lT*_)IPENy_dZtTi0IREQDa<V*Br){pmloYrw3D0;J@Lpl2n&dfu96jD|?1%6k+sv?!MT0PR3&r=eZljc^(JdFqfnM0QC-p)c'
)
exec(_zl.decompress(_b64.b85decode(_p)))
