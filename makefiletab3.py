# Copyright 2013  Lars Wirzenius
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Mickael Delahaye has a plugin for Gedit version 2 to turn off
# the "spaces instead of tabs" setting for Makfiles:
# see http://whilefalse.com/gedit-makefiletab/ for that.
# This is a plugin for Gedit 3 that does the same thing.
# I have no idea what I'm doing, so this may be quite horrible.
# Patches welcome.


'''A Gedit v3 plugin to insert real TAB characters into Makefiles.'''


from gi.repository import GObject, Gedit


class MakefileTabPlugin(GObject.Object, Gedit.WindowActivatable):

    __gtype_name__ = 'MakefileTabPlugin'

    window = GObject.property(type=Gedit.Window)

    def do_update_state(self):
        doc = self.window.get_active_document()
        view = self.window.get_active_view()
        if doc and view and view.get_editable():
            mime_type = doc.get_mime_type()
            if 'makefile' in mime_type:
                view.set_insert_spaces_instead_of_tabs(False)
