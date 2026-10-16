import json, glob, os, re, sys
base='/home/claude/ict'
# Load raw dumps: each is tool-result JSON [{type,text}] whose text is a JSON string of {"pls":..., "tx":{vid:[[sec,text],...]}}
meta=None; tx={}
for f in sorted(glob.glob(base+'/raw/*.txt')):
    d=json.load(open(f))
    t=d[0]['text'] if isinstance(d,list) else d
    # strip trailing browser context if any
    i=t.rfind('}')
    obj=json.loads(t[:i+1]) if not t.startswith('"') else json.loads(json.loads(t[:t.rfind('"')+1]))
    if 'pls' in obj and obj['pls']: meta=obj['pls']
    tx.update(obj.get('tx',{}))
print('videos with tx:',len(tx))
def ts(s):
    return f"{s//3600}:{s%3600//60:02d}:{s%60:02d}"
def slug(s):
    return re.sub(r'[^A-Za-z0-9]+','-',s).strip('-')[:60]
index=[]
short={'2022 ICT Mentorship':'M22','ICT 2024 Mentorship':'M24','2026 ICT Smart Money Concept Lecture':'L26'}
for p in meta:
    code=short.get(p['title'],'PX')
    n=len(p['videos'])
    for i,v in enumerate(p['videos']):
        vid=v['id']; lines=tx.get(vid)
        fn=f"{code}-{i+1:03d}-{vid}.txt"
        paras=[]; cur=[]; start=None
        for sec,text in (lines or []):
            if start is None: start=sec
            cur.append(text)
            if sec-start>=45 and text and text[-1:] not in ('',):
                paras.append(f"[{ts(start)}] "+' '.join(cur)); cur=[]; start=None
        if cur: paras.append(f"[{ts(start)}] "+' '.join(cur))
        body='\n'.join(paras)
        hdr=f"# {v['title']}\nPlaylist: {p['title']} | #{i+1} of {n} | ID: {vid} | Duration: {v.get('dur')}\nURL: https://www.youtube.com/watch?v={vid}\nTimestamps in [h:mm:ss]; link a moment as https://youtu.be/{vid}?t=<seconds>\n\n"
        if lines is None: body='(TRANSCRIPT NOT CAPTURED)'
        elif not lines: body='(NO CAPTIONS AVAILABLE FOR THIS VIDEO)'
        open(f"{base}/transcripts/{fn}",'w').write(hdr+body+'\n')
        index.append({'file':fn,'code':code,'n':i+1,'id':vid,'title':v['title'],'dur':v.get('dur'),'chars':len(body),'playlist':p['title']})
json.dump(index,open(base+'/index.json','w'),indent=1)
print('files:',len(index),'total chars:',sum(x['chars'] for x in index))
