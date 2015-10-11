Ajenti for yunohost
======

[![Crowdin](https://crowdin.net/badges/ajenti/localized.png)](https://crowdin.net/project/ajenti)

http://ajenti.org/

Ajenti is a Linux & BSD web admin panel.

![](http://ajenti.org/static/home/img/screens/ajenti/1.png)

![](http://ajenti.org/static/home/img/screens/ajenti/2.png)

![](http://ajenti.org/static/home/img/screens/ajenti/3.png)

Feature highlights
==================

Installation information
------------------------

This package installs ajenti in container with docker and use redirection in nginx to add the app in yunohost SSO.
The install script install docker if yunohost have installed on the host.
Docker-py has been used as a docker client to interact with docker thus this package can be used on a host with yunohost installed (not tested yet) or on a yunohost docker container.
The first installation can take time, because docker download the base image and construct the ajenti image, so be patient.
In yunohost this app is install with the name "ajenti_docker"

Existing configuration
----------------------

Picks up your current configuration and works on your existing system as-is, without any preparation.

Caring
------

Does not overwrite your config files, options and comments. All changes are non-destructive.

Batteries included
------------------

Includes lots of plugins for system and software configuration, monitoring and management.

Extensible
----------

Ajenti is easily extensible using Python. Plugin development is a quick and pleasant with Ajenti APIs.

Modern
------

Pleasant to look at, satisfying to click and accessible anywhere from tablets and mobile.

Lightweight
-----------

Small memory footprint and CPU usage. Runs on low-end machines, wall plugs, routers and so on.

See http://ajenti.org for more information

Credit
------

This work is based on Scith work : https://github.com/scith/redirect_ynh
