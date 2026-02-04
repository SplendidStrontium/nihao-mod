import numpy as np

# Load a numpy array
path = '/mnt/data0/pkrsnak/nihao2/Particles/noAgeSmooth/noSF/z0/g15784/'
stars = np.load(path + 'stars.npy')
gas = np.load(path + 'gas.npy')

# Check dimensions
print(f"Stars shape: {stars.shape}") # (247731, 10) = 247k particles, 10 properties each
print(f"Gas shape: {gas.shape}") # (19989, 7) = 20k particles, 7 properties each
# Preview first few rows
print(f"First 3 star particles:\n{stars[:3]}")
# Preview first particle
print(f"First star particle:\n{stars[0]}")
# Check specific columns
print(f"First 5 star masses (column 7): {stars[:5, 7]}")
# Check min/max values
print(f"Min star mass: {np.min(stars[:, 7])}")
print(f"Max star mass: {np.max(stars[:, 7])}")