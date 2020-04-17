# KarYo

![Logo](/images/logo.png?raw=true)

## An Automated Karytyping using Deep Learning and Image Processing

## Details
- Karyotyping is a process of pairing and ordering human chromosomes depending on size, centromere position, and banding pattern.
- It is used to analyse human chromosomes for various genetic disorders  especially during prenatal screenings.
- Since, manual karyotyping is a labor intensive and a time consuming task, developing automatic computer-assisted karyotyping system is required. 
- The proposed Automated Karyotyping System  detects chromosomes from the microscopic image with the help of Faster RCNN with inception v2 model, 
classiﬁes them with the help of inception v3 model and with cytogenetic parameter like length of chromosome. 
![Karyotype](/images/karyotype39.png?raw=true)

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

## Contributors
[Leeaa Nair](https://github.com/leeaanair)\
[Nishant Nimbalkar](https://github.com/Nishant98)\
[Sarah Solkar](https://github.com/SarahSolkar)


