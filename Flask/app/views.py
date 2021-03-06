#!/Usr/bin/env python
from flask import render_template,request
from app import app
import pymysql as mdb
from a_Model import ModelIt
import pickle
import json
import unicodedata

@app.route('/')
# @app.route('/cover')
def cover_input():
    return render_template("cover.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/input')
def input():
    # return render_template("input.html")
    hotels = []
    marker_lon = []
    marker_lat = []
#     marker_gps = []
    marker_ID = []
    marker_name=[]
    marker_rating= []
    marker_dict1={}
    
    marker_lon_e=[]
    marker_lat_e=[]
    marker_ID_e=[]
    marker_name_e=[]
    
    marker_lon_g=[]
    marker_lat_g=[]
    marker_ID_g=[]

    marker_lon_f=[]
    marker_lat_f=[]
    marker_ID_f=[]
    
    marker_lon_p=[]
    marker_lat_p=[]
    marker_ID_p=[]
    
    db = mdb.connect(user="hee", host="localhost", passwd="klee0108", db="hotelInfo_add", charset='utf8')
#    db = mdb.connect(user="root", host="localhost", passwd= "root", db="hotelInfo", charset='utf8')

    with db:
        cur = db.cursor()
        cur.execute("SELECT HotelID, HotelName, City, Ratepng, HotelRate, Hotel_lat , Hotel_len, TARate FROM ddScore_add;")
        query_results = cur.fetchall()

    for result in query_results:
        hotels.append(dict(ID=result[0], name=result[1], city=result[2], png=result[3],rate=result[4], lat=result[5], len=result[6], TArate=result[7]))
#         t= [result[5],result[6]]
        marker_lat.append(result[5])
        marker_lon.append(result[6])
      #   marker_gps.append(t)
        marker_ID.append(result[0])
        marker_name.append(result[1])
        marker_rating.append(result[4])
        hn = str(result[1])
        id = result[0]
        marker_dict1[id] = hn
#     print marker_dict1
#    print marker_name 

    for result in query_results:
        if 'Excellent' in result[4]:
            marker_lat_e.append(result[5])
            marker_lon_e.append(result[6])
            marker_ID_e.append(result[0])
            hn = str(result[1])
            marker_name_e.append(hn)
#     print marker_name_e, type(marker_name_e[0]), len(marker_name_e)
#     print marker_ID_e, type(marker_ID_e[0]), len(marker_ID_e)

    for result in query_results:
        if 'Good' in result[4]:
            marker_lat_g.append(result[5])
            marker_lon_g.append(result[6])
            marker_ID_g.append(result[0])
            

    for result in query_results:
        if 'Fair' in result[4]:
            marker_lat_f.append(result[5])
            marker_lon_f.append(result[6])
            marker_ID_f.append(result[0])
            

    for result in query_results:
        if 'Poor' in result[4]:
            marker_lat_p.append(result[5])
            marker_lon_p.append(result[6])
            marker_ID_p.append(result[0])
            

    return render_template("input.html", hotels=hotels, marker_lon=marker_lon, marker_lat=marker_lat ,marker_ID=marker_ID,marker_name=marker_name, marker_rating=marker_rating,  marker_lon_e=marker_lon_e, marker_lat_e=marker_lat_e, marker_ID_e=marker_ID_e, marker_lon_g=marker_lon_g, marker_lat_g=marker_lat_g, marker_ID_g=marker_ID_g,  marker_lon_f=marker_lon_f, marker_lat_f=marker_lat_f, marker_ID_f=marker_ID_f,  marker_lon_p=marker_lon_p, marker_lat_p=marker_lat_p, marker_ID_p=marker_ID_p, marker_dict1=marker_dict1, marker_name_e=marker_name_e)


@app.route('/output')
def output():
  #pull 'ID' from input field and store it
    rate = request.args.get('rating')

    hotels = []
    marker_lon=[]
    marker_lat=[]
#     marker_gps = []
    marker_ID=[]
    marker_name=[]
    marker_rating=[]

    marker_lon_e=[]
    marker_lat_e=[]
    marker_ID_e=[]
    
    marker_lon_g=[]
    marker_lat_g=[]
    marker_ID_g=[]

    marker_lon_f=[]
    marker_lat_f=[]
    marker_ID_f=[]
    
    marker_lon_p=[]
    marker_lat_p=[]
    marker_ID_p=[]

    db = mdb.connect(user="hee", host="localhost", passwd="klee0108", db="hotelInfo_add", charset='utf8')

    with db:
        cur = db.cursor()
    #just select the city from the world_innodb that the user inputs
        cur.execute("SELECT HotelID, HotelName, City, Ratepng, HotelRate, Hotel_lat , Hotel_len, TARate FROM ddScore_add  WHERE HotelRate='%s';" %rate)
        query_results = cur.fetchall()
    for result in query_results:
        hotels.append(dict(ID=result[0], name=result[1], city=result[2], png=result[3], rate=result[4], lat=result[5], len=result[6], TArate=result[7]))
        marker_lat.append(result[5])
        marker_lon.append(result[6])
      #   marker_gps.append(t)
        marker_ID.append(result[0])
        marker_name.append((result[0],result[1]))
        marker_rating.append(result[4])

    for result in query_results:
        if 'Excellent' in result[4]:
            marker_lat_e.append(result[5])
            marker_lon_e.append(result[6])
            marker_ID_e.append(result[0])
            

    for result in query_results:
        if 'Good' in result[4]:
            marker_lat_g.append(result[5])
            marker_lon_g.append(result[6])
            marker_ID_g.append(result[0])
            

    for result in query_results:
        if 'Fair' in result[4]:
            marker_lat_f.append(result[5])
            marker_lon_f.append(result[6])
            marker_ID_f.append(result[0])
            

    for result in query_results:
        if 'Poor' in result[4]:
            marker_lat_p.append(result[5])
            marker_lon_p.append(result[6])
            marker_ID_p.append(result[0])

    the_result = ''
    return render_template("output.html", hotels=hotels, marker_lon=marker_lon, marker_lat=marker_lat, marker_ID=marker_ID, marker_name=marker_name, marker_rating=marker_rating, marker_lon_e=marker_lon_e, marker_lat_e=marker_lat_e, marker_ID_e=marker_ID_e, marker_lon_g=marker_lon_g, marker_lat_g=marker_lat_g, marker_ID_g=marker_ID_g,  marker_lon_f=marker_lon_f, marker_lat_f=marker_lat_f, marker_ID_f=marker_ID_f,  marker_lon_p=marker_lon_p, marker_lat_p=marker_lat_p, marker_ID_p=marker_ID_p, the_result = the_result)
