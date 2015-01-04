#!/bin/sh
cd /usr/local/by
while true; do
  echo "(Re)Launching by-ypperst"
  python main.py > /dev/null
  sleep 10
done

