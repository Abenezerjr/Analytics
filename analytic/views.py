import http.client

from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from pandas.io import json

# Create your views here.

def home(request):
    print(request)
    if (request.method=='POST'):
        file_cvs=request.FILES['file']
        df=pd.read_csv(file_cvs)
        json_recoreds=df.reset_index().to_json(orient='records')
        data=[]
        data=json.ujson_loads(json_recoreds)
        print(data)

    else:
        print('this is get method')

    return render(request,'analytic/index.html',)