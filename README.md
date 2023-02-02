# RotationalText

This is my first repo that's entirely my idea, concept to implementation. I had something I wanted to do with a GUI that had text facing at least the top and bottom of the window simultaneously, and I couldn't find an existing way to do that within tkinter, so I came up with this.

Within Main, the drawString method takes the following arguments:
text: a string of text to draw. With the default simpleLetters, it does caps only, and numerals 0-9. Other characters will be replaced by an underscore.
target_window: an instance of a tkinter window
optional arguments:
position: a tuple with your intended x and y starting values in pixels from the upper left of the window
rotation: an int 0-7. 0 draws the text left to right, normal orientation. Each additional rotation sends it 45 degrees counter-clockwise. *Note: 90 degree intervals draw the instructions perfectly. Odd numbered intervals warp noticeably*
color: a string representing a color name in the palette tkinter uses. I know it takes black, blue, red, and cyan

Possible improvements:

Rotation method. The one I designed was for an imagined scenario where I needed to a single pixel width gap to continue to exist as it moved from horizontal to diagonal, and so treats distances as pixel counts instead of accounting for pythagorean theorem.

Fonts. I hand-created the instructions to create these letters, and they aren't particularly nice.

Scaling. With better drawing instructions and rotation methods, it should be possible to increase font size readily.
