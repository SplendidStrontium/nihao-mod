import pynbody
data = pynbody.load('/mnt/data0/pkrsnak/testdata/g15784.lr.01024')

# Check what particle types are available
# print('Available families:', data.families())

# if hasattr(data, 'gas'):
#    print('Gas particles:', len(data.gas))
# if hasattr(data, 'star'):
#    print('Star particles:', len(data.star))

# See what data fields are available for stars
print('Loadable keys:', data.star.loadable_keys())
# testdata first returned ['tform', 'pos', 'phi', 'mass', 'vel', 'metals', 'eps']
# with iord added, it returns ['eps', 'OxMassFrac', 'iord', 'vel', 'HeII', 'igasorder', 'mass', 'pos', 'tform', 'FeMassFrac', 'phi', 'coolontime', 'HI', 'metals']

# Try accessing fields one at a time with error handling
# try:
#     print("Trying to get star positions...")
#     pos = data.star['pos']
#     print("✓ Position data available")
#     print(f" Shape: {pos.shape}")
# except Exception as e:
#     print(f"✗ Position error: {e}")

# try:
#     print("\nTrying to get star mass...")
#     mass = data.star['mass']
#     print("✓ Mass data available")
#     print(f" Shape: {mass.shape}")
# except Exception as e:
#     print(f"✗ Mass error: {e}")