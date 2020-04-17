# KarYo

![Logo](/images/logo.png?raw=true)

## An Automated Karytyping System using Deep Learning and Image Processing

## Details
- Karyotyping is a process of pairing and ordering human chromosomes depending on size, centromere position, and banding pattern.
- It is used to analyse human chromosomes for various genetic disorders  especially during prenatal screenings.
- Since, manual karyotyping is a labor intensive and a time consuming task, developing automatic computer-assisted karyotyping system is required. 
- The proposed Automated Karyotyping System  detects chromosomes from the microscopic image with the help of Faster RCNN with inception v2 model, 
classiﬁes them with the help of inception v3 model and with cytogenetic parameter like length of chromosome.

 [//]: <> ![Karyotype](/images/karyotype39.png?raw=true)
 
<p align="center"> 
<img alt="Karyotype" src="/images/karyotype39.png?raw=true">
</p>

## System Architecture

![System Architecture](/images/schematic.png?raw=true)

## Prerequisites
Install Python 3.4 or above
```
sudo apt-get install python3
```

## Installation Steps
- Clone the repository from 
```
git clone https://github.com/BE-7/KarYo.git
```
- Open Command Prompt/ Terminal and run the following command to install all the required packages.
```
pip install -r requirements.txt 
```
- Execute the frame python file to start.
```
 python frame.py
 ```
 
 ## How to use?
- Open an image that has to be analysed from the menu bar.
- Click on Detect button to detect individual chromosome in the input image.
- Click on Process button to determine the length of individual chromosome.
- Use various options available in View menu to view intermediate steps of length determination.
- Click on Classify button to pass the individual chromosome for classiﬁcation.
- Click on Edit button to use the interactive drag and drop feature for arrangement of classiﬁed chromosomes.
- Click on Reset button to undo all the changes.
- Click on Generate Karyotype button to display the ﬁnal karyotype.


## Contributors
- [Leeaa Nair](https://github.com/leeaanair)
- [Nishant Nimbalkar](https://github.com/Nishant98)
- [Sarah Solkar](https://github.com/SarahSolkar)


