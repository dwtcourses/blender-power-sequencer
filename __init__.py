#
# Copyright (C) 2016-2019 by Nathan Lovato, Daniel Oakey, Razvan Radulescu, and contributors
#
# This file is part of Power Sequencer.
#
# Power Sequencer is free software: you can redistribute it and/or modify it under the terms of the
# GNU General Public License as published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Power Sequencer is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with Power Sequencer. If
# not, see <https://www.gnu.org/licenses/>.
#
import bpy

from .addon_preferences import register_preferences, unregister_preferences
from .addon_properties import register_properties, unregister_properties
from .operators import get_operator_classes
from .utils.register_shortcuts import register_shortcuts
from .handlers import register_handlers, unregister_handlers
from .utils import addon_auto_imports
from .ui import register_ui, unregister_ui


# load and reload submodules
##################################
modules = addon_auto_imports.setup_addon_modules(
    __path__, __name__, ignore_packages=[".utils", ".audiosync"]
)


bl_info = {
    "name": "Power Sequencer",
    "description": "Video editing tools for content creators",
    "author": "Nathan Lovato",
    "version": (1, 4, 0),
    "blender": (2, 80, 0),
    "location": "Sequencer",
    "tracker_url": "https://github.com/GDquest/Blender-power-sequencer/issues",
    "wiki_url": "https://www.gdquest.com/docs/documentation/power-sequencer/",
    "support": "COMMUNITY",
    "category": "Sequencer",
}


addon_keymaps = []


def register():
    global addon_keymaps

    register_preferences()
    register_properties()
    register_handlers()
    register_ui()

    operator_classes = get_operator_classes()
    for cls in operator_classes:
        bpy.utils.register_class(cls)

    keymaps = register_shortcuts(operator_classes)
    addon_keymaps += keymaps

    print("Registered {} with {} modules".format(bl_info["name"], len(modules)))


def unregister():
    global addon_keymaps

    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()

    operator_classes = get_operator_classes()
    for cls in operator_classes:
        bpy.utils.unregister_class(cls)

    unregister_ui()
    unregister_preferences()
    unregister_properties()
    unregister_handlers()

    print("Unregistered {}".format(bl_info["name"]))


def is_blender_version_compatible(version: Tuple[int, int, int]) -> bool:
    """Returns True if the `version` is greater or equal to the current Blender version.
    Converts the versions to integers to compare them."""
    version_int = version[0] * 1000 + version[1] * 10 + version[2]
    blender_version_int = bpy.app.version[0] * 1000 + bpy.app.version[1] * 10 + bpy.app.version[2]
    return blender_version_int >= version_int
