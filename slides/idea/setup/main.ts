export default function setup() {
  const style = document.createElement('style')
  style.textContent = `
/* ── Light mode (default) ── */
.slidev-layout {
  background: #fff !important;
  color: #000 !important;
}
.slidev-layout h1,
.slidev-layout h2,
.slidev-layout h3,
.slidev-layout h4,
.slidev-layout h5,
.slidev-layout h6 {
  color: #000 !important;
}
.slidev-layout code,
.slidev-layout pre {
  font-family: 'JetBrains Mono', monospace !important;
  background: #f5f5f5 !important;
  color: #000 !important;
}
.slidev-layout :not(pre) > code {
  background: #f0f0f0 !important;
  padding: 0.15em 0.4em;
  border-radius: 4px;
}
.slidev-layout a { color: #0969da !important; }
.slidev-layout blockquote {
  border-left-color: #ddd !important;
  color: #999 !important;
}
.slidev-layout table { color: #000 !important; }
.slidev-layout th { background: #f6f8fa !important; color: #000 !important; }
.slidev-layout td { border-color: #ddd !important; }

/* Muted text — single gray for all secondary content */
.text-muted { color: #999 !important; }

/* ── Dark mode (.dark class on <html>, toggled by d key / UI button) ── */
.dark .slidev-layout {
  background: #000 !important;
  color: #fff !important;
}
.dark .slidev-layout h1,
.dark .slidev-layout h2,
.dark .slidev-layout h3,
.dark .slidev-layout h4,
.dark .slidev-layout h5,
.dark .slidev-layout h6 {
  color: #fff !important;
}
.dark .slidev-layout code,
.dark .slidev-layout pre {
  font-family: 'JetBrains Mono', monospace !important;
  background: #1a1a1a !important;
  color: #eee !important;
}
.dark .slidev-layout :not(pre) > code {
  background: #1a1a1a !important;
}
.dark .slidev-layout a { color: #58a6ff !important; }
.dark .slidev-layout blockquote {
  border-left-color: #555 !important;
  color: #999 !important;
}
.dark .slidev-layout table { color: #fff !important; }
.dark .slidev-layout th { background: #1a1a1a !important; color: #fff !important; }
.dark .slidev-layout td { border-color: #555 !important; }
.dark .slidev-page-number { color: #999 !important; }
  `
  document.head.appendChild(style)
}
