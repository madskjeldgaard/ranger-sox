from __future__ import (absolute_import, division, print_function)

import os
import subprocess

from ranger.api.commands import Command


class sox_base(Command):
    # The so-called doc-string of the class will be visible in the built-in
    # help that is accessible by typing "?c" inside ranger.
    """:sox_base <filename>

    Not really used directly, so don't!
    """

    # The execute method is called when you run this command in ranger.
    def execute(self):

        # Do the sox stuff
        self.perform_on_selected_files()

        # Unmark files when done
        self.fm.thisdir.mark_all(False)

    def soxcommand(self, fn):
        # self.fm.notify("Normalizing file " + fn + "!")
        suffix = "_n"

        newfn = self.filename_with(suffix, fn)

        lvl = (-0.1)

        # The sox operation being used
        param = f"--norm={lvl}"

        # The full command
        command = f"sox '{fn}' '{newfn}' {param}"

        return command

    def filename_with(self, tag, filename):
        from pathlib import Path

        infile = Path(filename)
        fn = Path(infile.stem + tag + infile.suffix)
        fn = infile.parent.joinpath(fn)

        return fn

    def perform_on_selected_files(self):
        for file in self.fm.thisdir.get_selection():
            file = file.path

            # Make sure the file exists
            if not os.path.exists(file):
                self.fm.notify("The given file does not exist!", bad=True)
                return

            command = self.soxcommand(file)
            self.fm.notify("Executing: " + command + "!")

            # execute the command
            self.fm.execute_command(
                command,
                universal_newlines=True,
                stdout=subprocess.PIPE)


class norm(sox_base):
    """:norm <filename>

    Normalize file to -0.1 db
    """

    def soxcommand(self, fn):
        suffix = "_n"

        newfn = self.filename_with(suffix, fn)

        lvl = (-0.1)

        # The sox operation being used
        param = f"--norm={lvl}"

        # The full command
        command = f"sox '{fn}' '{newfn}' {param}"

        return command


class trim(sox_base):
    """:trim <filename>

    Trim silence from beginning and end of file
    """

    def soxcommand(self, fn):
        suffix = "_t"

        newfn = self.filename_with(suffix, fn)

        # The sox operation being used
        param = "silence -l 1 0.125 1% -1 2.0 1% ;"

        # The full command
        command = f"sox '{fn}' '{newfn}' {param}"

        return command


class splitbysilence(sox_base):
    """:splitbysilence <filename>

    Split file into several files by detecting silence
    """

    def soxcommand(self, fn):
        suffix = "_split"

        newfn = self.filename_with(suffix, fn)

        # The sox operation being used
        param = "silence 1 0.1 1% 1 0.1 1% : newfile : restart;"

        # The full command
        command = f"sox '{fn}' '{newfn}' {param}"

        return command


class stereo2mono(sox_base):
    """:stereo2mono <filename>

    Downmix to mono from stereo
    """

    def soxcommand(self, fn):
        suffix = "_mono"

        newfn = self.filename_with(suffix, fn)

        # The sox operation being used
        param = "remix 1,2 ;"

        # The full command
        command = f"sox '{fn}' '{newfn}' {param}"

        return command


class fade(sox_base):
    """:fade <filename>

    Add small fade in/out to file to remove clicks
    """

    def soxcommand(self, fn):
        suffix = "_faded"

        newfn = self.filename_with(suffix, fn)

        # The sox operation being used
        param = "fade t 0.01 0 0.01;"

        # The full command
        command = f"sox '{fn}' '{newfn}' {param}"

        return command


class reverse(sox_base):
    """:reverse <filename>

    Reverses audio file
    """

    def soxcommand(self, fn):
        suffix = "_rev"

        newfn = self.filename_with(suffix, fn)

        # The sox operation being used
        param = "reverse;"

        # The full command
        command = f"sox '{fn}' '{newfn}' {param}"

        return command


class channels1(sox_base):
    """:channels1 <filename>

    Convert to 1 channel
    """

    def soxcommand(self, fn):
        suffix = "_1chan"

        newfn = self.filename_with(suffix, fn)

        # The sox operation being used
        param = "channels 1;"

        # The full command
        command = f"sox '{fn}' '{newfn}' {param}"

        return command


class channels4(sox_base):
    """:channels4 <filename>

    Convert to 4 channel
    """

    def soxcommand(self, fn):
        suffix = "_4chan"

        newfn = self.filename_with(suffix, fn)

        # The sox operation being used
        param = "channels 4;"

        # The full command
        command = f"sox '{fn}' '{newfn}' {param}"

        return command


class samplerate48k(sox_base):
    """:samplerate48k <filename>

    Convert to 48khz
    """

    def soxcommand(self, fn):
        suffix = "_48khz"

        newfn = self.filename_with(suffix, fn)

        # The sox operation being used
        param = "rate 48k;"

        # The full command
        command = f"sox '{fn}' '{newfn}' {param}"

        return command


class bitrate16(sox_base):
    """:bitrate16 <filename>

    Convert to 16 bit bitrate
    """

    def soxcommand(self, fn):
        suffix = "_16bit"

        newfn = self.filename_with(suffix, fn)

        # The sox operation being used
        param = "-b 16;"

        # The full command
        command = f"sox '{fn}' {param} '{newfn}' "

        return command


class bitrate24(sox_base):
    """:bitrate24 <filename>

    Convert to 24 bit bitrate
    """

    def soxcommand(self, fn):
        suffix = "_24bit"

        newfn = self.filename_with(suffix, fn)

        # The sox operation being used
        param = "-b 24;"

        # The full command
        command = f"sox '{fn}' {param} '{newfn}' "

        return command
