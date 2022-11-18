#!/bin/sh

LD_PRELOAD=./libc.so.6 stdbuf -i0 -o0 -e0 ./shiny_bot
