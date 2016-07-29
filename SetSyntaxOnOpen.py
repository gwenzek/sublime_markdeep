import sublime_plugin
import os.path

class MarkdeepFileListener(sublime_plugin.EventListener):
    def on_load_async(self, view):
        if not view.window() or not view.window().active_view():
            return

        fileName = view.file_name()
        if not fileName:
            return
        if fileName.endswith('.md.html'):
            view.set_syntax_file('Packages/Markdeep/markdeep.sublime-syntax')
