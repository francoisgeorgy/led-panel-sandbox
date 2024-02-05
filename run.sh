#!/bin/bash

usage() {
    echo "Usage: $0 path_to_script [brightness]"
    echo "  path_to_script: Mandatory. The path to the script to run."
    echo "  brightness: Optional. An integer value between 0 and 100. Default is 66."
    exit 1
}

if [ $# -lt 1 ]; then
    echo "Error: Missing script path."
    usage
fi

script="$1"
brightness=66

if [ $# -gt 1 ]; then
    if ! [[ $2 =~ ^[0-9]+$ ]] || [ $2 -lt 0 ] || [ $2 -gt 100 ]; then
        echo "Error: The brightness must be an integer between 0 and 100."
        usage
    else
        brightness=$2
    fi
fi

export EGL_PLATFORM=surfaceless
export MESA_GL_VERSION_OVERRIDE=3.3

shady -ofmt rgb24 -g 128x64 -f 20 -i "$script" -w \
    | sudo /home/sandbox/rpi-rgb-led-matrix/examples-api-use/ledcat \
        --led-rows=64 --led-cols=128 --led-slowdown-gpio=5 \
        --led-brightness=$brightness --led-rgb-sequence=bgr
