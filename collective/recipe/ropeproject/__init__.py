"""
This recipe creates a `.ropeproject/config.py` configuration
with python_path matching the specified eggs and their dependencies.
"""

import logging, os, zc.buildout
import zc.recipe.egg
import inspect, shutil

from rope.base.project import Project
from rope.base import default_config

class Recipe:

    def __init__(self, buildout, name, options):
        self.name, self.options = name, options
        self.egg = zc.recipe.egg.Scripts(buildout, name, options)

    def install(self):
        requirements, ws = self.egg.working_set()
        MyProject('', pathlist=[f.location for f in ws])
        return ()

    update = install

ropefolder='.ropeproject'

class MyProject(Project):

    def __init__(self, projectroot, pathlist):
        remove_dir(os.path.join(projectroot, ropefolder))
        self.pathlist = pathlist
        super(MyProject, self).__init__(projectroot, ropefolder)
        print self.address

    def _default_config(self):
        orig_source = inspect.getsource(default_config)
        pref_source = inspect.getsource(default_config.set_prefs)
        start, end = orig_source.split(pref_source)
        pref_path_adds = '\n' + ''.join(
            ["    prefs.add('python_path', '%s')\n" % p for p in self.pathlist])
        return start + pref_source + pref_path_adds + end


def remove_dir(path):
    "removes recursively directory at path, if it exists"
    if os.path.exists(path):
        shutil.rmtree(path)
