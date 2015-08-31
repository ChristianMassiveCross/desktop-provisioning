#! /usr/bin/env sh
PAGE=$(wget -q "http://www.oracle.com/technetwork/java/javase/downloads/index.html" -O - | tr " " "\n" | grep "/technetwork/java/javase/downloads/jdk8" | head -n 1 | cut -d\" -f 2 | sed -e 's/^/http:\/\/www.oracle.com/')
wget -q "$PAGE" -O - | grep "Linux x64" | grep ".rpm" | cut -d\" -f 12 | grep -v demos | head -n 1 | awk -F "/" '{print $NF}' | cut -d "-" -f 2 | cut -c 3-
