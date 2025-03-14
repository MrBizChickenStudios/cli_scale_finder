# Musical Scale Generator
This script generates a musical scale based on a specified root note and mode. It uses the argparse module to accept command-line arguments for the root note and musical mode. It then calculates and prints the corresponding scale for the given root and mode.

## Features
Accepts two arguments: root note and mode.
Supports a variety of root notes and musical modes.
Prints the generated scale for the given root note and mode.
## Supported Root Notes
The root notes you can use are:

c, c#, d, d#, e, f, f#, g, g#, a, a#, b
## Supported Modes
The modes you can use are:

ionian (major)
dorian
phrygian
lydian
mixolydian
aeolian (minor)
locrian
## How to Use
### Command-Line Arguments
-r or --root: Specify the root note (e.g., "c", "d#", "f").
-m or --mode: Specify the mode (e.g., "ionian", "dorian").
Example Usage
## To generate a C major scale (Ionian mode):


        python script.py -r c -m ionian
Output:

Scale for c ionian: ['c', 'd', 'e', 'f', 'g', 'a', 'b', 'c']
## To generate a Dorian scale starting at D:


        python script.py -r d -m dorian
Output:


Scale for d dorian: ['d', 'e', 'f', 'g', 'a', 'b', 'c', 'd']
Requirements
Python 3.x
How It Works
The script calculates the scale based on the starting root note and mode. It uses predefined patterns of intervals (whole steps and half steps) to construct the scale.

Scale Construction
The pattern of intervals for the modes is:

Ionian (Major): 2, 2, 1, 2, 2, 2, 1
Dorian: 2, 1, 2, 2, 2, 1, 2
Phrygian: 1, 2, 2, 2, 1, 2, 2
Lydian: 2, 2, 2, 1, 2, 2, 1
Mixolydian: 2, 2, 1, 2, 2, 1, 2
Aeolian (Minor): 2, 1, 2, 2, 1, 2, 2
Locrian: 1, 2, 2, 1, 2, 2, 2
The root note and mode are used to determine the starting point in the list of root notes, and the scale is constructed by applying the interval pattern.

License
This script is licensed under the MIT License.
