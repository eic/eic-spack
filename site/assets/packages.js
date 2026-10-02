const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const link = u => /^https?:\/\//.test(u || "") ? `<a href="${esc(u)}">${esc(u)}</a>` : "";
let pkgs = [];
const $ = id => document.getElementById(id);

function card(p) {
  const vs = p.versions.slice(0, 8).map(v => v.version + (v.deprecated ? " (deprecated)" : "")).join(", ");
  const variants = Object.entries(p.variants).map(([n, v]) =>
    `<tr><td><code>${esc(n)}</code></td><td>${esc(v.default)}</td><td>${esc(v.description)}</td></tr>`).join("");
  return `<div class="card" id="${esc(p.name)}"><h3>${esc(p.name)}</h3>
  <div class="muted">${esc(p.description)}</div>
  <div>${p.tags.map(t => `<span class="tag">${esc(t)}</span>`).join("")}</div>
  <div class="muted">Versions: ${esc(vs) || "none"}${p.versions.length > 8 ? ", …" : ""}</div>
  <details><summary>Details</summary>
  ${p.homepage ? `<p>Homepage: ${link(p.homepage)}</p>` : ""}
  ${p.maintainers.length ? `<p>Maintainers: ${p.maintainers.map(m => `<a href="https://github.com/${esc(m)}">@${esc(m)}</a>`).join(", ")}</p>` : ""}
  ${p.builtin_base ? `<p class="muted">Extends builtin package ${esc(p.builtin_base)}.</p>` : ""}
  ${variants ? `<table><tr><th>Variant</th><th>Default</th><th>Description</th></tr>${variants}</table>` : ""}
  ${p.dependencies.length ? `<p>Depends on: ${p.dependencies.map(esc).join(", ")}</p>` : ""}
  </details></div>`;
}

function render() {
  const q = $("q").value.toLowerCase(), tag = $("tag").value;
  const hits = pkgs.filter(p => (!tag || p.tags.includes(tag)) &&
    (!q || [p.name, p.description, ...p.maintainers, ...Object.keys(p.variants)].join(" ").toLowerCase().includes(q)));
  $("status").textContent = `${hits.length} of ${pkgs.length} packages`;
  $("list").innerHTML = hits.map(card).join("");
}

fetch("data/packages.json").then(r => r.json()).then(d => {
  pkgs = d.packages;
  const tags = [...new Set(pkgs.flatMap(p => p.tags))].sort();
  $("tag").innerHTML += tags.map(t => `<option>${esc(t)}</option>`).join("");
  $("q").addEventListener("input", render);
  $("tag").addEventListener("change", render);
  render();
  if (location.hash) document.getElementById(decodeURIComponent(location.hash.slice(1)))?.querySelector("details")?.setAttribute("open", "");
}).catch(() => { $("status").textContent = "Could not load package data."; });
