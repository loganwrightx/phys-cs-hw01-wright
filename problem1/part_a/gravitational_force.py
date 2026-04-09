import time
import numpy as np

def direct_nbody_force(pos: np.ndarray, mass: np.ndarray, G: float = 1.0) -> np.ndarray:
    # Naive solution O(N^2) double for-loop gravitational force calculation in 2D
    # pos: (N, 2)
    # mass: (N)
    # result: (N, 2)
    result = np.zeros((len(mass), 2), float)
    for idx1, (r1, m1) in enumerate(zip(pos, mass)):
        for idx2, (r2, m2) in enumerate(zip(pos, mass)):
            if idx1 == idx2:
                continue
            
            # Get vector components pointing from 1 to 2
            dx = r2[0] - r1[0]
            dy = r2[1] - r2[1]
            # For efficiency, compute r ^ 3/2 to normalize the dx and dy vector components later
            dr = (dx * dx + dy * dy) ** 1.5

            # Newton's inverse-square gravitational model
            result[idx1][0] += (G * m1 * m2 * dx) / dr
            result[idx1][1] += (G * m1 * m2 * dy) / dr

    return result
