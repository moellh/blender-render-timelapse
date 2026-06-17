---
theme: default
background: false
fonts:
  sans: Inter
  mono: JetBrains Mono
  weights: '300,400,600,700'
  provider: google
layout: cover
class: text-center
highlighter: shiki
drawings:
  persist: false
transition: fade
info: |
  ## Render-Timelapse
  Blender Add-on for Project of Practical Course "Developing Blender Plugins for Digital Art and Content Creation" in Summer Term 2026
author: Henrik Möllmann
---
<script setup>
import { onMounted } from 'vue'

onMounted(() => {
  const el = document.createElement('div')
  el.id = 'slide-page-no'
  el.style.cssText = 'position:fixed;bottom:14px;right:20px;color:#999;font-size:20px;font-family:JetBrains Mono,monospace;z-index:9999;pointer-events:none'

  const update = () => {
    const slides = document.querySelectorAll('.slidev-page')
    for (let i = 0; i < slides.length; i++) {
      if (slides[i].offsetParent !== null) {
        const n = parseInt(slides[i].getAttribute('data-slidev-no'))
        el.textContent = n > 1 ? String(n) : ''
        return
      }
    }
  }

  document.body.appendChild(el)
  update()

  const observer = new MutationObserver(update)
  if (document.querySelector('#app')) {
    observer.observe(document.querySelector('#app'), {
      childList: true, subtree: true, attributes: true, attributeFilter: ['style', 'class']
    })
  }
})
</script>

<style>
#slide-page-no { color: #999; }
</style>

<div class="absolute top-6 left-0 right-0 text-muted text-xs">Idea Presentation for Project by Henrik Möllmann</div>

<div>

<h1 class="!mt-0 !mb-0">Render-Timelapse</h1>

<div class="h-8" />

<div class="italic text-xl">Record your Blender editing process and create a beautiful video of it.</div>

</div>

<div class="absolute bottom-6 left-0 right-0 text-center text-muted text-xs">Practical Course "Developing Blender Plugins for Digital Art and Content Creation" in Summer Term 2026</div>

---


<div class="flex flex-col justify-center h-full">

<div class="max-w-xl mx-auto mb-0">
  <div class="grid grid-cols-2 gap-4">
    <div class="flex items-center gap-3 p-3 rounded" style="background:rgba(245,158,11,0.1);border:1px solid #f59e0b;">
      <img src="/icons/3940120.png" class="w-16 h-16 shrink-0" />
      <div class="min-w-0 leading-tight text-left">
        <div class="text-xl font-bold mb-1" style="color:#f59e0b;line-height:1.2">Digital Artists</div>
        <div class="text-xs text-[var(--slidev-theme-text)] opacity-90" style="line-height:1.3">Reflect on creation process &amp; showcase on social media</div>
      </div>
    </div>
    <div class="flex items-center gap-3 p-3 rounded" style="background:rgba(245,158,11,0.1);border:1px solid #f59e0b;">
      <img src="/icons/8388575.png" class="w-16 h-16 shrink-0" />
      <div class="min-w-0 leading-tight text-left">
        <div class="text-xl font-bold mb-1" style="color:#f59e0b;line-height:1.2">Tutors</div>
        <div class="text-xs text-[var(--slidev-theme-text)] opacity-90" style="line-height:1.3">On the fly creation of step-by-step visualization for teaching others</div>
      </div>
    </div>
  </div>
</div>

<div class="flex justify-center my-0" style="height:40px;">
  <svg viewBox="0 0 200 40" style="width:200px;height:40px;">
    <defs>
      <marker id="m-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
        <path d="M 0 0 L 10 5 L 0 10 z" fill="#999"/>
      </marker>
    </defs>
    <path d="M 60 0 C 80 4, 100 10, 100 20 L 100 35" stroke="#999" stroke-width="2" fill="none"/>
    <path d="M 140 0 C 120 4, 100 10, 100 20" stroke="#999" stroke-width="2" fill="none"/>
    <line x1="100" y1="30" x2="100" y2="38" stroke="#999" stroke-width="2" marker-end="url(#m-arrow)"/>
  </svg>
</div>

<div class="flex justify-center mb-0">
  <div class="px-5 py-6 rounded bg-gray/10 border border-gray/30 text-center flex flex-col items-center gap-1">
    <img src="https://www.blender.org/wp-content/uploads/2020/07/blender_logo-1280x391.png" class="h-10 shrink-0" />
    <span class="text-xl font-bold" style="color:var(--slidev-theme-text)">Add-on</span>
  </div>
</div>

<div class="flex justify-center my-0 w-full max-w-2xl mx-auto" style="height:102px;margin-bottom:-32px;">
  <svg viewBox="0 0 692 102" style="width:100%;height:102px;">
    <defs>
      <marker id="s-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">
        <path d="M 0 0 L 10 5 L 0 10 z" fill="#999"/>
      </marker>
    </defs>
    <path d="M 346 0 Q 346 55, 220 78" stroke="#999" stroke-width="2" fill="none" marker-end="url(#s-arrow)"/>
    <path d="M 346 0 L 346 100" stroke="#999" stroke-width="2" marker-end="url(#s-arrow)"/>
    <path d="M 346 0 Q 346 55, 472 78" stroke="#999" stroke-width="2" fill="none" marker-end="url(#s-arrow)"/>
  </svg>
</div>

<div class="max-w-2xl mx-auto" style="margin-top:0;">
  <div class="flex justify-center gap-4 items-start">
    <div class="flex-1 max-w-[220px] flex flex-col items-center">
      <div class="w-full p-3 rounded text-center" style="background:rgba(56,189,248,0.1);border:1px solid #38bdf8;">
        <img src="/icons/4449102.png" class="w-16 h-16 mx-auto mb-1.5" />
        <div class="text-xl font-bold mb-0.5" style="color:#38bdf8;line-height:1.2">Rendered Output</div>
        <div class="text-xs text-[var(--slidev-theme-text)] opacity-90" style="line-height:1.3">No Blender UI. Stylized rendering of primitives</div>
      </div>
    </div>
    <div class="flex-1 max-w-[220px] flex flex-col items-center mt-8">
      <div class="w-full p-3 rounded text-center" style="background:rgba(56,189,248,0.1);border:1px solid #38bdf8;">
        <img src="/icons/16008186.png" class="w-16 h-16 mx-auto mb-1.5" />
        <div class="text-xl font-bold mb-0.5" style="color:#38bdf8;line-height:1.2">Action Filtering</div>
        <div class="text-xs text-[var(--slidev-theme-text)] opacity-90" style="line-height:1.3">Skip experimental &amp; faulty steps via undotree</div>
      </div>
    </div>
    <div class="flex-1 max-w-[220px] flex flex-col items-center">
      <div class="w-full p-3 rounded text-center" style="background:rgba(56,189,248,0.1);border:1px solid #38bdf8;">
        <img src="/icons/8540857.png" class="w-16 h-16 mx-auto mb-1.5" />
        <div class="text-xl font-bold mb-0.5" style="color:#38bdf8;line-height:1.2">Smart Camera</div>
        <div class="text-xs text-[var(--slidev-theme-text)] opacity-90" style="line-height:1.3">Smoothen users viewport path to display what is edited</div>
      </div>
    </div>
  </div>
</div>

</div>

---

<div class="flex flex-col h-full" style="gap:10px;">

<h1 style="color:#4ade80!important;font-weight:700;display:flex;align-items:center;gap:6px;margin:0;">
<img src="/icons/4449102.png" style="width:42px;height:42px;" /> Existing Work: Timelapse Recording
</h1>

<div class="grid grid-cols-[3fr_2fr] gap-6 flex-1">

<div>
<div style="margin-bottom:16px;">
<div class="text-xl leading-relaxed" style="color:var(--slidev-theme-text);margin:8px 0;">
Capture editor/viewport with fixed/rotating camera after some user actions.
</div>
<div class="text-xs" style="line-height:2;color:#999;">
<div>&bull; <strong style="color:var(--slidev-theme-text)">ScreenSnap Turntable</strong> (<a href="https://designersoup.itch.io/screensnap-blender-timelapse-plugin" target="_blank" style="color:#999!important;text-decoration:none!important;border-bottom:none!important;">designersoup.itch.io</a>)</div>
<div>&bull; <strong style="color:var(--slidev-theme-text)">Timelapse Extension</strong> (<a href="https://extensions.blender.org/add-ons/timelapse-extension/" target="_blank" style="color:#999!important;text-decoration:none!important;border-bottom:none!important;">extensions.blender.org</a>)</div>
<div>&bull; <strong style="color:var(--slidev-theme-text)">ReelFlow-Pro</strong> (<a href="https://superhivemarket.com/products/reelflow-pro" target="_blank" style="color:#999!important;text-decoration:none!important;border-bottom:none!important;">superhivemarket.com</a>)</div>
<div>&bull; <strong style="color:var(--slidev-theme-text)">Eastape Timelapse Pro</strong> (<a href="https://www.eastapefilms.com/blogs/eastape-timelapse-pro" target="_blank" style="color:#999!important;text-decoration:none!important;border-bottom:none!important;">eastapefilms.com</a>)</div>
<div>&bull; <strong style="color:var(--slidev-theme-text)">SavePoints</strong> (<a href="https://extensions.blender.org/add-ons/savepoints/" target="_blank" style="color:#999!important;text-decoration:none!important;border-bottom:none!important;">extensions.blender.org</a>)</div>
</div>
</div>

<div v-click="1">
<div class="text-xl" style="color:#ef4444;font-weight:700;">Limitations of ScreenSnap</div>
<ul class="text-xl leading-relaxed" style="color:var(--slidev-theme-text);padding-left:20px;">
<li>Captures in-editor shading mode, incl. &quot;Blender Look&quot; for primitives &amp; mode switches</li>
<li>Captures all actions, even undone actions</li>
<li>Simplistic camera movement independent of actions</li>
</ul>
</div>
</div>

<div v-click="1" style="text-align:center;display:flex;flex-direction:column;align-items:center;justify-content:center;">
<video src="./ScreenSnap_Example_Video.mp4" autoplay loop muted style="width:100%;max-width:300px;border-radius:10px;background:#000;"></video>
<div class="text-xl" style="margin-top:8px;">ScreenSnap Example Output</div>
<div style="margin-top:4px;">
<a href="https://www.youtube.com/watch?v=iDGZUz5b444" target="_blank" class="text-xs" style="color:#999!important;text-decoration:none!important;border-bottom:none!important;">youtube.com/watch?v=iDGZUz5b444</a>
</div>
</div>

</div>
</div>

---

<style>
.scroll-panel { overflow-y: auto; position: relative; height: 100%; padding: 6px; border-radius: 6px; -webkit-overflow-scrolling: touch; scrollbar-width: none; -ms-overflow-style: none; }
.scroll-panel::-webkit-scrollbar { display: none; width: 0; height: 0; }
.scroll-content { transform: translateZ(0); will-change: transform; -webkit-font-smoothing: antialiased; }
.scroll-card { transform: translateZ(0); padding: 8px 10px; margin-bottom: 8px; border-radius: 6px; border: 1px solid rgba(128,128,128,0.2); background: var(--slidev-theme-background); }
.scroll-card a { color: #999; text-decoration: none !important; border-bottom: none !important; }
.scroll-card a:hover { opacity: 0.6; }
.scroll-cat { font-weight: 700; margin-bottom: 6px; padding-left: 4px; }
</style>

<div class="flex flex-col h-full" style="gap:10px;">

<h1 style="color:var(--slidev-theme-text);font-weight:700;display:flex;align-items:center;gap:6px;margin:0;">
Existing Work
</h1>

<div class="grid grid-cols-2 gap-x-4 flex-1 text-left">

<div class="flex flex-col overflow-hidden justify-center">
<h1 style="color:#c084fc!important;font-weight:700;display:flex;align-items:center;gap:6px;margin:0;">
<img src="/icons/16008186.png" class="w-14 h-14 shrink-0" /> Action Recording
</h1>
<div style="padding:6px 4px;">
<div class="text-xl" style="color:var(--slidev-theme-text);line-height:1.4;margin-bottom:6px">
Record sequence of operators to reflect on action or to be repeated again later.
</div>
<div class="text-xs" style="line-height:1.9;color:#999">
<div>• <strong style="color:var(--slidev-theme-text)">Action Recorder</strong> (<a href="https://github.com/InamuraJIN/ActionRecorder" target="_blank" style="color:#999!important;text-decoration:none!important;border-bottom:none!important;">github.com/InamuraJIN/ActionRecorder</a>)</div>
<div>• <strong style="color:var(--slidev-theme-text)">Macros Recorder</strong> (<a href="https://github.com/dairin0d/macros-recorder" target="_blank" style="color:#999!important;text-decoration:none!important;border-bottom:none!important;">github.com/dairin0d/macros-recorder</a>)</div>
<div>• <strong style="color:var(--slidev-theme-text)">Chronicle</strong> (<a href="https://doi.org/10.1145/1866029.1866054" target="_blank" style="color:#999!important;text-decoration:none!important;border-bottom:none!important;">doi.org/10.1145/1866029.1866054</a>)</div>
<div>• <strong style="color:var(--slidev-theme-text)">3D Timeline</strong> (<a href="https://doi.org/10.1111/cgf.12311" target="_blank" style="color:#999!important;text-decoration:none!important;border-bottom:none!important;">doi.org/10.1111/cgf.12311</a>)</div>
</div>
</div>
</div>

<div v-click="1" class="flex flex-col overflow-hidden justify-center">
<h1 style="color:#58a6ff!important;font-weight:700;display:flex;align-items:center;gap:6px;margin:0;">
<img src="/icons/8540857.png" class="w-14 h-14 shrink-0" /> Camera Positioning
</h1>
<div style="padding:6px 4px;">
<div class="text-xl" style="color:var(--slidev-theme-text);line-height:1.4;margin-bottom:4px">
Translate WASD movements into smooth bezier curves.
</div>
<div class="text-xs" style="line-height:1.9;color:#999;margin-bottom:6px">
<div>• <strong style="color:var(--slidev-theme-text)">AutoCam</strong> (<a href="https://extensions.blender.org/add-ons/autocam/" target="_blank" style="color:#999!important;text-decoration:none!important;border-bottom:none!important;">extensions.blender.org</a>)</div>
</div>
<div class="text-xl" style="color:var(--slidev-theme-text);line-height:1.4;margin-bottom:4px">
Automatic extraction of view-points, -paths, and -surfaces.
</div>
<div class="text-xs" style="line-height:1.9;color:#999">
<div>• <strong style="color:var(--slidev-theme-text)">History Assisted View Authoring</strong> (<a href="https://doi.org/10.1145/2556288.2557009" target="_blank" style="color:#999!important;text-decoration:none!important;border-bottom:none!important;">doi.org/10.1145/2556288.2557009</a>)</div>
</div>
</div>
</div>

</div>
</div>

---

<div class="flex flex-col items-center justify-center h-full gap-3 text-center">

<h1 style="margin-bottom:8px;">User Workflow</h1>

<div class="flex items-center justify-center gap-1 w-full max-w-5xl">

<div class="flex flex-col items-center flex-1 relative">
  <div class="border border-gray/30 rounded-lg p-3 flex flex-col items-center gap-2 w-full" style="background:rgba(74,222,128,0.05);">
    <img src="/icons/16008186.png" class="w-16 h-16 shrink-0" />
    <div class="text-xl font-bold" style="color:#4ade80;">Track &amp; Filter Actions</div>
    <div class="flex items-center gap-2 mt-1">
      <div class="text-4xl" style="color:#999;">↑</div>
    </div>
    <div class="flex items-center gap-2">
      <img src="/icons/3940120.png" class="w-14 h-14 shrink-0" />
      <div class="text-xl" style="color:var(--slidev-theme-text);">User Actions</div>
    </div>
  </div>
</div>

<div class="text-4xl" style="color:#999;">→</div>

<div class="flex flex-col items-center flex-1">
  <div class="border border-gray/30 rounded-lg p-3 flex flex-col items-center gap-2 w-full" style="background:rgba(56,189,248,0.05);">
    <img src="/icons/8540857.png" class="w-16 h-16 shrink-0" />
    <div class="text-xl font-bold" style="color:#38bdf8;">Interpolate Camera</div>
    <div class="text-4xl" style="color:#999;">↓</div>
    <div class="flex items-center gap-2">
      <img src="/icons/4449102.png" class="w-14 h-14 shrink-0" />
      <div class="text-xl font-bold" style="color:#f59e0b;">Render Timelapse</div>
    </div>
  </div>
</div>

</div>

</div>

---

<div class="grid grid-cols-[1.4fr_2fr] gap-4 h-[460px] text-xl">

<div class="p-3 overflow-y-auto">
  <h1 style="color:#4ade80!important;font-weight:700;display:flex;align-items:center;gap:6px;margin:0 0 8px 0;">User Actions</h1>
  <div class="space-y-0.5">
    <div><span class="i-ph-monitor-duotone shrink-0 inline-block text-base" style="color:#4ade80"></span> Viewport</div>
    <div><span class="i-ph-cube-duotone shrink-0 inline-block text-base" style="color:#4ade80"></span> Objects</div>
    <div><span class="i-ph-pencil-simple-duotone shrink-0 inline-block text-base" style="color:#4ade80"></span> Edit Operations</div>
    <div><span class="i-ph-knife-duotone shrink-0 inline-block text-base" style="color:#4ade80"></span> Sculpting</div>
    <div><span class="i-ph-palette-duotone shrink-0 inline-block text-base" style="color:#4ade80"></span> Materials, Shading</div>
    <div><span class="i-ph-bone-duotone shrink-0 inline-block text-base" style="color:#4ade80"></span> Rigging</div>
    <div><span class="i-ph-tree-structure-duotone shrink-0 inline-block text-base" style="color:#4ade80"></span> Modifiers, Geometry Nodes</div>
    <div><span class="i-ph-arrow-counter-clockwise-duotone shrink-0 inline-block text-base" style="color:#4ade80"></span> Undo/Redo</div>
    <div><span class="i-ph-code-duotone shrink-0 inline-block text-base" style="color:#4ade80"></span> Scripts, Add-ons</div>
    <div class="text-base" style="color:#999;font-style:italic"><span class="i-ph-swap-duotone shrink-0 inline-block text-xs" style="color:#4ade80"></span> Mode</div>
    <div class="text-base" style="color:#999;font-style:italic"><span class="i-ph-atom-duotone shrink-0 inline-block text-xs" style="color:#4ade80"></span> Physics, Particles</div>
    <div class="text-base" style="color:#999;font-style:italic"><span class="i-ph-layout-duotone shrink-0 inline-block text-xs" style="color:#4ade80"></span> Workspace, UI</div>
    <div class="text-base" style="color:#999;font-style:italic"><span class="i-ph-play-duotone shrink-0 inline-block text-xs" style="color:#4ade80"></span> Animation</div>
  </div>
</div>

<div class="p-3 overflow-y-auto" v-click>
  <h1 style="color:#c084fc!important;font-weight:700;display:flex;align-items:center;gap:6px;margin:0 0 8px 0;">Tracking Techniques</h1>
  <div class="space-y-3">
    <div><div class="text-xl" style="line-height:1.3;">Operator-Polling</div><div class="text-xs" style="color:#999;line-height:1.5;">e.g. <span style="font-family:JetBrains Mono,monospace;color:#999;">bpy.context.window_manager.operators[i]</span></div></div>
    <div><div class="text-xl" style="line-height:1.3;">Depsgraph-Update</div><div class="text-xs" style="color:#999;line-height:1.5;">e.g. <span style="font-family:JetBrains Mono,monospace;color:#999;">bpy.app.handlers.depsgraph_update_post</span></div></div>
    <div><div class="text-xl" style="line-height:1.3;">Scene/Data Snapshot</div><div class="text-xs" style="color:#999;line-height:1.5;">e.g. <span style="font-family:JetBrains Mono,monospace;color:#999;">bpy.context.active_object</span></div></div>
    <div><div class="text-xl" style="line-height:1.3;">Viewport Draw</div><div class="text-xs" style="color:#999;line-height:1.5;">e.g. <span style="font-family:JetBrains Mono,monospace;color:#999;">bpy.types.SpaceView3D.draw_handler_add</span></div></div>
    <div><div class="text-xl" style="line-height:1.3;">Undo/Redo</div><div class="text-xs" style="color:#999;line-height:1.5;">e.g. <span style="font-family:JetBrains Mono,monospace;color:#999;">bpy.app.handlers.undo_pre</span></div></div>
    <div><div class="text-xl" style="line-height:1.3;">Rendering</div><div class="text-xs" style="color:#999;line-height:1.5;">e.g. <span style="font-family:JetBrains Mono,monospace;color:#999;">bpy.app.handlers.render_complete</span></div></div>
    <div><div class="text-base" style="color:#999;font-style:italic;line-height:1.3;">Keylogging</div><div class="text-xs" style="color:#999;line-height:1.5;font-style:italic;">e.g. <span style="font-family:JetBrains Mono,monospace;">modal_handler_add</span></div></div>
  </div>
</div>

</div>

---

<h1><span style="color:var(--slidev-theme-text);">Phase 1:</span> <strong style="color:#4ade80;">Core MVP Functionalities</strong></h1>

<div class="text-base mb-5 flex items-center justify-center gap-1" style="color:#999;">
  <span>Jun 17 → Jul 1</span>
  <span>(Milestone Presentation)</span>
</div>

<div class="text-left max-w-2xl mx-auto">
  <div class="space-y-3 pl-6">
    <div class="text-xl flex items-center gap-3"><span class="w-9 flex items-center justify-center shrink-0"><span class="i-ph-activity-duotone inline-block text-lg" style="color:#999"></span></span><span>Track actions (operators, viewport, scene)</span></div>
    <div class="text-xl flex items-center gap-3"><span class="w-9 flex items-center justify-center shrink-0"><span class="i-ph-database-duotone inline-block text-lg" style="color:#999"></span></span><span>Recording format &amp; storage</span></div>
    <div class="text-xl flex items-center gap-3"><span class="w-9 flex items-center justify-center shrink-0"><img src="/icons/16008186.png" class="w-8 h-8" /></span><span>Filter via undo-tree</span></div>
    <div class="text-xl flex items-center gap-3"><span class="w-9 flex items-center justify-center shrink-0"><img src="/icons/8540857.png" class="w-8 h-8" /></span><span>Basic camera interpolation</span></div>
    <div class="text-xl flex items-center gap-3"><span class="w-9 flex items-center justify-center shrink-0"><img src="/icons/4449102.png" class="w-8 h-8" /></span><span>Render video from recording in new blender project</span></div>
    <div class="text-xl flex items-center gap-3"><span class="w-9 flex items-center justify-center shrink-0"><span class="i-ph-sliders-duotone inline-block text-lg" style="color:#999"></span></span><span>UI panel</span></div>
  </div>
  <div class="mt-8 text-xl" style="color:var(--slidev-theme-text);opacity:0.9">→ Working add-on with scoped core features and a demo video.</div>
</div>

---

<h1><span style="color:var(--slidev-theme-text);">Phase 2:</span> <strong style="color:#38bdf8;">Polish &amp; Stretch Goals</strong></h1>

<div class="text-base mb-5 flex items-center justify-center gap-1" style="color:#999;">
  <span>Jul 1 → Jul 15</span>
  <span>(Final Presentation &amp; Demo)</span>
</div>

<div class="text-left max-w-2xl mx-auto">
  <div class="space-y-3 pl-6">
    <div class="text-xl flex items-center gap-3"><span class="w-9 flex items-center justify-center shrink-0"><span class="i-ph-warning-circle-duotone inline-block text-lg" style="color:#999"></span></span><span>Time buffer for unexpected issues</span></div>
    <div class="text-xl flex items-center gap-3"><span class="w-9 flex items-center justify-center shrink-0"><span class="i-ph-pencil-duotone inline-block text-lg" style="color:#999"></span></span><span>Polish UX &amp; edge cases with sensible defaults</span></div>
    <div class="text-xl flex items-center gap-3"><span class="w-9 flex items-center justify-center shrink-0"><span class="i-ph-timer-duotone inline-block text-lg" style="color:#999"></span></span><span>Adaptive frame timing</span></div>
    <div class="text-xl flex items-center gap-3"><span class="w-9 flex items-center justify-center shrink-0"><img src="/icons/8540857.png" class="w-8 h-8" /></span><span>Improved camera interpolation</span></div>
    <div class="text-xl flex items-center gap-3"><span class="w-9 flex items-center justify-center shrink-0"><span class="i-ph-lightning-duotone inline-block text-lg" style="color:#999"></span></span><span>Performance optimizations</span></div>
    <div class="text-xl flex items-center gap-3"><span class="w-9 flex items-center justify-center shrink-0"><img src="/icons/4449102.png" class="w-8 h-8" /></span><span>Vertex/edge overlays</span></div>
  </div>
  <div class="mt-8 text-xl" style="color:var(--slidev-theme-text);opacity:0.9">→ Polished demo video &amp; final presentation ready.</div>
</div>

<div class="flex items-center justify-center gap-3 mt-4 flex-wrap" v-click>
  <div class="text-xl" style="color:#c084fc;font-weight:bold">Further Ideas:</div>
  <div class="px-4 py-2 rounded-full text-base" style="background:rgba(192,132,252,0.1);border:1px solid rgba(192,132,252,0.3);color:#c084fc;">Action Inspector</div>
  <div class="px-4 py-2 rounded-full text-base" style="background:rgba(192,132,252,0.1);border:1px solid rgba(192,132,252,0.3);color:#c084fc;">Workflow Analysis</div>
  <div class="px-4 py-2 rounded-full text-base" style="background:rgba(192,132,252,0.1);border:1px solid rgba(192,132,252,0.3);color:#c084fc;">Semantic grouping of actions &amp; scene components</div>
  <div class="px-4 py-2 rounded-full text-base" style="background:rgba(192,132,252,0.1);border:1px solid rgba(192,132,252,0.3);color:#c084fc;">Action animations</div>
</div>

---

<h1 style="color:#b8855a!important;">Uncertainties</h1>

<div class="leading-relaxed text-left mt-6">
  <div class="space-y-4 pl-6">
    <div class="flex items-baseline gap-3"><span class="w-9 flex items-center justify-center shrink-0"><span class="i-ph-database-duotone inline-block text-2xl" style="color:#b8855a"></span></span><span class="w-64 shrink-0"><strong class="text-xl" style="color:#b8855a;">Recording Format:</strong></span><span class="text-xl" style="color:var(--slidev-theme-text);"><div>&bull; JSON/text initially or binary format for less storage</div><div>&bull; Representation of undo tree</div></span></div>
    <div class="flex items-baseline gap-3" v-click><span class="w-9 flex items-center justify-center shrink-0"><span class="i-ph-camera-duotone inline-block text-2xl" style="color:#b8855a"></span></span><span class="w-64 shrink-0"><strong class="text-xl" style="color:#b8855a;">Camera Interpolation:</strong></span><span class="text-xl" style="color:var(--slidev-theme-text);"><div>&bull; Linear, spline, ML-based approximation of view-path</div></span></div>
    <div class="flex items-baseline gap-3" v-click><span class="w-9 flex items-center justify-center shrink-0"><span class="i-ph-globe-duotone inline-block text-2xl" style="color:#b8855a"></span></span><span class="w-64 shrink-0"><strong class="text-xl" style="color:#b8855a;">Scene Types:</strong></span><span class="text-xl" style="color:var(--slidev-theme-text);"><div>&bull; Landscape vs. orbitable</div><div>&bull; No viewport change during scripts/geometry nodes</div></span></div>
    <div class="flex items-baseline gap-3" v-click><span class="w-9 flex items-center justify-center shrink-0"><span class="i-ph-timer-duotone inline-block text-2xl" style="color:#b8855a"></span></span><span class="w-64 shrink-0"><strong class="text-xl" style="color:#b8855a;">Timing Model:</strong></span><span class="text-xl" style="color:var(--slidev-theme-text);"><div>&bull; Adaptive intervals</div><div>&bull; Filter irrelevant actions</div><div>&bull; Pauses for camera movement</div><div>&bull; Script execution</div></span></div>
    <div class="flex items-baseline gap-3" v-click><span class="w-9 flex items-center justify-center shrink-0"><span class="i-ph-lightning-duotone inline-block text-2xl" style="color:#b8855a"></span></span><span class="w-64 shrink-0"><strong class="text-xl" style="color:#b8855a;">Performance Hit:</strong></span><span class="text-xl" style="color:var(--slidev-theme-text);"><div>&bull; Add-on overhead running constantly in background</div><div>&bull; Render speed for large or long-edited scenes</div></span></div>
  </div>
</div>

---

<div class="flex flex-col h-full">

<h1 style="margin-bottom:8px;">Q&amp;A</h1>

<div class="flex-1 grid grid-cols-2 gap-4 px-4 py-2">

<div class="bg-blue/15 border border-blue/40 p-4 shadow-sm max-w-[192px] text-left relative justify-self-end self-end" style="border-radius: 16px;">
  <div class="text-lg" style="color:var(--slidev-theme-text);opacity:0.95;">
    Who already used a timelapse tool (for modelling or elsewhere)?
  </div>
</div>

<div class="bg-blue/15 border border-blue/40 p-4 shadow-sm max-w-[169px] text-left relative justify-self-start self-end" style="border-radius: 16px;">
  <div class="text-lg" style="color:var(--slidev-theme-text);opacity:0.95;">
    What would you use such an add-on for?
  </div>
</div>

<div class="bg-blue/15 border border-blue/40 p-4 shadow-sm max-w-xs text-left relative justify-self-end self-start" style="border-radius: 16px;">
  <div class="text-lg" style="color:var(--slidev-theme-text);opacity:0.95;">
    Do you have suggestions for improvements or further ideas?
  </div>
</div>

<div class="bg-blue/15 border border-blue/40 p-4 shadow-sm max-w-sm text-left relative justify-self-start self-start" style="border-radius: 16px;">
  <div class="text-lg" style="color:var(--slidev-theme-text);opacity:0.95;">
    What do you think about the additions, like filtering of undone actions, smart camera, or custom rendering of primitives?
  </div>
</div>

</div>

<div class="text-center text-xl pb-6">
  <span class="i-ph-github-logo-duotone shrink-0 inline-block text-xl" style="color:#999" />
  <a href="https://github.com/moellh/blender-render-timelapse" target="_blank" style="color:#999;text-decoration:none;border-bottom:none;">github.com/moellh/blender-render-timelapse</a>
</div>

</div>
