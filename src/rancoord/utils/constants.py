# WGS 84 (World Geodetic System)

a = 6378.137  # length of semi-major axis of the ellipsoid (radius at equator) - kilometers (km)
f = 1 / 298.257223563 # flatenning factor of the ellipsoid (Earth)
b = (1 - f) * a  # length of semi-minor axis of the ellipsoid (radius at the poles) - kilometers (km)

MILES_PER_KILOMETER = 0.621371
KILOMETERS_PER_METER = 0.001

MAX_ITERATIONS = 200
CONVERGENCE_THRESHOLD = 1e-12  # .000,000,000,001

