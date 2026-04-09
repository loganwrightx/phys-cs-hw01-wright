import time
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

from gravitational_force import direct_nbody_force

# Initialize arrays
N = np.array([100, 200, 400, 800, 1200])
time_complexities = np.zeros(5)

# Iterate over n's
for idx, n in enumerate(N):
    # Create demo particles before timing the function
    positions = np.random.rand(n, 2)
    masses = np.random.rand(n)
    # Start timer
    start_time = time.perf_counter()
    # Compute forces
    _ = direct_nbody_force(positions, masses)
    # Compute time complexity for given n
    time_complexities[idx] = time.perf_counter() - start_time

linear_model = lambda x, m, b: m * x + b

# Get curve fit parameters
params, param_covariance = curve_fit(linear_model, np.log2(N), np.log2(time_complexities))

# Make log-log plot of the ratio
plt.xlabel("Log(N)")
plt.ylabel("Log(t)")
plt.title(f"Log-log plot of time complexity of grav. model")
plt.plot(np.log2(N), np.log2(time_complexities))
plt.savefig("problem1.png")

print("Curve fit results:")
print(f"\ty = {params[0]:.3f} x + {params[1]}")
print(f"\tt ~= N ^ ({params[0]:.3f} + {params[1]:.3f} * log_N (2))")
