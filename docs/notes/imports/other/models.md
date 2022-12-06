# Models

By which I almost entirely mean 3D models.

## Python libs

I thought maybe `vedo` was the option here, but it seems to not do what I want.
In fact, no library seems to do what I want.

What I want is to simply ask if a point lay on the face of a plane. Given a
bounding box, I want to check all points inside that box and generate a list of
points with a given interpolation that intersect with the outer hull of an
object.

This seemed easy to me. It apparently isn't.

Which kind of baffles me because honestly what you're really doing is slicing
the model at the point with a knife and then asking "okay, where does the knife
meet this circle?" (Except we do it three bloody times, but it's not hard math
to jump from point to point instead and do it once.)

## Home Baked

I want a tool that can do one thing and do it well. Is that really too much to
ask for? Yeesh.

### Wavefront OBJ notes

Here: [link][loc-wavefront].

[loc-wavefront]: https://www.loc.gov/preservation/digital/formats/fdd/fdd000507.shtml