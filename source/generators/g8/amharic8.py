import sys,os;sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from common8 import *
SN=E('Amharic','አማርኛ')
def A(q_en,q_am,opts,a=0): return {'q':E(q_en,q_am),'o':[o if isinstance(o,str) else E(*o) for o in opts],'a':a}
def W(sent,opts,a=0): return {'q':sent,'o':opts,'a':a}
def read(ptitle,paras,items): return {'title':E('Read and understand','አንብቦ መረዳት'),'type':'quiz','tip':E('Read the passage fluently, then answer. Think about the main idea and the writer\'s message.','ምንባቡን አቀላጥፋችሁ አንብቡ፤ ከዚያ መልሱ። ስለ ዋናው ሐሳብና ስለ ጸሐፊው መልእክት አስቡ።'),'passage':{'title':ptitle,'paras':paras},'items':items}
def build(rounds): return order(('Build the sentence','ዓረፍተ ነገር መሥርቱ'),('Put the words in the right order. Amharic sentences usually end with the verb and "።".','ቃላቱን በትክክለኛ ቅደም ተከተል አስቀምጡ። የአማርኛ ዓረፍተ ነገር ብዙ ጊዜ በግሥና በ"።" ይጨርሳል።'),('Tap the words in order.','ቃላቱን በቅደም ተከተል ንኩ።'),[(('Build:','መሥርቱ፦'),w) for w in rounds])
def vmatch(pairs): return {'title':E('Word meanings','የቃላት ፍቺ'),'type':'match','tip':E('Match each word with its meaning.','እያንዳንዱን ቃል ከፍቺው ጋር አዛምዱ።'),'rounds':[[[a,b] for a,b in pairs]]}
def U(n,title,extra,exam,nt,summ,foot):
    unit(f'g8-amharic-{n}','amharic',SN,E(f'Chapter {n}',f'ምዕራፍ {n}'),E(*title),E(f'Built on the Grade 8 Amharic student book (ANRS), Chapter {n}: {foot}.',f'በ8ኛ ክፍል የአማርኛ መጽሐፍ ምዕራፍ {n} ({title[1]}) ላይ የተመሰረተ።'),'(d=>[])',{},extra,exam,nt,summ)
def inn(t,x,s): return (t,x,s)

# 1
U(1,('Work ethics','የሥራ ባህል'),[
 read('የሙሉቀን ወርክሾፕ',['ሙሉቀን በደብረ ማርቆስ ትንሽ የእንጨት ሥራ ወርክሾፕ አለው። በየቀኑ ሁለት ሰዓት ላይ ይከፍታል፤ ደንበኞችን በትሕትና ይቀበላል።','አንድ ቀን አንድ ደንበኛ ያዘዘው ወንበር በቀጠሮው ቀን አልደረሰም። ሙሉቀን ይቅርታ ጠየቀ፤ ሌሊቱን ሠርቶ በማግሥቱ አስረከበ። "ቃል ኪዳን ከገንዘብ ይበልጣል" አለ።','ዛሬ ደንበኞቹ በእርሱ ይተማመናሉ። ሥራውም አድጎ ለአምስት ወጣቶች የሥራ ዕድል ፈጥሯል።'],[
  A('What kind of business does Mulukan have?','ሙሉቀን ምን ዓይነት ሥራ አለው?',['የእንጨት ሥራ','የልብስ ሱቅ','ምግብ ቤት']),A('What did he do when the chair was late?','ወንበሩ ሲዘገይ ምን አደረገ?',['ይቅርታ ጠይቆ ሌሊቱን ሠርቶ አስረከበ','ደንበኛውን ተቆጣ','ገንዘቡን አልመለሰም']),A('Main message?','ዋናው መልእክት?',['ታማኝነትና ትጋት ሥራን ያሳድጋሉ','ሥራ ማቆም ጥሩ ነው','ደንበኛ አያስፈልግም'])]),
 vmatch([('ትጋት','ጠንክሮ መሥራት'),('ቀጠሮ','የተወሰነ ጊዜ'),('ታማኝ','የሚታመን'),('ደንበኛ','ዕቃ ወይም አገልግሎት የሚገዛ')]),
 quiz(('Positive, negative and question sentences','አዎንታዊ፣ አሉታዊና መጠይቃዊ ዓረፍተ ነገሮች'),('A positive sentence states something (ሠራ). A negative one denies it, usually with አል-…-ም (አልሠራም). A question asks (ሠራ? / ማን ሠራ?) and ends with "?".','አዎንታዊ ዓረፍተ ነገር አንድን ነገር ያረጋግጣል (ሠራ)። አሉታዊው ይክዳል፤ ብዙ ጊዜ በአል-…-ም (አልሠራም)። መጠይቃዊው ይጠይቃል (ሠራ? / ማን ሠራ?)፤ በ"?" ያልቃል።'),[
  A('Make negative: "ሙሉቀን ወንበሩን ሠራ።"','አሉታዊ አድርጉ፦ "ሙሉቀን ወንበሩን ሠራ።"',['ሙሉቀን ወንበሩን አልሠራም።','ሙሉቀን ወንበሩን ሠራ?','ሙሉቀን ወንበሩን ይሠራል።']),A('Which is a question sentence?','መጠይቃዊ ዓረፍተ ነገር የትኛው ነው?',['ሥራውን መቼ ትጨርሳለህ?','ሥራውን ጨረስኩ።','ሥራውን አልጨረስኩም።']),
  A('Type of: "ተማሪዎቹ ዛሬ አልዘገዩም።"','"ተማሪዎቹ ዛሬ አልዘገዩም።" ዓይነቱ',['አሉታዊ','አዎንታዊ','መጠይቃዊ']),W('ሰነፍ ሰው ሥራውን በጊዜ ___።',['አይጨርስም','ይጨርሳል?','ጨረሰ'])]),
 build([['ታታሪ','ሠራተኛ','ቀጠሮውን','ያከብራል።'],['ሥራን','ማክበር','ለሀገር','ዕድገት','ይጠቅማል።']])],
 [A('Negative of "ትመጣለች"','የ"ትመጣለች" አሉታዊ',['አትመጣም','መጣች','ትመጣለች?']),A('A question ends with…','መጠይቃዊ ዓረፍተ ነገር የሚያልቀው በ…',['?','።','፣']),A('Meaning of ትጋት','የ"ትጋት" ፍቺ',['ጠንክሮ መሥራት','ስንፍና','ዕረፍት']),A('Good work ethics include…','ጥሩ የሥራ ባህል የሚያካትተው…',['ሰዓት ማክበርና ታማኝነት','መዘግየትና ማታለል','ሥራ መሸሽ'])],
 notes(('Good work ethics (punctuality, honesty, hard work) build trust and jobs; we practise positive, negative and question sentences.','ጥሩ የሥራ ባህል (ሰዓት ማክበር፣ ታማኝነት፣ ትጋት) እምነትንና ሥራን ይፈጥራል፤ አዎንታዊ፣ አሉታዊና መጠይቃዊ ዓረፍተ ነገሮችን እንለማመዳለን።'),
  [('Listening and reading about work culture.','ስለ ሥራ ባህል ማዳመጥና ማንበብ።'),('Vocabulary from context.','ቃላትን ከዐውዱ መረዳት።'),('Positive vs negative (አል-…-ም).','አዎንታዊና አሉታዊ (አል-…-ም)።'),('Question sentences end with "?".','መጠይቃዊ ዓረፍተ ነገር በ"?" ያልቃል።')],
  [('ትጋት','hard work','ጠንክሮ መሥራት'),('ታማኝነት','honesty','እምነት የሚጣልበት መሆን'),('ቀጠሮ','appointment','የተወሰነ ጊዜ')],('Say it, deny it, ask it: ሠራ – አልሠራም – ሠራ?','አረጋግጥ፣ ካድ፣ ጠይቅ፦ ሠራ – አልሠራም – ሠራ?'),
  [(('Make negative: "ደንበኛው ረካ።"','አሉታዊ አድርጉ፦ "ደንበኛው ረካ።"'),'ደንበኛው አልረካም።'),(('Make a question: "ወርክሾፑ ተከፈተ።"','መጠይቃዊ አድርጉ፦ "ወርክሾፑ ተከፈተ።"'),'ወርክሾፑ መቼ ተከፈተ?')],
  inn(('Class punctuality tracker','የክፍል ሰዓት አክባሪነት መከታተያ'),('A good work culture starts at school. Make a simple chart that rewards being on time.','ጥሩ የሥራ ባህል ከትምህርት ቤት ይጀምራል። በሰዓት መገኘትን የሚሸልም ቀላል ሰንጠረዥ ሥሩ።'),[('Agree on 3 class work rules.','3 የክፍል የሥራ ደንቦችን ተስማሙ።'),('Record arrival and homework daily for a month.','ለአንድ ወር መድረስንና የቤት ሥራን በየቀኑ መዝግቡ።'),('Give a weekly "ታታሪ" badge.','ሳምንታዊ "ታታሪ" ባጅ ስጡ።'),('Write a short report on the changes.','ስለ ለውጡ አጭር ሪፖርት ጻፉ።')])),
 sm(('Work culture and sentence types','የሥራ ባህልና የዓረፍተ ነገር ዓይነቶች'),[('Reading','ንባብ'),('Vocabulary','ቃላት'),('Positive/negative','አዎንታዊ/አሉታዊ'),('Questions','መጠይቅ')]),'Work ethics')

# 2
U(2,('Heritage','ቅርስ'),[
 read('የላሊበላ ድንጋዮች',['በላሊበላ ከአንድ ወጥ ዓለት ተፈልፍለው የተሠሩ ዐሥራ አንድ አብያተ ክርስቲያናት ይገኛሉ። ከእነርሱም የቅዱስ ጊዮርጊስ ቤተ ክርስቲያን በመስቀል ቅርጹ ይታወቃል።','እነዚህ ድንቅ ቅርሶች ከስምንት መቶ ዓመታት በፊት የተሠሩ ናቸው። ዩኔስኮ በ1978 እ.ኤ.አ. በዓለም ቅርስነት መዝግቧቸዋል።','ዝናብና የሰዎች ብዛት ቅርሶቹን ሊጎዱ ይችላሉ። ስለዚህ ቅርስን መጠበቅ ለመጪው ትውልድ የምንተወው ዕዳ ነው።'],[
  A('How were the Lalibela churches made?','የላሊበላ አብያተ ክርስቲያናት እንዴት ተሠሩ?',['ከአንድ ወጥ ዓለት ተፈልፍለው','በጡብ ተገንብተው','ከእንጨት ተሠርተው']),A('Which church has a cross shape?','የመስቀል ቅርጽ ያለው የትኛው ነው?',['ቅዱስ ጊዮርጊስ','ቅድስት ማርያም','መድኃኔ ዓለም']),A('What can damage the heritage?','ቅርሶቹን ምን ሊጎዳቸው ይችላል?',['ዝናብና የሰዎች ብዛት','ፀሐይ ብቻ','መጻሕፍት'])]),
 vmatch([('ቅርስ','ከቀድሞ ትውልድ የተላለፈ ሀብት'),('ተፈለፈለ','ተቀርጾ ወጣ'),('ትውልድ','በአንድ ዘመን የሚኖሩ ሰዎች'),('ዕዳ','መክፈል ያለብን ግዴታ')]),
 quiz(('Modifiers, dependent clauses and tense','ገላጮች፣ ጥገኛ ሐረጎችና ጊዜ'),('A noun modifier (ቅጽል) describes a noun: ጥንታዊ ቅርስ. A verb modifier (ተውሳከ ግሥ) describes a verb: በጥንቃቄ ጠበቁ. A dependent clause cannot stand alone: ቱሪስቶቹ ሲመጡ… Tense: ኃላፊ (ጎበኘ), ትንቢት/አሁን (ይጎበኛል).','የስም ገላጭ (ቅጽል) ስምን ይገልጻል፦ ጥንታዊ ቅርስ። የግሥ ገላጭ (ተውሳከ ግሥ) ግሥን ይገልጻል፦ በጥንቃቄ ጠበቁ። ጥገኛ ሐረግ ብቻውን አይቆምም፦ ቱሪስቶቹ ሲመጡ… ጊዜ፦ ኃላፊ (ጎበኘ)፣ ኃላፊ ያልሆነ (ይጎበኛል)።'),[
  A('Noun modifier in "ጥንታዊው ሐውልት ቆሟል።"','በ"ጥንታዊው ሐውልት ቆሟል።" ቅጽሉ',['ጥንታዊው','ሐውልት','ቆሟል']),A('Verb modifier in "ጎብኚዎቹ ቀስ ብለው ገቡ።"','በ"ጎብኚዎቹ ቀስ ብለው ገቡ።" ተውሳከ ግሥ',['ቀስ ብለው','ጎብኚዎቹ','ገቡ']),
  A('Which is a dependent clause?','ጥገኛ ሐረግ የትኛው ነው?',['ዝናቡ ሲዘንብ','ዝናቡ ዘነበ።','ቤተ ክርስቲያኑ ቆንጆ ነው።']),A('Tense of "ቅርሱን ጎበኘን።"','የ"ቅርሱን ጎበኘን።" ጊዜ',['ኃላፊ','ትንቢት','ትእዛዝ'])]),
 build([['ቅርሶቻችንን','በጥንቃቄ','መጠበቅ','አለብን።'],['ላሊበላ','በዓለም','ቅርስነት','ተመዝግቧል።']])],
 [A('Lalibela was registered by UNESCO in…','ላሊበላ በዩኔስኮ የተመዘገበው በ…',['1978 እ.ኤ.አ.','2000 እ.ኤ.አ.','1896 እ.ኤ.አ.']),A('ቅጽል describes a…','ቅጽል የሚገልጸው…',['ስም','ግሥ','ዓረፍተ ነገር ብቻ']),A('Dependent clause in "ሰዎቹ ሲደርሱ በሩ ተከፈተ።"','በ"ሰዎቹ ሲደርሱ በሩ ተከፈተ።" ጥገኛ ሐረጉ',['ሰዎቹ ሲደርሱ','በሩ ተከፈተ','ተከፈተ']),A('Another heritage site in Amhara region','ሌላ በአማራ ክልል ያለ ቅርስ',['የጎንደር ፋሲል ግንብ','የሶፍ ዑመር ዋሻ','የአክሱም ሐውልት'])],
 notes(('Ethiopia’s heritage tells our history; we describe it with noun and verb modifiers, dependent clauses and correct tense.','የኢትዮጵያ ቅርስ ታሪካችንን ይነግራል፤ በቅጽል፣ በተውሳከ ግሥ፣ በጥገኛ ሐረግና በትክክለኛ ጊዜ እንገልጸዋለን።'),
  [('Reading about Lalibela and other heritage.','ስለ ላሊበላና ሌሎች ቅርሶች ማንበብ።'),('Noun modifiers (ቅጽል) and verb modifiers (ተውሳከ ግሥ).','ቅጽልና ተውሳከ ግሥ።'),('Dependent clauses (ሲ-, ስለ-, ከ-…).','ጥገኛ ሐረጎች (ሲ-፣ ስለ-፣ ከ-…)።'),('Past and non-past tense.','ኃላፊና ኃላፊ ያልሆነ ጊዜ።')],
  [('ቅርስ','heritage','የተላለፈ ሀብት'),('ቅጽል','adjective','ስም ገላጭ'),('ተውሳከ ግሥ','adverb','ግሥ ገላጭ')],('ቅጽል → ስም፤ ተውሳከ ግሥ → ግሥ።','ቅጽል → ስም፤ ተውሳከ ግሥ → ግሥ።'),
  [(('Add a modifier: "ሐውልቱ ቆሟል።"','ገላጭ ጨምሩ፦ "ሐውልቱ ቆሟል።"'),'ረጅሙ ሐውልት ቆሟል።'),(('Name 3 heritage sites in Ethiopia','በኢትዮጵያ 3 ቅርሶችን ጥቀሱ'),'ላሊበላ፣ ፋሲል ግንብ፣ አክሱም')],
  inn(('Heritage QR guide','የቅርስ QR መሪ'),('Visitors like short guides. Make a bilingual audio guide for a local heritage site.','ጎብኚዎች አጭር መሪዎችን ይወዳሉ። ለአካባቢ ቅርስ ባለሁለት ቋንቋ የድምፅ መሪ ሥሩ።'),[('Choose a church, castle, monastery or old tree.','ቤተ ክርስቲያን፣ ቤተ መንግሥት፣ ገዳም ወይም ጥንታዊ ዛፍ ምረጡ።'),('Write 5 sentences with modifiers about it.','ገላጮች ያሏቸው 5 ዓረፍተ ነገሮችን ጻፉ።'),('Record them in Amharic and English.','በአማርኛና በእንግሊዝኛ ቅዱ።'),('Ask a teacher to help link them to a QR code.','ከQR ኮድ ጋር እንዲያገናኙ መምህራችሁን ጠይቁ።')])),
 sm(('Describing heritage','ቅርስን መግለጽ'),[('Reading','ንባብ'),('Modifiers','ገላጮች'),('Dependent clauses','ጥገኛ ሐረጎች'),('Tense','ጊዜ')]),'Heritage')

# 3
U(3,('Human values','ሰብአዊ እሴቶች'),[
 read('የእማማ ዘውዲቱ ቤት',['እማማ ዘውዲቱ በሰፈሩ የታወቁ ደግ ሴት ናቸው። ጎረቤት ሲታመም ገንፎ ያበስላሉ፤ ልጆች ሲራቡ ቂጣ ያካፍላሉ።','አንድ ቀን የጎረቤታቸው ቤት በእሳት ተቃጠለ። እማማ ዘውዲቱ ቤተሰቡን ወደ ቤታቸው አስገቡ። የሰፈሩ ሰዎችም ተሰብስበው አዲስ ቤት ሠሩላቸው።','"መተሳሰብ ከሌለ ሰውነት የለም" ይላሉ እማማ። ርኅራኄ፣ መተባበርና መከባበር የሰው ልጅ ውድ እሴቶች ናቸው።'],[
  A('What happened to the neighbour?','በጎረቤቱ ላይ ምን ደረሰ?',['ቤታቸው በእሳት ተቃጠለ','ሀብታም ሆኑ','ወደ ውጭ ሄዱ']),A('What did the community do?','ሰፈሩ ምን አደረገ?',['አዲስ ቤት ሠራላቸው','ምንም አላደረገም','ሰፈሩን ለቀቀ']),A('Which value does the story teach?','ታሪኩ የሚያስተምረው እሴት?',['መተሳሰብና መተባበር','ራስ ወዳድነት','ቁጣ'])]),
 vmatch([('ርኅራኄ','ለሌሎች ማዘን'),('መተባበር','በጋራ መሥራት'),('መከባበር','እርስ በርስ ማክበር'),('ደግ','ቸር፣ ለጋስ')]),
 quiz(('Plurals and agreement','ብዙ ቁጥርና ስምምነት'),('Most Amharic plurals add -ዎች or -ኦች: ልጅ → ልጆች, ቤት → ቤቶች. The verb must agree with the subject in number, person and gender: ልጁ መጣ, ልጆቹ መጡ, ልጅቷ መጣች.','አብዛኞቹ የአማርኛ ብዙ ቁጥሮች -ዎች ወይም -ኦች ይጨምራሉ፦ ልጅ → ልጆች፣ ቤት → ቤቶች። ግሡ ከባለቤቱ ጋር በቁጥር፣ በመደብና በጾታ መስማማት አለበት፦ ልጁ መጣ፣ ልጆቹ መጡ፣ ልጅቷ መጣች።'),[
  A('Plural of "ጎረቤት"','የ"ጎረቤት" ብዙ ቁጥር',['ጎረቤቶች','ጎረቤትዎች','ጎረቤቲ']),A('Plural of "ቤተሰብ"','የ"ቤተሰብ" ብዙ ቁጥር',['ቤተሰቦች','ቤተሰብዎች','ቤተሰቢ']),
  W('ልጆቹ ለጎረቤታቸው ምግብ ___።',['አመጡ','አመጣ','አመጣች']),W('እማማ ዘውዲቱ ገንፎ ___።',['አበሰሉ','አበሰለ','አበሰልን']),A('Which sentence has correct agreement?','ስምምነቱ ትክክል የሆነው?',['ሰዎቹ ቤት ሠሩ።','ሰዎቹ ቤት ሠራ።','ሰዎቹ ቤት ሠራች።'])]),
 build([['ደግ','ሰዎች','ሌሎችን','ይረዳሉ።'],['መከባበር','ሰላምን','ያመጣል።']])],
 [A('Plural of "ተማሪ"','የ"ተማሪ" ብዙ ቁጥር',['ተማሪዎች','ተማሪኦች','ተማሪቶች']),W('ሴቶቹ ወደ ገበያ ___።',['ሄዱ','ሄደ','ሄደች']),A('Meaning of ርኅራኄ','የ"ርኅራኄ" ፍቺ',['ለሌሎች ማዘን','መቆጣት','መሸሽ']),A('A human value is…','ሰብአዊ እሴት የሆነው…',['መከባበር','ስርቆት','ውሸት'])],
 notes(('Kindness, cooperation and respect are human values; we use plurals and make verbs agree with their subjects.','ደግነት፣ መተባበርና መከባበር ሰብአዊ እሴቶች ናቸው፤ ብዙ ቁጥርን እንጠቀማለን፤ ግሦችን ከባለቤታቸው ጋር እናስማማለን።'),
  [('Reading a story about caring neighbours.','ስለ ተሳሳቢ ጎረቤቶች ታሪክ ማንበብ።'),('Vocabulary for values.','የእሴት ቃላት።'),('Plurals: -ዎች / -ኦች.','ብዙ ቁጥር፦ -ዎች / -ኦች።'),('Subject–verb agreement.','የባለቤትና የግሥ ስምምነት።')],
  [('እሴት','value','ውድ የሆነ መርሕ'),('ብዙ ቁጥር','plural','ከአንድ በላይ'),('ስምምነት','agreement','መጣጣም')],('Many subjects, many verbs: ልጆቹ መጡ.','ብዙ ባለቤት፣ ብዙ ግሥ፦ ልጆቹ መጡ።'),
  [(('Correct: "ተማሪዎቹ መጣ።"','አስተካክሉ፦ "ተማሪዎቹ መጣ።"'),'ተማሪዎቹ መጡ።'),(('Plural of "ከተማ"','የ"ከተማ" ብዙ ቁጥር'),'ከተሞች')],
  inn(('Kindness box','የደግነት ሣጥን'),('Organise a box where students donate exercise books and clothes for those in need.','ተማሪዎች ለተቸገሩ ደብተርና ልብስ የሚለግሱበት ሣጥን አደራጁ።'),[('Get permission from the school.','ከትምህርት ቤቱ ፈቃድ አግኙ።'),('Make a poster with plural nouns and correct verbs.','በብዙ ቁጥር ስሞችና በትክክለኛ ግሦች ፖስተር ሥሩ።'),('Collect and record donations each week.','በየሳምንቱ ስጦታዎችን ሰብስቡና መዝግቡ።'),('Hand them over with the school leaders.','ከትምህርት ቤቱ አመራሮች ጋር አስረክቡ።')])),
 sm(('Values and agreement','እሴቶችና ስምምነት'),[('Reading','ንባብ'),('Vocabulary','ቃላት'),('Plurals','ብዙ ቁጥር'),('Agreement','ስምምነት')]),'Human values')

# 4
U(4,('Short story','አጭር ልቦለድ'),[
 read('የብርቱካን ዛፍ',['ታደለ የአሥራ አራት ዓመት ልጅ ነበር። አያቱ ከመሞታቸው በፊት "ይህን ትንሽ ብርቱካን ተንከባከበው" ብለው ችግኝ ሰጡት።','ታደለ በየቀኑ ውኃ አጠጣው። ድርቅ በመጣ ጊዜ ከወንዙ ውኃ በእንስራ እያመላለሰ አዳነው። ጓደኞቹ "ለምን ትደክማለህ?" ብለው ሳቁበት።','ከአምስት ዓመት በኋላ ዛፉ ብዙ ፍሬ አፈራ። ታደለ ፍሬውን ሸጦ የትምህርት ቤት ክፍያውን ከፈለ። ያኔ ጓደኞቹ ትዕግሥት ፍሬ እንዳለው ተረዱ።'],[
  A('Who gave Tadele the seedling?','ለታደለ ችግኙን የሰጠው ማን ነው?',['አያቱ','መምህሩ','ጓደኛው']),A('What is the climax (turning point)?','ቁንጮው (የለውጥ ነጥቡ) ምንድን ነው?',['ድርቅ መጥቶ ዛፉን ሲያድነው','ችግኙን ሲቀበል','ፍሬውን ሲበላ']),A('Theme of the story','የታሪኩ ጭብጥ',['ትዕግሥትና ትጋት ፍሬ አላቸው','ዛፍ መቁረጥ ጥሩ ነው','ጓደኛ አያስፈልግም'])]),
 vmatch([('ገጸ ባሕርይ','በታሪኩ ውስጥ ያለ ሰው'),('መቼት','ታሪኩ የተፈጸመበት ጊዜና ቦታ'),('ጭብጥ','የታሪኩ ዋና መልእክት'),('ሴራ','የሁነቶች ቅደም ተከተል')]),
 quiz(('Word order; simple and compound sentences','የቃላት ቅደም ተከተል፤ ነጠላና ውሑድ ዓረፍተ ነገር'),('Amharic word order is subject – object – verb: ታደለ ዛፉን አጠጣ. A simple sentence has one verb. A compound sentence joins two with እና, ግን, ወይም, ስለዚህ, or a semicolon.','የአማርኛ የቃላት ቅደም ተከተል ባለቤት – ተሳቢ – ግሥ ነው፦ ታደለ ዛፉን አጠጣ። ነጠላ ዓረፍተ ነገር አንድ ግሥ አለው። ውሑድ ዓረፍተ ነገር ሁለቱን በእና፣ ግን፣ ወይም፣ ስለዚህ ወይም በድርብ ሰረዝ ያጣምራል።'),[
  A('Correct order','ትክክለኛው ቅደም ተከተል',['ታደለ ውኃ አመላለሰ።','ውኃ አመላለሰ ታደለ።','አመላለሰ ታደለ ውኃ።']),A('Which is compound?','ውሑድ የሆነው?',['ዛፉ አደገ፤ ፍሬም አፈራ።','ዛፉ አደገ።','ታደለ ደከመ።']),
  W('ጓደኞቹ ሳቁበት፤ ___ ታደለ ተስፋ አልቆረጠም።',['ግን','ስለዚህ','ወይም']),A('The object in "ታደለ ፍሬውን ሸጠ።"','በ"ታደለ ፍሬውን ሸጠ።" ተሳቢው',['ፍሬውን','ታደለ','ሸጠ'])]),
 order(('Order the plot','ሴራውን ደርድሩ'),('A plot has a beginning, a problem, a climax and an ending.','ሴራ መጀመሪያ፣ ችግር፣ ቁንጮና መጨረሻ አለው።'),('Tap events in the order they happened.','ሁነቶቹን በተፈጸሙበት ቅደም ተከተል ንኩ።'),[(('The orange tree','የብርቱካን ዛፍ'),['አያቱ ችግኝ ሰጡት።','በየቀኑ አጠጣው።','ድርቅ መጣ።','ከወንዙ ውኃ አመላለሰ።','ዛፉ ፍሬ አፈራ።'])])],
 [A('Setting means…','መቼት ማለት…',['የታሪኩ ጊዜና ቦታ','ዋናው ገጸ ባሕርይ','የመጽሐፉ ዋጋ']),A('Simple sentence','ነጠላ ዓረፍተ ነገር',['ዝናብ ዘነበ።','ዝናብ ዘነበ፤ ወንዙም ሞላ።','ዝናብ ዘነበ ግን አልበረደም።']),A('Amharic word order','የአማርኛ የቃላት ቅደም ተከተል',['ባለቤት – ተሳቢ – ግሥ','ግሥ – ባለቤት – ተሳቢ','ተሳቢ – ግሥ – ባለቤት']),A('The main character','ዋናው ገጸ ባሕርይ',['ታደለ','አያቱ','ጓደኞቹ'])],
 notes(('A short story has characters, setting, plot and a theme; Amharic sentences follow subject–object–verb and can be simple or compound.','አጭር ልቦለድ ገጸ ባሕርያት፣ መቼት፣ ሴራና ጭብጥ አለው፤ የአማርኛ ዓረፍተ ነገር ባለቤት–ተሳቢ–ግሥ ይከተላል፤ ነጠላ ወይም ውሑድ ሊሆን ይችላል።'),
  [('Elements of a short story.','የአጭር ልቦለድ ክፍሎች።'),('Plot: beginning, problem, climax, end.','ሴራ፦ መጀመሪያ፣ ችግር፣ ቁንጮ፣ መጨረሻ።'),('Word order S–O–V.','የቃላት ቅደም ተከተል ባ–ተ–ግ።'),('Simple vs compound sentences.','ነጠላና ውሑድ ዓረፍተ ነገሮች።')],
  [('ጭብጥ','theme','ዋና መልእክት'),('ሴራ','plot','የሁነቶች ቅደም ተከተል'),('ውሑድ','compound','የተጣመረ')],('Who? Where? What happened? Why?','ማን? የት? ምን ሆነ? ለምን?'),
  [(('Join into a compound sentence: "ታደለ ደከመ። ዛፉ ዳነ።"','ውሑድ አድርጉ፦ "ታደለ ደከመ። ዛፉ ዳነ።"'),'ታደለ ደከመ፤ ስለዚህ ዛፉ ዳነ።'),(('Name 4 elements of a short story','4 የአጭር ልቦለድ ክፍሎችን ጥቀሱ'),'ገጸ ባሕርይ፣ መቼት፣ ሴራ፣ ጭብጥ')],
  inn(('Class story magazine','የክፍል የልቦለድ መጽሔት'),('Publish your own short stories as a small magazine and sell copies for the school library.','የራሳችሁን አጫጭር ልቦለዶች እንደ ትንሽ መጽሔት አሳትሙ፤ ለትምህርት ቤቱ ቤተ መጻሕፍት ቅጂዎችን ሽጡ።'),[('Each student writes a one-page story with a clear theme.','እያንዳንዱ ተማሪ ግልጽ ጭብጥ ያለው ባለ አንድ ገጽ ታሪክ ይጽፋል።'),('Peer-edit word order and sentence types.','የቃላት ቅደም ተከተልንና የዓረፍተ ነገር ዓይነቶችን በጋራ አርሙ።'),('Design a cover and contents page.','ሽፋንና የማውጫ ገጽ ንደፉ።'),('Print and sell at a small price.','አትሙና በትንሽ ዋጋ ሽጡ።')])),
 sm(('Stories and sentences','ታሪኮችና ዓረፍተ ነገሮች'),[('Story elements','የታሪክ ክፍሎች'),('Plot','ሴራ'),('Word order','የቃላት ቅደም ተከተል'),('Simple/compound','ነጠላ/ውሑድ')]),'Short story')

# 5
U(5,('Population','ሕዝብ'),[
 read('የሕዝብ ቁጥርና ልማት',['ኢትዮጵያ በሕዝብ ብዛት ከአፍሪካ ሀገራት ሁለተኛ ናት። የሕዝቡ ብዛት በፍጥነት ይጨምራል፤ አብዛኛው ሕዝብም ወጣት ነው።','ሕዝብ ሲበዛ የትምህርት ቤት፣ የጤና ጣቢያ፣ የውኃና የሥራ ፍላጎት ይጨምራል። ሀብቱ በቂ ካልሆነ ድህነትና ስደት ሊከሰቱ ይችላሉ።','ነገር ግን የተማረና ጤናማ ወጣት ለሀገር ትልቅ ሀብት ነው። ስለዚህ የሕዝብ ዕድገትን ከልማት ጋር ማመጣጠን ያስፈልጋል።'],[
  A('Ethiopia’s rank in Africa by population','ኢትዮጵያ በሕዝብ ብዛት በአፍሪካ',['ሁለተኛ','አምስተኛ','ዐሥረኛ']),A('What increases when population grows?','ሕዝብ ሲበዛ ምን ይጨምራል?',['የአገልግሎት ፍላጎት','የመሬት ስፋት','የወንዞች ቁጥር']),A('Writer’s view on youth','ጸሐፊው ስለ ወጣቶች ያለው አመለካከት',['የተማረ ወጣት ሀብት ነው','ወጣቶች ችግር ብቻ ናቸው','ወጣቶች ሊሰደዱ ይገባል'])]),
 vmatch([('ዕድገት','መጨመር፣ ማደግ'),('ስደት','ሀገርን ወይም ቀዬን ለቆ መሄድ'),('ማመጣጠን','እኩል ማድረግ'),('ፍላጎት','የሚያስፈልግ ነገር')]),
 quiz(('Compound sentences and non-past tense','ውሑድ ዓረፍተ ነገርና ኃላፊ ያልሆነ ጊዜ'),('Non-past (present/future) verbs often begin with ይ-, ት-, እ-, እን- and end in -ል: ይጨምራል, ትማራለች, እንሠራለን. Compound sentences join ideas with እና, ነገር ግን, ስለዚህ.','ኃላፊ ያልሆነ (የአሁንና የወደፊት) ግሥ ብዙ ጊዜ በይ-፣ ት-፣ እ-፣ እን- ይጀምራል፤ በ-ል ያልቃል፦ ይጨምራል፣ ትማራለች፣ እንሠራለን። ውሑድ ዓረፍተ ነገሮች ሐሳቦችን በእና፣ ነገር ግን፣ ስለዚህ ያጣምራሉ።'),[
  A('Non-past form of "ጨመረ"','የ"ጨመረ" ኃላፊ ያልሆነ ቅርጽ',['ይጨምራል','ጨመረ','አልጨመረም']),W('እኛ ነገ ዛፍ ___።',['እንተክላለን','ተከልን','ተከሉ']),W('ሕዝቡ በዛ፤ ___ የትምህርት ቤት ፍላጎት ጨመረ።',['ስለዚህ','ነገር ግን','ወይም']),A('Tense of "ወጣቶቹ ሥራ ይፈልጋሉ።"','የ"ወጣቶቹ ሥራ ይፈልጋሉ።" ጊዜ',['ኃላፊ ያልሆነ','ኃላፊ','ትእዛዝ'])]),
 build([['የተማረ','ወጣት','የሀገር','ሀብት','ነው።'],['ሕዝቡ','ይጨምራል፤','ስለዚህ','ልማት','ያስፈልጋል።']])],
 [A('Non-past of "ተማረች"','የ"ተማረች" ኃላፊ ያልሆነ ቅርጽ',['ትማራለች','ተማረች','አልተማረችም']),A('Meaning of ስደት','የ"ስደት" ፍቺ',['ቀዬን ለቆ መሄድ','መወለድ','መማር']),A('A conjunction for result','ውጤት የሚያሳይ አያያዥ',['ስለዚህ','ነገር ግን','ወይም']),A('Rapid population growth increases demand for…','ፈጣን የሕዝብ ዕድገት የሚጨምረው የ… ፍላጎት',['ትምህርትና ጤና','ጦርነት','በረሃ'])],
 notes(('Population growth brings both challenges and opportunities; we write compound sentences and use the non-past tense.','የሕዝብ ዕድገት ፈተናዎችንም ዕድሎችንም ያመጣል፤ ውሑድ ዓረፍተ ነገሮችን እንጽፋለን፤ ኃላፊ ያልሆነ ጊዜን እንጠቀማለን።'),
  [('Reading about population and development.','ስለ ሕዝብና ልማት ማንበብ።'),('Vocabulary of growth and needs.','የዕድገትና የፍላጎት ቃላት።'),('Non-past verbs: ይ-…-ል.','ኃላፊ ያልሆነ ግሥ፦ ይ-…-ል።'),('Compound sentences: እና, ነገር ግን, ስለዚህ.','ውሑድ ዓረፍተ ነገሮች፦ እና፣ ነገር ግን፣ ስለዚህ።')],
  [('ሕዝብ','population','በአንድ ቦታ የሚኖሩ ሰዎች'),('ልማት','development','ዕድገትና መሻሻል'),('ኃላፊ ያልሆነ','non-past','የአሁን/የወደፊት')],('ይ-…-ል = now or later.','ይ-…-ል = አሁን ወይም ወደፊት።'),
  [(('Change to non-past: "ሕዝቡ ጨመረ።"','ወደ ኃላፊ ያልሆነ ቀይሩ፦ "ሕዝቡ ጨመረ።"'),'ሕዝቡ ይጨምራል።'),(('Give 2 effects of rapid population growth','የፈጣን ሕዝብ ዕድገት 2 ውጤቶችን ስጡ'),'የሥራ እጥረት፣ የአገልግሎት ጫና')],
  inn(('Youth skills map','የወጣቶች ክህሎት ካርታ'),('Young people are a resource. Map the skills of youth in your kebele and match them to local needs.','ወጣቶች ሀብት ናቸው። በቀበሌያችሁ ያሉ ወጣቶችን ክህሎት ካርታ ሥሩና ከአካባቢ ፍላጎቶች ጋር አዛምዱ።'),[('Survey 20 young people about their skills.','20 ወጣቶችን ስለ ክህሎታቸው ጠይቁ።'),('List what the community needs.','ማኅበረሰቡ የሚፈልገውን ዘርዝሩ።'),('Match skills to needs in a table.','ክህሎትን ከፍላጎት ጋር በሰንጠረዥ አዛምዱ።'),('Present one small business idea.','አንድ ትንሽ የንግድ ሐሳብ አቅርቡ።')])),
 sm(('People and progress','ሕዝብና ዕድገት'),[('Reading','ንባብ'),('Vocabulary','ቃላት'),('Non-past tense','ኃላፊ ያልሆነ ጊዜ'),('Compound sentences','ውሑድ ዓረፍተ ነገሮች')]),'Population')

# 6
U(6,('Desertification','በረሃማነት'),[
 read('አረንጓዴ የነበረው ኮረብታ',['ከሠላሳ ዓመት በፊት ከመንደራችን አጠገብ ያለው ኮረብታ በደን የተሸፈነ ነበር። ምንጮችም ዓመቱን ሙሉ ይፈስሱ ነበር።','ሰዎች ዛፎችን ለማገዶና ለእርሻ ቆረጡ። ከብቶችም ሣሩን ጨረሱት። ዝናብ ሲዘንብ አፈሩ ታጥቦ ሄደ፤ ምንጮቹም ደረቁ።','ዛሬ የመንደሩ ሰዎች እርከን እየሠሩ፣ ችግኝ እየተከሉና ልቅ ግጦሽን እያስቀሩ ነው። ኮረብታው ቀስ በቀስ ወደ አረንጓዴነቱ እየተመለሰ ነው።'],[
  A('What covered the hill 30 years ago?','ከ30 ዓመት በፊት ኮረብታውን የሸፈነው?',['ደን','አሸዋ','ቤቶች']),A('Causes of the change','የለውጡ ምክንያቶች',['ዛፍ መቁረጥና ልቅ ግጦሽ','ብዙ ዝናብ ብቻ','የመንገድ ግንባታ ብቻ']),A('What are people doing now?','አሁን ሰዎች ምን እያደረጉ ነው?',['እርከን መሥራትና ችግኝ መትከል','ተጨማሪ ዛፍ መቁረጥ','መንደሩን መልቀቅ'])]),
 vmatch([('በረሃማነት','መሬት ወደ በረሃነት መለወጥ'),('እርከን','አፈርን የሚይዝ ደረጃ'),('ማገዶ','ለማንደጃ የሚውል እንጨት'),('ልቅ ግጦሽ','ቁጥጥር የሌለው ግጦሽ')]),
 quiz(('Positive, negative and question sentences (review)','አዎንታዊ፣ አሉታዊና መጠይቃዊ (ክለሳ)'),('Question words: ማን (who), ምን (what), የት (where), መቼ (when), ለምን (why), እንዴት (how). Negative non-past uses አ-…-ም: ይፈስሳል → አይፈስም.','የጥያቄ ቃላት፦ ማን፣ ምን፣ የት፣ መቼ፣ ለምን፣ እንዴት። ኃላፊ ያልሆነ አሉታዊ አ-…-ም ይጠቀማል፦ ይፈስሳል → አይፈስም።'),[
  A('Negative of "ምንጩ ይፈስሳል።"','የ"ምንጩ ይፈስሳል።" አሉታዊ',['ምንጩ አይፈስም።','ምንጩ ፈሰሰ።','ምንጩ ይፈስሳል?']),W('ኮረብታው ___ ተራቆተ?',['ለምን','እና','ግን']),A('Question word for place','ለቦታ የሚጠቅም የጥያቄ ቃል',['የት','መቼ','ማን']),A('Type of "ችግኝ እንትከል!"','"ችግኝ እንትከል!" ዓይነቱ',['ትእዛዛዊ/አነቃቂ','መጠይቃዊ','አሉታዊ'])]),
 build([['ዛፍ','መትከል','በረሃማነትን','ይከላከላል።'],['ለምን','ምንጮቹ','ደረቁ?']])],
 [A('Desertification is caused by…','በረሃማነት የሚከሰተው በ…',['የደን ጭፍጨፋና ልቅ ግጦሽ','ዛፍ በመትከል','እርከን በመሥራት']),A('Question word for time','ለጊዜ የሚጠቅም የጥያቄ ቃል',['መቼ','የት','ምን']),A('Negative of "ይዘንባል"','የ"ይዘንባል" አሉታዊ',['አይዘንብም','ዘነበ','ይዘንባል?']),A('A solution to soil erosion','ለአፈር መሸርሸር መፍትሔ',['እርከን','ልቅ ግጦሽ','ማቃጠል'])],
 notes(('Deforestation and overgrazing turn land into desert; terraces and trees bring it back. We review positive, negative and question sentences.','የደን ጭፍጨፋና ልቅ ግጦሽ መሬትን ወደ በረሃ ይለውጣሉ፤ እርከንና ዛፍ ይመልሱታል። አዎንታዊ፣ አሉታዊና መጠይቃዊ ዓረፍተ ነገሮችን እንከልሳለን።'),
  [('Causes and effects of desertification.','የበረሃማነት ምክንያትና ውጤት።'),('Solutions: terraces, trees, controlled grazing.','መፍትሔዎች፦ እርከን፣ ዛፍ፣ ቁጥጥር ያለው ግጦሽ።'),('Negative non-past: አ-…-ም.','ኃላፊ ያልሆነ አሉታዊ፦ አ-…-ም።'),('Question words: ማን, ምን, የት, መቼ, ለምን, እንዴት.','የጥያቄ ቃላት፦ ማን፣ ምን፣ የት፣ መቼ፣ ለምን፣ እንዴት።')],
  [('በረሃማነት','desertification','ወደ በረሃነት መለወጥ'),('እርከን','terrace','አፈር የሚይዝ ደረጃ'),('መጠይቅ','question','ጥያቄ')],('Six question words: ማን ምን የት መቼ ለምን እንዴት.','ስድስት የጥያቄ ቃላት፦ ማን ምን የት መቼ ለምን እንዴት።'),
  [(('Make a question with ለምን about the hill','ስለ ኮረብታው በ"ለምን" ጠይቁ'),'ኮረብታው ለምን ተራቆተ?'),(('Two causes of desertification','ሁለት የበረሃማነት ምክንያቶች'),'የደን ጭፍጨፋ፣ ልቅ ግጦሽ')],
  inn(('Fuel-saving stove campaign','የማገዶ ቆጣቢ ምድጃ ዘመቻ'),('Less firewood means more trees. Promote improved stoves in your village.','ያነሰ ማገዶ ማለት ብዙ ዛፍ ማለት ነው። በመንደራችሁ የተሻሻሉ ምድጃዎችን አስተዋውቁ።'),[('Find how much wood a family uses in a week.','አንድ ቤተሰብ በሳምንት ምን ያህል እንጨት እንደሚጠቀም ፈልጉ።'),('Compare with an improved stove.','ከተሻሻለ ምድጃ ጋር አወዳድሩ።'),('Make a short Amharic radio-style message.','አጭር የሬዲዮ ዓይነት የአማርኛ መልእክት ሥሩ።'),('Share it at a community meeting.','በማኅበረሰብ ስብሰባ አጋሩት።')])),
 sm(('Land, trees and questions','መሬት፣ ዛፍና ጥያቄዎች'),[('Causes','ምክንያቶች'),('Solutions','መፍትሔዎች'),('Negative sentences','አሉታዊ ዓረፍተ ነገሮች'),('Question words','የጥያቄ ቃላት')]),'Desertification')

# 7
U(7,('Child labour','የሕፃናት ጉልበት ብዝበዛ'),[
 read('የሰላም ሕልም',['ሰላም የዐሥራ ሁለት ዓመት ልጅ ናት። ከገጠር ወደ ከተማ መጥታ በሰው ቤት ትሠራለች። ጠዋት በጣም ቀድማ ትነሣለች፤ ማታ በጣም አምሽታ ትተኛለች።','ትምህርት ቤት መሄድ ትፈልጋለች፤ ነገር ግን አሠሪዋ አይፈቅዱላትም። አንድ ቀን የሴቶችና ሕፃናት ጉዳይ ባለሙያ ሁኔታዋን ሰማች።','ባለሙያዋ ከአሠሪዋ ጋር ተነጋገረች። አሁን ሰላም በማታ ትምህርት ትማራለች። "ሕፃናት መሥራት ሳይሆን መማር አለባቸው" ትላለች።'],[
  A('How old is Selam?','ሰላም ዕድሜዋ ስንት ነው?',['12','16','20']),A('What problem does she face?','የሚገጥማት ችግር',['ብዙ ሥራና የትምህርት መከልከል','የምግብ ብዛት','በጣም ብዙ መጫወቻ']),A('Who helped her?','የረዳት ማን ነው?',['የሴቶችና ሕፃናት ጉዳይ ባለሙያ','ጎረቤቷ','ፖሊስ ብቻ'])]),
 vmatch([('ብዝበዛ','አግባብ ባልሆነ መንገድ መጠቀም'),('አሠሪ','ሥራ የሚያሠራ ሰው'),('መብት','በሕግ የተፈቀደ ነገር'),('ባለሙያ','ልዩ ዕውቀት ያለው')]),
 quiz(('Adverbs and sentence functions','ተውሳከ ግሥና የዓረፍተ ነገር ተግባራት'),('Adverbs tell how, when or where: ቀድማ, ማታ, በጣም. Sentences can state (ገላጭ), ask (መጠይቃዊ), command (ትእዛዛዊ) or exclaim (አጋናኝ: እንዴት ያሳዝናል!).','ተውሳከ ግሥ እንዴት፣ መቼ ወይም የት እንደሆነ ይገልጻል፦ ቀድማ፣ ማታ፣ በጣም። ዓረፍተ ነገሮች ይገልጻሉ (ገላጭ)፣ ይጠይቃሉ (መጠይቃዊ)፣ ያዝዛሉ (ትእዛዛዊ) ወይም ስሜት ያጋንናሉ (አጋናኝ፦ እንዴት ያሳዝናል!)።'),[
  A('Adverb in "ሰላም ማታ ትማራለች።"','በ"ሰላም ማታ ትማራለች።" ተውሳከ ግሥ',['ማታ','ሰላም','ትማራለች']),A('Function of "ልጆችን አታሠሩ!"','የ"ልጆችን አታሠሩ!" ተግባር',['ትእዛዛዊ','መጠይቃዊ','ገላጭ']),A('Exclamatory sentence','አጋናኝ ዓረፍተ ነገር',['እንዴት ያሳዝናል!','ሰላም ትማራለች።','ሰላም የት ናት?']),W('ሕፃናት ___ መማር አለባቸው።',['በደንብ','ደንብ','ደንቦች'])]),
 build([['ሕፃናት','መሥራት','ሳይሆን','መማር','አለባቸው።'],['ሰላም','በጣም','ቀድማ','ትነሣለች።']])],
 [A('Child labour harms…','የሕፃናት ጉልበት ብዝበዛ የሚጎዳው…',['ጤናንና ትምህርትን','ደስታን ብቻ ይጨምራል','ምንም']),A('Command sentence','ትእዛዛዊ ዓረፍተ ነገር',['ወደ ትምህርት ቤት ሂጂ!','ትምህርት ቤት ሄደች።','ትምህርት ቤት ሄደች?']),A('Adverb of manner','የአኳኋን ተውሳከ ግሥ',['ቀስ ብሎ','ቤት','ልጅ']),A('Every child has the right to…','እያንዳንዱ ሕፃን መብት አለው…',['ለመማርና ለመጫወት','ለከባድ ሥራ','ለመሰደድ'])],
 notes(('Children have the right to learn and play, not to be exploited; we use adverbs and four sentence functions.','ሕፃናት የመማርና የመጫወት መብት አላቸው፤ ሊበዘበዙ አይገባም፤ ተውሳከ ግሥንና አራቱን የዓረፍተ ነገር ተግባራት እንጠቀማለን።'),
  [('Reading about child labour and rights.','ስለ ሕፃናት ጉልበት ብዝበዛና መብት ማንበብ።'),('Vocabulary: ብዝበዛ, መብት, አሠሪ.','ቃላት፦ ብዝበዛ፣ መብት፣ አሠሪ።'),('Adverbs: how, when, where.','ተውሳከ ግሥ፦ እንዴት፣ መቼ፣ የት።'),('Sentence functions: state, ask, command, exclaim.','የዓረፍተ ነገር ተግባራት፦ ገላጭ፣ መጠይቃዊ፣ ትእዛዛዊ፣ አጋናኝ።')],
  [('ብዝበዛ','exploitation','አግባብ የሌለው አጠቃቀም'),('መብት','right','በሕግ የተፈቀደ'),('ተውሳከ ግሥ','adverb','ግሥ ገላጭ')],('Learn, play, grow — not overwork.','ተማር፣ ተጫወት፣ እደግ — ከአቅም በላይ አትሥራ።'),
  [(('Turn into a command: "ልጆቹ ይማራሉ።"','ትእዛዛዊ አድርጉ፦ "ልጆቹ ይማራሉ።"'),'ልጆች ሆይ፣ ተማሩ!'),(('Two effects of child labour','የሕፃናት ጉልበት ብዝበዛ ሁለት ውጤቶች'),'ትምህርት ማቋረጥ፣ የጤና ጉዳት')],
  inn(('Evening-class helper','የማታ ትምህርት ረዳት'),('Many working children cannot attend day school. Plan a peer-tutoring evening club.','ብዙ ሠራተኛ ሕፃናት የቀን ትምህርት መከታተል አይችሉም። የአቻ ለአቻ የማታ ክበብ አቅዱ።'),[('Ask the school for a room and a teacher sponsor.','ከትምህርት ቤቱ ክፍልና ተቆጣጣሪ መምህር ጠይቁ።'),('Prepare simple reading and maths cards.','ቀላል የንባብና የሂሳብ ካርዶች አዘጋጁ።'),('Invite children through community leaders.','በማኅበረሰብ መሪዎች በኩል ሕፃናትን ጋብዙ።'),('Track attendance and progress.','መገኘትንና ዕድገትን ተከታተሉ።')])),
 sm(('Rights and sentence functions','መብትና የዓረፍተ ነገር ተግባራት'),[('Reading','ንባብ'),('Vocabulary','ቃላት'),('Adverbs','ተውሳከ ግሦች'),('Sentence functions','ተግባራት')]),'Child labour')

# 8
U(8,('Peace','ሰላም'),[
 read('የሽማግሌዎቹ ዳኝነት',['በሁለት ቀበሌዎች መካከል ስለ ግጦሽ መሬት ክርክር ተነሣ። ወጣቶቹ ተቆጥተው ለጠብ ተዘጋጁ።','የሁለቱም ቀበሌ ሽማግሌዎች በዛፍ ሥር ተሰበሰቡ። ሁለቱንም ወገኖች በትዕግሥት አዳመጡ፤ መሬቱን በጊዜ ተራ እንዲጠቀሙበት ወሰኑ።','ወጣቶቹ ውሳኔውን ተቀበሉ፤ ተጨባብጠውም ታረቁ። ሰላም ሲኖር ልማት ያድጋል፤ ልጆችም ያለ ፍርሃት ይማራሉ።'],[
  A('What was the dispute about?','ክርክሩ ስለ ምን ነበር?',['የግጦሽ መሬት','የትምህርት ቤት','ውኃ ብቻ']),A('Who solved it?','ማን ፈታው?',['ሽማግሌዎች','ፖሊስ','ወጣቶቹ ብቻቸውን']),A('What was the decision?','ውሳኔው ምን ነበር?',['መሬቱን በጊዜ ተራ መጠቀም','መሬቱን መሸጥ','መዋጋት'])]),
 vmatch([('እርቅ','ከጠብ በኋላ መስማማት'),('ሽምግልና','በሽማግሌ ማስታረቅ'),('ወገን','በክርክሩ ያለ አካል'),('ትዕግሥት','ሳይቸኩሉ መጠበቅ')]),
 quiz(('Verb forms, past tense and interview questions','የግሥ ቅርጾች፣ ኃላፊ ጊዜና የቃለ መጠይቅ ጥያቄዎች'),('Past tense: ተሰበሰቡ, ወሰኑ, ታረቁ. Many verbs change form for person: ወሰንኩ (I), ወሰንን (we), ወሰኑ (they). Interview questions should be clear and open: "ሰላም ለማምጣት ምን አደረጋችሁ?"','ኃላፊ ጊዜ፦ ተሰበሰቡ፣ ወሰኑ፣ ታረቁ። ብዙ ግሦች በመደብ ቅርጻቸው ይለወጣል፦ ወሰንኩ (እኔ)፣ ወሰንን (እኛ)፣ ወሰኑ (እነርሱ)። የቃለ መጠይቅ ጥያቄዎች ግልጽና ክፍት መሆን አለባቸው፦ "ሰላም ለማምጣት ምን አደረጋችሁ?"'),[
  W('እኛ ሽማግሌዎቹን ___።',['አዳመጥን','አዳመጡ','አዳመጠች']),W('እኔ ከጓደኛዬ ጋር ___።',['ታረቅሁ','ታረቁ','ታረቅን']),A('Best open interview question','ምርጡ ክፍት የቃለ መጠይቅ ጥያቄ',['ክርክሩን እንዴት ፈታችሁት?','ታረቃችሁ?','ስምህ አበበ ነው?']),A('Past tense verb','የኃላፊ ጊዜ ግሥ',['ተጨባበጡ','ይጨባበጣሉ','ይጨባበጡ'])]),
 build([['ሽማግሌዎቹ','ሁለቱንም','ወገኖች','አዳመጡ።'],['ሰላም','ሲኖር','ልማት','ያድጋል።']])],
 [A('Indigenous peace-making uses…','ሀገር በቀል የሰላም ማስፈኛ የሚጠቀመው…',['ሽማግሌዎችን','ጦር መሣሪያን','ማስፈራራትን']),W('እነርሱ ውሳኔውን ___።',['ተቀበሉ','ተቀበልኩ','ተቀበለች']),A('Open questions begin with…','ክፍት ጥያቄዎች የሚጀምሩት በ…',['እንዴት/ለምን','አዎ/አይ','ስም']),A('Meaning of እርቅ','የ"እርቅ" ፍቺ',['ከጠብ በኋላ መስማማት','መጣላት','መሸሽ'])],
 notes(('Peace grows when people listen and elders mediate; we use past-tense verb forms and ask good interview questions.','ሰዎች ሲደማመጡና ሽማግሌዎች ሲያስታርቁ ሰላም ያድጋል፤ የኃላፊ ጊዜ የግሥ ቅርጾችን እንጠቀማለን፤ ጥሩ የቃለ መጠይቅ ጥያቄዎችን እንጠይቃለን።'),
  [('Reading about traditional mediation.','ስለ ባህላዊ ሽምግልና ማንበብ።'),('Vocabulary of peace.','የሰላም ቃላት።'),('Past tense and person forms.','ኃላፊ ጊዜና የመደብ ቅርጾች።'),('Interview: clear, open questions.','ቃለ መጠይቅ፦ ግልጽና ክፍት ጥያቄዎች።')],
  [('ሰላም','peace','ጠብ የሌለበት ሁኔታ'),('ሽምግልና','mediation','ማስታረቅ'),('ቃለ መጠይቅ','interview','ጥያቄና መልስ')],('Listen first, judge later.','መጀመሪያ አድምጥ፣ ከዚያ ፍረድ።'),
  [(('Change to "we": "ታረቁ"','ወደ "እኛ" ቀይሩ፦ "ታረቁ"'),'ታረቅን'),(('Write one open interview question for an elder','ለሽማግሌ አንድ ክፍት ጥያቄ ጻፉ'),'ግጭትን እንዴት ታስታርቃላችሁ?')],
  inn(('School peace club podcast','የትምህርት ቤት የሰላም ክበብ ፖድካስት'),('Interview elders and students about solving conflicts peacefully.','ግጭትን በሰላም ስለ መፍታት ሽማግሌዎችንና ተማሪዎችን ቃለ መጠይቅ አድርጉ።'),[('Write 5 open interview questions.','5 ክፍት የቃለ መጠይቅ ጥያቄዎችን ጻፉ።'),('Record one elder and two students.','አንድ ሽማግሌና ሁለት ተማሪዎችን ቅዱ።'),('Edit to a 5-minute episode.','ወደ 5 ደቂቃ ክፍል አርሙ።'),('Play it at the school mini-media.','በትምህርት ቤቱ ሚኒ ሚዲያ አጫውቱ።')])),
 sm(('Making peace with words','በቃል ሰላም ማስፈን'),[('Reading','ንባብ'),('Vocabulary','ቃላት'),('Past tense forms','የኃላፊ ጊዜ ቅርጾች'),('Interviews','ቃለ መጠይቅ')]),'Peace')

# 9
U(9,('Climate change','የአየር ንብረት ለውጥ'),[
 read('ዝናቡ ለምን ዘገየ?',['አያቴ በልጅነታቸው ክረምቱ በሰኔ እንደሚገባ ይነግሩኛል። አሁን ግን ዝናቡ አንዳንዴ ይዘገያል፤ አንዳንዴ ደግሞ ጎርፍ ያመጣል።','ሳይንቲስቶች እንደሚሉት ሰዎች ነዳጅ ሲያቃጥሉና ደን ሲጨፈጭፉ ሙቀት አማቂ ጋዞች ይበዛሉ። ይህም የምድርን ሙቀት ስለሚጨምር የአየር ንብረት ይለወጣል።','ገበሬዎች ድርቅን የሚቋቋሙ ዘሮችን ቢዘሩ፣ ውኃ ቢያቆሩና ዛፍ ቢተክሉ ጉዳቱን መቀነስ ይችላሉ።'],[
  A('What has changed about the rain?','በዝናቡ ላይ ምን ተለወጠ?',['ይዘገያል ወይም ጎርፍ ያመጣል','ፈጽሞ አይለወጥም','በየቀኑ ይዘንባል']),A('What increases greenhouse gases?','ሙቀት አማቂ ጋዞችን የሚያበዛው?',['ነዳጅ ማቃጠልና ደን መጨፍጨፍ','ዛፍ መትከል','ውኃ ማቆር']),A('One solution for farmers','ለገበሬዎች አንድ መፍትሔ',['ድርቅ የሚቋቋም ዘር መዝራት','ደን መቁረጥ','ማረስ ማቆም'])]),
 vmatch([('ድርቅ','የዝናብ እጥረት'),('ጎርፍ','ብዙ የሚፈስ የዝናብ ውኃ'),('ማቆር','ውኃን ማጠራቀም'),('ሙቀት አማቂ','ሙቀትን የሚይዝ')]),
 quiz(('Dependent clauses and complex sentences','ጥገኛ ሐረጎችና ውስብስብ ዓረፍተ ነገሮች'),('A complex sentence has a main clause and a dependent clause. Dependent markers: ሲ- (when), ስለ- (because), ቢ- (if), እንደ- (as/that), ከ-…በኋላ (after): ዝናቡ ስለዘገየ ሰብሉ ደረቀ.','ውስብስብ ዓረፍተ ነገር ዋና ሐረግና ጥገኛ ሐረግ አለው። የጥገኛ ምልክቶች፦ ሲ-፣ ስለ-፣ ቢ-፣ እንደ-፣ ከ-…በኋላ፦ ዝናቡ ስለዘገየ ሰብሉ ደረቀ።'),[
  A('Dependent clause in "ዝናቡ ስለዘገየ ሰብሉ ደረቀ።"','በ"ዝናቡ ስለዘገየ ሰብሉ ደረቀ።" ጥገኛ ሐረጉ',['ዝናቡ ስለዘገየ','ሰብሉ ደረቀ','ደረቀ']),W('ዛፍ ___ ዝናብ ይጨምራል።',['ብንተክል','ተከልን','እንተክላለን']),A('Which is complex?','ውስብስብ የሆነው?',['ጎርፉ ሲመጣ ሰዎቹ ሸሹ።','ጎርፉ መጣ።','ሰዎቹ ሸሹ።']),A('Marker meaning "if"','"ከሆነ" የሚል ትርጉም ያለው ምልክት',['ቢ-','ሲ-','ስለ-'])]),
 build([['ደን','ስለተጨፈጨፈ','ዝናቡ','ቀነሰ።'],['ውኃ','ብናቁር','ድርቅን','እንቋቋማለን።']])],
 [A('Main cause of climate change','ዋናው የአየር ንብረት ለውጥ ምክንያት',['ሙቀት አማቂ ጋዞች መብዛት','የጨረቃ መውጣት','ተራሮች']),A('ሲ- means…','ሲ- ማለት…',['when','because','if']),A('Main clause in "ገበሬዎቹ ውኃ ስላቆሩ ሰብላቸው ዳነ።"','በ"ገበሬዎቹ ውኃ ስላቆሩ ሰብላቸው ዳነ።" ዋናው ሐረግ',['ሰብላቸው ዳነ','ገበሬዎቹ ውኃ ስላቆሩ','ስላቆሩ']),A('Meaning of ድርቅ','የ"ድርቅ" ፍቺ',['የዝናብ እጥረት','ብዙ ዝናብ','በረዶ'])],
 notes(('Burning fuel and cutting forests change our climate; we explain causes and effects using complex sentences with dependent clauses.','ነዳጅ ማቃጠልና ደን መቁረጥ የአየር ንብረታችንን ይለውጣሉ፤ ምክንያትንና ውጤትን በጥገኛ ሐረግ ያለባቸው ውስብስብ ዓረፍተ ነገሮች እንገልጻለን።'),
  [('Reading on climate change in Ethiopia.','በኢትዮጵያ ስለ አየር ንብረት ለውጥ ማንበብ።'),('Vocabulary: ድርቅ, ጎርፍ, ማቆር.','ቃላት፦ ድርቅ፣ ጎርፍ፣ ማቆር።'),('Dependent markers ሲ-, ስለ-, ቢ-, እንደ-.','የጥገኛ ምልክቶች ሲ-፣ ስለ-፣ ቢ-፣ እንደ-።'),('Complex sentences = main + dependent clause.','ውስብስብ = ዋና + ጥገኛ ሐረግ።')],
  [('የአየር ንብረት','climate','የረጅም ጊዜ የአየር ሁኔታ'),('ጥገኛ ሐረግ','dependent clause','ብቻውን የማይቆም'),('ውስብስብ','complex','ብዙ ክፍል ያለው')],('ሲ = when, ስለ = because, ቢ = if.','ሲ = መቼ፣ ስለ = ምክንያት፣ ቢ = ቅድመ ሁኔታ።'),
  [(('Join with ስለ-: "ደን ተጨፈጨፈ። አፈሩ ታጠበ።"','በስለ- አጣምሩ፦ "ደን ተጨፈጨፈ። አፈሩ ታጠበ።"'),'ደን ስለተጨፈጨፈ አፈሩ ታጠበ።'),(('Two ways to adapt to drought','ድርቅን የመቋቋም ሁለት መንገዶች'),'ውኃ ማቆር፣ ድርቅ የሚቋቋም ዘር')],
  inn(('Rain-water harvesting model','የዝናብ ውኃ ማቆሪያ ሞዴል'),('Build a small model that collects roof water for a school garden.','ለትምህርት ቤት የአትክልት ቦታ የጣራ ውኃ የሚሰበስብ ትንሽ ሞዴል ሥሩ።'),[('Measure the roof area and estimate litres per rain.','የጣራውን ስፋት ለኩና በአንድ ዝናብ ሊትር ገምቱ።'),('Use a gutter, pipe and container.','ቦይ፣ ቱቦና ማጠራቀሚያ ተጠቀሙ።'),('Write instructions with complex sentences.','መመሪያውን በውስብስብ ዓረፍተ ነገሮች ጻፉ።'),('Water the garden and record the results.','የአትክልት ቦታውን አጠጡና ውጤቱን መዝግቡ።')])),
 sm(('Cause, effect and complex sentences','ምክንያት፣ ውጤትና ውስብስብ ዓረፍተ ነገር'),[('Reading','ንባብ'),('Vocabulary','ቃላት'),('Dependent markers','የጥገኛ ምልክቶች'),('Complex sentences','ውስብስብ ዓረፍተ ነገሮች')]),'Climate change')

# 10
U(10,('Drama','ተውኔት'),[
 read('ትንሹ ተውኔት፦ "የገበያ ቀን"',['(መድረኩ የገበያ ቦታ ይመስላል። አልማዝ እንቁላል ትሸጣለች።)','ገዢ፦ እንቁላሉ ስንት ነው? — አልማዝ፦ አንዱ በዐሥር ብር። — ገዢ፦ ውድ ነው! በስምንት ስጪኝ። — አልማዝ፦ (ፈገግ ብላ) ትኩስ ስለሆነ ዋጋው ትክክል ነው፤ ግን ደንበኛዬ ስለሆንክ በዘጠኝ እሰጥሃለሁ።','ገዢ፦ ተስማማሁ! (ገንዘቡን ይከፍላል። መብራቱ ይጠፋል።)'],[
  A('What are the words in brackets called?','በቅንፍ ያሉት ቃላት ምን ይባላሉ?',['የመድረክ መመሪያ','ውይይት','ርዕስ']),A('Where is the setting?','መቼቱ የት ነው?',['ገበያ','ትምህርት ቤት','ሆስፒታል']),A('How is the conflict solved?','ግጭቱ እንዴት ተፈታ?',['በድርድር በዘጠኝ ብር','በጠብ','ገዢው ሄደ'])]),
 vmatch([('ተውኔት','በመድረክ የሚቀርብ ታሪክ'),('ተዋናይ','ገጸ ባሕርይን የሚጫወት'),('መድረክ','ተውኔቱ የሚቀርብበት ቦታ'),('ውይይት','በገጸ ባሕርያት መካከል ንግግር')]),
 quiz(('Dependent clauses, conjunctions and drama elements','ጥገኛ ሐረጎች፣ አያያዦችና የተውኔት ክፍሎች'),('Drama elements: characters, dialogue, stage directions, setting, conflict and theme. Conjunctions (እና, ግን, ወይም, ስለዚህ) and dependent clauses (ስለሆንክ, ሲከፍል) make dialogue natural.','የተውኔት ክፍሎች፦ ገጸ ባሕርያት፣ ውይይት፣ የመድረክ መመሪያ፣ መቼት፣ ግጭትና ጭብጥ። አያያዦች (እና፣ ግን፣ ወይም፣ ስለዚህ) እና ጥገኛ ሐረጎች (ስለሆንክ፣ ሲከፍል) ውይይትን ተፈጥሯዊ ያደርጋሉ።'),[
  A('Dependent clause in "ደንበኛዬ ስለሆንክ በዘጠኝ እሰጥሃለሁ።"','በ"ደንበኛዬ ስለሆንክ በዘጠኝ እሰጥሃለሁ።" ጥገኛ ሐረጉ',['ደንበኛዬ ስለሆንክ','በዘጠኝ እሰጥሃለሁ','እሰጥሃለሁ']),W('ውድ ነው፤ ___ ትኩስ ነው።',['ግን','ስለዚህ','ወይም']),A('Which is NOT a drama element?','የተውኔት ክፍል ያልሆነው?',['የገጽ ቁጥር','ውይይት','ግጭት']),A('A play is mainly written as…','ተውኔት በዋናነት የሚጻፈው በ…',['ውይይት','ግጥም ብቻ','ዜና'])]),
 order(('Stages of putting on a play','ተውኔትን የማቅረብ ደረጃዎች'),('From script to stage.','ከጽሑፍ እስከ መድረክ።'),('Tap the stages in order.','ደረጃዎቹን በቅደም ተከተል ንኩ።'),[(('Stages','ደረጃዎች'),['ጽሑፉን መጻፍ','ተዋናዮችን መምረጥ','ልምምድ ማድረግ','አልባሳትና መድረክ ማዘጋጀት','ለተመልካች ማቅረብ'])])],
 [A('Stage directions tell…','የመድረክ መመሪያ የሚነግረው…',['ተዋናዮች ምን እንደሚያደርጉ','የደራሲውን ዕድሜ','የመጽሐፉን ዋጋ']),A('Conflict in a play is…','በተውኔት ግጭት ማለት…',['የገጸ ባሕርያት ፍላጎት መጋጨት','መብራት','መጋረጃ']),A('Conjunction showing contrast','ተቃርኖ የሚያሳይ አያያዥ',['ግን','እና','ስለዚህ']),A('Person who plays a character','ገጸ ባሕርይን የሚጫወት',['ተዋናይ','ተመልካች','ደራሲ'])],
 notes(('A play tells a story through dialogue and action on stage; conjunctions and dependent clauses make the dialogue flow.','ተውኔት ታሪክን በመድረክ ላይ በውይይትና በድርጊት ይነግራል፤ አያያዦችና ጥገኛ ሐረጎች ውይይቱን ያፈስሳሉ።'),
  [('Reading a short play.','አጭር ተውኔት ማንበብ።'),('Drama elements: characters, dialogue, stage directions, conflict.','የተውኔት ክፍሎች፦ ገጸ ባሕርይ፣ ውይይት፣ መመሪያ፣ ግጭት።'),('Conjunctions and dependent clauses.','አያያዦችና ጥገኛ ሐረጎች።'),('Stages: write, cast, rehearse, prepare, perform.','ደረጃዎች፦ መጻፍ፣ መምረጥ፣ መለማመድ፣ ማዘጋጀት፣ ማቅረብ።')],
  [('ተውኔት','drama','የመድረክ ታሪክ'),('ውይይት','dialogue','ንግግር'),('ልምምድ','rehearsal','ዝግጅት')],('Write it, cast it, rehearse it, show it.','ጻፉት፣ ምረጡ፣ ተለማመዱ፣ አሳዩ።'),
  [(('What are stage directions?','የመድረክ መመሪያ ምንድን ነው?'),'ተዋናዮች የሚያደርጉትን የሚገልጽ በቅንፍ ያለ ጽሑፍ'),(('Name 3 drama elements','3 የተውኔት ክፍሎችን ጥቀሱ'),'ገጸ ባሕርይ፣ ውይይት፣ ግጭት')],
  inn(('Mini-drama for a cause','ለአንድ ዓላማ አጭር ተውኔት'),('Short plays can teach health, peace or saving. Write and perform a 5-minute play for your community.','አጫጭር ተውኔቶች ጤናን፣ ሰላምን ወይም ቁጠባን ሊያስተምሩ ይችላሉ። ለማኅበረሰባችሁ የ5 ደቂቃ ተውኔት ጽፋችሁ አቅርቡ።'),[('Choose one message (e.g. saving money).','አንድ መልእክት ምረጡ (ለምሳሌ ቁጠባ)።'),('Write dialogue with stage directions.','ከመድረክ መመሪያ ጋር ውይይት ጻፉ።'),('Rehearse three times.','ሦስት ጊዜ ተለማመዱ።'),('Perform and collect audience feedback.','አቅርቡና የተመልካቾችን አስተያየት ሰብስቡ።')])),
 sm(('Drama and joining words','ተውኔትና አያያዥ ቃላት'),[('Reading a play','ተውኔት ማንበብ'),('Drama elements','የተውኔት ክፍሎች'),('Conjunctions and clauses','አያያዦችና ሐረጎች'),('Staging','መድረክ ማቅረብ')]),'Drama')
dump('amharic')
