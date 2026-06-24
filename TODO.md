# Tasks


## Core Functionality

> Tasks part of initial 2-week implementation of core functionalities for scoped MVP.

- Tracking:
    - [ ] Depsgraph Updates: Complete history of depsgraph updates incl. timestamp & object IDs
    - [ ] Viewport Draw: Complete history of viewport changes incl timestamp and viewport perspective
    - [ ] Undo/Redo: Map undos & redos to operators and create undo-tree of operators
    - [ ] Store data into file, e.g. JSON, check size accumulation
- Action Filtering:
    - [ ] Filter out undo user actions and invisible actions
- Rendered Output:
    - [ ] Render video from tracked data (with fixed camera towards center)
    - [ ] Adaptive intervals between changes instead of actual time intervals
- Smart Camera:
    - [ ] Linear camera movement between tracked view points


## Optimization

> Tasks that improve upon the MVP and suffice for course submission.

- [ ] ...


## Further Tasks

> Further ideas of how the plugin can be extended.

- [ ] Undo-tree UI element for going back with live-preview


## Archived Tasks

> Finished or aborted from above sections.

- [x] Set up Blender Add-on / Extension
- [x] DISCARDED: Operator Polling for tracking user actions: Complete history of operators incl. timestamp
    - Discarded because not all changes are done by operators. Maybe this task is reactivated in smaller for to address possible further tasks: "Semantic grouping of actions" or "Workflow Analysis".
- [x] gzip JSON on stopping the recording with toggle in UI
- [x] Record viewport only on substantial change or time
    - Possibly improved upon further in the future by tracking plots of when new viewport states are written incl. viewport variables
