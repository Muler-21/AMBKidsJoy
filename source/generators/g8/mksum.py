import json,glob,os
D=os.environ.get('G8SUM','/tmp/g8sum');S={}
for f in sorted(glob.glob(os.path.join(D,'sum_*.json'))): S.update(json.load(open(f)))
out="/* Grade 8: one big idea per chapter; labels.length must equal notes.points.length */\nwindow.AMB_SUMMARY=window.AMB_SUMMARY||{};\nObject.assign(window.AMB_SUMMARY,{\n"+''.join(f"'{k}':{json.dumps(v,ensure_ascii=False,separators=(',',':'))},\n" for k,v in sorted(S.items()))+"});\n"
open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','grade8','summaries8.js'),'w').write(out);print('summaries',len(S))
