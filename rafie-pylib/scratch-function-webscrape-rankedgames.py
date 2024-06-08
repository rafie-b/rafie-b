### This is a scratch and basic idea for a function to scrape data into a slot ranking website
### It was made based in a test for Jr Data Enginer role

# Importing libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

# Defining the function
def find_basic_info(url):
  # Sending a request to the url and getting the html content
  response = requests.get(url)
  content = response.content

  # Parsing the html content using BeautifulSoup
  soup = BeautifulSoup(content, "html.parser")

  # Finding all the items in the best slot games list
  items = soup.find_all("div", class_="item")

  # Creating empty lists to store the basic information of each item
  game_names = []
  software_names = []
  release_dates = []
  rtps = []
  max_wins = []
  volatilities = []
  features = []

  # Looping through each item and extracting the basic information
  for item in items:
    # Finding and appending the game name
    game_name = item.find("h3", class_="title").text.strip()
    game_names.append(game_name)

    # Finding and appending the software name
    software_name = item.find("span", class_="provider").text.strip()
    software_names.append(software_name)

    # Finding and appending the release date
    release_date = item.find("span", class_="date").text.strip()
    release_dates.append(release_date)

    # Finding and appending the RTP
    rtp = item.find("span", class_="rtp").text.strip()
    rtps.append(rtp)

    # Finding and appending the max win
    max_win = item.find("span", class_="maxwin").text.strip()
    max_wins.append(max_win)

    # Finding and appending the volatility
    volatility = item.find("span", class_="volatility").text.strip()
    volatilities.append(volatility)

    # Finding and appending the features
    feature_list = item.find_all("li")
    feature_text = ", ".join([feature.text.strip() for feature in feature_list])
    features.append(feature_text)

  
  # Creating a pandas dataframe with all the lists as columns 
  df = pd.DataFrame({"Game": game_names,
                     "Software": software_names,
                     "Release Date": release_dates,
                     "RTP": rtps,
                     "Max Win": max_wins,
                     "Volatility": volatilities,
                     "Features": features})

  
  # Saving the dataframe as a CSV file 
  df.to_csv("basic_info.csv", index=False)

  
  # Printing out some sample rows of the dataframe 
  print(df.head())

# Calling the function with your url 
find_basic_info("https://clashofslots.com/best-online-slots/")