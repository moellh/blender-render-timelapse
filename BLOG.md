# Blog of Development Process

> Note that this Blog is in reverse chronological order, i.e. newest update on top.

## 2026-06-17

- Creating Slides for Idea Presentation using [Slidev](https://sli.dev/), which covers motivation incl. target group & main goals, existing plugins & similar work, basic workflow, user actions and possible tracking techniques, plan, uncertainties and brief set of questions. See slides for further information: [PDF export of slides](./slides/idea/slides-export-dark.pdf).
- Checking feasibility of tracking user actions with by researching types of user actions and techniques available for tracking them. main techniques found are operator polling and using DepsGraph which detects ID of Blender- or scene-element which was changed. The latter can be combined with querying the respective elements data. Also adding a view handler and callbacks for undo & redo actions are possible, which help with tracking the users perspective and filtering out undone actions via undotree approach. Generally, both callback/event-driven and timer/polling-driven approaches are possible. I also tested out each technique in Blender 5.1 to check whether it works. Furthermore, mouse- & key-logging and rendering-callbacks, and likely much more, is possible yet likely less relevant for the add-on given the already mentioned techniques, unless the core components work early and allow for optional tasks, e.g. analysis of user actions for to enhance user's workflow-review-process.
- After the presentation i was given some feedback. Notably, make the scope of the idea narrower, like focussing on mesh creation tracking rather than the huge landscape of Blender functionality. This is already somewhat encompassed in the plan for the first two weeks of implementing only core MVP functionalities and getting only "a simple, scoped example" to work. Still, the focus on mesh generation narrows it even further. Additionally, one student had the idea for adding a UI that allows the user to go back in time incl. live-preview of the scene at that state, similar to MacOS Time Machine (see this [image](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fcdn.macrumors.com%2Farticle-new%2F2016%2F01%2FTime-Machine-screen-800x450.jpg&f=1&nofb=1&ipt=398efad6dc61657ff4d8bae4dcf05e0cd556a894baf7c6c7721cc406a490562a)). I also had a similar idea of version tracking capabilities with in-editor UI. However, this greatly expands the add-on scope and is thus moved to week 3-4 for possible future tasks without guarantee to be implemented. Note, that I thus also added the [TODO.md](./TODO.md) file.

## 2026-06-03

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
