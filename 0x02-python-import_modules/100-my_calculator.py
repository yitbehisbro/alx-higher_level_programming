#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    if len(sys.argv) == 4:
        for i in range(1, len(sys.argv)):
            if sys.argv[2] == "+":
                result = add(int(sys.argv[1]), int(sys.argv[3]))
            elif sys.argv[2] == "-":
                result = sub(int(sys.argv[1]), int(sys.argv[3]))
            elif sys.argv[2] == "*":
                result = mul(int(sys.argv[1]), int(sys.argv[3]))
            elif sys.argv[2] == "/":
                result = div(int(sys.argv[1]), int(sys.argv[3]))
            else:
                print(f"Unknown operator. Available operators: +, -, * and /")
                exit(1)
        print("{:d} {} {:d} = {:d}\
            ".format(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), result))
    else:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>", end="\n")
        exit(1)
