#!/usr/bin/env bash

rm -rf ./dist
python subst.py --fname ./secure.properties --src_path ./templates --dst_path ./dist