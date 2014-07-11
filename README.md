ckanext-mx
==========

CKAN custom theme for datos.gob.mx

![screenshot](https://raw.githubusercontent.com/mxabierto/ckanext-dgm/master/screenshot.png)

Updating locales
----------------

This theme overrides some translations on CKAN. When installing it, remember to
run ```./bin/build-combined-ckan-mo.sh```.

That script considers that ```ckanext-mx``` is installed in the same folder as
```CKAN```, as in:

    src
      - ckanext-mx
      - ckan

If you're using a different structure, change the script.
