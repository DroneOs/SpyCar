from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from math import degrees, atan2
from decimal import *
import math
import string
import urllib
import re

from ..models import (
    DBSession,
    path,
    coordinates,
    )

from ..forms import ContactForm




def calculate_distance(latitude1, latitude2, longitude1, longitude2):
      
    
     
    # HAVERSINE FORMULA: 
      R = 6371; 
      latitude1 = math.radians(latitude1);
      latitude2= math.radians(latitude2);
      longitude1 = math.radians(longitude1);
      longitude2 = math.radians(longitude2);
      angle = math.atan2(longitude2 - longitude1, latitude2 - latitude1) * 180/3.14159265;
      dLat = (latitude2-latitude1);
      dLon = (longitude2-longitude1);
      latt1 = latitude1;
      latt2 = latitude2;
      arr = math.sin(dLat/2) * math.sin(dLat/2) +math.sin(dLon/2) * math.sin(dLon/2) * math.cos(latt1) * math.cos(latt2);
      c = 2 * atan2(math.sqrt(arr), math.sqrt(1-arr)); 
      d = float(R * c);
      return d;







@view_config(route_name='hello', renderer='hello.mako')
def say_hello(request):
  file1=request.POST['formvar'];
  file2=request.POST['formvar'];
  file3=request.POST['path_name'];
  
  
  results1=[]
  results2=[]
  results3=[]
  #results4=[]
  
  file2=str(file2);
  file1=str(file1);
  file3=str(file3);
  
  # To get latitudes in a list
  
  start_index=file1.find("(")
  while -1!= start_index:
    end_index=file1.find(",", start_index)
    if -1!= end_index:
      testing=file1[start_index+1:end_index]
      results1.append(testing)
    start_index=file1.find("(", end_index)
   
   
  # to get longitude in a list 
   
  index_1=file2.find(" ")
  while -1!= index_1:
    index_2=file2.find(")", index_1)
    if -1!= index_2:
      testing2=file2[index_1+1:index_2]
      results2.append(testing2)
    index_1=file2.find(" ", index_2)

  
  model1=path(name=file3)
  DBSession.add(model1)
  a = DBSession.query(path.id).order_by(path.id.desc()).first()
  index=0;
  lat1=results1[index]
  long1=results2[index]

  
  
  for index in range(len(results1)):
    # Code for retrieving points at index2
    lt2=results1[index+1:]
    lg2=results2[index+1:]
    for l2 in lt2:
      lat2=l2;
      break;
    for ln2 in lg2:
      long2=ln2;
      break;
      
  #evaluating direction for points
  
    lat1=float(lat1)
    lat2=float(lat2)
    long1=float(long1)
    long2=float(long2)
  
    if (lat1 < lat2 and long1 < long2):
	direct="Towards North East"
    elif (lat1 > lat2 and long1 < long2):
	direct="Towards South East"
    elif (lat1 > lat2 and long1 > long2):
	direct="Towards South West"
    elif (lat1 < lat2 and long1 > long2):
	direct="Towards North West"
    else:
	direct="Moving in right direction"
	
    
    # Code for calculating angle
    dx=lat2-lat1
    dy=long2-long1
    angle = degrees(atan2(dy, dx))
    #b1 = (angle + 360) % 360
    #b2 = (90 - angle) % 360
    
    # Conversion form decimal fraction to DMS-Format
    deg = int(angle)
    temp = 60 * (angle - deg)
    minut = int(temp)
    sec = 60 * (temp - minut)
    
    # Rounds seconds
    sec=int(sec * 10) / 10.0
    
    
    
    
    latitude1=lat1;
    latitude2=lat2;
    longitude1=long1;
    longitude2=long2;
    # PYTHAGORES THEOREM
    #latitude1=latitude2-latitude1; 
    #longitude1=longitude2-longitude1;
    #latitude1=latitude1*latitude1;
    #longitude1=longitude1*longitude1;
    #d=math.sqrt(latitude1+longitude1);
    
    
    
    #for calculating distance between ponits:  
      
    d=calculate_distance(latitude1, latitude2, longitude1, longitude2);
    # Code for database insertion 
    results3.append(direct)
    #results4.append(dist)
    lat1=lat2
    long1=long2
    aqsa= coordinates(Point="P_"+str(index), latitude= float(results1[index]), longitude=float(results2[index]), path_id=a.id, direction=results3[index], decimal_degree=angle,degrees=deg, minutes=minut, seconds=sec, distcalc=d)
    DBSession.add(aqsa)

    
    #distance=results4[index]
  acc2 = DBSession.query(coordinates).all()
  return {'acc2':acc2}  
 
  
@view_config(route_name='savings', renderer='savings.mako')   
def my_savings(request):
    acc2 = DBSession.query(coordinates).all()
    
    return {'acc2':acc2}  
    
    
    
    
@view_config(route_name='map', renderer='map.mako')   
def my_map(request):
    #acc2 = DBSession.query(coordinates).all()
    
    return {}  
    
    
    
@view_config(route_name='test', renderer='test.mako')   
def test(request):
  R=6371;
  latitude1= 33.6623534223548;
  latitude2= 33.5977488143793;
  longitude1=73.1740951538086;
  longitude2=73.0522155761719;
  latitude1 = math.radians(latitude1);
  latitude2= math.radians(latitude2);
  longitude1 = math.radians(longitude1);
  longitude2 = math.radians(longitude2);
  angle = math.atan2(longitude2 - longitude1, latitude2 - latitude1) * 180/3.14159265;
  dLat = (latitude2-latitude1);
  dLon = (longitude2-longitude1);
  latt1 = latitude1;
  latt2 = latitude2;
  arr = math.sin(dLat/2) * math.sin(dLat/2) +math.sin(dLon/2) * math.sin(dLon/2) * math.cos(latt1) * math.cos(latt2);
  c = 2 * atan2(math.sqrt(arr), math.sqrt(1-arr)); 
  d = float(R * c);
  
  return {'angle':angle}
  
    
    
    
    
    
    
@view_config(route_name='savings1', renderer='savings1.mako')   
def my_savings1(request):
    acc2 = DBSession.query(path).all()
    
    return {'acc2':acc2}      
    
  
  

@view_config(route_name='home', renderer='home.mako')
def my_view(request):
    one = None
    return {'one': one, 'project': 'spycar'}


@view_config(route_name='contact', renderer="contact.mako")
def contact_form(request):

    f = ContactForm(request.POST)   # empty form initializes if not a POST request

    if 'POST' == request.method and 'form.submitted' in request.params:
        if f.validate():
            #TODO: Do email sending here.

            request.session.flash("Your message has been sent!")
            return HTTPFound(location=request.route_url('home'))

    return {'contact_form': f}
