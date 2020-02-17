#!/usr/bin/env python
import argparse
import math


parser = argparse.ArgumentParser()
parser.add_argument("mean", type=float, help = "sample mean")
parser.add_argument("deviation", type=float, help ="standard deviation")
parser.add_argument("n", type=int, help ="sample size")
parser.add_argument("-i", "--interval", type= int, help = "confidence interval ", choices=[80,90,95,99], default = 95)
args = parser.parse_args()
error= args.deviation/math.sqrt(args.n)

z_star={
80: 1.282,
90: 1.645,
95: 1.96,
99: 2.576
}

new_interval = z_star[args.interval]*error

print("{} \u00B1 {}".format(args.mean, new_interval))
