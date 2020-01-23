# fastest_dinosaur
Algorithm responsible for selecting the fastest dinosaur based on two datasets.

Given the following formula:

Speed = (((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT (LEG_LENGTH * g) where g = 9.8 m / s ^ 2 (gravitational constant)

Algotimo reads the files and prints only the names of the biped dinosaurs from the fastest to the slowest.

To run the program in a Linux environment:

$ python code.py      or     $ ./code.py                      

or you can pass the datasets by parameter:

$ python code.py dataset1.csv dataset2.csv or ./code.py dataset1.csv dataset2.csv

Note: it is necessary to have Python 3 installed together with the Pandas library.
