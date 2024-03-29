"""
Source: http://toomanyideas.net/2013/improve-sublime-text-2-part-1.html
"""
import sublime
import sublime_plugin


class ResetFontSizeToUserDefaultsCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        s = sublime.load_settings("Preferences.sublime-settings")

        if s.has('default_font_size'):
            s.set('font_size', s.get('default_font_size'))
            sublime.save_settings("Preferences.sublime-settings")
