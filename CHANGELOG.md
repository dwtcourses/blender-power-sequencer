# Changelog

This document lists new features, improvements, changes, and bug fixes in every release of the add-on.

## Power Sequencer 1.5

This release is a work-in-progress. New features may contain bugs. New features may also require Blender 2.82.

### New features

- Interactive trim tool in the toolbar. In Blender 2.82+, press <kbd>T</kbd> to toggle the toolbar and select a tool, or press <kbd>Shift</kbd> <kbd>Spacebar</kbd> to bring the interactive tool menu.
- `Channel Offset` can trim strips in the way. Press <kbd>Ctrl</kbd> <kbd>Alt</kbd> <kbd>Up</kbd> and <kbd>Ctrl</kbd> <kbd>Alt</kbd> <kbd>Down</kbd> to do so.

### Improvements

- `Trim instantly`: Move the time cursor to the end of the trim, and when removing gaps.

### Changes

- Refactored the loading code to automatically discover operators and tools.
- Added a version check for features that require Blender 2.82, so the add-on keeps working with Blender 2.80+.
- Renamed `Make Still Image` to `Make Hold Frame`.

### Bug fixes

- Fixed an error when trying to use `Align Audios`.
- Fixed several bugs in `Merge From Scene Strip`.
- Fixed a couple of scene-related operators that weren't working anymore.
- Fixed two errors when using `Swap Strips`.
- Fixed an error when trying to apply `Make Hold Frame` to an audio sequence.
- Fixed `Merge From Scene Strips` not working

## Power Sequencer 1.4

This new release brings many quality of life improvements to the existing toolset, including a rewrite of the interactive trim tool.

### Manual

We now have a [Getting Started](https://www.gdquest.com/docs/documentation/power-sequencer/getting-started/) guide that showcases some of the most useful features in the add-on.

You can also read about all the features and shortcuts in the [Features Reference](https://www.gdquest.com/docs/documentation/power-sequencer/reference/).

### New features

Power Sequencer is now **included in Blender 2.81**! 🙂

Big thanks to everyone who helped us get there. Development continues in this repository, and help is still welcome, as always.

- `Expand to surrounding`: expands the sequence's handles to the surrounding cuts, for each contiguous block of selected sequences.
- `Snap`: Replacement for Blender's built-in snap that auto-selects strips under the time cursor if you don't have a selection.

### Improvements

- `Mouse trim`:
  - Allows you to trim strips in multiple channels freely.
  - The drawing now shows the trimmed area with a yellow overlay.
  - Displays shortcuts and information in the Sequencer's header.
  - Change the trim side on the fly by pressing the letter <kbd>O</kbd>.
  - Toggle ripple edit and select mode on the fly with <kbd>Alt</kbd> and <kbd>Shift</kbd> respectively.
  - Press <kbd>Ctrl</kbd> when starting the tool to snap the start frame to the closest cut.
  - Allow trimming gaps reliably with the mouse and tablet.
- `Import Local Footage`:
  - Does not impose a folder structure on you anymore.
  - Automatically sets imported sequences to use proxy sizes based on your preferences. See `Preferences -> Add-ons -> Power Sequencer -> Proxy`.
- `Set Playback Speed`: Add shortcut to set the speed to 3x.
- `Delete Direct`: You can now press <kbd>X</kbd> to remove strips without confirmation, but using Blender's default behavior, and <kbd>Alt</kbd><kbd>X</kbd> to smartly remove transitions.
- `Space Sequences`:
  - Offsets strips to the right of the time cursor, ignoring locked sequences.
  - Now also offsets timeline markers.
- `Snap Selection`: auto-select strips under the time cursor.
- `Add Speed`:
  - Use the full source clip for single sequences, so you can slip their content.
  - Change the shortcuts and add <kbd>Alt</kbd><kbd>2</kbd>, <kbd>Alt</kbd><kbd>3</kbd>, <kbd>Alt</kbd><kbd>4</kbd> to speed up to 2, 3, and 4 times the normal speed.
- `Copy Markers as Timecodes`: remove the hours if the last marker is at less than 1h.
- `Markers Delete Direct`: removed the confirmation popup when deleting markers with X.
- `Concatenate Strips`:
  - Now has a more consistent behavior, <kbd>C</kbd> will only concatenate one strip or the selection, while <kbd>Shift</kbd><kbd>C</kbd> will always concatenate all strips in the channel.
  - Added option to ripple edit.
- Improved performances when adding Power Sequencer's features to menus or panels.
- `Snap selection to time cursor`: Make behavior consistent and improve performances when many strips are selected.

#### User Interface

Cleaned up the Power Sequencer menu based on @tintwotin's suggestions:

- No more two levels deep sub-menus
- Removed most icons to be consistent with Blender's Sequencer menus
- Removed custom text, using the Operator names instead, for consistency with the rest of Blender
- Add `Speed Up Movie Strip` and `Speed Remove Effect` to the menu

### Changes

- Removed the add-on auto updater feature: we cannot have it in the add-on for official Blender releases.
- `Mouse cut`: renamed to `Mouse trim`, and the old `Mouse trim` to `Mouse trim instantly`.
- Changed the shortcuts of `Playback Speed Decrease` and `Playback Speed Increase` to <kbd>,</kbd> and <kbd>.</kbd> respectively, so they don't override the already bound <kbd>[</kbd> and <kbd>]</kbd>.
- Changed the shortcut of `Add Transform` to <kbd>Alt</kbd><kbd>T</kbd> so it doesn't collide with `Mouse Trim Modal`.
- Removed the `Add Transform` tool: the one from the VSE Transform tool add-on achieves the same result.
- Removed `Synchronize titles`: it was a weird, not so useful tool that was replaced by `Markers Snap Matching Strips`.
- Update the YouTube rendering preset to match the platform's recommendations for 1080p.
- `Playback Speed Set`: changed shortcuts from numpad keys to number keys.
- Source code:
  - Merged all utility functions into one `.utils.functions` module. See `/operators/utils/functions.py`.
  - Improved and simplified code around various operators.
  - Renamed `crossfade_remove.py` to `transitions_remove`.

### Bug fixes

- `Delete crossfade`: Fixed error when deleting a crossfade between color strips.
- `Add Crossfade`: Fixed not crossfading with color strips.
- `Expand to surrounding cuts`: Fixed breaking the strip if trying to use the tool on the the first or the last sequence in the scene.
- `Playback Speed`:
  - Fixed error when calling `Decrease Playback Speed`.
  - Fixed `Set Playback Speed` shortcuts not working anymore in Blender 2.80.
  - Fixed error with `Playback Speed Increase` when it was already at maximum speed.
- `Delete Direct`: Fixed always moving input strip handles when removing transition effects.
- `Import Local Footage`: Fixed error when importing footage in a new project.
- `Grab`: Fixed error when there was no selection and no strip under the mouse cursor.
- `Mouse Trim Instantly`: Rewrote the tool to fix cases where it would stop trimming.
- `Import Local Footage`: Fixed files re-importing after moving the project folder.
- `Preview To Selection`: Use sequences in the current context if nothing is selected.
- `Ripple Delete`:
  - Fixed changing the time cursor's position.
  - Fixed not working after an undo.
- `Speed Up Movie Strip`: Fixed created meta-strip being the length of the full source movie strip when speeding up a single movie strip.
- `Concatenate Strips`: Fixed error when there was no strip in the channel after the selected or hovered strip.

## Power Sequencer 1.3: Blender 2.80 support

### New features

- Power Sequencer now works in **Blender 2.80**

### Improvements

- `Trim left or right handles`, formerly `Smart Snap`:
  - Trims now ripple through the channel if you keep <kbd>Shift</kbd> down. E.g. <kbd>Shift</kbd><kbd>Alt</kbd><kbd>K</kbd>
  - Auto selects strips under the cursor if there is no selection
- `Cut`: Select side based on mouse cursor position after cut
- Various operators: use seconds instead of frames for duration.
- Added new shortcuts to deselect strips left or right of the time cursor, <kbd>Shift</kbd><kbd>Q</kbd> and <kbd>Shift</kbd><kbd>E</kbd>
- `Concatenate strips`: Add ability to trim and concatenate multicam, color, and adjustment strips
- `Fade add`: improved usability, now tries to detect and respect existing fades, detects the strips' length to prevent errors, updates instantly as you increase the fade duration
- `Mouse cut`:
  - Added snapping support with <kbd>Ctrl</kbd>
  - You can now trim multiple sequences in a single channel
  - Improved drawing
  - Use gizmo color from the user's color theme

### Changes

The code now follows the official Blender conventions for operator names etc. We also renamed some files and cleaned up some code to make it easier to browse and to maintain.

- `Import local footage`:
  - Removed code to find an empty channel, use Blender 2.80's default behavior instead
  - Use seconds for time
  - Changed shortcut to shortcut to <kbd>Ctrl</kbd><kbd>Shift</kbd><kbd>I</kbd>
- `Render for web` now only applies a render preset, it does not render
- Removed `border select` now we can click and drag to box select in the sequencer
- Removed Remove unused shortcut for `Edit Crossfade`
- Updated the Blender add-on updater to the latest version
- Removed empty panel UI
- Added workaround Blender 2.80's audio not updating bug

### Bug fixes

- `Concatenate strips`: Fixed error from concatenating strips with effect sequences
- `Clear Fades`:
  - Fixed wrong `eval`" string error
  - Fixed clear fades not working with audio strips
- `Remove gaps`: fixed strange ripple behavior
- `Trim left or right handles`: fixed error when the time cursor didn't overlap strips
- `Add speed`: fixed error with effect strips
- `Import local footage`:
  - fixed importing hidden directories
  - fixed error with gif files
- `Mouse cut`: fixed error when trying to cut a transition effect strip
- `Gap remove`: fixed error with effect strips
- Fixed error when removing `crossfades` between effect strips
- `Jump to cut`:
  - fixed skipping some cuts on short sequences
  - fixed error when there was no animation data in the sequencer
- `Channel offset`: fixed moving locked strips

### Support our work

- [Follow GDquest](https://twitter.com/NathanGDquest) on Twitter
- You can buy one of our [game creation courses](https://gumroad.com/gdquest) for you or one of your friends. They make for a great present and help us to keep going! ☺

## Power Sequencer 1.2

### 📘 Free Tutorials

Learn to use BPSrender from the command line! We still need people to tell us that it works well everywhere before we can integrate it in Blender. Also, we need your help to design a nice render panel 😄

- [Fast Blender VSE render with BPSrender](https://www.youtube.com/watch?v=LJQptYvXAnw)
- [Precise and Fast selections with Blender's Sequencer](https://www.youtube.com/watch?v=ewwFVsNCBNg)
- [BPSProxies: create proxies fast with FFMPEG](https://youtu.be/oFLo7IHfGB0)

_Note: if you [install bpsrender with pip](https://pypi.org/project/bpsrender/), you can call bpsrender directly like so: `bpsrender blender_file_path [options]`, instead of typing `python -m bpsrender ...`_

### 💻 User Interface

Thanks to @aditiapratama and @libreartist, we now have a nice **toolbar menu**! It will show you most available tools and keyboard shortcuts.

![Power Sequencer toolbar menu](https://i.imgur.com/M8Mk5RH.png)

### 🎥🕺 New features

- **Remove crossfade**: Remove crossfades in a clean way, as you'd expect! If you select one or more transition effects like Crossfade or Wipe, pressing <kbd>X</kbd> will now bring the sequences back together to form a precise cut.
- **Remove Gaps and ignore locked strips**: Blender's default tool to remove gap isn't very smart. We had to code our own to create the feature below...
- **Cut with the mouse, without touching locked strips**: edit to music with the add-on's fast mouse-based tools! Lock your audio strip and you're good to go 😃
- **Select related strips**: find and select effects related to the selection, to then cut, copy or duplicate a strip with everything that should come with it.
- **Space strips based on mouse position**: this is bound to the <kbd>=</kbd> key by default

#### BPSProxies

The proxy render script got serious love in this version.

- Thanks to François Grassard, a TV engineer, we now have **super efficient proxy rendering** presets! These proxies are designed to be easy on Blender, and they offer way smoother preview than Blender's ones 😃. They also generate way faster
- You can now use convenient presets to render proxies, thanks to [@jooert](https://github.com/jooert). Use the `--preset` or `-p` option followed by the preset's name. This version ships with the `mp4`, `webm`, and `nvenc` presets
  - Nvenc is Nvidia's solution to encode MP4 with your graphics card. It requires ffmpeg 4, an nvidia GPU that supports Nvenc encoding, and I'm not sure this is available on linux! But it will work on Windows. It's especially fast with 50% and 100% sized proxies. The rendering speed difference isn't as big with 25% proxies.
- You can now **render 25%, 50%, and 100% proxies**! The default size is still 25%. use the `--size` option (`-s` in short form) when calling the program from the command line. E.g. `-s 50` to generate 50% proxies
- The code is better organized now, easier to read and to contribute to in the future. Thanks [@sudopluto](https://github.com/sudopluto) for making this possible 🙂

#### Meta strips

- **Resize to content**: if you edit inside a group or meta strip, you may want to trim it to use it as a compositing group. Now you can! Works on all selected strips at once.
- **UnMeta many strips**: <kbd>Alt</kbd> <kbd>G</kbd> now works on all selected meta strips at once
- **Auto-trim** your nested timelines when you UnMeta strips: also works by default with <kbd>Alt</kbd> <kbd>G</kbd>. If you don't want this to happen, use Resize to Content first

#### Scenes

- **Convert selection to scene strip**: If you want to use the node compositor to do complex grade, or to help organize your project, you'll want to use scene strips at times, instead of meta strips.

### ✅ Improvements

- Auto crossfades (<kbd>Ctrl</kbd> <kbd>Alt</kbd> <kbd>C</kbd>) now work in a **single channel by default**, as in every other professional video editing program
  - You can also **add multiple crossfades** at a time, e.g. to create an image slideshow with fades between each picture
  - This makes it a lot easier to export Blender edits to Davinci Resolve, Premiere, or Final Cut with the [EDL export add-on](https://github.com/tin2tin/ExportEDL)
  - Also now works with the Multicam strips
- Grab closest cut (<kbd>Shift</kbd> <kbd>Alt</kbd> <kbd>G</kbd>) now supports linked strips! It's the fastest way to select and transform the strips' handles on either side of a cut.
- Delete direct now automatically **deletes the strip under the mouse cursor** if there's nothing selected.
- **Swap strips vertically**: You can now conveniently change the order of effects or linked strips, e.g. picture overlays
- Smartly remove strips: if you press X but don't have anything selected, Power Sequencer will find and delete the strips under the mouse cursor for you!
- Jump in time with <kbd>Shift</kbd> <kbd>➡</kbd> and <kbd>Shift</kbd> <kbd>⬅</kbd>: It's consistent with <kbd>⬅</kbd> and <kbd>➡</kbd> to move 1 frame on the timeline. This new tool works in seconds so the jump will be the same regardless of your project's framerate!
- **Concatenate in multiple channels at a time**, and concatenate linked strips! The concatenate tool got a rewrite to make better decisions based on your selection
- **Concatenate towards the right**: Press <kbd>Alt</kbd> <kbd>C</kbd> and <kbd>Shift</kbd> <kbd>Alt</kbd> <kbd>C</kbd> to respectively concatenate the previous strip towards the next one, or concatenate all strips before the selected towards the right.
- **Auto-selection**: If you don't have anything selected, Power Sequencer will use the strip under the cursor for concatenate, delete, and grab operators, saving your extra keystrokes and time 😄
- **Edit crossfades with the grab tool**: grab became smarter. If you only select cross effects, it G will select the handles on either side of the crossfade instead of trying to move it directly.

#### Improvements to the source code

We've reorganized and simplified many features, to make it easier for you to read and to contribute! Now, all marker-related features, fade-related features, etc. are grouped together.

### 🤕 Fixes

- Removed the option to swap strips with effects, as they were causing problems
- Fixed errors when adding crossfades, that could happen with different starting selections
- The add-on will now only load necessary files in Blender, making startup a little faster
- Fixed an error when trying to delete (<kbd>X</kbd>) without a selection
- BPSrender got a few fixes:
  - If you set your render to the /tmp\ folder, BPSrender wouldn't work. It now reads your render settings instead to properly set the render path
  - Render now works as expected when there's whitespace in the file paths
- Proxies rendered with BPSProxies should now be in sync with the original footage: the previous settings we used caused offsets in rare cases
- Fixed errors when trying to delete strips
- Fixed Concatenate not taking in account the selection if more than one strip is selected in a given channel
- Fixed strips changing channels when using Snap Selection to Cursor

## Power Sequencer 1.1: Faster edits 🎞✂

📅 Released in August 2018

_Huge thanks to all the contributors who made this release possible: @doakey3 and @sudopluto, @razcore-art, @jooert, and @Blezyn, who recently joined the adventure 😊. Thanks to them this new version brings many new features and improvements to the add-on!_

### Free tutorials

**Two new tutorials** came out to complement the project. They are about Python programming, to help more people create their own tools and contribute to existing add-ons:

- [Learn to Code Blender Features in Python: Add-On Programming Tutorial](https://www.youtube.com/watch?v=1_Jo9NShkP8)
- [Auto-Completion for Blender Python in Any Code Editor](https://www.youtube.com/watch?v=IQgLBnPO2uo)

### 🎥🕺 New features

- **Multithreaded rendering** with BPSRender: use this command line tool to leverage all your CPU cores! Works on all platforms and available as a stand-alone program. ⚠ Only tested on Ubuntu and Windows 10! _Known issues: on Windows, you will sometimes need to close Blender instances manually with the task manager if you interrupt the render._

- **Unspeed**: remove a speed effect from a video sequence
- **Clear fades**: remove fade animation cleanly on selected sequences
- **Deselect strips** to the left or right of the time cursor
- **Swap two strips**: works across channels and not just to the left or the right of the selected strip, unlike Blender's built-in tool
- **Markers as time codes**: write a list of timecodes followed by the markers' names to create quick links in your YouTube video description or comments
- **Markers from selected strips**: Create a new marker at the start of each strip in the selection
- **Match strips to markers**: snap selected strips to markers that have a similar name

### ✅ Improvements

_Existing features got some love as well!_

- **Multithreaded proxies** now shows a percentage-based progress for each video being rendered
- **Multithreaded proxies**: supports calling presets from the command line. More work planned for version 1.2
- Many small improvements happened to exsting features, e.g. to automatically select strip near the mouse cursor if nothing is selected.

### 🤕 Fixes

**Restored the missing interface** code so you can call the contextual Power Sequencer menu again, and find the power sequencer tab in the menu. We need help to design the UI: we have a developer who wants to work on it, but we need a UX designer to guide him!

Reply to [this issue](https://github.com/GDquest/Blender-power-sequencer/issues/90) and [that issue](https://github.com/GDquest/Blender-power-sequencer/issues/89) if you want to help us wit it 😄

### ⚠ Experimental

- **Auto align audio and video**: this tool for tech-savy people, currently not available in blender
- **Batch transcode videos**: transcode selected videos to the same frame rate from blender! Uses FFMPEG. More work planned for version 1.2
- **Trim in and and out points**: trim the left or the right of the strip closest to the mouse, using the time cursor. No shortcut assigned by default: you'll have to create shortcut entries manually for `power_sequencer.trim_three_point_edit`
