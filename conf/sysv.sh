#! /bin/sh
### BEGIN INIT INFO
# Provides:          CONTAINERNAME
# Required-Start:    $remote_fs $docker
# Required-Stop:     $remote_fs $docker
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: CONTAINERNAME initscript
# Description:       This file should be used to construct scripts to be
#                    placed in /etc/init.d.
### END INIT INFO

# Author: tuxalex <tuxy@tuxcloud.fr>
#
# Please remove the "Author" lines above and replace them
# with your own name if you copy and modify this script.

# Do NOT "set -e"

# PATH should only include /usr/* if it runs after the mountnfs.sh script
PATH=/sbin:/usr/sbin:/bin:/usr/bin
DESC="CONTAINERNAME app in docker container"
NAME=CONTAINERNAME
SCRIPTNAME=/etc/init.d/$NAME

case "$1" in
  start)
	python -c "from docker import Client; cli = Client(base_url='unix://docker.sock'); cli.start(container='$NAME')"
	;;
  stop)
	python -c "from docker import Client; cli = Client(base_url='unix://docker.sock'); cli.stop(container='$NAME')"
	;;
  restart|force-reload)
	python -c "from docker import Client; cli = Client(base_url='unix://docker.sock'); cli.restart(container='$NAME')"
	;;
  *)
	#echo "Usage: $SCRIPTNAME {start|stop|restart|reload|force-reload}" >&2
	echo "Usage: $SCRIPTNAME {start|stop|restart|force-reload}" >&2
	exit 3
	;;
esac

:


