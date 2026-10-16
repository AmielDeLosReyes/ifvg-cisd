import json, glob, os, re
base='/home/claude/ict'
meta=None; tx={}; status={}; order=[]
cur=None
for f in sorted(glob.glob(base+'/chunks/*.txt')):
    for line in open(f).read().split('\n'):
        if line.startswith('@@META '):
            meta=json.loads(line[7:]); continue
        if line.startswith('@@PAD'): cur=None; continue
        if line.startswith('@@VID '):
            vid,st=line[6:].split('\t'); cur=vid; status[vid]=st; tx.setdefault(vid,[]); continue
        if line.startswith('@@CONT '):
            cur=line[7:].strip(); continue
        if not line.strip() or cur is None: continue
        sec,_,text=line.partition('\t')
        try: tx[cur].append((int(sec),text))
        except: pass
def ts(s): return f"{s//3600}:{s%3600//60:02d}:{s%60:02d}"
short={'2022 ICT Mentorship':'M22','ICT 2024 Mentorship':'M24','2026 ICT Smart Money Concept Lecture':'L26'}
index=[]
for p in meta:
    code=short[p['title']]; n=len(p['videos'])
    for i,v in enumerate(p['videos']):
        vid=v['id']; fn=f"{code}-{i+1:03d}-{vid}.txt"
        st=status.get(vid); lines=tx.get(vid)
        paras=[]; cur=[]; start=None
        for sec,text in (lines or []):
            if start is None: start=sec
            cur.append(text)
            if sec-start>=45: paras.append(f"[{ts(start)}] "+' '.join(cur)); cur=[]; start=None
        if cur: paras.append(f"[{ts(start)}] "+' '.join(cur))
        body='\n'.join(paras)
        if st is None: body='(TRANSCRIPT NOT CAPTURED YET)'
        elif st=='no_captions': body='(NO CAPTIONS AVAILABLE FOR THIS VIDEO — YouTube has no transcript; it is likely a silent/live-execution video.)'
        hdr=f"# {v['title']}\nPlaylist: {p['title']} | #{i+1} of {n} | ID: {vid} | Duration: {v.get('dur')}\nURL: https://www.youtube.com/watch?v={vid}\nTimestamps are [h:mm:ss]; link a moment as https://youtu.be/{vid}?t=<seconds>\n\n"
        open(f"{base}/transcripts/{fn}",'w').write(hdr+body+'\n')
        index.append({'file':fn,'code':code,'n':i+1,'id':vid,'title':v['title'],'dur':v.get('dur'),'status':st,'chars':len(body) if st=='ok' else 0,'playlist':p['title']})
json.dump(index,open(base+'/index.json','w'),indent=1)
from collections import Counter
for code in ['M22','M24','L26']:
    xs=[x for x in index if x['code']==code]
    print(code, len(xs), 'ok',sum(1 for x in xs if x['status']=='ok'), 'nocap',sum(1 for x in xs if x['status']=='no_captions'), 'missing',sum(1 for x in xs if x['status'] is None), 'chars',sum(x['chars'] for x in xs))
