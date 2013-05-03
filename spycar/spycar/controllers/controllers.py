from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
import string
import urllib
import re

from ..models import (
    DBSession,
    path,
    coordinates,
    )

from ..forms import ContactForm
@view_config(route_name='hello', renderer='hello.mako')
def say_hello(request):
  file1=request.POST['formvar'];
  file2=request.POST['formvar'];
  file3=request.POST['path_name'];
  
  
  results1=[]
  results2=[]
  
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
  for index in range(len(results1)):
    aqsa= coordinates(Point="P_"+str(index), latitude= float(results1[index]), longitude=float(results2[index]), path_id=a.id)
    DBSession.add(aqsa)
  #model = path(name= file1)
  #DBSession.add(model)
  acc2 = DBSession.query(coordinates).all()
  return {'acc2':acc2}  
    
    
  #return {'file1':results2}
  
  
  
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
  str1="1245.0";
  str1=float(str1);
  str1=str1+1;
  return {'str1':str1}

    
    
    
    
    
    
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
