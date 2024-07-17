
https://docs.micropython.org/en/latest/esp32/tutorial/intro.html

https://www.amazon.de/dp/B0CSYPG716?psc=1&ref=ppx_yo2ov_dt_b_product_details


git submodule update --init --recursive
cd esp-idf
./install.sh
source export.sh

cd lv_micropython
git submodule update --init --recursive
make -C mpy-cross
make -C ports/esp32 LV_CFLAGS="-DLV_COLOR_DEPTH=16" BOARD=GENERIC_SPIRAM deploy




https://github.com/adafruit/micropython-adafruit-rgb-display/releases

ampy -p /dev/cu.usbserial-2110 put mpy-img-decoder/JPEGdecoder.py
#display stufff
# TODO mpycross
ampy -p /dev/cu.usbserial-2110 put micropython-ili9341/ili934xnew.mpy
ampy -p /dev/cu.usbserial-2110 put micropython-ili9341/glcdfont.mpy

ampy -p /dev/cu.usbserial-2110 put boot.py


idf v5.1.2
# build micropython with ujpeg

git submodule update --init --recurisve
cd esp-idf
./install.sh
. ./export.sh
cd ..

cd micropython/ports/esp32
make USER_C_MODULES=../../../ujpeg
