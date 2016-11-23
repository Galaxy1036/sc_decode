# sc_decode
An effort to reverse-engineer .sc sprite maps.

Usage: 

python sc_decode.py [-d] [-s] <filename>

-d: dumps the raw data (split in blocks) to a text file.

-s: dumps all the sprites mapped in <filename> to PNG files.

the output is saved in folders named <filename>_out

(structured data dump coming soon)

Input must be a file extracted with QuickBMS from the .sc files.

Known bugs:

* some red/blue sprite components (Canon) are pasted slightly misaligned
* some composite sprites (Barbarian's sword, Dark Prince's shield, Baby Dragon's tongue, etc) are pasted VERY misaligned


Want to help? Check our wiki!

[sc_decode wiki](https://github.com/umop-aplsdn/sc_decode/wiki)