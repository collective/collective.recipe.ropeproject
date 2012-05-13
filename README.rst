Usage
=====

In your buildout.cfg include the recipe, with the eggs property set to whatever you need
(tipically ${instance:eggs})::

    [buildout]
    ...
    parts = ... ropeproject
    
    [instance]
    eggs = ...
    
    [ropeproject]
    recipe = il.recipe.ropeproject
    eggs = ${instance:eggs}
