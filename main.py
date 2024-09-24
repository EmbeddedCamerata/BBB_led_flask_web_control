#!/usr/bin/env python
# From: https://towardsdatascience.com/python-webserver-with-flask-and-raspberry-pi-398423cc6f5d
from flask import Flask, render_template
import gpiod
import time

app = Flask(__name__)

LED_CHIP = "gpiochip1"
LED_LINE_OFFSET = [24]  # USR0 run: gpioinfo | grep -i -e chip -e usr

chip = gpiod.Chip(LED_CHIP)
lines = chip.get_lines(LED_LINE_OFFSET)
lines.request(consumer="main.py", type=gpiod.LINE_REQ_DIR_OUT)

state = 0  # Start with LED off
lines.set_values([0])


def blink_led():
    i = 5
    while i:
        state = lines.get_values()[0]
        lines.set_values([1 - state])
        time.sleep(0.5)
        i -= 1


@app.route("/")
def index():
    # Read Sensors Status
    state = lines.get_values()[0]
    templateData = {
        "title": "LED Status",
        "led": state,
    }
    return render_template("index.html", **templateData)


@app.route("/<action>")
def action(action):
    if action == "on":
        lines.set_values([1])
    if action == "off":
        lines.set_values([0])
    if action == "blink":
        blink_led()

    state = lines.get_values()[0]
    templateData = {
        "led": state,
    }
    return render_template("index.html", **templateData)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
