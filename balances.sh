#!/bin/sh

watch -n 1 python3 bitfinBal.py &
watch -n 1 python cbBal.py &
watch -n 1 python payPalBal.py &
watch -n 1 python lbtcBal.py &
watch -n 1 python poloBal.py &

wait