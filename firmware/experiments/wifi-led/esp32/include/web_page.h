#pragma once
#include <Arduino.h>
const char WEB_PAGE[] PROGMEM = R"HTML(<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>STM32 LED Lab</title><style>
*{box-sizing:border-box}body{margin:0;background:#f3f5f6;color:#172d35;font:18px system-ui,sans-serif;min-height:100vh;display:grid;place-items:center;padding:24px}
main{width:100%;max-width:490px;background:white;border:1px solid #d7e1e3;border-radius:20px;padding:32px}
small{color:#516970;letter-spacing:.1em}h1{font-size:32px;margin:14px 0}p{line-height:1.5}.state{padding:18px;background:#edf2f3;border-radius:10px;min-height:90px}
.controls{display:flex;gap:12px;margin:24px 0}button{font:inherit;border:1px solid #345660;border-radius:9px;padding:14px 20px;cursor:pointer;flex:1;background:white;color:#172d35}button:first-child{background:#153f49;color:white}button:disabled{opacity:.5;cursor:wait}button:focus-visible{outline:3px solid #df9200;outline-offset:3px}
footer{font-size:14px;color:#516970;line-height:1.6}#refresh{width:100%;font-size:16px;margin-bottom:20px}
</style></head><body><main><small>RESQ-VISION / BENCH EXPERIMENT</small><h1>STM32 LED Lab</h1>
<p>Send a command over Wi-Fi. The STM32 replies with its LED pin state.</p>
<p class="state" id="status" role="status" aria-live="polite">Checking STM32 connection…</p>
<div class="controls"><button id="on" type="button">Turn ON</button><button id="off" type="button">Turn OFF</button></div>
<button id="refresh" type="button">Check connection</button>
<footer>ESP32 → UART → STM32<br>Reported state is GPIO readback. Confirm the actual LED visually.</footer>
</main><script>
const statusEl=document.getElementById('status');
const buttons=[...document.querySelectorAll('button')];
async function request(on){
  buttons.forEach(b=>b.disabled=true);
  statusEl.textContent='Waiting for STM32 confirmation…';
  const controller=new AbortController();
  const timer=setTimeout(()=>controller.abort(),4000);
  try{
    const options={signal:controller.signal,cache:'no-store'};
    if(typeof on==='boolean'){options.method='POST';options.headers={'Content-Type':'application/json'};options.body=JSON.stringify({on});}
    const response=await fetch(typeof on==='boolean'?'/api/led':'/api/status',options);
    const data=await response.json();
    if(!response.ok)throw new Error(data.error||'Request failed; LED state is unknown.');
    if(typeof data.on!=='boolean')throw new Error('Invalid reply; LED state is unknown.');
    statusEl.textContent='STM32 confirmed: LED '+(data.on?'ON':'OFF');
  }catch(error){statusEl.textContent=error.name==='AbortError'?'Connection timed out. LED state is unknown.':error.message;}
  finally{clearTimeout(timer);buttons.forEach(b=>b.disabled=false);}
}
document.getElementById('on').onclick=()=>request(true);
document.getElementById('off').onclick=()=>request(false);
document.getElementById('refresh').onclick=()=>request();
request();
</script></body></html>)HTML";
