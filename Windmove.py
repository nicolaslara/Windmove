import sublime
import sublime_plugin

class NextGroupCommand(sublime_plugin.WindowCommand):
    def run(self):
        num_groups = self.window.num_groups()
        current_group = self.window.active_group()
        if current_group < num_groups - 1:
            self.window.focus_group(current_group + 1)


class PrevGroup(sublime_plugin.WindowCommand):
    def run(self):
        num_groups = self.window.num_groups()
        current_group = self.window.active_group()
        if current_group > 0:
            self.window.focus_group(current_group - 1)
