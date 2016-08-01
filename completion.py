import sublime_plugin

class MarkdeepCompletionListener(sublime_plugin.EventListener):

    def on_query_completions(self, view, prefix, locations):
        syntax = view.settings().get('syntax')
        if not 'Markdeep' in syntax:
            return []

        if prefix == '':
            elements = map(lambda e: view.substr(e), view.find_by_selector('entity.name.type'))
            suggestions = map(self.format_heading, elements)

            return list(suggestions)

        return []

    def format_heading(self, heading):
        lower = heading.replace(' ', '').lower()
        striped = lower.strip('#')
        return heading, striped
