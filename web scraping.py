'''
Name: Hariharan P
Date:31/052022

'''

import requests
from bs4 import BeautifulSoup
import argparse

import sqlite3

def connect(dbname):
    conn = sqlite3.connect(dbname)
    conn.execute("CREATE TABLE IF NOT EXISTS OYO_HOTELS (NAME TEXT,ADDRESS TEXT, PRICE INT,AMENITIES TEXT,RATING TEXT)")
    print("table created successfully")
    conn.close()

def insert_into_table(dbname,values):
    conn = sqlite3.connect(dbname)
    insert="INSERT INTO OYO_HOTELS (NAME, ADDRESS, PRICE, AMENITIES, RATING) VALUES (?,?,?,?,?)"
    conn.execute(insert,values)
    conn.commit()
    conn.close()

def get_hotel_info(dbname):
    conn =sqlite3.connect(dbname)
    cur=conn.cursor()
    cur.execute("SELECT * FROM OYO_HOTELS")
    table_data = cur.fetchall()
    for record in table_data:
        print(record)
    conn.close()    

parser =argparse.ArgumentParser()
parser.add_argument("--page_num_max", help="enter the number of pages to parse", type=int)
parser.add_argument("--dbname",help="enter the name of database",type=str)
args=parser.parse_args()

oyo_url = "https://www.oyorooms.com/hotels-in-bangalore/?page="
page_num_max=args.page_num_max

connect(args.dbname)

for page_num in range(1,page_num_max+1):
    req=requests.get(oyo_url+str(page_num))
    content=req.content
    soup=BeautifulSoup(content,"html.parser")
    all_hotels = soup.find_all("div",{"class":"hotelcardListing"})

    for hotel in all_hotels:
        hotel_dict={}
        hotel_dict["name"]=hotel.find("h3",{"class":"listingHotelDescription__hotelName"}).text
        hotel_dict["address"]=hotel.find("span",{"itemprop":"streetAddress"}).text
        hotel_dict["price"]=hotel.find("span",{"class":"listingPrice__finalPrice"}).text
        try:
            hotel_dict["rating"]=hotel.find("span",{"class":"hotelRating__ratingSummary"}).text
        except AttributeError:
            hotel_dict["rating"]="none"

        parent_amenities_element=hotel.find("div",{"class":"amenityWrapper"})
        amenities_list =[]
        for amenity in parent_amenities_element.find_all("div",{"class":"amenityWrapper__amenity"}):
                    amenities_list.append(amenity.find("span",{"class":"d-body-sm"}).text.strip())

        hotel_dict["amenities"] =", ".join(amenities_list[:-1])
        insert_into_table(args.dbname,tuple(hotel_dict.values()))

get_hotel_info(args.dbname)                
