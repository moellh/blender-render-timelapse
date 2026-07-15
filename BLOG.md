# Blog of Development Process

> Note that this Blog is in reverse chronological order, i.e. newest update on top.

## until 2026-07-15

- Filter out viewport samples from undone actions
- Store materials & shaders as separate `.blend` files, so full state storage for them just as for topology changes in mesh. Storing blend files simplifies storing all material & shader attributes.
    - The "Warn at (MB)" UI option still only tracks the JSON and then simply shows a warning at 90%. Would need to be applied to all data in the future since lots of data removed from JSON. Though, besides tracking mesh sizes, user likely already knows asset sizes and material sizes, so not as critical to track.
- Applied feedback of omittinh `_ref` entries in JSON
- Modularized recording storage via core recording JSON and subdirectories for compressed mesh, materials, assets, and previews
- Add adaptive timing by complexity of state changes, number of viewport changes, and duration of rendered video
- Moved rendering to separate Blender process which runs in background. Rendering panel shows its progress incl. number of frames done out of all frames and estimated time.
- Added Add-on defaults and updating preferences of all UI elements.
- Implemented basic "History" Panel: Contains list of states and live preview image below which is captured during recording as simple JPG of 3D viewport.
    - If history branches a state entry shows two buttons for switching between different branches / child nodes.
    - Clicking a state in the list updates the model with that very state. Of course only updates any modelling aspects tracked so far by the add-on, so other blender scene data is ignored.
    - Clicking a state while recording does not create a new state triggered by the state-change registered by the DepsGraph
- Added more state transition animations:
    - Smoother object transforming & vertex movements via interpolation.
    - Creation & Deletion (or just visibility change), topology & Material updates all via simple crossfade: insert new state by "increasing" its opacity, then remove old state by "decreasing" its opacilty.
- Added tracking world background, incl. override in UI with static color or environment map.
- Replaced car example with rocket for demo because simpler, also considering live demo with respect to my novice modelling skills so far
- Create final presentation using [Typst](https://typst.app/), because we must submit the slides (I guess as PDF), and Typst allows for simultaneous PDF & HTML export (latter for directly showing videos).
    - Presentation includes idea recap, example rendering video, implementation parts & challenges (incl. UI captures), comparison to ScreenSnap Add-on, Current state vs. "future work", live demo at the end with super simple demo.
- Fixed sculpting to not flicker in rendering. Grouped DepsGraph updates by brush-stroke lifetime, so mesh update is triggered on stroke finish. Still noticable lags.
- Added additional second at end of rendering to briefly see finished result before video ends.
- For camera interpolation, removed setting interpolating between viewport entries (creating smoothened curve between viewport entires, exactly interpolating them), since keeping this one fully enabled always looks best. Though, added easing UI slider which controls camera speed at start & end to not abruply stop before state changes.
- Create demo videos for presentation with super-basic planned live demo, but 

## until 2026-07-07

- Further modularize recording files: Put meshes into separate files in `meshes_<timestamp>/` directory, always compressed to make JSON smaller and decrease size of any intermediately-decompressed files, e.g. decrease chance of GB+ files in long sessions.
- Add `demo/` dir for recording a simple demo creation process with the working plugin. Current idea is to create a car given reference images. May change or simplify since I'm not yet as good in creating models, so may take unnecessarily long time for little benefit.
- Restructuring and cleaning up the add-on a bit.

## until 2026-07-01

- Implementation of Basic Rendering from Recorded file to complete full add-on pipeline, though incomplete:
    - Added UI panel for Rendering with options as described below
    - Rendering reads the selected JSON which is automatically the just recorded session when stopping a recording
    - Rendering sequentially displays the recorded states & viewport entries. Currently, the add-on assumes alternating (so not overlapping) states and viewport changes as user usually does not both at the same time.
    - Introduced two camera modes "Direct" and "Smooth":
        - Direct is simply creates a frame in the rendered video per state node or viewport entry. The resulting video somewhat resembles classic viewport-captured timelapses and is useful to debug a recording.
        - Smooth regards states and "viewport sections" which are all viewports that happend during a specific state. The rendering shows states and viewport sections alternating. The mode uses variables for setting the duration of each state change (useful for animating state changes) and another one for viewport entry sections. The viewport is approximately interpolated between first and last viewport section with currently two ui parameters defining the curvature/linearity of the interpolation and another one controlling how much the curve approximates/intersects all viewport entries in the viewport section vs. just linearly interpolating the first and the last one.
    - Rendering of primitives by turning vertices/edges/faces on and off in the UI. Vertices are currently basic icospheres. Also added basic UI parameters for setting vertex size and edge thickness, also for each primitive a color and added emission for basic luminance even when not lit. Note that face color is only intended to be applied when it has not material. Besides, to now display all primitives all the time which can be unnecessarily distracting, I added a "dynamic" mode which only renders edges and vertices if not attached to some face.
    - Adapted implementation, so topology changes are correctly recognized in the rendering. This was noticed while testing out whether sculpting works: Currently normal sculpting and topology changes via mesh editing work, however, live updates of dyntopo-sculpting cannot be recorded and tracked since Blender highly optimized them in its low-level implementation which is not accessible to the Python API. Thus, the latter are technically only recognized on mode changes. Maybe, in the future, the addition of animations on state changes from mesh & topology changes could automatically smoothen such larger changes. However, currently no workaround for dyntopo-sculpting is found and user would have to regularly change the mode, e.g. using TAB twice.
- Prepared Milestone presentation, this time using [ObsidianMD](https://obsidian.md/) slides with the [Slides Extended](https://github.com/ebullient/obsidian-slides-extended) plugin, because I found Slidev, which I used for the idea presentation unnecessarily hard and the new solution is just markdown (with minimal HTML). The presentation also shows a video of a rendered output containing 3 objects: The final sculpting part shows that it's still buggy, because I tried hard to get dyntopo-sculpting to work, but it didn't work, just before the presentation.
    - Feeback from Presentation:
        - Regularly save JSON file (and compress) and start with new "part". On max. storage reached, maybe with warning.
        - Next, `_ref` entries in JSON are unnecessary, since the JSON could just look back to the last entry which has a value. Would reduce file size from restating all refs.

## until 2026-06-24

- Optimize mesh storing:
    - Fixed issues where full mesh is unnecessarily stored again, dramatically decreasing JSON file size growth for large models when only a few vertices are changed.
    - Fixed EDIT_MESH and SCULPT mode requiring different treatment when editing the mesh by reading from different data of Blender API
    - Before a mesh was either stored as "full mesh" or "individual vertices" where changed. Handling topology was not handled correctly, especially when using Dyntopo in sculpt mode. Thus, besides "full mesh" storage, implemented "mesh patches", similar to how [Git Diff or Patch files](https://git-scm.com/docs/git-diff) present source code changes. So, unless more than 50% of the mesh are changed, any changes to the mesh are stored individually in the JSON. Unless 100 states with  patches where already applied to the mesh after a "full mesh" state or some ratio of the vertices where patched, only "mesh patches" are used in the JSON rather than "full mesh".
- Implemented basic handling of assets: Currently only textures are covered. So, next to the JSON or gzipped file, an assets folder contains copies of the assets being used in while recording. With hashes, any files there are deduplicated and uniquely identified. Storing them additionally there ensures that any deleted assets in the users project directory are still captured by the recording. However, any assets are currently only weakly associated with materials or other Blender functionalities. This still needs to be correctly implemented.


## until 2026-06-23

- Writing initial tasks to [TODO.md](./TODO.md), categorized into Core Functionality, Optimization, Further Tasks, and Archived Tasks
- Working on Tracking implementation:
    - Early noticed that Operator-Polling can be discarded as tracking method because it only captures some user actions. Instead rely on DepsGraph (returning changed object ID), Viewport handler, and reading scene object data directly. Also using undo- & redo-handlers for recognizing undone or redone state without having to store additional data.
    - Writing tracking data into JSON and optionally adding or replacing it with a gzipped version, which dramatically decreases file size without having to optimize the file format. Simple tracked workflows show filesizes in the few KB to MB range. Of course, user actions adding many vertices or creating topology changes and storing the entire mesh again dramatically increase the file size. Still okay but performance-improvements especially on larger models remains important. Just tested on the Sponza model which has 145185 vertices and edited a few vertices being tracked by the plugin: Raw JSON quickly scales to 80MB, gzipped version is 7MB, zstd compressed file with max. compression is 1MB (but takes a few seconds to compress).
    - After testing multiple layouts for the JSON file, like storing an initial .blend file and tracking further changes, I instead decided on storing all data in the json except for assets, i.e. the add-on regularly stores data to a JSON files and puts any assets used like textures into an assets/ directory to retain assets even when removed in the actual workspace of the user editing the scene. Inside the JSON, some metadata and then a list of "viewport" entries as well as a list of "state" nodes. The viewport entries capture noticable changed viewport state, e.g. angle changed by some degree or distance to pivot point changed by 1% relative to its current distance. Also, only changed data is written into future viewport states, else reference to previous viewport state to save space. Similarly, state entries store visible scene information like the mesh. Then, on mesh update, preferably only the updated mesh data is changed which is currently decided on by <50% mesh data changed or no topology changes. If a state variable is not updated, a reference points to the corresponding entry with the original value.
        - Note that I'm still working on which state variables to capture, so which should be tracked and which must not because irrelevant to rendering. I'll likely start a list of properties tracked or not tracked.
- Added UI N-panel (i.e. opened via N key) in 3D-viewport which has two sections: Recording, Rendering. Rendering is still empty. Recording has start/stop button. While tracking runs, some data is shown like number of captured states & viewports, as well as raw JSON size. Below, you can select the directory where the file is saved, defaulting to blenders temporary directory at /tmp/blender_*/ on Linux. Then, there are some settings for setting save interval, max. file size and file stored on stopping the recording: JSON or gzipped JSON.

## until 2026-06-22

- Setting up basic Blender Add-on/Extension with placeholder UI and Operator rather than using a simple script.

## until 2026-06-17

- Creating Slides for Idea Presentation using [Slidev](https://sli.dev/), which covers motivation incl. target group & main goals, existing plugins & similar work, basic workflow, user actions and possible tracking techniques, plan, uncertainties and brief set of questions. See slides for further information: [PDF export of slides](./slides/idea/slides-export-dark.pdf).
- Checking feasibility of tracking user actions with by researching types of user actions and techniques available for tracking them. main techniques found are operator polling and using DepsGraph which detects ID of Blender- or scene-element which was changed. The latter can be combined with querying the respective elements data. Also adding a view handler and callbacks for undo & redo actions are possible, which help with tracking the users perspective and filtering out undone actions via undotree approach. Generally, both callback/event-driven and timer/polling-driven approaches are possible. I also tested out each technique in Blender 5.1 to check whether it works. Furthermore, mouse- & key-logging and rendering-callbacks, and likely much more, is possible yet likely less relevant for the add-on given the already mentioned techniques, unless the core components work early and allow for optional tasks, e.g. analysis of user actions for to enhance user's workflow-review-process.
- After the presentation i was given some feedback. Notably, make the scope of the idea narrower, like focussing on mesh creation tracking rather than the huge landscape of Blender functionality. This is already somewhat encompassed in the plan for the first two weeks of implementing only core MVP functionalities and getting only "a simple, scoped example" to work. Still, the focus on mesh generation narrows it even further. Additionally, one student had the idea for adding a UI that allows the user to go back in time incl. live-preview of the scene at that state, similar to MacOS Time Machine (see this [image](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.macrumors.com%2Farticle-new%2F2016%2F01%2FTime-Machine-screen-800x450.jpg&f=1&nofb=1&ipt=398efad6dc61657ff4d8bae4dcf05e0cd556a894baf7c6c7721cc406a490562a)). I also had a similar idea of version tracking capabilities with in-editor UI. However, this greatly expands the add-on scope and is thus moved to week 3-4 for possible future tasks without guarantee to be implemented. Note, that I thus also added the [TODO.md](./TODO.md) file.

## until 2026-06-03

- Presentation of blender add-on ideas in practical course "Developing Blender Plugins for Digital Art and Content Creation" at University of Stuttgart.
  This idea aligns with the interests of the course organisers and myself for development of a Blender add-on.
  The basic idea is as follows:
    - Add-on tracks actions being performed by user in Blender-editor and creates a nice-looking video of the creation process.
    - "Nice-looking video" refers to a timelapse of the rendered output of the actual scene being edited, rather than a screen-recording of the Blender-editor.
    - It tracks the Blender-editor viewport and applies an interpolated view to the generated video.
    - It tracks every action of the user which can update the rendered output, with fixed time-intervals in rendered video. Furthermore, using "undo tree" like tracking of actions, inspired by [Vim' feature](https://vimdoc.sourceforge.net/htmldoc/usr_32.html), undone actions are filtered out of the generated video.
    - UI for customization with sensible defaults for seemless workflow while editing.
    - Further possible ideas, like opinionated rendering of invisible primitives like vertices or edges, handling of different types of scenes, minimal post-editing.
    - The most similar plugin idea I could find is [ScreenSnap](https://designersoup.itch.io/screensnap-blender-timelapse-plugin) which screenshots a fixed or rotating viewport after a preconfigured number actions. However, when not captured with "rendered" shading, blender primitives and mode changes are visible. Camera movement is simplistic and not focusing on what is currently being worked.
- Creation of this Git repo and blog file, intended to be reviewed by course organizers.
