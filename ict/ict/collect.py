import json, glob, os, shutil, sys
src='/root/.claude/projects/-home-claude/a6e8d268-c7a0-5219-aff6-14d0b096a3bb/tool-results/'
done=set(open('collected.txt').read().split()) if os.path.exists('collected.txt') else set()
files=sorted(glob.glob(src+'mcp-remote-devices-Claude_Browser__javascript_tool-*.txt'), key=os.path.getmtime)
new=0
for f in files:
    b=os.path.basename(f)
    if b in done: continue
    d=json.load(open(f)); t=d[0]['text']
    try: s=json.JSONDecoder().raw_decode(t)[0]
    except Exception as e:
        print('SKIP (not json string)',b, t[:60].replace('\n',' ')); done.add(b); continue
    if not isinstance(s,str) or not (s.startswith('@@VID') or s.startswith('@@META') or s.startswith('@@CONT')):
        print('SKIP (not chunk)',b, str(s)[:60]); done.add(b); continue
    if 'truncated: content too large' in t: print('TRUNCATED!',b)
    n=len(glob.glob('chunks/*.txt'))+1
    os.makedirs('chunks',exist_ok=True)
    open(f'chunks/{n:03d}.txt','w').write(s)
    vids=[l.split()[1] for l in s.split('\n') if l.startswith('@@VID')]
    print(f'chunk {n:03d}: {len(s)} chars, {len(vids)} videos, starts {s[:30]!r}')
    done.add(b); new+=1
open('collected.txt','w').write('\n'.join(sorted(done)))
print('new',new)
