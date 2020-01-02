# ranger-sox
SoX integration plugin for the [Ranger File Manager](https://github.com/ranger/ranger) making audio conversion easy

# Installation
Copy `ranger-sox.py` file to ~/.config/ranger/plugins folder and restart ranger.

# Usage
Select one or more files you want to manipulate using SoX and then execute one of the following commands

Currently available commands:
- `:norm <filename>` - normalize file to -0.1 db
- `:trim <filename>` - trim silence off the beginning and end of file
- `:splitbysilence <filename>` - split a file name into smaller pieces based on silence parts of file
- `:stereo2mono <filename>` - convert stereo to mono
- `:fade <filename>` - add small fades to beginning and end of file to avoid clicks
- `:reverse <filename>` - reverse file
