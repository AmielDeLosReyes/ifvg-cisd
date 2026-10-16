import json,re,collections
s=json.load(open('sections.json'))
B=[
('ifvg', r'inversion|ifvg|i-fvg|reclaim'),
('fpfvg', r'first[- ]present|first instance|first fvg|first utiliz|reflection|first gap'),
('bpr', r'balanced price range|\bbpr\b'),
('special_gaps', r'breakaway|immediate rebalance|implied fair|implied fvg|reaper|exhaustion gap|measuring gap|vacuum'),
('ob_family', r'order ?block|cisd|change in (the )?state|state of delivery|breaker|mitigation block|rejection block|propulsion|suspension|mean threshold|hangman|bolo|defensive|fulcrum'),
('wick', r'wick|grey pool|gray pool|gray pole|mohawk|shadow'),
('open_gaps', r'opening range gap|\borg\b|ndog|nwog|new day opening|new week opening|opening gap|event horizon|black hole|settlement|gap fill|half[- ]gap|mid[- ]?gap'),
('opening_range', r'opening range|pre-?market|premarket|pre-8:?30|pre-830|initial (high|low|bsl|ssl|buy|sell)'),
('fvg', r'fair value gap|\bfvg|sibi|bisi|imbalance|consequent encroachment|\bce\b|quadrant|octant|gradient|inefficien|gap'),
('structure', r'market structure|swing|structure shift|\bmss\b|break of structure|displacement|short[- ]term (high|low)|intermediate|long[- ]term (high|low)|three drives|complex reversal|climax|capitulation'),
('liquidity', r'liquidity(?! run)|equal high|equal low|stop (run|hunt)|raid|sweep|turtle soup|engineer|smooth|jagged|inducement|draw on|buy[- ]side|sell[- ]side|\bbsl\b|\bssl\b|\birl\b|\berl\b|pool|old high|old low|previous day|unfinished'),
('pd_ranges', r'premium|discount|equilibrium|dealing range|\bote\b|optimal trade|fib|standard deviation|projection|retracement|range reset'),
('pd_matrix', r'pd array|matrix|hierarchy|toolbox|reference point'),
('time_sessions', r'killzone|kill zone|session|midnight|8:30|\b830\b|9:30|\b930\b|lunch|london|asia|afternoon|\bpm\b|\bam\b|macro|silver bullet|time window|clock|new york time|first hour|last hour|market on close|bond auction|6 ?pm|7:00|dead time|hour'),
('power3', r'power of (3|three)|\bamd\b|judas|daily profile|weekly profile|tgif|day of (the )?week|monday|friday|thursday|tuesday|wednesday|seasonal|holiday|weekly range|inside day|life cycle|weekly|daily range|daily high|daily low'),
('news', r'news|nfp|non ?farm|cpi|ppi|fomc|powell|\bfed\b|jackson hole|manual intervention|event[- ]driven|geopolit|economic calendar|embargo'),
('bias', r'bias|narrative|smt|divergence|bellwether|intermarket|dxy|dollar|correlation|decoupl|sister|risk[- ]on|ipda|data range|quarterly|higher[- ]time|htf|top[- ]down|lay of the land|if[- ]then'),
('conditions', r'resistance liquidity|hrlr|seek (and|&) destroy|consolidation|time distortion|chop|low[- ]probability|high[- ]probability|condition|large[- ]range|one[- ]sided|clean|fickle|heav|speed|day[- ]type|profile|stand aside|sit out|no[- ]trade'),
('models', r'model|2022|one shot|osok|obsidian|zircon|enigma|chain of custody|grid|caleb|mmsm|mmbm|setup|protocol|cork'),
('entries', r'entry|entries|iofed|entry drill|limit order|lowest threshold|price delivery continuum|15[- ]second|1[- ]second|second chart|pyramid|scal(e|ing) in|add[- ]on|re-?entr|missed|buffer|staging|parameter'),
('management', r'stop|target|partial|terminus|trail|break[- ]?even|exit|management|hold|low[- ]hanging|objective|double tap|cover'),
('risk', r'risk|position siz|contract|micro|mini|leverage|drawdown|compound|funded|prop|margin|cfd|futures|rollover|continuous|instrument|forex|crude|gold|bitcoin|commod'),
('practice', r'journal|backtest|back[- ]test|drill|tape[- ]read|observation|paper|demo|replay|study|learning|student|homework|\blog\b|chart|layout|annotat|screenshot|notepad|naked'),
('psychology', r'psych|mindset|fear|fomo|patience|emotion|anxiety|discipline|ego|confiden|expectation|sniper|independen|responsib|motivation|mental|indifferen|need to be right|self'),
('algorithm', r'algorithm|order ?flow|efficien|smart money|retail|institution|price engine|handshake|spool|two reasons|delivery|why price|time and price|time & price|time is'),
]
assign=collections.defaultdict(list)
for i,x in enumerate(s):
    h=x['head'].lower()
    for k,pat in B:
        if re.search(pat,h):
            assign[k].append(i); x['bucket']=k; break
    else:
        assign['other'].append(i); x['bucket']='other'
json.dump(s,open('sections.json','w'))
for k,_ in B+[('other','')]:
    idx=assign[k]; print(f"{k:15s} {len(idx):4d} {sum(len(s[i]['body']) for i in idx):8d}")
import random
random.seed(1)
print('--- other sample')
for i in random.sample(assign['other'],min(60,len(assign['other']))): print('  ',s[i]['head'][:100])
