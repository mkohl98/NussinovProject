# Implemtation of Nussinov algorithm
### Prerequisites

- Python 3
    
### Getting Started

- Download algorithm.py 
- Make a new directory
- Execute algorithm.py in command line

###Usage
_Note_: Make sure you have algorithm.py in your working directory.

For help run the command:

    algorithm.py -h

##### Input

    algorithm.py -input INPUT

As Input you can use a sequence or a fasta file. If you want to automate the program you have to use a for-loop in command line.
Setting an input is required.

##### Minimal loop lenght

You can modify the minimal loop length. This is not required. The default is 3.

    algorithm.py -mll MINLOOP
    
_Note_: The changes will only work with odd numbers.

##### Output

If you want to get the Output in the terminal you can skip this parameter. The default setting is '_False_'.
If you set this parameter '_True_' you will receive the annotated dot-parentheses file for each submitted sequence.

    algorithm.py -file {True, False}
    
### Acknowledgement

This program is based on the NUSSINOV-algorithm by Ruth Nussinov. The calculated free binding energy is a simple model based on the ZUKER-algorithm.



    
