from Crypto.Util.number import *

n = 6490672189669430139114400786639333113650863732867815870606429370427099270227279738621589688223906197984721050486808591335490904404708174060116995977172122744460471805992518748917458226955524540237932402641647003072967853690526802275763600822169949032898673059477956586679175750328326608487545472403485431842687069411360858447980824464846552029823027658153109603505927067997232658765046181792839482838747203015105578831560635141846083676999069506691341363144465152996781602519993854582114553772270645162223051976390709976226421674266080734282790735536176932147926033789899985746704438891457144721057499029728013950686558919045192440299550355180521630731621644764407723183455736956821000476348607391325607851381514678069136610463215355032315833961683505726678516384810551589932978265877187138442428038640188914148491356160605455931519000654709091120837030070429980847939962962915065508458189078969747731733872071093977269066386242385009484833506582710801474603907510475403485732685616153994238718492334522458390256147418360932132889124937980403947289259190786522850337546825910672776549972462165852751037458701942824922836698639638682404956746307912188751518185110232176447839748903241694003725697240785025556789151670788141524061477173543645035165242661533764047899523140748529241789683722473463399278420513436952710083313387746122250694915900625104923330888457927487558322591397859481
e = 65537
c = 930825889684924069599267757740040740503282520283641409082718703898328834671510392580769138993840235976996770373031510784259953541296295025763818867118966635625160291186496694985960889902069900975788689691985613193385446409978542298611011381381360238009518594126156995112007756492954274106277027584463666508879447915171190156836949024457456697420916790055350000516253893306018365705236620853048820805193968710920339336953017129602687728897846950913765756773749378584861570199437424313026266069656985749071847644284395220688076419295728780301169726347451537522184329536307092540638757809990363433710907440726960207793201916848408935749339676635486446389512302213832664181211585948507052559170619997598580427139653726565958349337443928033310555431825851948137323782552616090286745520009126318713868484320108553177106360190798106111251447099749695266323077184750989629537669326491750242433986931757068648289461301534281559150434081711339539484692510176119115990079798875029889516783060855544166127943811612333867899784202401636798835172100901394458502476089524816978443450475062474835987316252148116590825897736290334289503519971357817551180337132284280899016347741715669507277806033927928522953243748214931952169660735807327728651006482106187204474455172589565863378471689385527507036246009864289291467599713677133831406440486426913366648785361970582036416604100085147772642269526807060
L = 2
R = 2 ** 768 - 1


def binary_search(n, L, R):
    while L < R:
        x = (L + R) // 2
        p = x ** 2 - x + 1
        q = x ** 4 - x ** 3 + x ** 2 - x + 1
        if p * q < n:
            L = x + 1
        elif p * q > n:
            R = x - 1
        else:
            return x
    return -1

x = binary_search(n, L, R)
p = x ** 2 - x + 1
q = x ** 4 - x ** 3 + x ** 2 - x + 1
phi = (p - 1) * (q - 1)
d = inverse(e, phi)

print("Flag: " + long_to_bytes(pow(c, d, n)).decode())
