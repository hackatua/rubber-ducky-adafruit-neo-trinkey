import time
import os
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import adafruit_ducky
import touchio
import board
import neopixel

payloads_folder = 'payloads'
colors_mappings = {
    'r': 0xFF0000,
    'g': 0x00FF00,
    'b': 0x0000FF
}

touch1 = touchio.TouchIn(board.TOUCH1)
touch2 = touchio.TouchIn(board.TOUCH2)

pixels = neopixel.NeoPixel(board.NEOPIXEL, 4)

pixels.fill((0x000000))
pixels.brightness = 0.05

time.sleep(1)

keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

pixels.fill((0xFFFFFF))
time.sleep(0.1)
pixels.fill((0x000000))
time.sleep(0.1)
pixels.fill((0xFFFFFF))
time.sleep(0.1)
pixels.fill((0x000000))

def get_payload_color(payload_file_name):
    color_code = payload_file_name.split('_')[-1].split('.')[0]

    colors = []
    for key_color_code in color_code:
        colors.append(colors_mappings[key_color_code])

    return colors

def set_leds_colors():
    for led_index in range(4):
        led_color = payloads[selected_payload]['colors'][led_index]
        pixels[led_index] = led_color

payloads_file_names = os.listdir(payloads_folder)
payloads = []
for payload_file_name in payloads_file_names:
    payload = {
        'path': payloads_folder + '/' + payload_file_name,
        'colors': get_payload_color(payload_file_name)
    }
    payloads.append(payload)

selected_payload = 0
set_leds_colors()

touched = time.monotonic()
is_running = False
while True:
    if is_running:
        is_running = duck.loop()
        continue
    if time.monotonic() - touched < 0.25:
        continue
    if touch1.value:
        selected_payload = (selected_payload + 1) % len(payloads)
        set_leds_colors()
        touched = time.monotonic()
    if touch2.value:
        duck = adafruit_ducky.Ducky(
            payloads[selected_payload]['path'],
            keyboard,
            keyboard_layout
        )
        is_running = True
        touched = time.monotonic()

