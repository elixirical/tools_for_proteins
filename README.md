# tools_for_proteins

Requires python3; distribution.py requires Pillow as well. To install pillow, simply open your console and type 

```
pip install Pillow
```

Put your amino acid sequence in protein.txt as capital single letter amino acid values, with or without new lines. Do not include anything else in the body of the file! 

main.py counts all the amino acids protein.txt and spits it back out into data.txt, including its side chain properties and percentage of the sequence that is that amino acid. When running the program again, either delete or clear the contents of data.txt, if its present.

distribution.txt requires you to know the length of your sequence, which can be defined into the variable protLength. I should have made it just count the length of protein.txt but I was really lazy when programming these (just look at main.txt to see how lazy lol). Once run, it will spit out 25 png files that correspond to each of the 20 primary amino acids, charged amino acids, positive and negative amino acids, and polar and hydrophobc amino acids. 
