# Wednesday, February 4, 2026

## start with makeparticles.py

I ran makeparticles the last time I was working on this. It made a directory in:
> /mnt/data0/pkrsnak/nihao2/Particles/

which made a directory structure into which can be found the numpy data structures. (directory set on line 319 of makeparticles.py) the source from which the testdata is loaded appears to be set on line 16.

I had encountered issues where the fields expected by the script were not what the testdata actually contained. This is why some lines (around 24-37) are commented out.

I am making inspect_testdata.py to try to figure out which fields are contained in the testdata.

FYI use:
> python3

b/c regular old python not aliased to python3

## what I did before

It looks like, based on supernote note, I generated the numpy array with the following cmd
> python bin/makeParticles.py --ageSmooth=False --SF=False --tauClear=10 --z=0 --galaxy=g15784

## tform vs. age

OK weirdness here; tform suggests the time the star formed, while age would be the age of the star.

TODO: Verify tform interpretation with real data. Test data shows tform max ~1.67 Myr which seems too young. May need age = t_current - tform conversion, or param file for correct unit conversion.

## inspecting the output npy arrays

> ls -lh /mnt/data0/pkrsnak/nihao2/Particles/noAgeSmooth/noSF/z0/g15784/stars.npy
makes sure that the file is not empty or overly large

I created and ran inspect_numpy_array.py, It spits out data it is looking at in the array. What each field is is determined by the creation of the datafile by makeParticles.py, around line 341, 342

numpy arrays do NOT have units in them; they only have raw numbers. units have to be inferred by the makeParticles.py script; here in lines 24-36. Simulation data has its own relative units -- when you set the .inunits() part, you tell it what units you want to use.

usually this is found in a param file, but this testdata does not have a param file. that's why i keep getting an error each time I call it, and we're just guessing what the units are

## next, use sampleOrientations.py to generate viewing angles

Updating paths here from the original NIHAO project. Directory structure is hardcoded (line 26-27); pay attention to whether this is appropriate with real data. make sure any call to 'python' is replaced with 'python3'. additionally script only seems to work on stars, but does nothing with gas particles?

before we run the next step, let's make sure the files we need actually exist
> ls /mnt/data0/pkrsnak/nihao2/Particles/noAgeSmooth/noSF/z0/g15784/

SKIRT can take a while to run, so let's do some tests before we proceed into the heart of it. just doing five orientations.
> python3 bin/sampleOrientations.py --num=5 --z=0 --galaxy=g15784

Ran it. Went alright. check the output with the following
> ls /mnt/data0/pkrsnak/nihao2/sampleOrientations_SKIRT/z0/g15784/

## third step is calcAxisRatios.py

updating paths like I did in step two

## OK let's go back

so we solved the mystery of age and tform. I was missing some input files, so I have those now and I was able to get different output from makeParticles.py and correct the discrepancy between tform and age and all that.

also, good to know
> gunzip *.gz

## commenting hack

in VSCode, highlight sections of code and press:

CTRL + /

to comment or un-comment entire sections.

## ending

I have reverted the pieces of makeParticles.py that did not work, now that I have the iord file, into the original formulation. It now matches the original NIHAO project with the pieces of the testdata that it expects to find. next I will move on to sampleOrientations.py and find out whether that will work correctly going forward. As a note, I need to make at least ten orientations, or the latter parts of the code are not expected to function correctly.