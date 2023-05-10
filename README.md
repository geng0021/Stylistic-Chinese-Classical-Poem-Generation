# FYP
This is the code for a Final Year Project : Stylistic Classical Chinese Poem Generation – The anatomy of an AI poet
The report of this project could be found at NTU Library.

This project consists of three parts and is dedicated to build an AI poem generator that can generate stylistic classical Chinese poems based on user input keywords. 

Firstly, this project will build a Chinese poetry generator using the sequence-to-sequence model. 
Then, the project will explore unsupervised and supervised machine learning algorithms to classify Chinese poems by style. 
Finally, this project will integrate the results of the first two parts and use stylized data to train the Chinese poetry generator. 

The result is a successful model that generates Chinese poems based on the keywords entered by the user and the style chosen.

The methodology contains 3 parts in total, as shown in the following slides:

<img width="932" alt="Screenshot 2023-05-10 at 4 41 57 PM" src="https://github.com/geng0021/FYP/assets/72501075/d561415d-9504-43d2-8a38-05d7ccd1ec56">

## Part 1: Build Classical Chinese Poem Generator
The poem generator is built based on the Working Memory model, refering to Xiaoyuan Yi's work at (https://github.com/THUNLP-AIPoet/WMPoetry)

## Part 2: Classify Chinese Poetry Data
Part 2 tried both supervised Machine Learning method and unsupervised Machine Learning method.
For Unsupervised ML Method, the code is included in clustering.ipynb
for supervised ML method, the code is included in /sv_ML/ml_ccpc.ipynb.
By running this notebook, a few csv file will be generated. these files have been uploaded to /sv_ML for reference, noted that the generated result might be different everytime runing the file.
The following picture shows an flow chart of classification using ML method.
<img width="929" alt="Screenshot 2023-05-10 at 5 13 14 PM" src="https://github.com/geng0021/FYP/assets/72501075/d6edd1f1-9e04-47bb-b958-69f88cb615cb">

## Part 3: Build Stylistic Chinese Poetry Generator
The code is included in the retrain.py.
After Part 2 is done, all data generated will need to be combined with result from part 1.
All parameters should be modified accordingly.
Here is a flowchart of this part
<img width="932" alt="Screenshot 2023-05-10 at 5 19 55 PM" src="https://github.com/geng0021/FYP/assets/72501075/ef12138f-5941-471c-abb6-e802274668a0">

## Result obtained:
Given the same keywords as Wind and Flower, and genre pattern as 1, generating 7-character quatrain.
### Original generator
<img width="930" alt="Screenshot 2023-05-10 at 5 23 06 PM" src="https://github.com/geng0021/FYP/assets/72501075/3b202472-8ccb-4c44-a65f-ff4fd58cc3fb">

### The Bold School generator<img width="930" alt="Screenshot 2023-05-10 at 5 23 31 PM" src="https://github.com/geng0021/FYP/assets/72501075/68b50203-cb6a-4ec3-975b-754bdf912942">

### The Graceful School generator & The Landscape School generator
<img width="930" alt="Screenshot 2023-05-10 at 5 24 25 PM" src="https://github.com/geng0021/FYP/assets/72501075/085211c8-36f6-454d-82d8-347e9bec8b51">

