import pynbody
data = pynbody.load('/mnt/data0/pkrsnak/testdata/g15784.lr.01024')
tform = data.star['tform'].in_units('yr')
print(f"Min tform: {tform.min():.2e} yr")
print(f"Max tform: {tform.max():.2e} yr")
print(f"Mean tform: {tform.mean():.2e} yr")

age = data.star['age'].in_units('yr')
print(f"Min age: {age.min():.2e} yr")
print(f"Max age: {age.max():.2e} yr")
print(f"Mean age: {age.mean():.2e} yr")