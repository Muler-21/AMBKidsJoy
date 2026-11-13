import sys,os;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common8 import *
SN=E('Mathematics','ሒሳብ');B='(d=>K8.drills(d))'
def U(n,title,drills,extra,exam,nt,summ,foot):
    unit(f'g8-math-{n}','math',SN,E(f'Unit {n}',f'ክፍል {n}'),E(*title),E(f'Built on the Grade 8 Mathematics student textbook (ANRS), Unit {n}: {foot[0]}.',f'በ8ኛ ክፍል የሒሳብ መጽሐፍ ክፍል {n} ላይ የተመሰረተ፦ {foot[1]}።'),B,drills,extra,exam,nt,summ)

# 1 Rational numbers
U(1,('Rational numbers','ምክንያታዊ ቁጥሮች'),[
 D('fracdec',('Fractions and decimals','ክፍልፋይና አስርዮሽ'),('A rational number can be written as a/b with b ≠ 0. As a decimal it either terminates (3/4 = 0.75) or repeats (1/3 = 0.333…).','ምክንያታዊ ቁጥር በa/b (b ≠ 0) ይጻፋል። በአስርዮሽ ሲጻፍ ያበቃል (3/4 = 0.75) ወይም ይደጋገማል (1/3 = 0.333…)።'),5),
 D('ratcmp',('Compare and order','ማወዳደርና መደርደር'),('On the number line, the number further right is bigger. −1/2 > −3/4 because it is closer to 0 from the left.','በቁጥር መስመር ላይ ወደ ቀኝ ያለው ይበልጣል። −1/2 > −3/4 ምክንያቱም ከግራ ለ0 ይቀርባል።'),5),
 D('absval',('Absolute value','ፍጹም ዋጋ'),('|x| is the distance of x from 0: |−7| = 7 and |7| = 7.','|x| የx ከ0 ያለ ርቀት ነው፦ |−7| = 7 እና |7| = 7።'),4),
 D('ratops',('Operations with rational numbers','በምክንያታዊ ቁጥሮች ማስላት'),('Use a common denominator to add or subtract; multiply straight across; to divide, multiply by the reciprocal. Signs follow the integer rules.','ለመደመርና ለመቀነስ የጋራ ታህታይ ተጠቀሙ፤ ለማባዛት ቀጥታ አባዙ፤ ለማካፈል በተገላቢጦሹ አባዙ። ምልክቶች የኢንቲጀር ሕግን ይከተላሉ።'),6),
 D('interest',('Interest and loans','ወለድና ብድር'),('Simple interest I = P × R × T ÷ 100. Banks pay interest on savings and charge interest on loans.','ቀላል ወለድ I = P × R × T ÷ 100። ባንኮች ለቁጠባ ወለድ ይከፍላሉ፤ ለብድር ወለድ ያስከፍላሉ።'),5)],
 [sortm(('Is it rational?','ምክንያታዊ ነው?'),('Rational: can be written as a fraction of two integers (terminating or repeating decimals too). Irrational: endless, non-repeating decimals such as √2 and π.','ምክንያታዊ፦ በሁለት ኢንቲጀሮች ክፍልፋይ ይጻፋል (የሚያበቁና የሚደጋገሙ አስርዮሾችም)። ኢ-ምክንያታዊ፦ የማያበቁና የማይደጋገሙ አስርዮሾች፣ ለምሳሌ √2 እና π።'),[('Rational','ምክንያታዊ'),('Not rational','ምክንያታዊ ያልሆነ')],
  [('−3/5',0),('0.25',0),('7',0),('0.333…',0),('−2.4',0),('√9',0),('√2',1),('π',1),('0.1010010001…',1)])],
 [q('Which is NOT a rational number?','ከሚከተሉት ምክንያታዊ ያልሆነው?',['√2','−4/7','0.6']),q('−2/3 written as a decimal is…','−2/3 በአስርዮሽ…',['−0.666…','−0.23','−1.5']),
  q('|−9| + |4| = ?','|−9| + |4| = ?',['13','−5','5']),q('3/4 ÷ (−1/2) = ?','3/4 ÷ (−1/2) = ?',['−3/2','−3/8','3/2']),q('Birr 5,000 at 10% simple interest for 2 years earns…','ብር 5,000 በ10% ቀላል ወለድ ለ2 ዓመት የሚያስገኘው…',['Birr 1,000','Birr 500','Birr 10,000'])],
 notes(('Rational numbers are fractions of integers; we compare them on the number line and calculate with them, as in interest and loans.','ምክንያታዊ ቁጥሮች የኢንቲጀሮች ክፍልፋዮች ናቸው፤ በቁጥር መስመር እናወዳድራቸዋለን፤ እንደ ወለድና ብድር ባሉ ስሌቶችም እንጠቀማቸዋለን።'),
  [('a/b with b ≠ 0; decimals terminate or repeat.','a/b፣ b ≠ 0፤ አስርዮሾች ያበቃሉ ወይም ይደጋገማሉ።'),('Further right on the number line = bigger.','በቁጥር መስመር ወደ ቀኝ = ትልቅ።'),('|x| = distance from 0, never negative.','|x| = ከ0 ያለ ርቀት፤ አሉታዊ አይሆንም።'),('Simple interest I = P × R × T ÷ 100.','ቀላል ወለድ I = P × R × T ÷ 100።')],
  [('ምክንያታዊ ቁጥር','rational number','በa/b የሚጻፍ ቁጥር'),('ፍጹም ዋጋ','absolute value','ከ0 ያለ ርቀት'),('ወለድ','interest','በገንዘብ ላይ የሚጨመር ክፍያ'),('ተገላቢጦሽ','reciprocal','b/a ለa/b')],('Divide by a fraction? Flip it and multiply!','በክፍልፋይ ማካፈል? ገልብጣችሁ አባዙ!'),
  [(('Order −0.5, 1/3, −3/4 from least','−0.5፣ 1/3፣ −3/4ን ከትንሹ ጀምራችሁ ደርድሩ'),'−3/4, −0.5, 1/3'),(('Interest on Birr 2,000 at 5% for 3 years','ብር 2,000 በ5% ለ3 ዓመት ወለድ'),('Birr 300','ብር 300'))],
  (('Village savings calculator','የመንደር ቁጠባ ማስያ'),('Many families save in iqub or in a bank. Make a poster that shows how money grows with simple interest.','ብዙ ቤተሰቦች በዕቁብ ወይም በባንክ ይቆጥባሉ። ገንዘብ በቀላል ወለድ እንዴት እንደሚያድግ የሚያሳይ ፖስተር ሥሩ።'),[('Choose a saving (for example Birr 1,000) and a bank rate.','ቁጠባ (ለምሳሌ ብር 1,000) እና የባንክ መጠን ምረጡ።'),('Calculate the amount after 1, 2, 3, 4 and 5 years.','ከ1፣ 2፣ 3፣ 4 እና 5 ዓመት በኋላ ያለውን ገንዘብ አስሉ።'),('Draw a bar chart of the results.','ውጤቱን በአምድ ግራፍ ሳሉ።'),('Compare with the cost of a loan at a higher rate.','ከፍ ባለ መጠን ከሚገኝ ብድር ወጪ ጋር አወዳድሩ።')])),
 sm(('Fractions of integers, on a line, in money','የኢንቲጀሮች ክፍልፋይ፣ በመስመር፣ በገንዘብ'),[('Fraction and decimal forms','የክፍልፋይና የአስርዮሽ ቅርጽ'),('Compare and order','ማወዳደርና መደርደር'),('Absolute value','ፍጹም ዋጋ'),('Interest and loans','ወለድና ብድር')]),
 ('the concept of rational numbers, decimal and fraction forms, the number line, comparing and ordering, absolute value, operations and their properties, interest and loans','የምክንያታዊ ቁጥሮች ጽንሰ ሐሳብ፣ የአስርዮሽና የክፍልፋይ ቅርጾች፣ የቁጥር መስመር፣ ማወዳደርና መደርደር፣ ፍጹም ዋጋ፣ ስሌቶችና ባሕርያቸው፣ ወለድና ብድር'))

# 2 Squares, roots, cubes
U(2,('Squares, square roots, cubes and cube roots','ካሬ፣ ካሬ ሥር፣ ኩብና ኩብ ሥር'),[
 D('sqroot',('Squares and square roots','ካሬና ካሬ ሥር'),('a² = a × a. The square root undoes squaring: √49 = 7 because 7² = 49. √(a/b) = √a ÷ √b.','a² = a × a። ካሬ ሥር ማስካትን ይቀለብሳል፦ √49 = 7 ምክንያቱም 7² = 49። √(a/b) = √a ÷ √b።'),6),
 D('sqapprox',('Estimating square roots','ካሬ ሥርን መገመት'),('Find the two perfect squares around the number: 25 < 30 < 36, so 5 < √30 < 6 (about 5.5).','ቁጥሩን የሚከቡትን ሁለት ፍጹም ካሬዎች ፈልጉ፦ 25 < 30 < 36፣ ስለዚህ 5 < √30 < 6 (በግምት 5.5)።'),5),
 D('cube',('Cubes and cube roots','ኩብና ኩብ ሥር'),('a³ = a × a × a. ∛64 = 4 because 4³ = 64. A negative number has a negative cube root: ∛(−8) = −2.','a³ = a × a × a። ∛64 = 4 ምክንያቱም 4³ = 64። አሉታዊ ቁጥር አሉታዊ የኩብ ሥር አለው፦ ∛(−8) = −2።'),5)],
 [match(('Number and its root','ቁጥርና ሥሩ'),('Perfect squares: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100. Perfect cubes: 1, 8, 27, 64, 125, 1000.','ፍጹም ካሬዎች፦ 1፣ 4፣ 9፣ 16፣ 25፣ 36፣ 49፣ 64፣ 81፣ 100። ፍጹም ኩቦች፦ 1፣ 8፣ 27፣ 64፣ 125፣ 1000።'),[[('√144','12'),('√0.36','0.6'),('√(9/16)','3/4')],[('∛27','3'),('∛(−125)','−5'),('∛1000','10')]]),
  quiz(('Squares in real life','ካሬ በሕይወት'),('A square field with area A has side √A. A cube box with volume V has edge ∛V.','ስፋቱ A የሆነ ካሬ ማሳ ጎኑ √A ነው። ይዘቱ V የሆነ ኩብ ሳጥን ጠርዙ ∛V ነው።'),[
  q('A square garden has area 81 m². Its side is…','ካሬ የአትክልት ቦታ ስፋቱ 81 ሜ² ነው። ጎኑ…',['9 m','40.5 m','27 m']),
  q('A cube water tank holds 8 m³. Each edge is…','ኩብ የውኃ ማጠራቀሚያ 8 ሜ³ ይይዛል። እያንዳንዱ ጠርዝ…',['2 m','4 m','8 m']),
  q('Which number is a perfect square?','ፍጹም ካሬ የሆነው ቁጥር?',['196','200','150']),
  q('√50 is between…','√50 በ… መካከል ነው',['7 and 8','6 and 7','25 and 26'])])],
 [q('√(0.81) = ?','√(0.81) = ?',['0.9','0.09','9']),q('(−3)³ = ?','(−3)³ = ?',['−27','27','−9']),q('Which is a perfect cube?','ፍጹም ኩብ የሆነው?',['125','100','150']),q('√20 is closest to…','√20 የሚቀርበው…',['4.5','10','5.5']),q('If x² = 64 and x > 0, x = ?','x² = 64 እና x > 0 ከሆነ x = ?',['8','32','16'])],
 notes(('Squaring and cubing multiply a number by itself; roots undo them and can be estimated between perfect squares.','ማስካትና ኩብ ማድረግ ቁጥርን በራሱ ማባዛት ነው፤ ሥሮች ይቀለብሷቸዋል፤ በፍጹም ካሬዎች መካከል ሊገመቱ ይችላሉ።'),
  [('a² = a × a; √ undoes it.','a² = a × a፤ √ ይቀለብሰዋል።'),('Estimate: 5 < √30 < 6.','ግምት፦ 5 < √30 < 6።'),('a³ = a × a × a; ∛ undoes it.','a³ = a × a × a፤ ∛ ይቀለብሰዋል።'),('√ of a fraction: root top and bottom.','የክፍልፋይ √፦ ላዕላዩንና ታህታዩን።')],
  [('ካሬ','square','በራሱ የተባዛ ቁጥር'),('ካሬ ሥር','square root','ሲስኬት ቁጥሩን የሚሰጥ'),('ኩብ ሥር','cube root','ሦስት ጊዜ ሲባዛ ቁጥሩን የሚሰጥ')],('Square = area of a square; cube = volume of a cube.','ካሬ = የካሬ ስፋት፤ ኩብ = የኩብ ይዘት።'),
  [(('√(49/100)','√(49/100)'),'7/10'),(('∛(−64)','∛(−64)'),'−4')],
  (('Square-root rope trick','የገመድ ካሬ ሥር ዘዴ'),('Builders mark square plots with rope. Use roots to plan a square school garden.','ግንበኞች ካሬ ቦታዎችን በገመድ ያመላክታሉ። ካሬ የትምህርት ቤት አትክልት ለማቀድ ሥሮችን ተጠቀሙ።'),[('Decide the area you need, for example 50 m².','የሚያስፈልጋችሁን ስፋት ወስኑ፣ ለምሳሌ 50 ሜ²።'),('Estimate the side: √50 ≈ 7.1 m.','ጎኑን ገምቱ፦ √50 ≈ 7.1 ሜ።'),('Mark it with rope and pegs; check the corners are square.','በገመድና በችካል አመልክቱ፤ ማዕዘኖቹ ቀጥ መሆናቸውን አረጋግጡ።'),('Measure the real area and compare.','እውነተኛውን ስፋት ለኩና አወዳድሩ።')])),
 sm(('Multiply by itself, and undo it','በራሱ ማባዛትና መቀልበስ'),[('Squares and roots','ካሬና ሥር'),('Estimating roots','ሥርን መገመት'),('Cubes and cube roots','ኩብና ኩብ ሥር'),('Roots of fractions','የክፍልፋይ ሥር')]),
 ('squares and square roots, approximating square roots, cubes and cube roots','ካሬና ካሬ ሥር፣ ካሬ ሥርን መገመት፣ ኩብና ኩብ ሥር'))

# 3 Linear equations and inequalities
U(3,('Linear equations and inequalities','ቀጥተኛ እኩልታዎችና ያለእኩልነቶች'),[
 D('lineq',('Solve the equation','እኩልታውን ፍቱ'),('Do the same thing to both sides. Collect x-terms on one side and numbers on the other, then divide.','በሁለቱም ጎን ተመሳሳይ ነገር አድርጉ። የx ቃላትን በአንድ ጎን፣ ቁጥሮችን በሌላው ሰብስቡ፤ ከዚያ አካፍሉ።'),6),
 D('ineq',('Solve the inequality','ያለእኩልነቱን ፍቱ'),('Same steps as an equation, but multiplying or dividing by a negative number flips the sign: −2x > 6 → x < −3.','እንደ እኩልታ፣ ግን በአሉታዊ ቁጥር ማባዛት ወይም ማካፈል ምልክቱን ይገለብጣል፦ −2x > 6 → x < −3።'),6),
 D('linegraph',('Graph of a line','የመስመር ግራፍ'),('y = mx + c is a straight line: m is the slope (steepness), c is where it crosses the y-axis.','y = mx + c ቀጥተኛ መስመር ነው፦ m ዝንባሌ፣ c የy ዘንግን የሚቆርጥበት ነጥብ ነው።'),5)],
 [quiz(('Word problems','የቃላት ጥያቄዎች'),('Let x be the unknown, write an equation from the story, solve it and check the answer makes sense.','የማይታወቀውን x በሉት፤ ከታሪኩ እኩልታ ጻፉ፤ ፍቱት፤ መልሱ ትርጉም እንዳለው አረጋግጡ።'),[
  q('Three times a number plus 5 is 26. The number is…','የአንድ ቁጥር ሦስት እጥፍ ሲደመር 5 26 ነው። ቁጥሩ…',['7','9','10']),
  q('A pen costs x birr. 4 pens and a Birr 10 book cost Birr 50. x = ?','አንድ እስክሪብቶ x ብር ነው። 4 እስክሪብቶና የብር 10 ደብተር ብር 50 ናቸው። x = ?',['10','15','12.5']),
  q('You need at least 50 marks. You have 32. The next test: x ≥ ?','ቢያንስ 50 ማርክ ያስፈልጋችኋል። 32 አላችሁ። የሚቀጥለው ፈተና፦ x ≥ ?',['18','82','32']),
  q('x + 4 < 10 has solutions…','x + 4 < 10 መፍትሔዎቹ…',['x < 6','x > 6','x < 14'])]),
  sortm(('Which way does it flip?','ምልክቱ ይገለበጣል?'),('Only multiplying or dividing both sides by a NEGATIVE number reverses the inequality.','በሁለቱም ጎን በአሉታዊ ቁጥር ማባዛት ወይም ማካፈል ብቻ ያለእኩልነቱን ይገለብጣል።'),[('Sign stays','ምልክቱ ይቆያል'),('Sign flips','ምልክቱ ይገለበጣል')],
  [(('add 5 to both sides','በሁለቱም ጎን 5 መደመር'),0),(('subtract 3 from both sides','ከሁለቱም ጎን 3 መቀነስ'),0),(('multiply both sides by 2','ሁለቱንም ጎን በ2 ማባዛት'),0),(('divide both sides by −4','ሁለቱንም ጎን በ−4 ማካፈል'),1),(('multiply both sides by −1','ሁለቱንም ጎን በ−1 ማባዛት'),1)])],
 [q('Solve 5x − 3 = 2x + 9','5x − 3 = 2x + 9ን ፍቱ',['x = 4','x = 2','x = 12']),q('Solve −3x ≤ 12','−3x ≤ 12ን ፍቱ',['x ≥ −4','x ≤ −4','x ≥ 4']),q('In y = 2x + 1, the slope is…','በy = 2x + 1 ዝንባሌው…',['2','1','x']),q('Which point is on y = x + 3?','በy = x + 3 ላይ ያለው ነጥብ?',['(1, 4)','(4, 1)','(0, 0)']),q('2(x + 3) = 14, x = ?','2(x + 3) = 14፣ x = ?',['4','5.5','8'])],
 notes(('Linear equations have one answer; linear inequalities have a range of answers, and y = mx + c draws a straight line.','ቀጥተኛ እኩልታ አንድ መልስ አለው፤ ቀጥተኛ ያለእኩልነት የመልሶች ክልል አለው፤ y = mx + c ቀጥተኛ መስመር ይሥላል።'),
  [('Keep the balance: same step on both sides.','ሚዛኑን ጠብቁ፦ በሁለቱም ጎን ተመሳሳይ እርምጃ።'),('× or ÷ by a negative flips <, >.','በአሉታዊ × ወይም ÷ <፣ >ን ይገለብጣል።'),('Show inequality answers on a number line.','የያለእኩልነት መልሶችን በቁጥር መስመር አሳዩ።'),('y = mx + c: slope m, y-intercept c.','y = mx + c፦ ዝንባሌ m፣ የy መቁረጫ c።')],
  [('እኩልታ','equation','= ያለው ዓረፍተ ሒሳብ'),('ያለእኩልነት','inequality','<፣ >፣ ≤፣ ≥ ያለው'),('ዝንባሌ','slope','የመስመሩ ቁልቁለት')],('Negative flip: × or ÷ by a negative turns the sign around.','አሉታዊ ይገለብጣል፦ በአሉታዊ × ወይም ÷ ምልክቱ ይዞራል።'),
  [(('Solve 4 − 2x > 10','4 − 2x > 10ን ፍቱ'),'x < −3'),(('Where does y = 3x − 2 cross the y-axis?','y = 3x − 2 የy ዘንግን የት ይቆርጣል?'),'(0, −2)')],
  (('Phone-credit planner','የስልክ ካርድ እቅድ'),('A shop sells credit in packages. Use an inequality to find how many days your money lasts.','ሱቅ የአየር ሰዓት በጥቅል ይሸጣል። ገንዘባችሁ ስንት ቀን እንደሚበቃ በያለእኩልነት ፈልጉ።'),[('Write your budget, for example Birr 100.','በጀታችሁን ጻፉ፣ ለምሳሌ ብር 100።'),('Write the daily cost, for example Birr 7.','የዕለት ወጪውን ጻፉ፣ ለምሳሌ ብር 7።'),('Solve 7d ≤ 100 to find the days d.','ቀናቱን d ለማግኘት 7d ≤ 100ን ፍቱ።'),('Draw the line y = 100 − 7x and read where it reaches 0.','y = 100 − 7x የሚለውን መስመር ሳሉና 0 የሚደርስበትን አንብቡ።')])),
 sm(('Balance, range, line','ሚዛን፣ ክልል፣ መስመር'),[('Solving equations','እኩልታ መፍታት'),('Solving inequalities','ያለእኩልነት መፍታት'),('Number-line answers','በቁጥር መስመር መልስ'),('Graph y = mx + c','የy = mx + c ግራፍ')]),
 ('solving linear equations, solving linear inequalities, graphs of linear equations and inequalities','ቀጥተኛ እኩልታዎችን መፍታት፣ ቀጥተኛ ያለእኩልነቶችን መፍታት፣ የቀጥተኛ እኩልታዎችና ያለእኩልነቶች ግራፍ'))

# 4 Similarity
U(4,('Similarity of figures','የምስሎች ተመሳሳይነት'),[
 D('simside',('Missing sides of similar triangles','የተመሳሳይ ሦስት ማዕዘኖች የጎደሉ ጎኖች'),('Similar figures have equal angles and proportional sides. Scale factor k = big side ÷ matching small side.','ተመሳሳይ ምስሎች እኩል ማዕዘኖችና ተመጣጣኝ ጎኖች አሏቸው። የመጠን ብዜት k = ትልቅ ጎን ÷ ተዛማጅ ትንሽ ጎን።'),6),
 D('simarea',('Area of similar figures','የተመሳሳይ ምስሎች ስፋት'),('If lengths grow by k, perimeter grows by k and area grows by k².','ርዝመቶች በk ቢያድጉ ዙሪያው በk፣ ስፋቱ በk² ያድጋል።'),5)],
 [sortm(('Similarity tests for triangles','የሦስት ማዕዘን ተመሳሳይነት መፈተሻዎች'),('AA: two pairs of equal angles. SSS: all three sides in the same ratio. SAS: two sides in the same ratio and the included angle equal.','AA፦ ሁለት ጥንድ እኩል ማዕዘኖች። SSS፦ ሦስቱም ጎኖች በአንድ ምጣኔ። SAS፦ ሁለት ጎኖች በአንድ ምጣኔና በመካከላቸው ያለው ማዕዘን እኩል።'),[('AA','AA'),('SSS','SSS'),('SAS','SAS')],
  [(('Angles 40° and 60° in both triangles','በሁለቱም 40° እና 60° ማዕዘኖች'),0),(('Sides 3, 4, 5 and 6, 8, 10','ጎኖች 3፣ 4፣ 5 እና 6፣ 8፣ 10'),1),(('Sides 2, 3 with 50° between and 4, 6 with 50° between','ጎኖች 2፣ 3 በመካከላቸው 50° እና 4፣ 6 በመካከላቸው 50°'),2),(('Two right angles and a shared 35° angle','ሁለት ቀኝ ማዕዘኖችና የጋራ 35° ማዕዘን'),0),(('Sides 5, 5, 8 and 10, 10, 16','ጎኖች 5፣ 5፣ 8 እና 10፣ 10፣ 16'),1)]),
  quiz(('Shadows and maps','ጥላና ካርታ'),('Similar triangles let us measure tall things: a pole and a tree in the sun make similar shadow triangles.','ተመሳሳይ ሦስት ማዕዘኖች ረጃጅም ነገሮችን ለመለካት ይረዳሉ፦ በፀሐይ ላይ ያሉ ምሰሶና ዛፍ ተመሳሳይ የጥላ ሦስት ማዕዘኖች ይሠራሉ።'),[
  q('A 2 m pole casts a 3 m shadow; a tree casts 15 m. The tree is…','2 ሜ ምሰሶ 3 ሜ ጥላ ይጥላል፤ ዛፉ 15 ሜ። ዛፉ…',['10 m tall','22.5 m tall','5 m tall']),
  q('Are all squares similar?','ሁሉም ካሬዎች ተመሳሳይ ናቸው?',[('Yes, equal angles and sides in one ratio','አዎ፣ እኩል ማዕዘኖችና በአንድ ምጣኔ ያሉ ጎኖች'),('No','አይደሉም')]),
  q('Are all rectangles similar?','ሁሉም አራት ማዕዘኖች ተመሳሳይ ናቸው?',[('No, side ratios can differ','አይደሉም፣ የጎን ምጣኔ ይለያያል'),('Yes','አዎ')]),
  q('A photo 4 × 6 cm is enlarged by k = 3. The new size is…','4 × 6 ሴ.ሜ ፎቶ በk = 3 ተሰፋ። አዲሱ መጠን…',['12 × 18 cm','7 × 9 cm','12 × 6 cm'])])],
 [q('Scale factor from 5 cm to 15 cm','ከ5 ሴ.ሜ ወደ 15 ሴ.ሜ የመጠን ብዜት',['3','10','1/3']),q('Similar triangles, k = 2. Small perimeter 12 cm, big perimeter…','ተመሳሳይ ሦስት ማዕዘኖች፣ k = 2። ትንሹ ዙሪያ 12 ሴ.ሜ፣ ትልቁ…',['24 cm','48 cm','14 cm']),q('k = 3, small area 5 cm², big area…','k = 3፣ ትንሹ ስፋት 5 ሴ.ሜ²፣ ትልቁ…',['45 cm²','15 cm²','135 cm²']),q('Two equal angle pairs prove similarity by…','ሁለት እኩል የማዕዘን ጥንዶች ተመሳሳይነትን የሚያረጋግጡት በ…',['AA','SSS','SAS'])],
 notes(('Similar figures have the same shape: equal angles, proportional sides; perimeter scales by k and area by k².','ተመሳሳይ ምስሎች አንድ ዓይነት ቅርጽ አላቸው፦ እኩል ማዕዘኖች፣ ተመጣጣኝ ጎኖች፤ ዙሪያ በk፣ ስፋት በk² ይለወጣል።'),
  [('Same shape, any size; k = scale factor.','አንድ ቅርጽ፣ የተለያየ መጠን፤ k = የመጠን ብዜት።'),('Tests: AA, SSS, SAS.','መፈተሻዎች፦ AA፣ SSS፣ SAS።'),('Perimeter × k, area × k².','ዙሪያ × k፣ ስፋት × k²።'),('Use shadows, maps and photos.','ጥላ፣ ካርታና ፎቶ ተጠቀሙ።')],
  [('ተመሳሳይ','similar','አንድ ዓይነት ቅርጽ'),('የመጠን ብዜት','scale factor','የጎኖች ምጣኔ'),('ተዛማጅ ጎኖች','corresponding sides','በአንድ ቦታ ያሉ ጎኖች')],('Lengths k, areas k², volumes k³.','ርዝመት k፣ ስፋት k²፣ ይዘት k³።'),
  [(('A 1.5 m girl casts 2 m; a building casts 24 m. Height?','1.5 ሜ ልጅ 2 ሜ ጥላ፤ ሕንጻ 24 ሜ። ቁመቱ?'),'18 m'),(('k = 4: how many times bigger is the area?','k = 4፦ ስፋቱ ስንት እጥፍ ይበልጣል?'),'16')],
  (('Shadow height-meter','የጥላ ቁመት መለኪያ'),('Measure a tall tree or school flagpole without climbing.','ረጅም ዛፍ ወይም የትምህርት ቤት ሰንደቅ ዓላማ ምሰሶን ሳትወጡ ለኩ።'),[('On a sunny day, stand a 1 m stick upright.','በፀሐያማ ቀን 1 ሜ ዱላ ቀጥ አድርጋችሁ ትከሉ።'),('Measure its shadow and the tree’s shadow at the same time.','የዱላውንና የዛፉን ጥላ በአንድ ጊዜ ለኩ።'),('Use height = shadow × (1 ÷ stick shadow).','ቁመት = ጥላ × (1 ÷ የዱላ ጥላ) ተጠቀሙ።'),('Compare results from different times of day.','በቀኑ የተለያዩ ሰዓቶች ያገኛችሁትን አወዳድሩ።')])),
 sm(('Same shape, scaled size','አንድ ቅርጽ፣ የተለወጠ መጠን'),[('Scale factor','የመጠን ብዜት'),('AA, SSS, SAS','AA፣ SSS፣ SAS'),('Perimeter and area','ዙሪያና ስፋት'),('Real-life uses','በሕይወት ያለ ጥቅም')]),
 ('similar plane figures, tests for similarity of triangles, perimeter and area of similar triangles','ተመሳሳይ የጠለል ምስሎች፣ የሦስት ማዕዘኖች ተመሳሳይነት መፈተሻዎች፣ የተመሳሳይ ሦስት ማዕዘኖች ዙሪያና ስፋት'))

# 5 Theorems on triangles
U(5,('Theorems on triangles','የሦስት ማዕዘን ቲዎረሞች'),[
 D('trisum',('Angle sum of a triangle','የሦስት ማዕዘን ማዕዘኖች ድምር'),('The three angles of any triangle add up to 180°.','የማንኛውም ሦስት ማዕዘን ሦስት ማዕዘኖች ድምር 180° ነው።'),5),
 D('extang',('Exterior angles','ውጫዊ ማዕዘኖች'),('An exterior angle equals the sum of the two remote interior angles; it is bigger than each of them.','ውጫዊ ማዕዘን ከሁለቱ ራቅ ያሉ ውስጣዊ ማዕዘኖች ድምር ጋር እኩል ነው፤ ከእያንዳንዳቸው ይበልጣል።'),5),
 D('pyth',('Pythagoras’ theorem','የፓይታጎረስ ቲዎረም'),('In a right triangle, hypotenuse² = leg² + leg²: c² = a² + b². Triples: 3, 4, 5 and 5, 12, 13.','በቀኝ ሦስት ማዕዘን፣ ሐይፖቴኑዝ² = ጎን² + ጎን²፦ c² = a² + b²። ሦስትዮሾች፦ 3፣ 4፣ 5 እና 5፣ 12፣ 13።'),6)],
 [quiz(('Is it a right triangle?','ቀኝ ሦስት ማዕዘን ነው?'),('The converse of Pythagoras: if c² = a² + b² for the longest side c, the triangle has a right angle. Builders use 3-4-5 to make square corners.','የፓይታጎረስ ተገላቢጦሽ፦ ለረጅሙ ጎን c፣ c² = a² + b² ከሆነ ሦስት ማዕዘኑ ቀኝ ማዕዘን አለው። ግንበኞች ቀጥ ያለ ማዕዘን ለመሥራት 3-4-5 ይጠቀማሉ።'),[
  q('Sides 6, 8, 10:','ጎኖች 6፣ 8፣ 10፦',[('right triangle (36 + 64 = 100)','ቀኝ ሦስት ማዕዘን (36 + 64 = 100)'),('not right','ቀኝ አይደለም')]),
  q('Sides 4, 5, 6:','ጎኖች 4፣ 5፣ 6፦',[('not right (16 + 25 ≠ 36)','ቀኝ አይደለም (16 + 25 ≠ 36)'),('right','ቀኝ ነው')]),
  q('A 5 m ladder stands 3 m from a wall. It reaches…','5 ሜ መሰላል ከግድግዳ 3 ሜ ርቆ ቆሟል። የሚደርሰው…',['4 m up','2 m up','8 m up']),
  q('The longest side of a right triangle is the…','የቀኝ ሦስት ማዕዘን ረጅሙ ጎን…',[('hypotenuse','ሐይፖቴኑዝ'),('base','መሠረት'),('height','ቁመት')])]),
  order(('From the theorem to the answer','ከቲዎረሙ ወደ መልሱ'),('Order the steps to find a missing side with Pythagoras.','በፓይታጎረስ የጎደለ ጎን ለማግኘት እርምጃዎቹን ደርድሩ።'),('Tap the steps in order.','እርምጃዎቹን በቅደም ተከተል ንኩ።'),[(('Find the hypotenuse','ሐይፖቴኑዙን ፈልጉ'),[('Name the legs a, b','ጎኖቹን a፣ b በሉ'),('Square them: a², b²','አስኩ፦ a²፣ b²'),('Add: a² + b²','ደምሩ፦ a² + b²'),('Take the square root','ካሬ ሥሩን ውሰዱ')])])],
 [q('Angles 90° and 35°. Third angle?','ማዕዘኖች 90° እና 35°። ሦስተኛው?',['55°','125°','65°']),q('Remote interior angles 50° and 70°. Exterior angle?','ራቅ ያሉ ውስጣዊ ማዕዘኖች 50° እና 70°። ውጫዊው?',['120°','60°','20°']),q('Legs 9 and 12. Hypotenuse?','ጎኖች 9 እና 12። ሐይፖቴኑዝ?',['15','21','13']),q('Hypotenuse 13, leg 5. Other leg?','ሐይፖቴኑዝ 13፣ ጎን 5። ሌላው?',['12','8','18'])],
 notes(('Triangle angles sum to 180°, an exterior angle equals the two remote interior angles, and right triangles obey c² = a² + b².','የሦስት ማዕዘን ማዕዘኖች ድምር 180° ነው፤ ውጫዊ ማዕዘን ከሁለቱ ራቅ ያሉ ውስጣዊ ማዕዘኖች ድምር ጋር እኩል ነው፤ ቀኝ ሦስት ማዕዘኖች c² = a² + b²ን ይከተላሉ።'),
  [('Angle sum = 180°.','የማዕዘኖች ድምር = 180°።'),('Exterior = sum of remote interiors.','ውጫዊ = የራቅ ውስጣዊዎች ድምር።'),('c² = a² + b² (c = hypotenuse).','c² = a² + b² (c = ሐይፖቴኑዝ)።'),('Converse: test for a right angle.','ተገላቢጦሽ፦ የቀኝ ማዕዘን መፈተሻ።')],
  [('ቲዎረም','theorem','የተረጋገጠ የሒሳብ እውነት'),('ሐይፖቴኑዝ','hypotenuse','ከቀኝ ማዕዘን ትይዩ ያለ ረጅሙ ጎን'),('ውጫዊ ማዕዘን','exterior angle','ከጎን ማራዘሚያ ጋር የሚሠራ ማዕዘን')],('3-4-5 makes a perfect corner.','3-4-5 ፍጹም ማዕዘን ይሠራል።'),
  [(('A TV screen is 30 cm by 40 cm. Diagonal?','የቴሌቪዥን ስክሪን 30 ሴ.ሜ በ40 ሴ.ሜ። ሰያፉ?'),'50 cm'),(('Is 7, 24, 25 a right triangle?','7፣ 24፣ 25 ቀኝ ሦስት ማዕዘን ነው?'),('Yes: 49 + 576 = 625','አዎ፦ 49 + 576 = 625'))],
  (('Rope corner-maker','የገመድ ማዕዘን መሥሪያ'),('Make a tool that farmers and builders can use to lay out square corners.','ገበሬዎችና ግንበኞች ቀጥ ያሉ ማዕዘኖችን ለማውጣት የሚጠቀሙበት መሣሪያ ሥሩ።'),[('Tie 12 equal knots in a rope loop.','በገመድ ቀለበት 12 እኩል ቋጠሮዎችን አስሩ።'),('Stretch it into a 3-4-5 triangle with pegs.','በችካሎች 3-4-5 ሦስት ማዕዘን አድርጋችሁ ወጥሩት።'),('Check the right angle with a set square.','ቀኝ ማዕዘኑን በስኩየር አረጋግጡ።'),('Teach someone at home to use it.','በቤት ያለ ሰው እንዲጠቀምበት አስተምሩ።')])),
 sm(('Three rules every triangle obeys','ሦስት ማዕዘን የሚከተላቸው ሦስት ሕጎች'),[('180° angle sum','የ180° ድምር'),('Exterior angle','ውጫዊ ማዕዘን'),('Pythagoras','ፓይታጎረስ'),('Converse','ተገላቢጦሽ')]),
 ('theorems of triangles, exterior angles of a triangle, theorems on right-angled triangles','የሦስት ማዕዘን ቲዎረሞች፣ የሦስት ማዕዘን ውጫዊ ማዕዘኖች፣ የቀኝ ሦስት ማዕዘን ቲዎረሞች'))

# 6 Circles
U(6,('Lines and angles in a circle','በክብ ውስጥ ያሉ መስመሮችና ማዕዘኖች'),[
 D('circang',('Central and inscribed angles','ማዕከላዊና የክብ ውስጥ ማዕዘኖች'),('A central angle has its vertex at the centre; an inscribed angle has its vertex on the circle. Inscribed = ½ × central on the same arc.','ማዕከላዊ ማዕዘን ጫፉ በመሃሉ ነው፤ የክብ ውስጥ ማዕዘን ጫፉ በክቡ ላይ ነው። የክብ ውስጥ = ½ × ማዕከላዊ (በአንድ ቅስት ላይ)።'),6),
 D('chordang',('Intersecting chords','የሚቆራረጡ አውታሮች'),('When two chords cross inside a circle, each angle = ½ (sum of the two intercepted arcs).','ሁለት አውታሮች በክብ ውስጥ ሲቆራረጡ፣ እያንዳንዱ ማዕዘን = ½ (የሁለቱ የተያዙ ቅስቶች ድምር)።'),5)],
 [match(('Parts of a circle','የክብ ክፍሎች'),('Know the names before you find angles.','ማዕዘን ከመፈለጋችሁ በፊት ስሞቹን እወቁ።'),[[(('Chord','አውታር'),('joins two points on the circle','በክቡ ላይ ያሉ ሁለት ነጥቦችን ያገናኛል')),(('Diameter','ዲያሜትር'),('chord through the centre','በመሃሉ የሚያልፍ አውታር')),(('Radius','ራዲየስ'),('centre to the circle','ከመሃል እስከ ክቡ'))],[(('Tangent','ታንጀንት'),('touches the circle at one point','ክቡን በአንድ ነጥብ ይነካል')),(('Secant','ሴካንት'),('line cutting the circle twice','ክቡን ሁለት ጊዜ የሚቆርጥ መስመር')),(('Arc','ቅስት'),('part of the circle','የክቡ ክፍል'))]]),
  quiz(('Special facts','ልዩ እውነታዎች'),('An angle in a semicircle is 90°. A tangent is perpendicular to the radius at the point of contact.','በግማሽ ክብ ውስጥ ያለ ማዕዘን 90° ነው። ታንጀንት በመነኪያ ነጥቡ ከራዲየሱ ጋር ቀጥ ያለ ነው።'),[
  q('An angle inscribed in a semicircle is…','በግማሽ ክብ ውስጥ ያለ ማዕዘን…',['90°','180°','45°']),
  q('A tangent and the radius at the touching point meet at…','ታንጀንትና በመነኪያው ነጥብ ያለው ራዲየስ የሚገናኙት በ…',['90°','60°','0°']),
  q('Inscribed angles on the same arc are…','በአንድ ቅስት ላይ ያሉ የክብ ውስጥ ማዕዘኖች…',[('equal','እኩል'),('double','እጥፍ'),('half','ግማሽ')]),
  q('The longest chord of a circle is the…','የክብ ረጅሙ አውታር…',[('diameter','ዲያሜትር'),('radius','ራዲየስ'),('tangent','ታንጀንት')])])],
 [q('Central angle 140°. Inscribed angle on the same arc?','ማዕከላዊ 140°። በአንድ ቅስት ላይ ያለው የክብ ውስጥ?',['70°','140°','280°']),q('Inscribed angle 35°. Central angle?','የክብ ውስጥ 35°። ማዕከላዊው?',['70°','17.5°','145°']),q('Chords cross; arcs 80° and 100°. Angle?','አውታሮች ተቆራረጡ፤ ቅስቶች 80° እና 100°። ማዕዘኑ?',['90°','180°','10°']),q('A line touching a circle at one point is a…','ክብን በአንድ ነጥብ የሚነካ መስመር…',[('tangent','ታንጀንት'),('secant','ሴካንት'),('chord','አውታር')])],
 notes(('Angles in a circle are measured by their arcs: inscribed angles are half the central angle, and crossing chords make half the sum of the arcs.','በክብ ውስጥ ያሉ ማዕዘኖች በቅስቶቻቸው ይለካሉ፦ የክብ ውስጥ ማዕዘን የማዕከላዊው ግማሽ ነው፤ የሚቆራረጡ አውታሮች የቅስቶቹን ድምር ግማሽ ይሠራሉ።'),
  [('Chord, diameter, radius, tangent, secant, arc.','አውታር፣ ዲያሜትር፣ ራዲየስ፣ ታንጀንት፣ ሴካንት፣ ቅስት።'),('Inscribed = ½ central.','የክብ ውስጥ = ½ ማዕከላዊ።'),('Semicircle angle = 90°; tangent ⟂ radius.','የግማሽ ክብ ማዕዘን = 90°፤ ታንጀንት ⟂ ራዲየስ።'),('Chords: angle = ½(arc + arc).','አውታሮች፦ ማዕዘን = ½(ቅስት + ቅስት)።')],
  [('አውታር','chord','በክቡ ላይ ያሉ ሁለት ነጥቦችን የሚያገናኝ'),('ቅስት','arc','የክብ ክፍል'),('ማዕከላዊ ማዕዘን','central angle','ጫፉ በመሃል ያለ')],('Inscribed is half; centre is whole.','የክብ ውስጥ ግማሽ፤ ማዕከላዊ ሙሉ።'),
  [(('Arc of 100°: inscribed angle on it?','የ100° ቅስት፦ በእሱ ላይ ያለ የክብ ውስጥ ማዕዘን?'),'50°'),(('Why do bicycle wheels touch the road at one point?','የብስክሌት ጎማ መንገዱን በአንድ ነጥብ ለምን ይነካል?'),('The road is a tangent','መንገዱ ታንጀንት ነው'))],
  (('Find the centre of a round table','የክብ ጠረጴዛ መሃልን ፈልጉ'),('Carpenters find centres with chords. Try it with a paper plate.','አናጢዎች መሃልን በአውታሮች ያገኛሉ። በወረቀት ሳህን ሞክሩት።'),[('Draw two chords on the plate.','በሳህኑ ላይ ሁለት አውታሮችን ሳሉ።'),('Draw the perpendicular bisector of each chord.','የእያንዳንዱን አውታር ቀጥ ያለ መክፈያ ሳሉ።'),('Where they cross is the centre.','የሚቆራረጡበት ቦታ መሃሉ ነው።'),('Check with a ruler that every radius is equal.','እያንዳንዱ ራዲየስ እኩል መሆኑን በማስመሪያ አረጋግጡ።')])),
 sm(('Arcs decide the angles','ቅስቶች ማዕዘኖችን ይወስናሉ'),[('Circle vocabulary','የክብ ቃላት'),('Inscribed vs central','የክብ ውስጥና ማዕከላዊ'),('Semicircle and tangent','ግማሽ ክብና ታንጀንት'),('Crossing chords','የሚቆራረጡ አውታሮች')]),
 ('circles and lines, central and inscribed angles, angles formed by two intersecting chords','ክብና መስመሮች፣ ማዕከላዊና የክብ ውስጥ ማዕዘኖች፣ በሚቆራረጡ አውታሮች የሚፈጠሩ ማዕዘኖች'))

# 7 Solid figures
U(7,('Solid figures and measurements','ጠጣር ምስሎችና ልኬታቸው'),[
 D('solid',('Surface area and volume','የገጽ ስፋትና ይዘት'),('Prism and cylinder: V = base area × height. Pyramid and cone: V = ⅓ × base area × height. Surface area = total area of all faces.','ፕሪዝምና ሲሊንደር፦ ይዘት = የመሠረት ስፋት × ቁመት። ፒራሚድና ኮን፦ ይዘት = ⅓ × የመሠረት ስፋት × ቁመት። የገጽ ስፋት = የሁሉም ገጾች ስፋት ድምር።'),8)],
 [sortm(('Name the solid family','የጠጣሩን ቤተሰብ ሰይሙ'),('Prisms and cylinders have two equal parallel bases. Pyramids and cones narrow to a point (apex).','ፕሪዝምና ሲሊንደር ሁለት እኩል ትይዩ መሠረቶች አሏቸው። ፒራሚድና ኮን ወደ አንድ ጫፍ ይጠባሉ።'),[('Prism or cylinder','ፕሪዝም ወይም ሲሊንደር'),('Pyramid or cone','ፒራሚድ ወይም ኮን')],
  [(('brick','ጡብ'),0),(('water pipe','የውኃ ቱቦ'),0),(('tent with a square floor and one top point','ካሬ ወለልና አንድ ጫፍ ያለው ድንኳን'),1),(('ice-cream cone','የአይስክሬም ኮን'),1),(('tin of tomato paste','የቲማቲም ድልህ ጣሳ'),0),(('a traditional thatched roof','ባህላዊ የሣር ክዳን'),1)]),
  quiz(('Nets and units','ንድፎችና መለኪያዎች'),('A net is the flat shape that folds into a solid. Area is in cm², volume in cm³; 1 litre = 1,000 cm³.','ንድፍ ታጥፎ ጠጣር የሚሆን ጠፍጣፋ ቅርጽ ነው። ስፋት በሴ.ሜ²፣ ይዘት በሴ.ሜ³፤ 1 ሊትር = 1,000 ሴ.ሜ³።'),[
  q('A cube has how many faces?','ኩብ ስንት ገጾች አሉት?',['6','8','12']),
  q('A cylinder’s net has two circles and a…','የሲሊንደር ንድፍ ሁለት ክቦችና… አለው',[('rectangle','አራት ማዕዘን'),('triangle','ሦስት ማዕዘን'),('square pyramid','ካሬ ፒራሚድ')]),
  q('A box 10 × 10 × 10 cm holds…','10 × 10 × 10 ሴ.ሜ ሳጥን የሚይዘው…',['1 litre','10 litres','100 cm³']),
  q('Volume is measured in…','ይዘት የሚለካው በ…',['cm³','cm²','cm'])])],
 [q('Volume of a 3 × 4 × 5 cm box','የ3 × 4 × 5 ሴ.ሜ ሳጥን ይዘት',['60 cm³','47 cm³','94 cm³']),q('Surface area of a cube with edge 2 cm','ጠርዙ 2 ሴ.ሜ የሆነ ኩብ የገጽ ስፋት',['24 cm²','8 cm²','12 cm²']),q('Cylinder r = 1 cm, h = 10 cm (π ≈ 3.14). Volume?','ሲሊንደር r = 1 ሴ.ሜ፣ h = 10 ሴ.ሜ (π ≈ 3.14)። ይዘት?',['31.4 cm³','62.8 cm³','10.47 cm³']),q('A cone and cylinder share base and height. The cone holds…','ኮንና ሲሊንደር መሠረትና ቁመት ይጋራሉ። ኮኑ የሚይዘው…',['⅓ as much','the same','half as much'])],
 notes(('Solids have surface area (cm²) and volume (cm³); prisms and cylinders use base × height, pyramids and cones use one third of that.','ጠጣሮች የገጽ ስፋት (ሴ.ሜ²) እና ይዘት (ሴ.ሜ³) አላቸው፤ ፕሪዝምና ሲሊንደር መሠረት × ቁመት፣ ፒራሚድና ኮን የዚያን አንድ ሦስተኛ ይጠቀማሉ።'),
  [('Families: prism, cylinder, pyramid, cone, sphere.','ቤተሰቦች፦ ፕሪዝም፣ ሲሊንደር፣ ፒራሚድ፣ ኮን፣ ሉል።'),('Surface area = sum of the faces (use the net).','የገጽ ስፋት = የገጾች ድምር (ንድፉን ተጠቀሙ)።'),('V = base × h; ⅓ for pyramid and cone.','ይዘት = መሠረት × h፤ ለፒራሚድና ለኮን ⅓።'),('1 litre = 1,000 cm³.','1 ሊትር = 1,000 ሴ.ሜ³።')],
  [('ጠጣር','solid','ቦታ የሚይዝ ባለ 3 ልኬት ምስል'),('ይዘት','volume','በውስጡ የሚይዘው ቦታ'),('ንድፍ','net','ታጥፎ ጠጣር የሚሆን ቅርጽ')],('Cylinder = circle × height; cone = one third.','ሲሊንደር = ክብ × ቁመት፤ ኮን = አንድ ሦስተኛ።'),
  [(('Litres in a 50 × 40 × 30 cm tank','በ50 × 40 × 30 ሴ.ሜ ማጠራቀሚያ ውስጥ ያሉ ሊትሮች'),('60 litres','60 ሊትር')),(('Paint needed for a 2 m cube (all faces)','ለ2 ሜ ኩብ (ሁሉም ገጾች) የሚያስፈልግ ቀለም ስፋት'),'24 m²')],
  (('Rain-water tank designer','የዝናብ ውኃ ማጠራቀሚያ ንድፍ አውጪ'),('Many schools collect roof water. Design a tank that holds a week of drinking water for your class.','ብዙ ትምህርት ቤቶች የጣሪያ ውኃ ይሰበስባሉ። ለክፍላችሁ የአንድ ሳምንት የመጠጥ ውኃ የሚይዝ ማጠራቀሚያ ንድፉ።'),[('Estimate litres needed: students × 1 litre × 5 days.','የሚያስፈልገውን ሊትር ገምቱ፦ ተማሪዎች × 1 ሊትር × 5 ቀን።'),('Choose a cylinder or cuboid shape and work out its size.','ሲሊንደር ወይም አራት ማዕዘን ጠጣር ምረጡና መጠኑን አስሉ።'),('Find the surface area to know how much sheet metal is needed.','ምን ያህል ቆርቆሮ እንደሚያስፈልግ ለማወቅ የገጽ ስፋቱን ፈልጉ።'),('Draw the tank with labels and present it.','ማጠራቀሚያውን በስያሜዎች ሳሉና አቅርቡ።')])),
 sm(('Measure the outside and the inside','ውጪውንና ውስጡን ለኩ'),[('Solid families','የጠጣር ቤተሰቦች'),('Surface area','የገጽ ስፋት'),('Volume formulas','የይዘት ቀመሮች'),('Litres and cm³','ሊትርና ሴ.ሜ³')]),
 ('solid figures, surface area of solid figures, volume of solid figures','ጠጣር ምስሎች፣ የጠጣር ምስሎች የገጽ ስፋት፣ የጠጣር ምስሎች ይዘት'))
dump('math')
