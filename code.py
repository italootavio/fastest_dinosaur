#!/usr/bin/python3
# coding: utf-8

import sys
import pandas

class Program:
    # standardization of private attribute in python
    __dataSet = [] 
    __strScreen = ''

    #contructor
    def __init__(self,ds1 = 'dataset1.csv',ds2 = 'dataset2.csv'):
        try:
            # read datasets 1 and 2
            dataSet1 = pandas.read_csv(ds1)
            dataSet2 = pandas.read_csv(ds2)
        except IOError:
            print("Erro: Nao foi possivel abrir o dataset 1 ou o dataset 2")

        # merge datasets to Pandas Dataframe using column "NAME" present in the two data sets
        self.__dataSet = pandas.merge(dataSet1, dataSet2, on='NAME', how='outer')
        self.removeNaN()

    def removeNaN(self,value = 0):
        # put 0 in the values ​​where NaN exists due to the lack of information in the fields
        self.__dataSet = self.__dataSet.fillna(value)

    def calculSpeed(self):
        # adds a column with the result of the SQRT
        self.__dataSet['sqrt'] = (self.__dataSet['LEG_LENGTH'] * 9.8) ** (1 / 2)

        # calculates speed based on formula
        self.__dataSet = self.__dataSet.eval('VEL = ((STRIDE_LENGTH / LEG_LENGTH) -1) * sqrt')

    def selectDinoType(self,type = 'bipedal'):
        # selects only biped dinosaurs
        self.__dataSet = self.__dataSet.loc[self.__dataSet['STANCE'] == type]

        # put 0 where the speed result cannot be calculated due to the lack of any value
        self.removeNaN()

    def orderDinoFaster(self,order = False):
        # sorts the result by speed
        self.__dataSet = self.__dataSet.sort_values(by=['VEL'], ascending=order)

    def printDinoScreen(self):
        # only shows the name of the dinosaurs
        self.__strScreen = self.__dataSet['NAME'].tolist()
        self.__strScreen = ''.join([str(elem) + ', ' for elem in self.__strScreen])
        self.__strScreen = self.__strScreen[:-2]
        print(self.__strScreen)

    def writeFileOutput(self,nameFile = 'output.txt'):
        # writes the answer to the output file
        file = open(nameFile, "w")
        file.write(self.__strScreen)
        file.close()

def main(ds1 = 'dataset1.csv',ds2 = 'dataset2.csv'):
    prg = Program(ds1,ds2)
    prg.calculSpeed()
    prg.selectDinoType()
    prg.orderDinoFaster()
    prg.printDinoScreen()
    prg.writeFileOutput()

if __name__ == "__main__":
    if len(sys.argv) == 3:
        main(sys.argv[1],sys.argv[2])
    elif len(sys.argv) == 2:
        print("E necessario informar 2 datasets")
    else:
        main()