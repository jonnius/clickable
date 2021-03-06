.. _clickable-json:

clickable.json Format
=====================

Example:

.. code-block:: javascript

    {
        "template": "cmake",
        "scripts": {
            "test": "make test"
        },
        "dependencies": [
            "libpoppler-qt5-dev"
        ]
    }


.. _clickable-json-arch:

arch
----

Optional, the default is armhf. You may also specify this as a cli arg
(ex: ``--arch="armhf"``)

prebuild
--------

Optional, a custom command to run before a build.

.. _clickable-json-template:

template
--------

Optional, see :ref:`build template <build-templates>` for the full list of options.
If left blank the template will be auto detected.

build
-----

Optional, a custom command to run instead of the default build. If using
the `custom` template this is required.

postbuild
---------

Optional, a custom command to execute after build and before click build.

launch
------

Optional, a custom command to launch the app.

.. _clickable-json-dir:

dir
---

Optional, a custom build directory. Defaults to ``./build/``

kill
----

Optional, a custom process name to kill (useful for killing the running app,
then relaunching it). If left blank the process name will be assumed.

scripts
-------

Optional, an object detailing custom commands to run. For example:

.. code-block:: javascript

    {
        "test": "make test",
        "echo": "echo Hello World"
    }

.. _clickable-json-lxd:

lxd
---

Optional, whether or not to use a lxd container to build the app. Default is to use
docker to build the app. LXD is deprecated and its support will be removed
in a future version of clickable.

.. _clickable-json-default:

default
-------

Optional, a list of space separated sub-commands to run when no sub-commands are
specified. Defaults to ``clean build click-build install launch``.

dependencies
------------

Optional, a list of dependencies that will be installed in the build container.
These will be assumed to be `dependencie:arch` unless `specificDependencies`
is set to `true`.

.. _clickable-json-docker-image:

docker_image
------------

Optional, the name of a docker image to use. When building a custom docker image
it's recommended to use one of the Clickable images as a base. You can find them
on `Docker Hub <https://hub.docker.com/r/clickable/ubuntu-sdk/tags/>`__.

ignore
------

Optional, a list of files to ignore when building a `pure` template
Example:

.. code-block:: javascript

    "ignore": [
        ".clickable",
        ".git",
        ".gitignore",
        ".gitmodules"
    ]

.. _clickable-json-make-jobs:

make_jobs
---------

Optional, the number of jobs to use when running make, equivalent to make's `-j`
option. If left blank this defaults to the number of cpus your computer has.

.. _clickable-json-gopath:

gopath
------

Optional, the gopath on the host machine. If left blank, the ``GOPATH`` env var will be used.

.. _clickable-json-build-args:

build_args
----------

Optional, arguments to pass to qmake or cmake. Ex: ``CONFIG+=ubuntu``
