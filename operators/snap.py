import bpy

from .utils.functions import get_sequences_under_cursor
from .utils.doc import doc_name, doc_idname, doc_brief, doc_description


class POWER_SEQUENCER_OT_snap(bpy.types.Operator):
    """
    *Brief* Snaps selected strips to the time cursor ignoring locked sequences.

    Automatically selects sequences if there is no active selection.
    """

    doc = {
        "name": doc_name(__qualname__),
        "demo": "",
        "description": doc_description(__doc__),
        "shortcuts": [
            ({"type": "S", "value": "PRESS", "shift": True}, {}, "Snap sequences to cursor")
        ],
        "keymap": "Sequencer",
    }
    bl_idname = doc_idname(__qualname__)
    bl_label = doc["name"]
    bl_description = doc_brief(doc["description"])
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return context.sequences

    def execute(self, context):
        sequences = (
            context.selected_sequences
            if len(context.selected_sequences) > 0
            else get_sequences_under_cursor(context)
        )
        for s in sorted(sequences, key=lambda s: s.frame_final_start):
            s.frame_start = context.scene.frame_current

        return {"FINISHED"}