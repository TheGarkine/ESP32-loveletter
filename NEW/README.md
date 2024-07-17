git clone https://github.com/espressif/esp-idf
cd esp-idf
git checkout v5.1.2
git submodule update --init --recursive
idf.py menuconfig

git clone --recurse-submodules https://github.com/lvgl/lv_port_esp32.git
cd lv_port_esp32