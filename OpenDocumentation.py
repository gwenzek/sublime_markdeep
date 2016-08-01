import webbrowser
import sublime_plugin

DOC_URL = "http://casual-effects.com/markdeep/features.md.html"

CONTEXT_HELP = {
    'markup': 'basicformatting',
    'markup.raw.block': 'fencedcodeblocks',
    'markup.raw.block.diagram': 'diagramexamples',
    'markup.raw.math, markup.raw.block.math': 'embeddedmath',
    'meta.image': 'imagesandvideo',
    'meta.link': 'links',
    'meta.paragraph.list, markup.list': 'lists',
}

class MarkdeepOpenDocumentation(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        cursor = view.sel()[0].begin()
        scopes = sorted(map(lambda s: (view.score_selector(cursor, s), s), CONTEXT_HELP.keys()))
        score, scope = scopes[-1]

        url = DOC_URL
        if score > 0:
            url += '#' + CONTEXT_HELP[scope]
        webbrowser.open_new_tab(url)
