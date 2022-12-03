# World

I wish the real world would just stop hassaling me.

## Votes

None?

## Data Sources

### Locations of major cities

https://simplemaps.com/data/world-cities

Requires attribution.

### Streets/POI/Etc

https://wiki.openstreetmap.org/wiki/Overpass_API

Lib for it at

https://pypi.org/project/overpass/

### Various things about the planet

https://neo.gsfc.nasa.gov/

Maps in equirectangular projection.

Requests attribution, although I believe it's public domain? Anyway, their
specific notice says:

> The images available in NEO are freely available for public use without
> further permission. Please use the credit statement attached to each dataset,
> or at the very least credit NASA Earth Observations as the source.

I'unno. Depends on how much I end up using, I guess? Well, either way they get
credit, it's just the difference between a few lines and an entire novel.

## Notes

### Elevation and dimension counters.

Here is how I see it:

Nobody "really" cares about the ocean, and I don't "really" care about any
location that my players aren't from or likely to actually reach.

Which means this is interesting enough already, I reckon.

Some quick data points follow about this nonsense, all in meters.

#### Atmospheric layers

Turns out to not matter, as the main layer humans live in covers all the way to
almost - but not quite - the peak of Mt. Everest.

#### Highest and Lowest Points

Worldwide highest point         -   8848  
Lowest known point in the ocean - -10929  
Difference between the two      -  19777

Lowest known point on land      -   -430

average global elevation        -   2440  
average ocean depth             -  -3682  
difference between the two      -   6122

#### Locations of Interest

Brazil      - ???                   - Rio de Janeiro    -      2  
Egypt       - ???                   - Giza              -     19  
England     - ???                   - London            -     11  
India       - ???                   - Agra              -    170  
Italy       - ???                   - Rome              -     21  
Jordan      - ???                   - Petra             -    810  
Mexico      - Yucatan               - Chichen Itza      -     39  
Norway      - ???                   - Oslo              -      1
Scotland    - South Lanarkshire     - Douglas           -    200  
USA         - AK                    - Anchorage         -     31  
USA         - AK                    - Nome              -      6  
USA         - CA                    - Redding           -    172  
USA         - DC                    - Washington        -    125  
USA         - MA                    - Boston            -     43  
USA         - NC                    - Camp Lejeune      -     10  
USA         - NV                    - Las Vegas         -    610  
USA         - NY                    - New York          -     10  
USA         - PA                    - Allentown         -    103  
USA         - WV                    - Philippi          -    397  
USA         - WV                    - Belington         -    519  
USA         - WV                    - Junior            -    532  

Notes:

* I've sloppily rounded here. Deal with it.

* Rio de Janeiro is a little weird in that it goes from the ocean to
  1020m high.

* The Iditarod Trail Sled Dog Race goes from Anchorage, Alaska to Nome,
  Alaska, hence their inclusion.

* Control takes place in New York. Nominally.

#### World Habitations
cities and whatnot

worlwide highest settlement -   5000  
highest large city          -   4150  
usa highest settlement      -   3224

worldwide average elevation -   840  
usa average elevation       -   740

### Flat Earth model of the globe

I reckon I can just put the thing on a square plane. Should be no problem to
flat earthers.

Their reference map appears to be an azimuthal equidistant
projection, but given the inherent distortion I might actually put the center
in America somewhere and then put antarctica around the edge no matter where it
should "actually" be. Then again, distortion isn't THAT bad as is, I just need
to rotate the map so America is upright before we all go insane trying to work
that one out.

### Rotsprite and models

I reckon if I can get models together, rotsprite can handle rotating them in
space if needbe, by doing it one layer at a time.

This algorithm is described by SonicRetro's Xenowhirl, here:
https://forums.sonicretro.org/index.php?threads/sprite-rotation-utility.8848/#post-159754

But, "just in case", here is a copy of that post.

> The algorithm is dead simple, so I'll just describe it and you can decide:
> First it scales the image to 8x size, using a "pixel guessing" algorithm to
> add detail. Then it scales the image to 1/8 size and also rotates it using
> standard aliased rotation and scaling. That's basically it. To get a big speed
> increase for a small penalty in quality, you could use 4x instead of 8x and
> skip some other optional steps I did, but I wanted high quality above all
> else.
> 
> Here's the more detailed version: First it scales the image to double size
> using something similar to Scale2x, but checking if pixels are more similar
> to each other instead of if they're equal, which makes the result less blocky
> and ultimately leads to smoother output. The important thing is that the
> scaling algorithm works by choosing a pixel instead of by blending pixels. It
> does that 3 times to achieve an 8x scale, determined empirically to be a good
> place to stop. Then (optional step) it tries to find the best rotation offsets
> by looping through a small grid of offsets between 0 and 7 pixels in x and y,
> and for each one looping through the 8x image at the rotation angle with step
> size 8 pixels, and adding the squared distance of the difference in color
> components between each point and its immediate (1 pixel) neighbors in the 8x
> image, which will be 0 except on the boundaries between 8x pixels. Then it
> simply performs standard nearest-neighbor scaling+rotation, starting at the
> offsets that gave minimal sum of squared differences, and using 1/8 scale to
> return the image to normal size while rotating it. Finally (optional step), it
> tries to fix any overlooked single-pixel details by checking for any pixels in
> the output image that have 3 or 4 identical neighbors equal to them and
> unequal to the color at the corresponding place in the source image, and
> replacing those pixels with the one from the source image.
> 
> You might say I'm cheating by not vectorizing the graphics into lines and
> curves and rotating those, but I say this method is an approximation of that
> and works better in practice. When the original image has little detail at the
> angle it's being sampled, aliased rotation makes too many arbitrary decisions,
> but the smoothing of a pixel-choosing enlargement algorithm is sufficient to
> resolve most of the ambiguity.

Yep.