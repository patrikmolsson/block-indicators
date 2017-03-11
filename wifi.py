#!/usr/bin/env python3

from subprocess import check_output

wifi = check_output(["iwgetid", "-r"]).decode('UTF-8').rstrip()

out = "<span font='FontAwesome'>\uf1eb {}</span>"

if ('comhem_6BC649' == wifi):
    print(out.format("\uf015"))
elif ('eduroam' == wifi):
    print(out.format("\uf19d"))
else:
    print(out.format(wifi))

