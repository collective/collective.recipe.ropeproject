import logging, os, zc.buildout

class Recipe:

    def __init__(self, buildout, name, options):
        self.name, self.options = name, options

    def install(self):
        myoption = self.options['myoption']
        logging.getLogger(self.name).info('**** Hello %s ****', myoption)
        return myoption

    def update(self):
        pass
