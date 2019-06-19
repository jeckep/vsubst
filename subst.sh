#!/usr/bin/env bash

rm -rf ./dist
# used for directory
python subst.py --fname ./example/secure.properties --src_path ./templates --dst_path ./dist

# can be used for one file
#python subst.py --fname ./secure.properties --src_path ./templates/test.txt --dst_path ./dist/test.txt