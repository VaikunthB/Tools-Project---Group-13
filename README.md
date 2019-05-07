# Tools for Analytics Project - Group 13

This readme consists information about the Python based program to classify music lyrics based on certain attributes as part of the Tools for Analytics class at Columbia University.

The team consists of two members:

Gaurang Bhatt: (UNI: gb2642)

Vaikunth Bharadwaj: (UNI: vb2469)


## Project Description

The program created takes in a folder of lyrics and uses a Python program to classify them based on their mood, love, length, complexity and child friendliness. The classification provides an a dimension to each song between the range 0-1. The output of the program is a JSON object, set to StdOut. This contains information about the song such as song name and id, artist and the dimensions of the classifications.

## Program Execution

The program can be run by cloning the repository:

Cloning with SSH: git@github.com:VaikunthB/Tools-Project---Group-13.git

Cloning with HTTPS: https://github.com/VaikunthB/Tools-Project---Group-13.git

There is an extra package that must be installed - scipy, which has been used to do percentile calculation for the songs.

After the installation, the program is run by typing the following code in the command line:

```bash
$ python3 main.py <absolute path to lyrics folder>/
```

## Program Logic

There are five files used in this program, and they are explaind below:

### main.py

This is the function that calls all other functions required for the classification. It uses argument parser and takes the input for the lyrics folder directory. It then performs the function of storing the data of all the txt files in the folder locally for further processing. It then calculates dimensions for all the files and stores them in a list to be used for future percentile calculations by calling the average_calculator.py file.

The second part of the file is to carry out the dimension calculator for each individual file by looping through it, and then sending then storing the values in a dictionary format. 

After all calculations are complete, the information is converted into a StdOut JSON object, which is then printed.

### analyzer.py

This file contains the various different functions to classify the song. The first few functions use regex to identify song names, artists and the ID. 

The other analyzing functions for mood, length, complexity, child-friendliness use song lyrics and average values as inputs and then find its dimension. The dimension is calculated on a relative basis, i.e. each song is given a dimension based on its percentile value in the library.

### average_calculator.py

This file contains the various functions to calculate the characterization value of all songs in the folder and store the in a list. This serves as a preprocessor for the analzyer function.

### stopwords.py

This file contains lists of words used for comparison. There are four lists, love words, stopwords, positive words and negative words. 

### file_extractor.py

This file contains an extractor function to reduce the multiple usage of reading the text files.

### testing.py

This file contains unittesting to check if the analyzer functions are running effectively, as well as the main.py file.
