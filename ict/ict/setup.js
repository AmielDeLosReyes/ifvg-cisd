// ===== ICT transcript capture setup (runs in youtube.com watch page) =====
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
window.__tx = window.__tx || {}; window.__tt = window.__tt || {}; window.__status = window.__status || {};
window.__ready = window.__ready || []; window.__cur = window.__cur || ''; window.__exported = window.__exported || 0;
if(!window.__po){ window.__po = new PerformanceObserver(list=>{ for(const e of list.getEntries()){ if(e.name.includes('/api/timedtext')){ try{const u=new URL(e.name); window.__tt[u.searchParams.get('v')]=e.name;}catch(_){} } } }); window.__po.observe({type:'resource', buffered:true}); }
try{ performance.setResourceTimingBufferSize(5000); }catch(e){}
function walk(o, out, conts){ if(!o||typeof o!=='object') return; if(Array.isArray(o)){o.forEach(x=>walk(x,out,conts));return;}
 if(o.lockupViewModel){ const l=o.lockupViewModel; const t=l?.metadata?.lockupMetadataViewModel?.title?.content; let dur=null; const m=JSON.stringify(l).match(/"text":"(\d+:\d+(?::\d+)?)"/); if(m) dur=m[1]; out.push({id:l.contentId,title:t,dur}); return;}
 if(o.playlistVideoRenderer){const p=o.playlistVideoRenderer; out.push({id:p.videoId,title:p.title?.runs?.[0]?.text,dur:p.lengthText?.simpleText}); return;}
 if(o.continuationCommand && typeof o.continuationCommand.token==='string') conts.push(o.continuationCommand.token);
 for(const k in o) walk(o[k],out,conts);}
async function getPlaylist(listId){
  const html = await fetch('https://www.youtube.com/playlist?list='+listId).then(r=>r.text());
  const d = JSON.parse(html.match(/var ytInitialData = (\{.*?\});<\/script>/s)[1]);
  const title = d?.metadata?.playlistMetadataRenderer?.title;
  let out=[], conts=[], used=new Set(); walk(d.contents,out,conts); let guard=0;
  while(conts.length && guard<15){ const tok=conts.shift(); if(used.has(tok)) continue; used.add(tok); guard++;
    const r = await fetch('/youtubei/v1/browse?prettyPrint=false',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({context:ytcfg.get('INNERTUBE_CONTEXT'),continuation:tok})}).then(r=>r.json()).catch(()=>({}));
    walk(r,out,conts);}
  const seen=new Set(); out=out.filter(v=>v.id&&v.id.length===11&&!seen.has(v.id)&&seen.add(v.id));
  return {listId,title,count:out.length,videos:out};
}
window.__fetchTT = async function(vid){ const u=new URL(window.__tt[vid]); u.searchParams.set('fmt','json3'); const j=await fetch(u.toString()).then(r=>r.json()).catch(e=>null); if(!j) return null; return (j.events||[]).filter(e=>e.segs).map(e=>[Math.floor(e.tStartMs/1000), e.segs.map(x=>x.utf8).join('').replace(/[\n\t]/g,' ').trim()]).filter(x=>x[1]); };
window.__emit = function(vid, status, lines){
  let block = '@@VID '+vid+'\t'+status+'\n' + (lines||[]).map(l=>l[0]+'\t'+l[1]).join('\n') + '\n';
  while(block.length){ const room = 200000 - window.__cur.length;
    if(block.length <= room){ window.__cur += block; block=''; }
    else if(window.__cur.length > 20000){ window.__ready.push(window.__cur); window.__cur=''; }
    else { const cut = block.lastIndexOf('\n', room); const k = cut>0?cut+1:room; window.__cur += block.slice(0,k); window.__ready.push(window.__cur); window.__cur=''; block = '@@CONT '+vid+'\n'+block.slice(k); } }
  if(window.__cur.length >= 180000){ window.__ready.push(window.__cur); window.__cur=''; }
};
window.__cap2 = async function(vid, maxMs=60000){
  const mp=document.querySelector('#movie_player'); const t0=Date.now(); let i=0;
  if(window.__tx[vid]) return {vid,status:'have'};
  if(mp.getVideoData().video_id!==vid){ mp.mute(); mp.loadVideoById({videoId:vid,startSeconds:0}); }
  while(Date.now()-t0<maxMs){ await sleep(300); i++;
    if(window.__tt[vid]){ const lines=await window.__fetchTT(vid); if(lines&&lines.length){ window.__tx[vid]=lines.length; window.__emit(vid,'ok',lines); try{mp.pauseVideo();}catch(e){} return {vid,status:'ok',lines:lines.length,ms:Date.now()-t0}; } }
    const pr=mp.getPlayerResponse();
    if(pr?.videoDetails?.videoId===vid){ const tracks=pr?.captions?.playerCaptionsTracklistRenderer?.captionTracks||[]; if(!tracks.length && i>8) { window.__tx[vid]=-1; window.__emit(vid,'no_captions',[]); return {vid,status:'no_captions'}; }
      if(i%6===3){ try{ mp.loadModule('captions'); mp.setOption('captions','track',{languageCode:(tracks.find(t=>t.languageCode==='en')||tracks[0])?.languageCode||'en'}); }catch(e){} } }
    const sk=document.querySelector('.ytp-skip-ad-button, .ytp-ad-skip-button, .ytp-ad-skip-button-modern'); if(sk&&sk.offsetParent) sk.click();
  }
  return {vid,status:'pending'};
};
window.__take = function(){ if(!window.__ready.length && window.__done && window.__cur.length){ window.__ready.push(window.__cur); window.__cur=''; } const c = window.__ready.shift(); if(c) window.__exported++; return c || ''; };
if(!window.__pls){ window.__pls = await Promise.all(['PLVgHx4Z63paYiFGQ56PjTF1PGePL3r69s','PLVgHx4Z63paaM41aubnHOmqfeNjSAoBCV','PLVgHx4Z63paaja3GW0dYSr6y_V2Sttx4-'].map(getPlaylist)); }
if(!window.__metaDone){ window.__cur = '@@META '+JSON.stringify(window.__pls)+'\n' + window.__cur; window.__metaDone=true; }
if(!window.__running){
  window.__queue = window.__pls.flatMap(p=>p.videos.map(v=>v.id)).filter(id=>!window.__tx[id]);
  window.__running = true; window.__done=false;
  (async()=>{ while(window.__queue.length){ const vid=window.__queue.shift(); let r; try{ r = await window.__cap2(vid, 60000); }catch(e){ r={vid,status:'error',err:String(e)}; } window.__status[vid]=r; if(r.status==='pending'||r.status==='error'){ (window.__retry=window.__retry||[]).push(vid); } await sleep(1000); } window.__done=true; window.__running=false; })();
}
({counts: window.__pls.map(p=>p.count), queued: window.__queue.length})
