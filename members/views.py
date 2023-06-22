from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse
from members.form import Input_financedata_info

from members.thread_with_return_value import ThreadWithReturnValue
from .models import Member
import FinanceDataReader as fdr
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import asyncio
import warnings
warnings.simplefilter("ignore", UserWarning)

from threading import Thread


def members(request):
    
    # member1 = Member(firstname='Tobias', lastname='Refsnes')
    # member2 = Member(firstname='Linus', lastname='Refsnes')
    # member3 = Member(firstname='Lene', lastname='Refsnes')
    # member4 = Member(firstname='Stale', lastname='Refsnes')
    # member5 = Member(firstname='Jane', lastname='Doe')
    # members_list = [member1, member2, member3, member4, member5]
    # for x in members_list:
    #   x.save()
    
    
    # return HttpResponse("Hello world!")
    # template = loader.get_template('myfirst.html')

    mymembers = Member.objects.all().values()
    name = "panha"
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers,
        'y' : name
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('templates.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
  return HttpResponse(template.render(context, request))


def test(start,end):
  df = fdr.DataReader('FRED:M2,NASDAQCOM,UMCSENT',start=str(start),end=str(end))
  df.plot(secondary_y='UMCSENT')
  pic_IObytes = BytesIO()
  plt.savefig(pic_IObytes,  format='png')
  pic_IObytes.seek(0)
  pic_hash = base64.b64encode(pic_IObytes.read())
  value = pic_hash.decode()
  return value

def finance_data_view(request):
  img = ''
  twrv = ThreadWithReturnValue(target=test, args=(2000,''))
  twrv.start()
  img = twrv.join()

  context = {
    'value' : img,
  }

  template = loader.get_template('fdr.html')
  return HttpResponse(template.render(context, request))


def finance_data_view_show_image(request):
  img = ''
  start_year = ''
  end_year = ''
  if request.method == 'POST':
    start_year = request.POST['start_year']
    end_year = request.POST['end_year']
    twrv = ThreadWithReturnValue(target=test, args=(start_year,end_year))
    twrv.start()
    img = twrv.join()
    return HttpResponse(img)
  if request.method == 'POST':
    ticker = request.POST['ticker']
    #end_year = request.POST['end_year']
    twrv = ThreadWithReturnValue(target=test, args=(ticker))
    twrv.start()
    img = twrv.join()
    return HttpResponse(img)