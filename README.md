# map-reduce-amulya
This is to practice map and reduce

## Question to be answered
Google play store apps individual downloads based on genres 

## Data
For this map reduce, I have used google play store App data. Each app (row) has values for catergory, rating, size, installs, reviews and more. This data is taken from the website kaggle. The data set I have taken consists of 18 different data columns. The dataset consists of 10841 records.

[Link to my data](https://www.kaggle.com/lava18/google-play-store-apps)
## Summary of the result

From the below graph we can analyze that communication genre has high downloads followed by tools.

![image1](Images/all.png)


![image2](Images/Picture1.png)

## Instructions to Execute

cat googleplaystore.csv | python 21mapper.py | sort | python 22reducer.py > mallepalliOutput.txt
