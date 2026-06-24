import bpy

from .log import get_logger
from .tracking.recorder import get_recorder

_logger = get_logger()


class RENDER_TIMELAPSE_PT_recording(bpy.types.Panel):
    bl_category = "Render Timelapse"
    bl_label = "Recording"
    bl_idname = "RENDER_TIMELAPSE_PT_recording"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_order = 0

    def draw(self, context):
        layout = self.layout
        if layout is None:
            return

        recorder = get_recorder()

        if recorder.recording:
            layout.operator(
                "render_timelapse.stop_recording",
                text="Stop Recording",
                icon="PAUSE",
            )
            row = layout.row()
            row.label(text=f"Events: {len(recorder.events)}")
            row.label(text=f"Undo nodes: {len(recorder.undo_tree.nodes)}")
        else:
            layout.operator(
                "render_timelapse.start_recording",
                text="Start Recording",
                icon="PLAY",
            )

        layout.separator()

        layout.label(text="Output Directory:")
        layout.prop(context.scene, "rtl_data_dir", text="")

        layout.separator()

        layout.label(text="Settings:")
        box = layout.box()
        box.prop(context.scene, "rtl_poll_interval", text="Poll interval")
        box.prop(context.scene, "rtl_save_interval", text="Save interval")
        box.prop(context.scene, "rtl_max_file_mb", text="Max. file size (MB)")


class RENDER_TIMELAPSE_PT_rendering(bpy.types.Panel):
    bl_category = "Render Timelapse"
    bl_label = "Rendering"
    bl_idname = "RENDER_TIMELAPSE_PT_rendering"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_order = 1

    def draw(self, context):
        layout = self.layout
        if layout is None:
            return

        layout.label(text="TBD")


class RENDER_TIMELAPSE_OT_start_recording(bpy.types.Operator):
    bl_idname = "render_timelapse.start_recording"
    bl_label = "Start Recording"
    bl_description = "Start recording operators, depsgraph, viewport, and undo tree"

    def execute(self, context):
        recorder = get_recorder()
        data_dir = getattr(context.scene, "rtl_data_dir", "") or ""
        recorder.poll_interval = context.scene.rtl_poll_interval
        recorder.save_interval = context.scene.rtl_save_interval
        recorder.max_file_size_mb = context.scene.rtl_max_file_mb
        recorder.start(data_dir)
        return {"FINISHED"}


class RENDER_TIMELAPSE_OT_stop_recording(bpy.types.Operator):
    bl_idname = "render_timelapse.stop_recording"
    bl_label = "Stop Recording"
    bl_description = "Stop recording and save remaining data to JSON file"

    def execute(self, context):
        recorder = get_recorder()
        recorder.stop()
        return {"FINISHED"}


def _register_properties():
    bpy.types.Scene.rtl_data_dir = bpy.props.StringProperty(
        name="Data Directory",
        description="Directory to save recording JSON files",
        default=bpy.app.tempdir,
        subtype="DIR_PATH",
    )
    bpy.types.Scene.rtl_poll_interval = bpy.props.FloatProperty(
        name="Poll Interval (s)",
        description="Interval between operator polls (lower = more accurate)",
        default=0.2,
        min=0.05,
        max=1.0,
        step=0.05,
        precision=2,
    )
    bpy.types.Scene.rtl_save_interval = bpy.props.FloatProperty(
        name="Save Interval (s)",
        description="How often to flush events to JSON",
        default=5.0,
        min=1.0,
        max=60.0,
        step=1.0,
    )
    bpy.types.Scene.rtl_max_file_mb = bpy.props.IntProperty(
        name="Max File (MB)",
        description="Warn when JSON file exceeds this size",
        default=50,
        min=1,
        max=1000,
    )


def _unregister_properties():
    props = (
        "rtl_data_dir",
        "rtl_poll_interval",
        "rtl_save_interval",
        "rtl_max_file_mb",
    )
    for p in props:
        if hasattr(bpy.types.Scene, p):
            delattr(bpy.types.Scene, p)


_classes = (
    RENDER_TIMELAPSE_PT_recording,
    RENDER_TIMELAPSE_PT_rendering,
    RENDER_TIMELAPSE_OT_start_recording,
    RENDER_TIMELAPSE_OT_stop_recording,
)


def register():
    _register_properties()
    _logger.debug("Registered properties")
    for cls in _classes:
        try:
            bpy.utils.register_class(cls)
            _logger.debug(f"Registered class {cls.__name__}")
        except RuntimeError:
            _logger.warning(f"Class {cls.__name__} already registered (reload)")


def unregister():
    for cls in reversed(_classes):
        try:
            bpy.utils.unregister_class(cls)
            _logger.debug(f"Unregistered class {cls.__name__}")
        except RuntimeError:
            pass
    _unregister_properties()
    _logger.debug("Unregistered properties")
