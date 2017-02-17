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
    if temp_status != "Unknown" and bat_status != "Discharging" and bat_status != "Charging":
        bat_status = temp_status

percentage_left = energy_now / energy_full * 100

icon = ""

time_left = 0
if bat_status == "Discharging":
    time_left = energy_now / power_now
    if percentage_left > 87.5:
        icon = ""
    elif percentage_left > 62.5:
        icon = ""
    elif percentage_left > 37.5:
        icon = ""
    elif percentage_left > 10:
        icon = ""
    else:
        icon = ""
elif bat_status == "Charging":
    time_left = ( energy_full - energy_now ) / power_now
    icon += " "

icon_text = "<span font='FontAwesome'>{}</span>".format(icon)

percentage_left_text = ""
if (percentage_left < 100):
    percentage_left_text = " {:.0f}%".format(percentage_left)

time_left_text = " "

if (time_left > 0):
    time_left_text = " ({:0>2d}:{:0>2d})".format(math.floor(time_left), math.floor((time_left % 1) * 60))

print("{}{}{}".format(icon_text, percentage_left_text, time_left_text))

if percentage_left < 10 and bat_status == "Discharging":
    exit(33)
