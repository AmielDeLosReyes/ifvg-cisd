import json, os, re, glob
ix={x['file'].replace('.txt',''):x for x in json.load(open('index.json'))}
secs=[]
for p in sorted(glob.glob('notes/*.md')):
    base=os.path.basename(p)[:-3]
    if base not in ix: continue
    meta=ix[base]
    t=open(p).read()
    # split concept sections: '### ' headings until next '### ' or '## '
    parts=re.split(r'(?m)^(### .*)$', t)
    for i in range(1,len(parts),2):
        head=parts[i][4:].strip()
        body=parts[i+1]
        body=re.split(r'(?m)^## ', body)[0]
        secs.append({'file':base,'code':meta['code'],'n':meta['n'],'title':meta['title'],'id':meta['id'],'head':head,'body':body.strip()})
json.dump(secs,open('sections.json','w'))
print(len(secs))
