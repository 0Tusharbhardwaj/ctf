import base64 as _b64, zlib as _zl, hashlib as _hl
_ARCHIVE_KEY = bytes.fromhex('78892e9ecc387ab8b4585023a0286cce')
_EXPECTED = 'CTF{deadbeef}'
_GEN = 7; _MOD = 13
def _unmask85(x):
    return sum((i+1)*c for i,c in enumerate(bytes(x,'utf8'))) % _MOD
def _entropy75(x):
    return _hl.sha256(bytes(x,'utf8')+_ARCHIVE_KEY).hexdigest()[:4]

_p = (
    b'c-oy-ZI9wM5dO}ua4l6z)DXemRo6x0!@gwO(_M)QoT_StA}1LZ-zITtJM1FFfA2U>LOAH2bbP@c&+9Ye$KiP?q$WZQxLv6#E~Q97sli%`oZv=_L}a8nXX@D_'
    b'3gi}=a}=uf(0Q1Lv*mpl&OLHF4?hL?e|K~DN8ph~Fk60{1)n`~AKZoic;s_%|2v)!$ocQ@aE_+Yjn}Sj-N9fUhD$QVO#PDSjh}K^upFFr&thf%ohVxK45G+&'
    b'2Y2B-=vjOfyl{*ckI*ehzUCl@iI70i`yhoisiiw7VMWSQroo-m*=f0(bZM68@raQxtHOCSfjrWgtvsUPRZo|)0wXSUB_R@(E~{3kc@8L;j@{0&1XL@?p0Xr?'
    b'QbS57r1Y&c5h;-Al#F_**T+hy=m!5JFCCW%NvNraR0Z2Ip0PLsdZ<IdtMN*la1lr;q}MNEX|oAlOD-XGCvWETz%m7=d0dKV5#1mr88{ODZM-HT&ryaTqRf8+'
    b'?a)R<(dP!Tl3GX**uD~Oje>+SW4qyK+-mU?SGcG^=~{C*{?I7#^)c*}P%TQ4iKiXCP-iaEDg%WzJ)$!uGOW^gi=}wBt7OB3suwKTfLXi<iDyIBTgUX`Tz5aJ'
    b'pwPU4%-E!mh@DwvkUrTUr{jr&CmgF6wxg?azq9~t!kRv0LX<H}o`<5yYL|-VRfe`{#7kS%`1;Bp`By%ogXiPx-~3<4{&+O<ug(5y^bSwQ<9Gi1_jGl*1RpO{'
    b'35mXd-brdy;zR+4M8a@dF4)(7oS5d;&9vQ`m^L2V)6yDzt$o8G`|p@+fMt5q*c=IGPoJOw$ut)x_=ht)+W~9Vu+#TK*+xgKu{tu=o_0K7OuHfPgjhIr59EIw'
    b'#-|Q%f81d+P1apQwr`bnvDruxIq&zn3wv^dPjl%FhN?1+nrFn?sUY-RVP8;*rb9}8A;@Kps`8_<4>kWeu1kI<IH{x2w-Fv`>n7qUU7@dbf2P=$Z<G*#v-3h|'
    b'y#A{?9WxcgAkp4dvSk@s6NYTZ(k)j)?&!DIz<Rm_CerN|dRQ`##Badp9ZwXdVi~fB?iTI0@ey5y7R@s5Yh^V@GV;?D!<k&R?D0tGD=UioqH|uXQ#b5iyECN4'
    b'6+&WYpz(~dHJ9~ZnZ(+ZaTj0UEDMsMtXVi4ewlsz>q{^T77P41_%oa>mh+osa8C_@Hh;i3rv^~0F{!V}KbXzMiLIZI3(Vf=SQ6}>0Po0WUN`Mt+p0@!3$H9M'
    b'GjkO?pQenXY5%s;yXC{)OzeRkY_?rKU|wOPQWejIcqvHl8T_GK&6A5*M3MO{ilQ2fD9RZxqNo9+{%q@iquJ-#9sCD&Iqkg'
)
exec(_zl.decompress(_b64.b85decode(_p)))
