import pynbody
data = pynbody.load('/mnt/data0/pkrsnak/testdata/g15784.lr.01024')

tform = data.star['tform']

# Check raw values and what pynbody thinks the units are
print(f"Raw min tform: {tform.min()}")
print(f"Raw max tform: {tform.max()}")
print(f"Units pynbody assigned: {tform.units}")

# Also check what the simulation time properties are
print(f"\nSimulation properties:")
print(f"  properties: {data.properties}")