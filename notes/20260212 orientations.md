# Thursday, February 12, 2026

## make orientations

According to my work last week, I need to now generate a collection of orientations.

Always make sure the hardcoded directories, generated based on parameters passed to makeParticles.py, match what you're working on. This is on line 26, the data passed to particlePath.

Question, should this work on gas as well as stars? There appears to be work on stars files starting line 52, but no similar work on gas.

> python3 bin/sampleOrientations.py --num=11 --z=0 --galaxy=g15784

## examine orientations

It appears orientations were placed in /mnt/data0/pkrsnak/nihao2/

OK I don't know; some of these files I think are from what I ran before. I'm going to delete and try again (how could I avoid this in the future?)

Got rid of old files. Now have 11 total (which always includes the inc0 and az0 orientation)

## calcAxisRatios.py

First, correct hardcoded directories. Lines 50-51.

Image dimensions hardcoded, line 69. Correct this if necessary, but I will leave it as-is today.

This part of the code analyzes the way the orientation is presented in space, and how that affects its apparent 2D shape. A face-on galaxy will have an axis ratio near 1; because ba - that is, b vs. a in an ellipse (semi major and minor axis) will be closer to a circle. ba is smaller if the galaxy is more tilted compared to the pov of the viewer.

> python3 bin/calcAxisRatios.py --num=11 --z=0 --galaxy=g15784

OK very cool, I have 11 pictures, each organized by the axisratio, as denoted in the filename. The filename also preserves the inclination and azimuth of each view.