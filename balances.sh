#!/bin/sh
python3 bitfinBal.py &
python cbBal.py &
python payPalBal.py &
python lbtcBal.py
#python poloniexBal.py
