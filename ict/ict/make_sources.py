import json,re,collections
s=json.load(open('sections.json'))
pools=json.load(open('pools.json'))
ix={x['file'].replace('.txt',''):x for x in json.load(open('index.json'))}
era={'M22':'2022 Mentorship','M24':'2024 Mentorship','L26':'2026 Lectures'}
def label(base):
    x=ix[base]; 
    pre={'M22':'2022 Ep','M24':'2024 #','L26':'2026 #'}[x['code']]
    return f"{pre}{x['n']} — {x['title']} (ID {x['id']})"
for x in s:
    if x['bucket']=='fvg':
        h=x['head'].lower()
        if re.search(r'consequent|quadrant|octant|gradient|volume imbalance|inefficien|\bce\b|mean threshold|equilibrium',h): x['bucket']='grading'
        else: x['bucket']='fvg_core'
CH=[
 ('ch01','The ICT worldview: time, price and the algorithm',['algorithm','other'],None),
 ('ch02','Market structure and displacement',['structure'],None),
 ('ch03','Liquidity: buy-side, sell-side and the draw',['liquidity'],None),
 ('ch04','Premium, discount, dealing ranges and OTE',['pd_ranges','pd_matrix'],None),
 ('ch05','Fair value gaps (BISI and SIBI)',['fvg_core'],None),
 ('ch06','Grading price: CE, quadrants, octants and volume imbalances',['grading'],None),
 ('ch07','Inversion FVGs, reclaimed FVGs and balanced price ranges',['ifvg','bpr'],None),
 ('ch08','First presented FVGs and special gaps',['fpfvg','special_gaps'],None),
 ('ch09','Order blocks, CISD, breakers and the block family',['ob_family'],None),
 ('ch10','Wicks as PD arrays',['wick'],None),
 ('ch11','Opening gaps: NDOG, NWOG, the RTH opening range gap and Event Horizon',['open_gaps'],None),
 ('ch12','Sessions, killzones, key opens and macros',['time_sessions','opening_range'],None),
 ('ch13','Daily and weekly templates: Power of 3, Judas swing, TGIF',['power3'],None),
 ('ch14','News days and manual intervention',['news'],None),
 ('ch15','Building bias and narrative: HTF draw, SMT, intermarket',['bias'],None),
 ('ch16','Reading market conditions: high vs low resistance, seek and destroy',['conditions'],None),
 ('ch17','The ICT models, from 2022 to 2026',['models'],r'silver bullet|2022|one shot|osok|obsidian|zircon|enigma|chain of custody|grid|market maker (buy|sell)|mmsm|mmbm|caleb|turtle soup'),
 ('ch18','Entries: IOFED, limit orders and the price delivery continuum',['entries'],None),
 ('ch19','Stops, targets, partials and trade management',['management'],None),
 ('ch20','Risk, sizing and instruments',['risk'],'PROC:risk'),
 ('ch21','Practice: tape reading, journaling, backtesting and drills',['practice'],'PROC:practice'),
 ('ch22','Psychology and the trader\'s process',['psychology'],'PROC:psych'),
]
order={'M22':0,'M24':1,'L26':2}
procre={'risk':r'risk|contract|micro|mini|size|sizing|loss|losing|%|percent|leverage|drawdown|funded|prop|account|stop|capital|salary|dollar|\$',
        'practice':r'journal|backtest|back test|demo|drill|tape|replay|study|practice|paper|log|annotat|screenshot|chart|observ|learn|homework|walk[- ]forward',
        }
summ={}
for ch,title,bks,extra in CH:
    items=[x for x in s if x['bucket'] in bks]
    if extra and not extra.startswith('PROC'):
        ids={id(x) for x in items}
        items+= [x for x in s if id(x) not in ids and re.search(extra,x['head'].lower())]
    items.sort(key=lambda x:(order[x['code']],x['n']))
    out=[f"# SOURCE NOTES FOR: {title}\n\nEach block below is one concept section from study notes of a specific ICT video. Blocks are ordered 2022 Mentorship → 2024 Mentorship → 2026 Lectures, so you can see how the teaching evolved. Timestamp links inside are real.\n"]
    cur=None
    for x in items:
        if x['code']!=cur:
            cur=x['code']; out.append(f"\n\n######## {era[cur].upper()} ########\n")
        out.append(f"\n=== [{label(x['file'])}] — {x['head']}\n{x['body']}\n")
    if extra and extra.startswith('PROC'):
        kind=extra.split(':')[1]
        out.append(f"\n\n######## PROCESS / RISK / PSYCHOLOGY BULLETS FROM ALL VIDEOS (filtered for this chapter) ########\n")
        for base,txt in sorted(pools['process'],key=lambda b:(order[ix[b[0]]['code']],ix[b[0]]['n'])):
            lines=[l for l in txt.split('\n') if l.strip()]
            if kind=='psych':
                keep=[l for l in lines if not re.search(procre['risk'],l.lower()) or re.search(r'fear|emotion|mind|patien|ego|confiden|anxi|fomo|psych|discipline|expectation|feel',l.lower())]
                keep=[l for l in keep if not re.search(procre['practice'],l.lower()) or re.search(r'fear|emotion|mind|patien|ego|confiden|anxi|fomo|psych|discipline|feel',l.lower())]
            else:
                keep=[l for l in lines if re.search(procre[kind],l.lower())]
            if keep: out.append(f"\n=== [{label(base)}]\n"+'\n'.join(keep)+'\n')
    txt=''.join(out)
    open(f'sources/{ch}.md','w').write(txt)
    summ[ch]=(title,len(items),len(txt))
for k,v in summ.items(): print(k,v)
json.dump([[c,t] for c,t,_,_ in CH],open('chapters.json','w'))
