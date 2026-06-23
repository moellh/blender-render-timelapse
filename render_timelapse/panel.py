import bpy

from .log import get_logger

_logger = get_logger()


class RENDER_TIMELAPSE_PT_panel(bpy.types.Panel):
    bl_category = "Render Timelapse"
    bl_label = "Render Timelapse"
    bl_idname = "RENDER_TIMELAPSE_PT_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_order = 0

    def draw(self, context):
        layout = self.layout
        if layout is None:
            return
        layout.label(text="Placeholder Text")
        layout.operator("render_timelapse.placeholder")


class RENDER_TIMELAPSE_OT_placeholder(bpy.types.Operator):
    bl_idname = "render_timelapse.placeholder"
    bl_label = "Placeholder"
    bl_description = "Operator without functionality"

    def execute(self, context):
        _logger.info("Operator without functionality executed")
        return {"FINISHED"}


_classes = (
    RENDER_TIMELAPSE_PT_panel,
    RENDER_TIMELAPSE_OT_placeholder,
)


def register():
    for cls in _classes:
        try:
            bpy.utils.unregister_class(cls)
        except RuntimeError:
            pass
        bpy.utils.register_class(cls)
        _logger.debug(f"Registered class {cls.__name__}")


def unregister():
    for cls in reversed(_classes):
        try:
            bpy.utils.unregister_class(cls)
            _logger.debug(f"Unregistered class {cls.__name__}")
        except RuntimeError:
            pass
