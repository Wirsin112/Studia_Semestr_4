import sys
if len(sys.argv) != 2 or not sys.argv[1].isdecimal():
    if int(int(sys.argv[1]))%2 == 0:
        print("Parzysta")
    else:
        print("Nie parzysta")