#!/usr/bin/env python
import argparse
import math
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt

def restrictedFloat(num):
  try:
    num = float(num)
  except ValueError:
    raise argparse.ArgumentTypeError("Confidence interval {} not a floating-point literal".format(num))

  if num < 0.0 or num > 1.0:
    raise argparse.ArgumentTypeError("Confidence interval {} not in range [0.0, 1.0]".format(num))
  return num

parser = argparse.ArgumentParser()
parser.add_argument("mean", type = float, help = "sample mean")
parser.add_argument("deviation", type = float, help ="standard deviation")
parser.add_argument("n", type = int, help = "sample size")
parser.add_argument(
  "-i", "--interval",
  type = restrictedFloat,
  help = "Confidence interval in decimal form between 0.0 and 1.0",
  default = 0.95
)
args = parser.parse_args()
error = args.deviation/math.sqrt(args.n)
proportion = (1 - args.interval)/2

z_star = math.fabs(norm.ppf(proportion))

new_interval = z_star * error

print("{} \u00B1 {}".format(args.mean, new_interval))

mean = args.mean
standard_deviation = error
x = np.linspace(mean - 3 * standard_deviation,mean + 3 * standard_deviation, 10000)
nVals = [norm.pdf(i,mean,standard_deviation) for i in x]
line = plt.plot(x,nVals)
x1 = mean - new_interval
x2 = mean + new_interval
plt.fill_between(x,nVals,color = '#111111',where = (x > x1) & (x < x2))
plt.show()
