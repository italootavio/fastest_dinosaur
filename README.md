# fastest_dinosaur
Algorithm responsible for selecting the fastest dinosaur based on two datasets.

Given the following formula:

Speed = (((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT (LEG_LENGTH * g) where g = 9.8 m / s ^ 2 (gravitational constant)

Algotimo reads the files and prints only the names of the biped dinosaurs from the fastest to the slowest.

$ cat > dataset1.csv
NAME,LEG_LENGTH,DIET
Hadrosaurus,1.2,herbivore
Struthiomimus,0.92,omnivore
Velociraptor,1.0,carnivore
Triceratops,0.87,herbivore
Euoplocephalus,1.6,herbivore
Stegosaurus,1.40,herbivore
Tyrannosaurus Rex,2.5,carnivore

$ cat > dataset2.csv
NAME,STRIDE_LENGTH,STANCE
Euoplocephalus,1.87,quadrupedal
Stegosaurus,1.90,quadrupedal
Tyrannosaurus Rex,5.76,bipedal
Hadrosaurus,1.4,bipedal
Deinonychus,1.21,bipedal
Struthiomimus,1.34,bipedal
Velociraptor,2.72,bipedal
