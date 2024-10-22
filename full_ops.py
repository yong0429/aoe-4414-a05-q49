# full_ops.py
#
# Usage: python3 full_ops.py c_in n_wv
#  Fully Ops.
# Parameters:
#  c_in: input channel count
#  n_wv: number of weight vectors

# Output:
#  c_out: output channel count
#  h_out: output height count
#  w_out: output width count
#  adds: number of additions performed
#  muls: number of multiplications performed
#  divs: number of divisions performed

# Written by Yonghwa Kim
# Other contributors: None

# import Python modules
import math # math module
import sys  # argv

# initialize script arguments
c_in = float('nan')
h_wv = float('nan')

# parse script arguments
if len(sys.argv)==3:
  c_in = float(sys.argv[1])
  h_in = float(sys.argv[2])
else:
  print(\
   'Usage: '\
   'python3 full_ops.py c_in n_wv'\
  )
  exit()

# Calculations
c_out = n_wv
h_out = 1
w_out = 1
adds = n_wv*c_in
muls = n_wv*c_in
divs = 0

print(int(c_out))
print(int(h_out))
print(int(w_out))
print(int(adds))
print(int(muls))
print(int(divs))