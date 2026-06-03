# Blog of Development Process

> Note that this Blog is in reverse chronological order, i.e. newest update on top.

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
    - The most similar plugin idea I could find is [ScreenSnap](https://designersoup.itch.io/screensnap-blender-timelapse-plugin) which ...TBD watch video for more information on minor details... However, ...TBD...
- Creation of this Git repo and blog file, intended to be reviewed by course organizers.
