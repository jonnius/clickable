.. _changelog:

Changelog
=========

Changes in v5.1.0
-----------------

- Added app template for QML/C++ with a main.cpp

Changes in v5.0.2
-----------------

- Fixed publish command not exiting with an error code when there is an error

Changes in v5.0.1
-----------------

- Fixed typo in cache path
- Improved Cordova support

Changes in v5.0.0
-----------------

- New features
    - Xenial by default (use ``--vivid`` to compile for 15.04)
    - Major code refactor
    - More environment variables
        - ``CLICKABLE_ARCH`` - Overrides the clickable.json's ``arch``
        - ``CLICKABLE_TEMPLATE`` - Overrides the clickable.json's ``template``
        - ``CLICKABLE_DIR`` - Overrides the clickable.json's ``dir``
        - ``CLICKABLE_LXD`` - Overrides the clickable.json's ``lxd``
        - ``CLICKABLE_DEFAULT`` - Overrides the clickable.json's ``default``
        - ``CLICKABLE_MAKE_JOBS`` - Overrides the clickable.json's ``make_jobs``
        - ``GOPATH`` - Overrides the clickable.json's ``gopath``
        - ``CLICKABLE_DOCKER_IMAGE`` - Overrides the clickable.json's ``docker_image``
        - ``CLICKABLE_BUILD_ARGS`` - Overrides the clickable.json's ``build_args``
        - ``OPENSTORE_API_KEY`` - Your api key for publishing to the OpenStore
        - ``CLICKABLE_CONTAINER_MODE`` - Same as ``--container-mode``
        - ``CLICKABLE_SERIAL_NUMBER`` - Same as ``--serial-number``
        - ``CLICKABLE_SSH`` - Same as ``--ssh``
        - ``CLICKABLE_OUTPUT`` - Override the output directory for the resulting click file
        - ``CLICKABLE_NVIDIA`` - Same as ``--nvidia``
        - ``CLICKABLE_VIVID`` - Same as ``--vivid``
- Removed
    - Chroot support has been removed, docker containers are recommended going forward
- clickable.json
    - Removed
        - ``package`` - automatically grabbed from the manifest.json
        - ``app`` - automatically grabbed from the manifest.json
        - ``sdk`` - Replaced by docker_image and the ``--vivid`` argument
        - ``premake`` - Use ``prebuild``
        - ``ssh`` - Use the ``--ssh`` argument
- Commands
    - New
        - ``log`` - Dumps the full log file from the app
        - ``desktop`` - Replaces ``--desktop`` to run the app in desktop mode
    - Changed
        - ``init`` - Changed to ``create`` (``init`` will still work)
        - ``update-docker`` - Changed to ``update``
    - Removed
        - ``kill`` - Changed to be part of the ``launch`` command
        - ``setup-docker`` - Automatically detected and run when using docker
        - ``display-on`` - Not very useful
- Command line arguments
    - New
        - ``--vivid`` - Compile the app for 15.04
        - ``--docker-image`` - Compile the app using a specific docker image
    - Changed
        - ``--serial-number`` - Replaces ``--device-serial-number``
        - ``--ssh`` - Replaces ``--ip``
    - Removed
        - ``--desktop`` - Use the new ``desktop`` command
        - ``--xenial`` - Xenial is now the default
        - ``--sdk`` - Use ``--vivid`` or ``--docker-image``
        - ``--device`` - Use ``shell``
        - ``--template`` - Use the ``CLICKABLE_TEMPLATE`` env var
        - ``--click`` - Specify the path to the click after the ``install`` command: ``clickable install /path/to/click``
        - ``--app`` - Specify the app name after the ``launch`` command: ``clickable launch app.name``
        - ``--name`` - Specify the app template after the ``create`` command: ``clickable create pure-qml-cmake``
