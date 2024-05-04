from sage.all import *
from Crypto.Util.number import bytes_to_long

flag=b'Securinets{test_flag}'

rand=randint(2,2**2048)
p = next_prime(1234*rand + randint(2, 2**512))
q = next_prime(5678*rand + randint(2, 2**512))
e=65537
n = p * q

c=pow(bytes_to_long(flag),e,n)
print(f'n={n}')
print(f'c={c}')

'''
Output:

n=4363344124911080644942120682241878321831640157036886548748673857378211792360734595478338368785280912542424129928159954890766046138350212114698883594173023513521014960739849361545635713652507914927649432440040895244930712300708244254556780681790710847051947537537776132046567882034173133508182249952137114927462066709786872760519282806990952390110722454488120108241792368595803005188457006661033010231205854799175028256298124402500521140477038116546482402028233985212633458633145460572488694919448969871058632050961929538162277400991868810071646428488610663785662352200195912678508254867001144836896252031404532687807479992091375240116368988881586039466725242739490780371448767316492353396884746729079370024764119781501608211723819008548351878262892152466640714238703420463990597575545418095010385035912636874158897765342534337263809403694949418214896533224224490478875476586048903441685998735703138421486124500112371047616625143827656602520003279912124383899400257472619215798629413114642245631195564442240471321808875720956395563690636059031375440115328198122927583838825102384547609877404032236864193669637728610866057538923950191015473204558044234113568107773829931010032423914906445782017096822009101058759855766195882362810743545916853

c=3101554505817718004313996428593525031342357881223209991932730986510855300821755108854251730188788054991396083048283155961610130613904730719671527642968251668270136499458157182479474353495813638375761607165510142791403043668202428721873503224533909899563446795866301206286985622453133254636769669939866492538531430551275690704116271385812437388376041337625534148732542957789938572858632526366655010621273748041627573574641103186499328482910592688108912184512811725550395342150476856439640461703618839225661339614813145279002735559642982175441352018859318122756502986341354153497690031708959453355097865551612363778194327578299413274052923047171542755616563603038632415040317780652823492857036112836728751527562361524478775593949891029231562643699882024289851812960049903313843190147368198510652595704088518500153939978919446000350688064709706773465398951685645692306878745493876281806490128051017965521181972359174513279539022281406590153400993973717996562891907975879921885463475799098526051811936880335375371648269360745362763602798579135537964938295416559841487217689273939517118961756330733457483567939240426500592540579431131903768727962732893195341597969642376610839626208141423090389544824560770528446920779822074390750287400929000791
'''