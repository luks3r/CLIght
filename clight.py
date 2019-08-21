#!/usr/bin/env python3

import pifx
from time import sleep
import os
import click

VERSION = "0.2"
p = pifx.PIFX(api_key=os.getenv("LIFX_API"))

@click.group()
@click.version_option(version=VERSION, message="%(prog)s %(version)s")
def clight():
  """A CLI wrapper"""


@click.option("-s", "--selector", help="The selector to limit which lights are controlled..", default="all")
@clight.command()
def toggle(selector: str):
  p.toggle_power(selector=selector)

@click.option("-s", "--selector", help="The selector to limit which lights are controlled.", default="all")
@clight.command()
def on(selector: str):
  p.set_state(selector=selector, power="on")

@click.option("-s", "--selector", help="The selector to limit which lights are controlled.", default="all")
@clight.command()
def off(selector: str):
  p.set_state(selector=selector, power="off")

@clight.group()
def set():
  """Sets 'state'"""

@click.option("-s", "--selector", help="The selector to limit which lights are controlled.", default="all")
@click.option("-p", "--power", help="The power state you want to set on the selector. on or off")
@click.option("-c", "--color", help="The color to set the light to.")
@click.option("-b", "--brightness", help="The brightness level from 0.0 to 1.0. Overrides any brightness set in color (if any).")
@click.option("-d", "--duration", help="How long in seconds you want the power action to take. Range: 0.0 – 3155760000.0 (100 years)")
#@click.option("-i", "--infrared", help="The maximum brightness of the infrared channel from 0.0 to 1.0.")
#@click.option("-f", "--fast", is_flag=True, help="Execute the query fast, without initial state checks and wait for no results.")
@set.command()
def state(selector: str, power: str, color: str, brightness: float, duration: float):
  p.set_state(selector=selector, power=power, color=color, brightness=brightness, duration=duration)

if __name__ == "__main__":
  clight(prog_name="clight")