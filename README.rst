Motivation
==========

`Rope <http://rope.sourceforge.net/>`_ is a great tool for python development.

It is a `refactoring library <http://rope.sourceforge.net/overview.html>`_
with the marvelous side effect of letting you navigate throughout code.

You can use it with either `emacs <http://rope.sourceforge.net/ropemacs.html>`_
of `vim <http://rope.sourceforge.net/ropevim.html>`_

This recipe
===========

This `zc.buildout <http://www.buildout.org/>`_ recipe makes a
`.ropeproject folder <http://rope.sourceforge.net/overview.html#ropeproject-folder>`_
with search paths pointing to the eggs of your choice... and their transitive dependencies!

Benefits
~~~~~~~~

1. Make rope both faster and more precise. [#]_

   The reason is that search paths are set **explicitly**,
   so rope does't have to guess through directory hierarchies.

2. A very good complement to the `omelette recipe <http://pypi.python.org/pypi/collective.recipe.omelette>`_.
   Actually, code navigation is way easier that grepping. Give it a try.

.. [#] *This statement has not been evaluated by the FDA.*


Usage
~~~~~

In your buildout.cfg include the recipe, with the eggs property set to one or more eggs::

    [buildout]
    ...
    parts = ... ropeproject

    [ropeproject]
    recipe = collective.recipe.ropeproject
    eggs = ${anything_you_want}

Source
~~~~~~

Source code lives at http://github.com/collective/collective.recipe.ropeproject.git.
