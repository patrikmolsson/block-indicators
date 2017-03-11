#!/usr/bin/env python3

import psutil

bluetooth_active = False

for p in psutil.process_iter():
    if p.name() == 'bluetoothd':
        print ('')
        break
