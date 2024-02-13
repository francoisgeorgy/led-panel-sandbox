LED Panel sandbox
=================

Various experiments with LED Panels.

Raspberry Pi 4B setup : 
-----------------------

The code in this repo has been tested with **Raspberry Pi OS Lite (32-bit)**. I have not tested with another distribution.

### Prepare the OS :

First, make sure the OS is up-to-date : 

    sudo apt update && sudo apt upgrade -y
 
Some changes are necessary to use the `rpi-rgb-led-matrix` library :

    sudo sed -i 's/audio=on/audio=off/' /boot/config.txt
    echo " isolcpus=3" | sudo tee -a /boot/firmware/cmdline.txt

`audio=off` is not sufficient, we need to blacklist the bmc2835 module  :
   
do : 

    cat <<EOF | sudo tee /etc/modprobe.d/blacklist-rgb-matrix.conf

enter : 

    blacklist snd_bcm2835
    EOF
   
source : https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/README.md#bad-interaction-with-sound

setup for i2c :

    sudo raspi-config nonint do_i2c 0

install packages we will need later on :

    sudo apt install \
         git build-essential cmake \
         python3-dev python3-pillow \
         python3 python3-pip \
         libxcursor-dev libxinerama-dev libxi-dev libx11-dev \
         libglu1-mesa-dev libxrandr-dev libxxf86vm-dev \
         i2c-tools -y

reboot to activate all the changes :

    sudo reboot

### Install the library to drive the LED panel : 

Create a home dir for the code :

    sudo mkdir /home/sandbox
    sudo chown $USER:$USER /home/sandbox
    cd /home/sandbox
   
Install the RGB lib : 

    cd /home/sandbox
    git clone https://github.com/hzeller/rpi-rgb-led-matrix.git
    cd rpi-rgb-led-matrix/
    make
    make build-python PYTHON=$(command -v python3)
    sudo make install-python PYTHON=$(command -v python3)

Connect your panel and try a demo : 

    cd examples-api-use/
    sudo ./demo --led-rows=64 --led-cols=64 --led-slowdown-gpio=5 -D 0

If you have the adafruit hat : 

    sudo ./demo --led-rows=64 --led-cols=64 --led-gpio-mapping=adafruit-hat --led-slowdown-gpio=5 -D 0

### Install `go` : 

First, copy `tools/install-go.sh` to the RPi. 

Then. do : 

    mkdir -p ~/.local/share
    chmod +x install-go.sh
    ./install-go.sh

Logout/login again to force the reload of .profile (you can also do `source .profile`) and test that go is installed : 

    $ go version
    go version go1.21.5 linux/arm

### Test `ledcat` : 

    cat /dev/random | sudo /home/sandbox/rpi-rgb-led-matrix/examples-api-use/ledcat \
        --led-rows=64 --led-cols=64 --led-slowdown-gpio=5


### Install `shady` :

The following package must be installed prior to shady : 

    sudo apt install libegl-dev -y 

Install shady : 

    go install github.com/polyfloyd/shady/cmd/shady@latest

Clone this repository : 

    cd /home/sandbox
    git clone https://github.com/francoisgeorgy/led-panel-sandbox.git

Test `shady` : 

    cd /home/sandbox/led-panel-sandbox

    export EGL_PLATFORM=surfaceless
    export MESA_GL_VERSION_OVERRIDE=3.3
 
    shady -ofmt rgb24 -g 128x64 -f 20 -i src/shaders/example.frag -w \
        | sudo /home/sandbox/rpi-rgb-led-matrix/examples-api-use/ledcat \
            --led-rows=64 --led-cols=64 --led-slowdown-gpio=5 \
            --led-brightness=66

## Learning shaders

- [An introduction to Shader Art Coding](https://www.youtube.com/watch?v=f4s1h2YETNY)
- [The Book of Shaders](https://thebookofshaders.com/02/)
- http://editor.thebookofshaders.com/

Tools : 

- http://editor.thebookofshaders.com/
- https://shaderboy.net/
- [Simple WebGL Fragment Shader Editor](https://github.com/patriciogonzalezvivo/glslEditor)
- https://iquilezles.org/articles/distfunctions2d/
- https://graphtoy.com/
 
## Python

    cd /home/sandbox
    python3 -m venv --system-site-packages .venv
    source .venv/bin/activate

On your dev machine (your PC or your Mac) you can install the simulator with : 

    pip install RGBMatrixEmulator


----

## Notes : 

### Using "sudo" in a Python venv : 

We need to have root privileges to get good performances, so we need to use sudo.

Here is how to use a python venv with sudo  :

    sudo -E env PATH=$PATH ...

example : 

    (.venv) $ sudo -E env PATH=$PATH python -c 'import sys; print(sys.path)'
    (.venv) $ sudo -E env PATH=$PATH pip -VV

Note: sudo is only needed when running a python script which uses the rip-rgb lib. It is not needed otherwise.

