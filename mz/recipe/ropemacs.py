import logging, os, zc.buildout
import zc.recipe.egg

class Recipe:

    def __init__(self, buildout, name, options):
        self.name, self.options = name, options
        self.egg = zc.recipe.egg.Scripts(buildout, name, options)

    def install(self):
        requirements, ws = self.egg.working_set()
        print 'Part:', self.name
        print 'Egg requirements:'
        for r in requirements:
            print r
        print 'Working set:'
        for d in ws:
            print d
        print 'extra paths:', self.egg.extra_paths
        return ()

    update = install
