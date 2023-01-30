# Rubber Ducky - Adafruit Neo Trinkey

Multiplayload [Rubber Ducky](https://shop.hak5.org/products/usb-rubber-ducky) with [Adafruit Neo Trinkey - SAMD21 USB Key with 4 NeoPixels](https://www.adafruit.com/product/4870)

## How it works

The script allows to have multiple payloads and select one of them to run. The LEDs show the selected payload, and with the touch pads you can select the desired payload (pad farthest from the reset button) and run it (pad closest from the reset button).

## Setup

1. Install Circuit Python in the board
2. Copy in `CIRCUITPY` device:
    - `./lib`
    - `./payloads`
    - `./code.py`
3. It's ready to run!

## Configure the payloads

The name of the payloads must be in the `payloads` folder and must end with the color pattern for the 4 LEDs:

```text
payload_<color patter>.txt
```

For example, this file name `payload_rrgg.txt` shold turn on the LEDs with the following color pattern: red, red, gree, gree.

The avalible colors are:

- r: red
- g: green
- b: blue
