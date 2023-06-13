from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
from gmpy2 import invert, gcdext

n = 15170797923892054990521305052012509493080568087081023750033741867542316768999951573646413753990834682138025772136109204509899638782616660243658254139599441045875522966283555995043016187825383943336990507193641549144516174056706810327582160942467845635495500282175716057977476074952304306822781341844677001797438535701007875365722512160465708455832225273446521621543823855283418665848061608565467010656663089973001969597624553258295614154262448569387247406903093192587512853122780974388687415079948784446715412138463084264315211437439421528085827503277507203193141860916227982534613135645331857382065795066181077972687
e1 = 9576072468337167131
e2 = 14939113163917820627
c1 = 2513254454937818539320001229715025367247490957880668052989469295768681316833496719591412918630312453676811713071414028525870397074185767769616621123070069290764497635067026772298781749325373581840750494743329569059911576372085939972798876709058137797441729480657418587957036217376669515209286767084322875440709473172117549721159755662718590954657925357615152141194701388245440956597032994743626281679318033304014413523468865879100948882376690862202243813943679264465530741774092309002963261692618613612757084511814696332961571153968794051052454203918248339932068292297123047852899029619284314623645966095118119009347
c2 = 111884194864476659139117439739496481475155670608279036093048194153438641356919888323493937575276768933859172174857427366301659912545016807339447507119749910478246208487569012877733924932126136220607107687643614867740936831894203006503190514539481184016080767542829000468460046831987529804871513461035761669072519101709086162745537847204230913330316446448321633091235409913844098851446548290633634428674269538902219278990312260703412892258533797387149328008600614619162876396153768090553946757954666629947494973412821804101257176286021758524844324847062425088549302146311886502815379004832574784487510491117203079999

gcd, a, b = gcdext(e1, e2)

m = pow(c1, a, n) * pow(c2, b, n) % n
print(long_to_bytes(m))