const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
fetch("data/environments.json").then(r => r.json()).then(d => {
  document.getElementById("envs").innerHTML = d.environments.map(e =>
    `<div class="card"><h3>${esc(e.name)}</h3><ul>${e.specs.map(s => `<li><code>${esc(s)}</code></li>`).join("")}</ul>
    <p class="muted"><a href="https://github.com/eic/eic-spack/blob/develop/environments/${esc(e.name)}/spack.yaml">spack.yaml</a></p></div>`).join("");
}).catch(() => { document.getElementById("envs").textContent = "Could not load environment data."; });
