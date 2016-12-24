#!/usr/bin/env python3
import math

numberOfBatteries = 2

power_now = 0
energy_now = 0
energy_full = 0
bat_status = "Full"

for i in range(numberOfBatteries):
    with open('/sys/class/power_supply/BAT{}/power_now'.format(i)) as f:
        power_now += int(f.read())
    with open('/sys/class/power_supply/BAT{}/energy_now'.format(i)) as f:
        energy_now += int(f.read())
    with open('/sys/class/power_supply/BAT{}/energy_full'.format(i)) as f:
        energy_full += int(f.read())
    with open('/sys/class/power_supply/BAT{}/status'.format(i)) as f:
        temp_status = f.read().strip()
    if temp_status != "Unknown":
        bat_status = temp_status

percentage_left = energy_now / energy_full * 100

if bat_status == "Discharging":
    time_left = energy_now / power_now
elif bat_status == "Charging":
    time_left = ( energy_full - energy_now ) / power_now

print("{:.0f}% ({:0>2d}:{:0>2d})".format(percentage_left, math.floor(time_left), math.floor((time_left % 1) * 60)))

if percentage_left < 10:
    exit(33)
