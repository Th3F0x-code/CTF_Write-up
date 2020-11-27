import gmpy2
from Crypto.Util.number import *

gmpy2.get_context().precision = int(8000)

n = 23606413766185125262715665064098566623392366241549799634536224249606821166508227661740963059390510723969542207420674403866302781734490190584327801883726734032078963903132346089383414812961131951474870457122782912866128207079825120011396670079612200883368880755263795594045770557800307577612649185609143459990250705270899075372732462351203338356687954929562907624387508223669835198161500541223853908304758164434125791065298963775559151746919521768558386507634585806044506359628534349719576557511850094141412958204131051925016158924842149605538033982403051452611258604768375962306349429212807320398845497859144547996527
y = [
    4525378769631249566244977471897300614866560736266259975908397510012737494956566617381502438794014727854889718181911378152998641026929902118170421346949931286522194349443052417574441576358833971754953241812309251772026259915877917090213817244523040289167891599867320580181862721332605390261883096160062124032826906947020479111505769862994328817442655622791326614092270594159299823940068956115680704908939376540075590153580411903703101062677967582828934914868515341773539758028428871167827435637597669409923861761295261613203526142470432108663654597077567466133772066684681016873916660847339562150611606875182092076747,
    10172735311139530699605801066001604371200661094358260342392004380609091599491445007621569572730528007213603532285433070714283212002659767339317913009735445913936839236136136317225848872060024826651469980094298505689620956131817386821110797264073358204216337754890530637685833810019492317120012785929280086664917654155804421781103769012386285484397833314578860517006477753670275972937399848570953454457594300181990814514260868465771475694027441647750408361573878741462372842574791467349786885013303504507258134982535903368406483033869397798769650628468865161839214573530007810862766821126984737250324234847589513058569,
    2227060622231017112810183337871567667710669960386807798108316064846234792846864759847654302635488115451385882008160666716857009943700159083293350411903039563964249756463539812328540527896366502459538825055036253734211485128491340972560832697514492848834194085703098012472707942482910460449741522913386044654154046491053065661530251267448363456369149215363633902843311408750667917053390508638660435885059453366105512987332779316890388243159349290320804371506523364055394589040348799728812357961002300391287402897804354719101619793128058550667388155552628739463459259252191247115431112364476319460584549335194551842079,
    9181198739883924674262577976574080839604033433089422736970738072462688908040351153438466304266985952969750956794586135273753050004215013974417810470681608130130489047507539176804082510852245411368681478259682031096252377598320002363387961411850851931035802345092191610135511904800337822534477599351098742654324305322262337437503115193360343414083931764469122224172424390209847262499640368362531535916015916278036286434131652956971303170132714895420317010320064070889097959403124401509672648853727890286757665544936418429561485912274366845641146542105108156247157759856869485926363831994924875752485708876235530600469]
c = 8732887389012565362794468502195330360222856683604467832197432048819169030676361164946570568885336785517860079674077246088629086674791372660295987165603174734870438666976597741293243369886505663272137317343952834616100616810165692898933884591814361670638847324009736541971088552142146631155640225750522504079435937001071705455783315076780659468125576524645263757207392680127994493487526081774970513138806894257713616118887635279335491399979284195160569209004422048321045606742073363617818351514156305596845433723109623289408072350115117126321400739315026602591833319799639537262545757199551813901348602918586933926990
e = 0x1337

p = 0
delta = 0.437
n = gmpy2.mpz(n)
D = [n ^ 2, n ^ 1.5, n ^ (2 + delta), n, n ^ (2 + delta), n ^ (1.5 + delta), n ^ (1.5 + delta), n ^ 0.5,
     n ^ (2 + delta), n ^ (1.5 + delta), n ^ (2 + 2 * delta), n ^ (1 + delta), n ^ (2 + 2 * delta), n ^ (1 + delta),
     n ^ (1 + delta), 1]
for i in range(1, 100):
    G = 2 * i
    e1, e2, e3, e4 = y[0] * G, y[1] * G, y[2] * G, y[3] * G
    B = [
        [1, -n, 0, n ^ 2, 0, 0, 0, -n ^ 3, 0, 0, 0, 0, 0, 0, 0, n ^ 4],
        [0, e1, -e1, -e1 * n, -e1, 0, e1 * n, e1 * n ^ 2, -e1, 0, 0, 0, 0, 0, -e1 * n ^ 2, -e1 * n ^ 3],
        [0, 0, e2, -e2 * n, 0, e2 * n, 0, e2 * n ^ 2, 0, e2 * n, 0, 0, 0, -e2 * n ^ 2, 0, -e2 * n ^ 3],
        [0, 0, 0, e1 * e2, 0, -e1 * e2, -e1 * e2, -e1 * e2 * n, 0, -e1 * e2, 0, 0, e1 * e2, e1 * e2 * n, e1 * e2 * n,
         e1 * e2 * n ^ 2],
        [0, 0, 0, 0, e3, -e3 * n, -e3 * n, e3 * n ^ 2, 0, 0, 0, -e3 * n ^ 2, 0, 0, 0, -e3 * n ^ 3],
        [0, 0, 0, 0, 0, e1 * e3, 0, -e1 * e3 * n, 0, 0, e1 * e3, e1 * e3 * n, 0, 0, e1 * e3 * n, e1 * e3 * n ^ 2],
        [0, 0, 0, 0, 0, 0, e2 * e3, -e2 * e3 * n, 0, 0, -e2 * e3, e2 * e3 * n, -e2 * e3, e2 * e3 * n, 0,
         e2 * e3 * n ^ 2],
        [0, 0, 0, 0, 0, 0, 0, e1 * e2 * e3, 0, 0, 0, -e1 * e2 * e3, 0, -e1 * e2 * e3, -e1 * e2 * e3, -e1 * e2 * e3 * n],
        [0, 0, 0, 0, 0, 0, 0, 0, e4, -e4 * n, 0, e4 * n ^ 2, 0, e4 * n ^ 2, e4 * n ^ 2, -e4 * n ^ 3],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, e1 * e4, -e1 * e4, -e1 * e4 * n, -e1 * e4, -e1 * e4 * n, 0, e1 * e4 * n ^ 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, e2 * e4, -e2 * e4 * n, 0, 0, -e2 * e4 * n, e2 * e4 * n ^ 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, e1 * e2 * e4, 0, 0, 0, -e1 * e2 * e4 * n],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, e3 * e4, -e3 * e4 * n, -e3 * e4 * n, e3 * e4 * n ^ 2],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, e1 * e3 * e4, 0, -e1 * e3 * e4 * n],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, e2 * e3 * e4, -e2 * e3 * e4 * n],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, e1 * e2 * e3 * e4]
    ]
    B4 = [[0] * 16 for _ in range(16)]
    for j in range(16):
        for k in range(16):
            B4[j][k] = int(D[k] * B[j][k])
    B4 = matrix(B4)
    v4 = B4.LLL()
    x4 = v4 * B4.inverse()
    phi = int(gmpy2.mpfr(e1) * x4[0][1] / x4[0][0])
    print(phi)
    if (n + 1 - phi) ^ 2 > 4 * n and gmpy2.iroot((n + 1 - phi) ^ 2 - 4 * n, int(2))[1]:
        p = int(((n + 1 - phi) - gmpy2.iroot((n + 1 - phi) ^ 2 - 4 * n, int(2))[0]) // 2)
        q = int(((n + 1 - phi) + gmpy2.iroot((n + 1 - phi) ^ 2 - 4 * n, int(2))[0]) // 2)
        break
    if p:
        break

phi = (p - 1) * (q - 1)
d = inverse(e, phi)
print(long_to_bytes(pow(c, d, n)))

'''B=[
    [1,-n,0,n^2,0,0,0,-n^3,0,0,0,0,0,0,0,n^4],
    [0,e1*G,-e1,-e1*n*G,-e1,0,e1*n,e1*n^2*G,-e1,0,0,0,0,0,-e1*n^2,-e1*n^3*G],
    [0,0,e2,-e2*n*G,0,e2*n,0,e2*n^2*G,0,e2*n,0,0,0,-e2*n^2,0,-e2*n^3*G],
    [0,0,0,e1*e2*G^2,0,-e1*e2*G,-e1*e2*G,-e1*e2*n*G^2,0,-e1*e2*G,0,0,e1*e2,e1*e2*n*G,e1*e2*n*G,e1*e2*n^2*G^2],
    [0,0,0,0,e3,-e3*n,-e3*n,e3*n^2*G,0,0,0,-e3*n^2,0,0,0,-e3*n^3*G],
    [0,0,0,0,0,e1*e3*G,0,-e1*e3*n*G^2,0,0,e1*e3,e1*e3*n*G,0,0,e1*e3*n*G,e1*e3*n^2*G^2],
    [0,0,0,0,0,0,e2*e3*G,-e2*e3*n*G^2,0,0,-e2*e3,e2*e3*n*G,-e2*e3,e2*e3*n*G,0,e2*e3*n^2*G^2],
    [0,0,0,0,0,0,0,e1*e2*e3*G^3,0,0,0,-e1*e2*e3*G^2,0,-e1*e2*e3*G^2,-e1*e2*e3*G^2,-e1*e2*e3*n*G^3],
    [0,0,0,0,0,0,0,0,e4,-e4*n,0,e4*n^2,0,e4*n^2,e4*n^2,-e4*n^3*G],
    [0,0,0,0,0,0,0,0,0,e1*e4*G,-e1*e4,-e1*e4*n*G,-e1*e4,-e1*e4*n*G,0,e1*e4*n^2*G^2],
    [0,0,0,0,0,0,0,0,0,0,e2*e4,-e2*e4*n*G,0,0,-e2*e4*n*G,e2*e4*n^2*G^2],
    [0,0,0,0,0,0,0,0,0,0,0,e1*e2*e4*G^2,0,0,0,-e1*e2*e4*n*G^3],
    [0,0,0,0,0,0,0,0,0,0,0,0,e3*e4,-e3*e4*n*G,-e3*e4*n*G,e3*e4*n^2*G^2],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,e1*e3*e4*G^2,0,-e1*e3*e4*n*G^3],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,e2*e3*e4*G^2,-e2*e3*e4*n*G^3],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,e1*e2*e3*e4*G^4]
    ]'''
