/* AMBKidsJoy — "Fidel Fun!" book card, shown above the author card on every page.
   Loaded by author.js (or directly). Bilingual: follows <html lang="am|en">. */
(function(){
if (window.__ambBookPromo) return; window.__ambBookPromo = true;
const ME=(document.currentScript&&document.currentScript.src)||'';
const BASE=ME?ME.replace(/book-promo\.js.*$/,''):'/AMBKidsJoy/';
const IMG=BASE+'books/fidel-fun/img/';
const BUY=BASE+'buy/';                 // sends each visitor to their own Amazon store
const PAGE=BASE+'books/fidel-fun/';    // book page with the free 9-page sample
const T={
 k:{en:'New book by AMBKidsJoy',am:'አዲስ መጽሐፍ ከAMBKidsJoy'},
 t:'Fidel Fun! · ፊደል በደስታ',
 d:{en:'An Amharic–English alphabet workbook for children aged 4–7: all 34 letters, their 7 sounds, tracing pages, games and a certificate. Full colour, 86 pages.',
    am:'ከ4–7 ዓመት ለሆኑ ልጆች የአማርኛ–እንግሊዝኛ የፊደል መለማመጃ መጽሐፍ፤ 34ቱ ፊደላት ከ7 ድምፆቻቸው ጋር፣ ተከትሎ መጻፍ፣ ጨዋታዎችና የምስክር ወረቀት። ባለቀለም፣ 86 ገጾች።'},
 buy:{en:'Buy on Amazon',am:'በአማዞን ይግዙ'},
 free:{en:'Free sample',am:'ነጻ ናሙና'},
 scan:{en:'Scan with your phone to buy',am:'ለመግዛት በስልክዎ ይቃኙ'}};
const css=`.amb-book{max-width:1040px;margin:22px auto 0;display:grid;grid-template-columns:auto 1fr auto;gap:18px;align-items:center;padding:16px 18px;border-radius:20px;
background:linear-gradient(135deg,#FFF6D6 0%,#E6F5EC 60%,#E6F0FB 100%);border:2px solid #F4B400;color:var(--ink,#1B2A4A);font-family:var(--body,system-ui,sans-serif);box-sizing:border-box}
.amb-book .cv{width:104px;height:auto;border-radius:8px;box-shadow:0 6px 16px rgba(0,0,0,.18);display:block}
.amb-book .k{font-size:.78rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:#1E8A5B}
.amb-book h2{margin:2px 0 4px;font-family:var(--display,system-ui);font-size:1.3rem;line-height:1.25;color:#D9302B}
.amb-book p{margin:0 0 10px;font-size:.95rem;line-height:1.5}
.amb-book .links{display:flex;flex-wrap:wrap;gap:8px}
.amb-book .links a{display:inline-flex;align-items:center;gap:6px;padding:8px 16px;border-radius:999px;text-decoration:none;font-weight:800;font-size:.95rem;border:2px solid #E0A800;color:#1B2A4A;background:#fff}
.amb-book .links a.buy{background:#FF9900;border-color:#FF9900;color:#111}
.amb-book .qr{text-align:center;font-size:.75rem;font-weight:700;color:var(--ink-soft,#4F5F7E);max-width:140px}
.amb-book .qr img{width:120px;height:120px;display:block;margin:0 auto 4px;border-radius:10px;background:#fff;padding:4px;border:2px solid #FF9900}
@media (max-width:720px){.amb-book{grid-template-columns:auto 1fr}.amb-book .qr{display:none}}
@media (max-width:440px){.amb-book{grid-template-columns:1fr;text-align:center}.amb-book .cv{margin:0 auto}.amb-book .links{justify-content:center}}`;
function lang(){return document.documentElement.lang==='en'?'en':'am'}
function tx(o){return typeof o==='string'?o:o[lang()]}
function place(el){
  const a=document.getElementById('amb-author');
  if(a&&a.parentNode){ if(el.nextSibling!==a) a.parentNode.insertBefore(el,a); }
  else if(el.parentNode!==document.body||document.body.lastElementChild!==el){ document.body.appendChild(el); }
}
function render(){
  let el=document.getElementById('amb-book');
  if(!el){el=document.createElement('aside');el.id='amb-book';el.className='amb-book';el.setAttribute('aria-label','Fidel Fun! book');}
  el.innerHTML=`<a href="${PAGE}" aria-hidden="true" tabindex="-1"><img class="cv" src="${IMG}cover-thumb.jpg" alt="" loading="lazy" width="104" height="135"></a>
  <div><div class="k">${tx(T.k)}</div><h2>${T.t}</h2><p>${tx(T.d)}</p>
   <div class="links"><a class="buy" href="${BUY}" target="_blank" rel="noopener" data-goatcounter-click="fidelfun-buy-amazon">🛒 ${tx(T.buy)} · $14.99</a><a href="${PAGE}" data-goatcounter-click="fidelfun-free-sample">⬇ ${tx(T.free)}</a></div></div>
  <div class="qr"><img src="${IMG}qr-buy-amazon.svg" alt="QR code: buy Fidel Fun! on Amazon" loading="lazy" width="120" height="120">${tx(T.scan)}</div>`;
  place(el);
}
function init(){
  const s=document.createElement('style');s.textContent=css;document.head.appendChild(s);
  render();
  new MutationObserver(render).observe(document.documentElement,{attributes:true,attributeFilter:['lang']});
  // author.js may add its card after us: keep the book card just above it
  const a=document.getElementById('amb-author'); if(!a){ setTimeout(()=>{const el=document.getElementById('amb-book'); if(el) place(el);},0); }
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
