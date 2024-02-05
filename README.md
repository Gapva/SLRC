![sfvcWide](https://github.com/Gapva/SLRC/assets/90116898/b47cc84a-b7b2-4ac5-af00-f06573f553d4)

# what is it?

SLRC (`.slrc`) stands for *Simplified Lane-based Rhythm Game Chart*

it is a file format with a simple goal of allowing easy parsing for lane-based rhythm game charts, and it is intended to be both readable and editable by humans

# docs

below, an example `.slrc` file is shown, along with helpful annotations that describe each portion of the file in its entirety

![image](https://github.com/Gapva/SLRC/assets/90116898/e2797768-9724-4315-9593-3c9650849820)
![image](https://github.com/Gapva/SLRC/assets/90116898/694a23b6-fc5e-482b-8551-764b54e639b1)
![image](https://github.com/Gapva/SLRC/assets/90116898/8658f65b-2510-4183-9637-ba9024af0053)

additional notes and tips
- obviously, this is not limited to just four columns
- in the second image, a Double Note is defined, but it is not limited to just doubles
- - you may place up to four notes of any kind in their respective columns
- when parsing, you should always case-convert the entire file to lowercase
- it's worth noting that the tempo parameter should have no influence on the map, and it is only a statistic
- - it's part of the format because it's important information
- when parsing, you should rid any duplicate notes
- - this only includes notes that start at the same exact time and lie in the exact same column
  - if there is a noodle strand, the end-time should not be checked because only the spawn time matters

# libraries

at the moment, there are no libraries for parsing `.slrc` files; however, there is a Python library planned as well as a Godot add-on

for now, you can refer to the [example parser](/example/example.py) (only 24 lines!) as a rough outline of how parsing should work
