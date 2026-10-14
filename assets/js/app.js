/* =========================================================
   MAYO REAL ESTATES — site behaviour (no server needed)
   Listings live in assets/js/listings.js
   ========================================================= */
(function(){
"use strict";
var $=function(s,r){return (r||document).querySelector(s)}, $$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
var L=window.LISTINGS||[], S=window.SITE||{}, SOC=window.SOCIETIES||[];
var socBySlug={}; SOC.forEach(function(s){socBySlug[s.slug]=s;});
var TYPES={house:"House",villa:"Villa",farmhouse:"Farmhouse",plot:"Plot",commercial:"Commercial",apartment:"Apartment"};
var COND={new:"Brand new",old:"Old house",grey:"Grey structure"};

/* ---------- helpers ---------- */
function esc(t){return String(t==null?"":t).replace(/[&<>"']/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c];});}
function photo(p,small){ if(typeof p==="number"||/^\d+$/.test(p)) return "images/p/"+(small?"t/":"")+p+".jpg"; return p; }
function crore(n){
  if(n>=1e7){var v=n/1e7; return (v>=100?Math.round(v):Math.round(v*100)/100)+" Crore";}
  if(n>=1e5){return Math.round(n/1e5*10)/10+" Lakh";}
  return n.toLocaleString("en-PK");
}
function priceHTML(n){return '<span class="pkr">PKR</span> '+crore(n);}
function areaLabel(a){ if(!a) return ""; var u={marla:"Marla",kanal:"Kanal",sqyd:"Sq. Yd",sqft:"Sq. Ft",acre:"Acre"}[a.u]||a.u; if(a.u==="kanal"&&a.v!==1) u="Kanal"; return (a.v>=1000?a.v.toLocaleString("en-PK"):a.v)+" "+u; }
function toMarla(a){ if(!a) return 0; var f={marla:1,kanal:20,sqft:1/225,sqyd:9/225,acre:160}[a.u]||1; return a.v*f; }
function waLink(msg,num){ return "https://wa.me/"+(num||S.whatsapp)+"?text="+encodeURIComponent(msg); }
function socName(slug){ return socBySlug[slug]?socBySlug[slug].name:slug; }
function locText(l){ return (l.block?l.block+", ":"")+socName(l.society)+(socName(l.society).indexOf(l.city)>-1?"":", "+l.city); }
function url(l){ return "property.html?id="+encodeURIComponent(l.id); }
function toast(t){ var e=$("#toast"); if(!e){e=document.createElement("div");e.id="toast";e.className="toast";e.setAttribute("role","status");document.body.appendChild(e);} e.textContent=t; e.classList.add("show"); clearTimeout(e._t); e._t=setTimeout(function(){e.classList.remove("show")},2200); }

/* ---------- saved (shortlist) ---------- */
function getSaved(){ try{ return JSON.parse(localStorage.getItem("mre_saved")||"[]"); }catch(e){ return []; } }
function setSaved(a){ try{ localStorage.setItem("mre_saved",JSON.stringify(a)); }catch(e){} updateSavedCount(); }
function isSaved(id){ return getSaved().indexOf(id)>-1; }
function toggleSaved(id){ var a=getSaved(), i=a.indexOf(id); if(i>-1){a.splice(i,1);toast("Removed from your shortlist");} else {a.push(id);toast("Saved to your shortlist");} setSaved(a); return i===-1; }
function updateSavedCount(){ var n=getSaved().length; $$(".saved-count").forEach(function(e){e.textContent=n; e.style.display=n?"":"none";}); }

/* ---------- card ---------- */
function card(l){
  var b=[];
  if(l.status==="sold") b.push('<span class="badge ink">Sold</span>');
  if(l.luxury) b.push('<span class="badge gold">Luxury</span>');
  b.push('<span class="badge">'+TYPES[l.type]+'</span>');
  if(l.condition&&l.type!=="plot") b.push('<span class="badge">'+COND[l.condition]+'</span>');
  var sp=[];
  sp.push('<span><i class="fa-solid fa-vector-square"></i>'+areaLabel(l.area)+'</span>');
  if(l.beds) sp.push('<span><i class="fa-solid fa-bed"></i>'+l.beds+' Beds</span>');
  if(l.baths&&l.type!=="commercial") sp.push('<span><i class="fa-solid fa-bath"></i>'+l.baths+' Baths</span>');
  if(l.floors&&l.type==="commercial") sp.push('<span><i class="fa-solid fa-building"></i>'+l.floors+' Floors</span>');
  var msg="Assalam o Alaikum, I am interested in: "+l.title+" ("+locText(l)+") — PKR "+crore(l.price)+". "+location.origin+location.pathname.replace(/[^\/]*$/,"")+url(l);
  return '<article class="card">'+
    '<a class="ph" href="'+url(l)+'"><img src="'+photo(l.photos[0],true)+'" alt="'+esc(l.title+", "+locText(l))+'" loading="lazy" width="720" height="540">'+
    '<div class="badges">'+b.join("")+'</div><span class="count"><i class="fa-regular fa-images"></i> '+l.photos.length+'</span></a>'+
    '<button class="save'+(isSaved(l.id)?" on":"")+'" data-save="'+l.id+'" aria-label="Save '+esc(l.title)+'"><i class="fa-'+(isSaved(l.id)?"solid":"regular")+' fa-heart"></i></button>'+
    '<div class="bd"><div class="price">'+priceHTML(l.price)+'</div>'+
    '<h3><a href="'+url(l)+'">'+esc(l.title)+'</a></h3>'+
    '<div class="loc"><i class="fa-solid fa-location-dot"></i>'+esc(locText(l))+'</div>'+
    '<div class="specs">'+sp.join("")+'</div>'+
    '<div class="act"><a class="btn btn-wa btn-sm" target="_blank" rel="noopener" href="'+waLink(msg)+'"><i class="fa-brands fa-whatsapp"></i> WhatsApp</a>'+
    '<a class="btn btn-line btn-sm" href="tel:'+S.phone1.replace(/\s/g,"")+'"><i class="fa-solid fa-phone"></i> Call</a></div>'+
    '</div></article>';
}
document.addEventListener("click",function(e){
  var b=e.target.closest("[data-save]"); if(!b) return;
  e.preventDefault(); var on=toggleSaved(b.getAttribute("data-save"));
  $$('[data-save="'+b.getAttribute("data-save")+'"]').forEach(function(x){ x.classList.toggle("on",on); var i=x.querySelector("i"); if(i) i.className="fa-"+(on?"solid":"regular")+" fa-heart"; });
  if(document.body.getAttribute("data-page")==="properties" && new URLSearchParams(location.search).get("saved")) runFilters();
});

/* ---------- filter engine ---------- */
function match(l,f){
  if(f.type&&f.type!=="all"){ if(f.type==="house"){ if(l.type!=="house"&&l.type!=="villa") return false; } else if(l.type!==f.type) return false; }
  if(f.city&&l.city!==f.city) return false;
  if(f.society&&l.society!==f.society) return false;
  if(f.condition&&l.condition!==f.condition) return false;
  if(f.luxury&&!l.luxury) return false;
  if(f.featured&&!l.featured) return false;
  if(f.min&&l.price<+f.min) return false;
  if(f.max&&l.price>+f.max) return false;
  if(f.beds&&(l.beds||0)<+f.beds) return false;
  if(f.minArea&&toMarla(l.area)<+f.minArea) return false;
  if(f.ids&&f.ids.indexOf(l.id)===-1) return false;
  if(f.exclude&&l.id===f.exclude) return false;
  if(f.q){ var hay=(l.title+" "+l.summary+" "+locText(l)+" "+l.city+" "+TYPES[l.type]).toLowerCase(); var ok=f.q.toLowerCase().split(/\s+/).every(function(w){return hay.indexOf(w)>-1;}); if(!ok) return false; }
  return true;
}
function sortList(a,s){
  a=a.slice();
  if(s==="price-asc") a.sort(function(x,y){return x.price-y.price});
  else if(s==="price-desc") a.sort(function(x,y){return y.price-x.price});
  else if(s==="size-desc") a.sort(function(x,y){return toMarla(y.area)-toMarla(x.area)});
  else a.sort(function(x,y){return (y.featured?1:0)-(x.featured?1:0)});
  return a;
}
/* static blocks: <div data-listings='{"type":"farmhouse"}' data-limit="6"> */
$$("[data-listings]").forEach(function(box){
  var f={}; try{ f=JSON.parse(box.getAttribute("data-listings")||"{}"); }catch(e){}
  var list=sortList(L.filter(function(l){return l.status!=="sold"&&match(l,f);}), f.sort||"");
  var lim=+box.getAttribute("data-limit")||list.length;
  if(!list.length){ box.outerHTML='<div class="empty"><h3>New listings coming soon</h3><p class="muted">Tell us what you are looking for and we will send matching properties on WhatsApp.</p><a class="btn btn-wa" target="_blank" rel="noopener" href="'+waLink("Assalam o Alaikum, I am looking for a property. My requirement is: ")+'"><i class="fa-brands fa-whatsapp"></i> Send your requirement</a></div>'; return; }
  box.innerHTML=list.slice(0,lim).map(card).join("");
});

/* ---------- society selects ---------- */
function fillSocieties(sel,city,keep){
  if(!sel) return; var cur=keep||sel.value;
  var opts='<option value="">All societies & areas</option>';
  var groups={};
  SOC.forEach(function(s){ if(city&&s.city!==city) return; (groups[s.city]=groups[s.city]||[]).push(s); });
  Object.keys(groups).forEach(function(c){ opts+='<optgroup label="'+c+'">'+groups[c].map(function(s){return '<option value="'+s.slug+'">'+esc(s.name)+'</option>';}).join("")+'</optgroup>'; });
  sel.innerHTML=opts; sel.value=cur; if(sel.value!==cur) sel.value="";
}

/* ---------- home search ---------- */
var hs=$("#homeSearch");
if(hs){
  var typeVal="house";
  $$(".search-tabs button",hs).forEach(function(b){ b.addEventListener("click",function(){ $$(".search-tabs button",hs).forEach(function(x){x.classList.remove("on");x.setAttribute("aria-selected","false");}); b.classList.add("on"); b.setAttribute("aria-selected","true"); typeVal=b.getAttribute("data-type"); }); });
  var hc=$("[name=city]",hs), hsoc=$("[name=society]",hs);
  fillSocieties(hsoc,"");
  hc.addEventListener("change",function(){ fillSocieties(hsoc,hc.value); });
  hs.addEventListener("submit",function(e){ e.preventDefault(); var p=new URLSearchParams(); p.set("type",typeVal); ["city","society","max","beds"].forEach(function(k){ var v=$("[name="+k+"]",hs); if(v&&v.value) p.set(k,v.value); }); location.href="properties.html?"+p.toString(); });
}

/* ---------- properties page ---------- */
var ff=$("#filters");
function readForm(){ var f={}; ["type","city","society","condition","min","max","beds","minArea","q"].forEach(function(k){ var el=$("[name="+k+"]",ff); if(el&&el.value) f[k]=el.value; }); return f; }
function runFilters(push){
  var f=readForm(), sort=$("#sort")?$("#sort").value:"";
  var qs=new URLSearchParams(location.search);
  if(qs.get("saved")){ f.ids=getSaved(); }
  var list=sortList(L.filter(function(l){return match(l,f);}),sort);
  $("#count").textContent=list.length;
  var title=$("#resultsTitle");
  if(title){ var t=qs.get("saved")?"Your shortlist":(f.type&&f.type!=="all"?{house:"Houses & villas",villa:"Luxury villas",farmhouse:"Farmhouses",plot:"Plots",commercial:"Commercial property",apartment:"Apartments"}[f.type]:"All properties"); if(f.society) t+=" in "+socName(f.society); else if(f.city) t+=" in "+f.city; title.textContent=t; }
  $("#results").innerHTML=list.length?list.map(card).join(""):'<div class="empty" style="grid-column:1/-1"><h3>No property matches these filters yet</h3><p class="muted">Try widening your budget or area — or send us your requirement and we will find it for you.</p><a class="btn btn-wa" target="_blank" rel="noopener" href="'+waLink("Assalam o Alaikum, I am looking for: "+JSON.stringify(f).replace(/[{}"]/g," "))+'"><i class="fa-brands fa-whatsapp"></i> Send requirement on WhatsApp</a></div>';
  if(push!==false){ var p=new URLSearchParams(); Object.keys(f).forEach(function(k){ if(k!=="ids") p.set(k,f[k]); }); if(sort) p.set("sort",sort); if(qs.get("saved")) p.set("saved","1"); history.replaceState(null,"","properties.html"+(p.toString()?"?"+p.toString():"")); }
}
if(ff){
  var qs=new URLSearchParams(location.search);
  var fc=$("[name=city]",ff), fs=$("[name=society]",ff);
  if(qs.get("city")) fc.value=qs.get("city");
  fillSocieties(fs,fc.value,qs.get("society")||"");
  if(qs.get("society")&&socBySlug[qs.get("society")]&&!fc.value){ fc.value=socBySlug[qs.get("society")].city; fillSocieties(fs,fc.value,qs.get("society")); }
  ["type","condition","min","max","beds","minArea","q"].forEach(function(k){ var el=$("[name="+k+"]",ff); if(el&&qs.get(k)) el.value=qs.get(k); });
  if(qs.get("sort")&&$("#sort")) $("#sort").value=qs.get("sort");
  fc.addEventListener("change",function(){ fillSocieties(fs,fc.value); runFilters(); });
  ff.addEventListener("change",function(e){ if(e.target!==fc) runFilters(); });
  ff.addEventListener("input",function(e){ if(e.target.name==="q") runFilters(); });
  ff.addEventListener("submit",function(e){ e.preventDefault(); runFilters(); });
  $("#resetFilters").addEventListener("click",function(){ ff.reset(); fillSocieties(fs,""); history.replaceState(null,"","properties.html"); runFilters(); });
  if($("#sort")) $("#sort").addEventListener("change",function(){runFilters();});
  var tg=$("#filterToggle"); if(tg) tg.addEventListener("click",function(){ ff.classList.toggle("collapsed"); });
  runFilters(false);
}

/* ---------- property detail ---------- */
var pd=$("#propertyDetail");
if(pd){
  var id=new URLSearchParams(location.search).get("id");
  var l=L.filter(function(x){return x.id===id;})[0];
  if(!l){ pd.innerHTML='<div class="empty"><h2>This property is no longer listed</h2><p class="muted">It may have been sold. Browse our current properties or tell us what you need.</p><a class="btn btn-brass" href="properties.html">Browse properties</a></div>'; }
  else renderDetail(l);
}
function renderDetail(l){
  document.title=l.title+" — "+socName(l.society)+" | Mayo Real Estates";
  var md=$('meta[name="description"]'); if(md) md.setAttribute("content",l.summary);
  var link=location.href;
  var msg="Assalam o Alaikum, I am interested in: "+l.title+" ("+locText(l)+") — PKR "+crore(l.price)+". Please share details. "+link;
  var g=l.photos.slice(0,5).map(function(p,i){ return '<button type="button" data-lb="'+i+'" aria-label="Open photo '+(i+1)+'"><img src="'+photo(p,i>0)+'" alt="'+esc(l.title)+' — photo '+(i+1)+'" '+(i?'loading="lazy"':'fetchpriority="high"')+'></button>'; }).join("");
  var rows=[["Property type",TYPES[l.type]],["Purpose","For sale"],["Price","PKR "+crore(l.price)+" ("+l.price.toLocaleString("en-PK")+")"],["Area / size",areaLabel(l.area)],["City",l.city],["Society / area",socName(l.society)],["Block / location",l.block||"—"]];
  if(l.condition) rows.push(["Condition",COND[l.condition]]);
  if(l.beds) rows.push(["Bedrooms",l.beds]); if(l.baths) rows.push(["Bathrooms",l.baths]); if(l.floors) rows.push(["Floors",l.floors]); if(l.built) rows.push(["Year built",l.built]);
  rows.push(["Listing ID","MRE-"+(L.indexOf(l)+101)]);
  var ks=[];
  ks.push('<div><i class="fa-solid fa-vector-square"></i>Area<b>'+areaLabel(l.area)+'</b></div>');
  if(l.beds) ks.push('<div><i class="fa-solid fa-bed"></i>Bedrooms<b>'+l.beds+'</b></div>');
  if(l.baths) ks.push('<div><i class="fa-solid fa-bath"></i>Bathrooms<b>'+l.baths+'</b></div>');
  ks.push('<div><i class="fa-solid fa-house-flag"></i>Type<b>'+TYPES[l.type]+'</b></div>');
  if(l.condition&&!l.beds) ks.push('<div><i class="fa-solid fa-star"></i>Condition<b>'+COND[l.condition]+'</b></div>');
  if(l.type==="plot") ks.push('<div><i class="fa-solid fa-map"></i>Society<b>'+esc(socName(l.society))+'</b></div>');
  var mapQ=encodeURIComponent((l.block||"")+" "+socName(l.society)+" "+l.city+" Pakistan");
  pd.innerHTML=
   '<div class="gallery">'+g+'<button type="button" class="btn btn-ink btn-sm all" data-lb="0"><i class="fa-regular fa-images"></i> View all '+l.photos.length+' photos</button></div>'+
   '<div class="detail"><div>'+
     '<div class="d-head"><div><div class="crumbs" style="color:var(--muted)"><a href="index.html">Home</a><span>/</span><a href="properties.html?city='+encodeURIComponent(l.city)+'">'+l.city+'</a><span>/</span><a href="'+l.society+'.html">'+esc(socName(l.society))+'</a></div>'+
     '<h1>'+esc(l.title)+'</h1><div class="loc muted"><i class="fa-solid fa-location-dot" style="color:var(--brass)"></i> '+esc(locText(l))+'</div></div>'+
     '<div><div class="price">'+priceHTML(l.price)+'</div><button class="btn btn-line btn-sm mt" style="margin-top:10px" data-save="'+l.id+'"><i class="fa-'+(isSaved(l.id)?"solid":"regular")+' fa-heart"></i> Save</button> <button class="btn btn-line btn-sm" id="shareBtn"><i class="fa-solid fa-share-nodes"></i> Share</button></div></div>'+
     '<div class="keyspecs">'+ks.join("")+'</div>'+
     '<div class="box"><h2>About this property</h2><p><b>'+esc(l.summary)+'</b></p><p>'+esc(l.desc)+'</p></div>'+
     '<div class="box"><h2>Features</h2><ul class="feat">'+l.features.map(function(f){return '<li>'+esc(f)+'</li>';}).join("")+'</ul></div>'+
     '<div class="box"><h2>Details</h2><table class="table">'+rows.map(function(r){return '<tr><td>'+r[0]+'</td><td><b>'+esc(r[1])+'</b></td></tr>';}).join("")+'</table></div>'+
     '<div class="box"><h2>Location</h2><p class="muted">'+esc(locText(l))+'. Exact address is shared before your site visit.</p><iframe class="map" loading="lazy" title="Map of '+esc(socName(l.society))+'" src="https://maps.google.com/maps?q='+mapQ+'&z=13&output=embed"></iframe></div>'+
     '<div class="box"><h2>Monthly installment estimate</h2><p class="muted">For bank home finance. Change the numbers to see your monthly payment.</p>'+
       '<div class="tool-row"><div class="field"><label for="dp">Down payment (%)</label><input id="dp" type="number" value="30" min="0" max="100"></div><div class="field"><label for="yr">Years</label><input id="yr" type="number" value="15" min="1" max="30"></div><div class="field"><label for="rt">Yearly rate (%)</label><input id="rt" type="number" value="12" step="0.1"></div></div>'+
       '<div class="out" id="emiOut"></div></div>'+
   '</div><aside class="agent"><div class="box"><div class="who"><div class="av">WM</div><div><b>'+esc(S.owner)+'</b><div class="muted" style="font-size:.88rem">Mayo Real Estates</div></div></div>'+
     '<div class="act"><a class="btn btn-wa btn-block" target="_blank" rel="noopener" href="'+waLink(msg)+'"><i class="fa-brands fa-whatsapp"></i> WhatsApp about this property</a>'+
     '<a class="btn btn-ink btn-block" href="tel:'+S.phone1.replace(/\s/g,"")+'"><i class="fa-solid fa-phone"></i> '+S.phone1+'</a>'+
     '<a class="btn btn-line btn-block" href="tel:'+S.phone2.replace(/\s/g,"")+'"><i class="fa-solid fa-phone"></i> '+S.phone2+'</a>'+
     '<a class="btn btn-line btn-block" href="mailto:'+S.email+'?subject='+encodeURIComponent("Enquiry: "+l.title)+'&body='+encodeURIComponent(msg)+'"><i class="fa-solid fa-envelope"></i> Email us</a>'+
     '<a class="btn btn-brass btn-block" target="_blank" rel="noopener" href="'+waLink("Assalam o Alaikum, I would like to book a site visit for: "+l.title+" ("+locText(l)+"). "+link)+'"><i class="fa-regular fa-calendar-check"></i> Book a site visit</a></div>'+
     '<p class="note" style="margin-top:14px">Photos may be representative. Every detail — size, documents and price — is confirmed at your site visit.</p></div></aside></div>'+
   '<section class="mt"><div class="sec-head"><h2>Similar properties</h2><a class="more" href="properties.html?type='+(l.type==="villa"?"house":l.type)+'&city='+encodeURIComponent(l.city)+'">See all</a></div><div class="grid" id="similar"></div></section>';
  var sim=sortList(L.filter(function(x){return x.id!==l.id&&x.status!=="sold"&&(x.type===l.type||x.city===l.city);}),"").sort(function(a,b){return (b.type===l.type?2:0)+(b.city===l.city?1:0)-((a.type===l.type?2:0)+(a.city===l.city?1:0));}).slice(0,3);
  $("#similar").innerHTML=sim.map(card).join("");
  /* emi */
  function emi(){ var P=l.price*(1-(+$("#dp").value||0)/100), n=(+$("#yr").value||1)*12, r=(+$("#rt").value||0)/1200; var m=r?P*r*Math.pow(1+r,n)/(Math.pow(1+r,n)-1):P/n;
    $("#emiOut").innerHTML='<div>Property price<b>'+crore(l.price)+'</b></div><div>Down payment<b>'+crore(l.price-P)+'</b></div><div>Loan amount<b>'+crore(P)+'</b></div><div>Monthly payment<b>PKR '+Math.round(m).toLocaleString("en-PK")+'</b></div>'; }
  ["dp","yr","rt"].forEach(function(k){$("#"+k).addEventListener("input",emi);}); emi();
  /* share */
  $("#shareBtn").addEventListener("click",function(){ if(navigator.share){ navigator.share({title:l.title,text:l.summary,url:link}).catch(function(){}); } else { try{ navigator.clipboard.writeText(link); toast("Link copied"); }catch(e){ window.open(waLink(l.title+" — "+link),"_blank"); } } });
  lightbox(l.photos.map(function(p){return photo(p,false);}), l.title);
  /* structured data */
  var ld={"@context":"https://schema.org","@type":"RealEstateListing","name":l.title,"description":l.summary,"url":link,"image":l.photos.slice(0,4).map(function(p){return location.origin+location.pathname.replace(/[^\/]*$/,"")+photo(p,false);}),
    "offers":{"@type":"Offer","price":l.price,"priceCurrency":"PKR","availability":l.status==="sold"?"https://schema.org/SoldOut":"https://schema.org/InStock"},
    "address":{"@type":"PostalAddress","addressLocality":l.city,"addressRegion":socName(l.society),"addressCountry":"PK"}};
  var s=document.createElement("script"); s.type="application/ld+json"; s.textContent=JSON.stringify(ld); document.head.appendChild(s);
}

/* ---------- lightbox ---------- */
function lightbox(srcs,title){
  var lb=document.createElement("div"); lb.className="lb"; lb.setAttribute("role","dialog"); lb.setAttribute("aria-label","Photo gallery");
  lb.innerHTML='<img alt=""><button class="x" aria-label="Close"><i class="fa-solid fa-xmark"></i></button><button class="pv" aria-label="Previous photo"><i class="fa-solid fa-chevron-left"></i></button><button class="nx" aria-label="Next photo"><i class="fa-solid fa-chevron-right"></i></button><div class="cap"></div>';
  document.body.appendChild(lb);
  var i=0, img=$("img",lb), cap=$(".cap",lb);
  function show(n){ i=(n+srcs.length)%srcs.length; img.src=srcs[i]; img.alt=title+" — photo "+(i+1); cap.textContent=(i+1)+" / "+srcs.length; }
  function open(n){ show(n); lb.classList.add("open"); document.body.style.overflow="hidden"; $(".x",lb).focus(); }
  function close(){ lb.classList.remove("open"); document.body.style.overflow=""; }
  $$("[data-lb]").forEach(function(b){ b.addEventListener("click",function(){ open(+b.getAttribute("data-lb")); }); });
  $(".x",lb).onclick=close; $(".pv",lb).onclick=function(){show(i-1)}; $(".nx",lb).onclick=function(){show(i+1)};
  lb.addEventListener("click",function(e){ if(e.target===lb) close(); });
  document.addEventListener("keydown",function(e){ if(!lb.classList.contains("open")) return; if(e.key==="Escape") close(); if(e.key==="ArrowLeft") show(i-1); if(e.key==="ArrowRight") show(i+1); });
  var x0=null; lb.addEventListener("touchstart",function(e){x0=e.touches[0].clientX;},{passive:true});
  lb.addEventListener("touchend",function(e){ if(x0===null) return; var dx=e.changedTouches[0].clientX-x0; if(Math.abs(dx)>40) show(dx<0?i+1:i-1); x0=null; });
}

/* ---------- area converter ---------- */
var cv=$("#converter");
if(cv){
  function conv(){ var v=+$("#cvVal").value||0, u=$("#cvUnit").value, mSize=+$("#cvMarla").value;
    var sqft={sqft:1,sqyd:9,marla:mSize,kanal:mSize*20,acre:mSize*160,sqm:10.7639}[u]*v;
    var out=[["Square feet",sqft],["Square yards",sqft/9],["Marla",sqft/mSize],["Kanal",sqft/(mSize*20)],["Acre",sqft/(mSize*160)],["Square metres",sqft/10.7639]];
    $("#cvOut").innerHTML=out.map(function(o){ return '<div>'+o[0]+'<b>'+(Math.round(o[1]*100)/100).toLocaleString("en-PK")+'</b></div>'; }).join(""); }
  $$("input,select",cv).forEach(function(e){e.addEventListener("input",conv);}); conv();
}
/* ---------- installment calculator (calculators page) ---------- */
var ic=$("#instCalc");
if(ic){
  function inst(){ var price=+$("#icPrice").value||0, dp=+$("#icDp").value||0, n=(+$("#icYears").value||1)*12, r=(+$("#icRate").value||0)/1200, P=price*(1-dp/100);
    var m=r?P*r*Math.pow(1+r,n)/(Math.pow(1+r,n)-1):P/n;
    $("#icOut").innerHTML='<div>Down payment<b>PKR '+Math.round(price-P).toLocaleString("en-PK")+'</b></div><div>Loan amount<b>PKR '+Math.round(P).toLocaleString("en-PK")+'</b></div><div>Monthly payment<b>PKR '+Math.round(m).toLocaleString("en-PK")+'</b></div><div>Total paid to bank<b>PKR '+Math.round(m*n).toLocaleString("en-PK")+'</b></div>'; }
  $$("input",ic).forEach(function(e){e.addEventListener("input",inst);}); inst();
}
/* ---------- construction estimate ---------- */
var cc=$("#costCalc");
if(cc){
  function cost(){ var covered=+$("#ccArea").value||0, grey=+$("#ccGrey").value||0, fin=+$("#ccFinish").value||0;
    $("#ccOut").innerHTML='<div>Covered area<b>'+covered.toLocaleString("en-PK")+' sq ft</b></div><div>Grey structure<b>PKR '+crore(covered*grey)+'</b></div><div>Finishing<b>PKR '+crore(covered*fin)+'</b></div><div>Total estimate<b>PKR '+crore(covered*(grey+fin))+'</b></div>'; }
  var pre=$("#ccPreset"); if(pre) pre.addEventListener("change",function(){ $("#ccArea").value=pre.value; cost(); });
  $$("input",cc).forEach(function(e){e.addEventListener("input",cost);}); cost();
}

/* ---------- WhatsApp forms ---------- */
$$("form[data-wa]").forEach(function(f){
  f.addEventListener("submit",function(e){
    e.preventDefault();
    var bad=$$("[required]",f).filter(function(x){return !x.value.trim();});
    if(bad.length){ bad[0].focus(); toast("Please fill in: "+(bad[0].getAttribute("data-label")||bad[0].name)); return; }
    var lines=[f.getAttribute("data-wa")];
    $$("input,select,textarea",f).forEach(function(x){ if(x.type==="submit"||!x.name||!x.value) return; if((x.type==="checkbox"||x.type==="radio")&&!x.checked) return; lines.push("• "+(x.getAttribute("data-label")||x.name)+": "+x.value); });
    window.open(waLink(lines.join("\n")),"_blank","noopener");
    toast("Opening WhatsApp…");
  });
});

/* ---------- menu, drawer, side toggle ---------- */
var dr=$("#drawer");
$$("[data-open-drawer]").forEach(function(b){ b.addEventListener("click",function(){ dr.classList.add("open"); b.setAttribute("aria-expanded","true"); $(".close",dr).focus(); }); });
if(dr){ $$(".shade,.close",dr).forEach(function(x){ x.addEventListener("click",function(){ dr.classList.remove("open"); }); }); document.addEventListener("keydown",function(e){ if(e.key==="Escape") dr.classList.remove("open"); }); }
var st=$(".side-toggle"); if(st){ $(".tab",st).addEventListener("click",function(){ var o=st.classList.toggle("open"); this.setAttribute("aria-expanded",o); }); }
var here=location.pathname.split("/").pop()||"index.html";
$$(".menu a").forEach(function(a){ if(a.getAttribute("href")===here) a.classList.add("active"); });
$$(".year").forEach(function(e){ e.textContent=new Date().getFullYear(); });
/* counters on category tiles */
$$("[data-countf]").forEach(function(e){ var f={}; try{f=JSON.parse(e.getAttribute("data-countf"));}catch(x){} var n=L.filter(function(l){return l.status!=="sold"&&match(l,f);}).length; e.textContent=n+(n===1?" property":" properties"); });
/* counters on home */
$$("[data-count]").forEach(function(e){ var k=e.getAttribute("data-count"); var n=0;
  if(k==="all") n=L.filter(function(l){return l.status!=="sold";}).length;
  else if(k==="house") n=L.filter(function(l){return l.type==="house"||l.type==="villa";}).length;
  else n=L.filter(function(l){return l.type===k;}).length;
  e.textContent=n+(n===1?" property":" properties"); });
updateSavedCount();
})();
