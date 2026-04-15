# Wednesday, April 15, 2026

## back to troubleshooting bestparams
Still using the same command, giving PTS error.

> python bin/bestParamsRT.py --ageSmooth=False --SF=False --tauClear=10 --numPhotons=1e7 --pixels=250 --dustFraction=0.3 --maxTemp=7e4 --SSP=Bpass_Chabrier --z=0 --galaxy=g15784

Says it's constructing a simulation from ski file sph.ski, then returns error that SpatialGridConvergenceProbe is not defined in the schema, then makes reference to the schemadef in SKIRT.

15/04/2026 09:51:08.187 * *** Error: Type 'SpatialGridConvergenceProbe' is not defined in the schema
15/04/2026 09:51:08.187 * *** Error: On line 870 in file /mnt/data0/jillian/SKIRT/git/SMILE/schema/SchemaDef.cpp

SpatialGridConvergenceProbe is a part of that sph.ski XML file; but when it tries to read it, SKIRT doesn't know what that means.

/mnt/data0/pkrsnak/nihao2/bestParamsRT/noAgeSmooth/noSF/noDust/numPhotons1e7/Bpass_Chabrier/z0/g15784

In the dir with sph.ski, ran:

> pts upgrade_ski .

## restart from step 2: sampleOrientations.py

> python bin/sampleOrientations.py --num=11 --z=0 --galaxy=g15784

## step 3: calcAxisRatios

> python bin/calcAxisRatios.py --num=11 --z=0 --galaxy=g15784

## step 4: selectOrientations

> python bin/selectOrientations.py --z=0 --galaxy=g15784

## step 5: bestParamsRT

> python bin/bestParamsRT.py --ageSmooth=False --SF=False --tauClear=10 --numPhotons=1e7 --pixels=250 --dustFraction=0.3 --maxTemp=7e4 --SSP=Bpass_Chabrier --z=0 --galaxy=g15784
