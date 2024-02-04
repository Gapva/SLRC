![sfvcWide](https://github.com/Gapva/SFVC/assets/90116898/7b552e79-f213-471a-ac18-ba435e7784b2)

# what is it?

SFVC (`.sfvc`) stands for *Simplified Four-Lane (4K) Vertically-Scrolling-Rhythm-Game (VSRG) Chart*

it is a file format with a simple goal of allowing easy parsing for 4K VSRG charts, and it is intended to be both readable and editable by humans

# docs

below, an example `.sfvc` file is shown, along with helpful annotations that describe each portion of the file in its entirety

![image](https://github.com/Gapva/SFVC/assets/90116898/fffb12e8-799b-4bf0-a867-262e301cb186)
![image](https://github.com/Gapva/SFVC/assets/90116898/a272c7aa-3a77-4102-b47e-a5d19f926e57)
![image](https://github.com/Gapva/SFVC/assets/90116898/ab4092de-30bf-4dab-bb9f-a487cf34d641)

additional notes and tips
- in the second image, a Double Note is defined, but it is not limited to just doubles
- - you may place up to four notes of any kind in their respective columns
- when parsing, you should always case-convert the entire file to lowercase
- when parsing, you should rid any duplicate notes
- - this only includes notes that start at the same exact time and lie in the exact same column
  - if there is a noodle strand, the end-time should not be checked because only the spawn time matters
