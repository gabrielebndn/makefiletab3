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

from setuptools import setup, find_packages
from pkg_resources import parse_version
import os
import subprocess as sp
import makefiletab3_globals

from setuptools.command.install import install as _install
class PluginFileCreateInstall(_install):
    def  run(self):
        # skip call to super.run because there's no use and produces error message due to missing permission
        from Cheetah.Template import Template
        t = Template(file="makefiletab3.plugin.tmpl")
        t.module_name = makefiletab3_globals.app_name
        t.description = makefiletab3_globals.description
        t.loader = "python3"
        t_file = open(os.path.join(os.path.expanduser("~"), ".local", "share", "gedit", "plugins", makefiletab3_globals.app_name, "makefiletab3.plugin"), "w")
        t_file.write(str(t))
        t_file.flush()
        t_file.close()

setup(
    name = makefiletab3_globals.app_name,
    version = makefiletab3_globals.app_version_string,
    install_requires = ["cheetah"],
    cmdclass={'install': PluginFileCreateInstall},
    
    # metadata for upload to PyPI
    author = "Karl-Philipp Richter",
    author_email = "krichter722@aol.de",
    url='https://github.com/krichter722/makefiletab3',
    description = makefiletab3_globals.description,
    license = "GPLv3",
    keywords = "gedit, make, makefile",
)

