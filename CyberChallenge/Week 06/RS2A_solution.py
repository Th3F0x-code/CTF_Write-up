from Crypto.Util.number import *
from mpmath import *

n = 89143641593174996017940829434512620472224212719309414452132595836026220427903487320145994697980651982586504529272767661555487338482783564424860474662728864727273993580514641009440479387474215286497920469499137949139655612482534401155809883650788060442770065019330384241207178840133249405439436496214028307558903734242093172998730879440661363638565003329426368977132976057381117500008934189745613221516544513088897518129440859518756071033568194072765218076133667694638728726443287851900688835938080123387337393462387971999466486709250841797151090540874529267419498338329387042916613083146322232965416622470175180495907743430928207190178789080163648956980077548725164945509668997957352565065365941457195088869603665129286984836792952175330148059378293202649610713572446104281953627989163859485809788808508534529382088091029311893877546583669928496131753084896411819111283062837536076097760085135992412357419561774991459364679835378229023651827107364565360470564651977131126249972290200870911790594913743365416646767857884901614015788665683936809635125758430261265314698098466094059017437368507646477819703333772656927273514343778076300501054023098959237661073008808162603803715204854674041298849906327433101431951012146985495761696367870636202433101361960626531600926348142089226552198325016919487083750374489915175146866153953735781193481225863312482746912826070856446017147809208460333465329313456535455411936007666276592807784175302044822812942479141626037467345477917321281968041172167384212163578257658480098463281481529344185464314996956903202741886322363438074048846810969993605250398067874876841896624103759460110133424828446810356511251290637743636702614183409991197132491575032562653418023395238437365608671140737743212645395637665694544881795680378218113444819654272727321072445927623648315543634115399551663510510735009384569247623659827431855711560072567876179851492489603910135190717108556764597233253240486389390643320276977726818025163050601640195450675677567227240411410779412826621028244616810433555533373165859867659781475202135633012093950050241606596357743280710872377776727787269924266524289879775918931638125115068012082514110296027304474289875338899839927318803719580838392092527967209138703512452980175031916627885371740515686162857561710587568854295969137154479177237177380425711176079879774111887004965360114290161247594614252139752042951129604433598880629673492659084063055136817622895706476020680778245545944356200807866648970359643982729489217922876388914990334641094906598976794816011323954673578775401227682807125101250910329421091332002553259830155614494471563564788639372860417136501602811385110297914078406187310233425260560208166547368508305114439695200276774956574553369183599031538963793443751389132785931400583759761329688811878041707652282301287881496588584959270290771909341163174019367385710360542113310489866571786757528552497260740725907099267133050539378588214119265553407800485956012897071160518447438688157842664409659729663838644168009746236157786265024829565917528621175431999886530297179524853203422517926325525973856980800009929571680708523445596309737166498443582703660487278503320404126167116825609252398952218982584267002404396262125673210079685035571771806049071996834889288105295449461079417309562186167517894706744964094448011591870153240384231867709576445763818898789909204583608413229433640492485167158187128576178732492022050179948556553185003868439821440412105961884570513216236564405911276816908917540908766337307171792823318966862301244071574549519086107627838844024147888183205462782131151279743220241080118178832528849478279898624288523002900825161697769734745725621783167394340435718725636973149265960393992982803414662669788693830305371461660492803601699066048539186277412941332469805288305513788946522052887729727457902735242025113943809287023506757501472605369924291550550767828325884976226423462622691574052383035493292680106711990702947156527902051216860850870758108902970671024186499777181388089151385892709970626904193691618526904210630678120735403118123535439246596030740162151650185349774268014558661317331447460771664818916530122300884284886337101065903844876378219496158306575618571119179385239049762182557943522765774767146505125117849797675232102348367863819241145558435654409025934827240995628479046632482776557441431256950838992871457427986657951956675210822565582665945622167638836037702141064014451547559700945267256958160256602259721359531500777466535303862656372761288300254233735763878304211184282168735778866744062452680956626464676516389026153592963535743681771531180886999926359749971591365201944501543757615412816526209817289582076963245251856730985817648973390825762653523636279683208836735678802993412956498927182293160041234640712051733146394236355520002411673955557279015169500889428326023497042992264435757322515845650489616672662183180638392895882814005861260974739307704463230242290002903216578356645936452580469214415932816346000289237
e2 = 7
c = 4646642449734441795234716931873293337783178140295369476477414842493124786921367410881883742032891927674175802184387462112160099639235866128869152699193604169126692210658727708932871872023684255128054850532442397694479339589044019605244318335689745815134153090707404781703605885093038671892987162453083145333870361779070165023194343649585368917744026385936244068253021787577318611063841675505845949101602680733302819197803902930243946808728999105280115072171655797971649055822574030686629682830354992117

mp.prec = 300  # set the mp precision to have a better precision for the root
m = mp.root(c, e2)  # We can divide the cipher text for his exp to take his factor
print("Flag: " + long_to_bytes(m).decode())
