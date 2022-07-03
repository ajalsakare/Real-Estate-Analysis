# End-to-End Real Estate Analysis and Price-Prediction

## Introduction

This project is based on 🏠 Real Estate data from <a href="https://www.magicbricks.com">MagicBricks</a> which is a place for property buyers & sellers across India. Does it ever happen to you, when you’re planning to buy a property but are unsure about the prices? It might be a case that this property is located in another city which you don’t know about. So we have got a solution, by using the technique of <b>Machine Learning</b> we can predict property prices and also do <b>Data Analysis</b> which gives you a rough idea before you consider any place.

As the title suggests this is an end-to-end project, let me explain how and which are those stages ?

![Screenshot (31)](https://user-images.githubusercontent.com/74727461/177031032-d13bbb97-d425-41a5-b941-158bcf7269eb.png)

## Stages Involved

<h3> 1. Data Collection </h3> 

This involves the process of collecting data from different sources such as any property dealer firm, which has past records or advertisement agencies, but I've used Web Scraping for this i.e I have extracted property data from a website which posts advertisements. Once you write the code you can use it repeatedly after specific intervals for updated data, it makes the the data collection part hassle free. The tools I've used are `Beautiful Soup` & `Selenium`.

<h3> 2. Data Cleaning </h3>

The real world data is not as clean and ready to use as you think. It contains irrelevant entries, null values, invalid datatypes and many such things to work upon. After the collection part is done all these things needs to be taken care of inorder to perform further Analysis and Modeling. What I've done is drop the columns containing large percentage of null values, extracted valuable information from property description, converting values from different units to same unit & put all these cleaned data into a separate excel file for serving as a source for next stage.

<h3> 3. EDA & Modeling </h3>

In this part I've performed analysis on this dataset and plotted different visualizations. Analysis helps us to understand the data in-depth, gives us valuable insights, helps in decision making. For example if you have a question how the average price and area changes for different cities or tiers or even for number of bedrooms and bathrooms. After comes building ML models which trains on this dataset and helps us predict prices of properties which it has not seen before.

<h3> 4. Deployment </h3>

The final stage of the project includes deploying the project live on the internet, which others can use whenever and wherever they want. For hosting my project I've used Heroku as the platform and designed a simple UI with the help of HTML & CSS and Flask as the backend framework. I would love if you try and play around with this making some predictions. Here is the link <a href="https://property-price-predictions.herokuapp.com/">Property Price Prediction</a>.

<h3> Tools & Technologies used</h3>

1. Language 
   * Python

2. Manipulation
   * Pandas
   * Numpy

3. Visualization
   * Plotly
   * Matplotlib

4. Modeling
   * Scikit-Learn
   * Joblib

5. Frontend UI
   * HTML
   * CSS

6. Backend
   * Flask

7. Deployment
   * Github
   * Heroku

Feel free to connect with me on <a href="https://www.linkedin.com/in/aniket-jalasakare-3a45901a7/">LinkedIn</a> or <a href="https://twitter.com/AniketJalsakare">Twitter</a> for any feedback you have.
