import http.client

from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from pandas.io import json
from .models import Data

# Create your views here.

def home(request):
    print(request)
    if (request.method=='POST'):

        try:
            priveious_data=Data.objects.all()
            priveious_data.delete() # all priveious  data deleted
            file_cvs=request.FILES['file'] # chacke the post request is CSV file
            df=pd.read_csv(file_cvs)  # read that csv file
            json_recoreds=df.reset_index().to_json(orient='records') # convert that file  in jeson format with index number integaer
            data=[] # create empty list
            data=json.ujson_loads(json_recoreds) # add that file in the list in ordere to extracte each
            print(data)
            for d in data:
                name=d['property_name']
                price=d['property_price']
                rent=d['property_price']
                emi=d['emi']
                tax=d['tax']
                exp=d['other_exp']
                expenses_monthly=exp+tax+emi
                income_monthly=rent-expenses_monthly
                dt=Data(name=name,price=price,rent=rent,emi=emi,tax=tax,exp=exp,expenses_monthly=expenses_monthly,income_monthly=income_monthly)
                dt.save()


        except:
            return HttpResponse('select file')



    else:
        print('this is get method')
    data = Data.objects.all()
    context={
        'datas':data
    }

    return render(request,'analytic/index.html',context)