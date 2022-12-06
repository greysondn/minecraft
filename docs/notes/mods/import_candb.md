# Import Chisel and Bits

A command or tool to import images and/or models via chisel and bits.

Originally, this was going to be part of a commands mod, but the developer of
C&B pointed out that there was a command to do this, so...

## Process

We need two commands, mostly. The first clears out a space, without checking it;
the second writes to where we just cleared.

In Minecraft 1.16.5...

### Position Tuple

```
let `Position` be a tuple of three floats separated by spaces, signifying,
in order:
    - position west to   east, going  east as values increase
    - position down to     up, going    up as values increase
    - position north to south, going south as values increase
```

### Clear

```
/candb clear <start:Position> <end:Position>
```

### Fill

```
/candb fill <start:Position> <end:Position> <block> <state>
```

## Notes for Python

As this is going to be wrapped in python, let's go down the line, shall we.

### Image library

Easily PIL.

### 3d obj library

Harder. I'm thinking [vedo][vedo-homepage].

## Code Iteration Notes

What I want out of different versions and how it went.

### First version: Proof of concept

Can I take an image and import it, sloppily, into the game?

I just want to hardcode the starting coordinate and the image into a minecraft
function to call later on. Colors can be hardcoded, but I'll actually read the
image.

One bit at a time, etc.

### Later versions: ideas
* read minecraft texture colors to optimize bit selection.
  * variable res pack paths with fallback
  * do it in three dimensions
  * support for something like RGB Blocks
  * add a list of chiselable blocks and their texture paths
* batching is easier on the host and easier on the client.
  * Run length encoding?
    * One dimension
    * Two dimensions
    * Three dimensions
* clear *before* putting in blocks

[vedo-homepage]: https://vedo.embl.es/