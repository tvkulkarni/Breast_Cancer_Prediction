from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import json
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd



def about(request):
    #return HttpResponse("THE ABOUT PAGE")
    return render(request,"about.html")

def homepage(request):
    #return HttpResponse("HOME PAGE")
    return render(request,"homepage.html")

def evaluser(request):
    if request.method == "POST":
        name = request.POST['username']
        df = pd.read_csv('breast_cancer/wdbc.data',header=None)
        data=df.columns.values.tolist()
        print(data)
        #data=[]
        for i in range(30):
            # if data[i]==0:
            #     data[i]='ID'
            # if data[i]==1:
            #     data[i]='DIAGNOSIS'
            if data[i]==0:
                data[i]='RADIUS_MEAN'
            if data[i]==1:
                data[i]='TEXTURE_MEAN'
            if data[i]==2:
                data[i]='PERIMETER_MEAN'
            if data[i]==3:
                data[i]='AREA_MEAN'
            if data[i]==4:
                data[i]='SMOOTHNESS_MEAN'
            if data[i]==5:
                data[i]='COMPACTNESS_MEAN'
            if data[i]==6:
                data[i]='CONCATIVITY_MEAN'
            if data[i]==7:
                data[i]='CONCAVE_POINTS'
            if data[i]==8:
                data[i]='SYMMETRY'
            if data[i]==9:
                data[i]='FRACTAL_DIMENSIONS'
            if data[i]==10:
                data[i]='RADIUS_SE'
            if data[i]==11:
                data[i]='TEXTURE_SE'
            if data[i]==12:
                data[i]='PERIMETER_SE'
            if data[i]==13:
                data[i]='AREA_WORST'
            if data[i]==14:
                data[i]='SMOOTHNESS_SE'
            if data[i]==15:
                data[i]='COMPACTNESS_SE'
            if data[i]==16:
                data[i]='CONCATIVITY_SE'
            if data[i]==17:
                data[i]='CONCAVE_POINTS_SE'
            if data[i]==18:
                data[i]='SYMMETRY_SE'
            if data[i]==19:
                data[i]='FRACTAL_DIMENSION_SE'
            if data[i]==20:
                data[i]='RADIUS_WORST'
            if data[i]==21:
                data[i]='TEXTURE_WORST'
            if data[i]==22:
                data[i]='PERIMETER_WORST'
            if data[i]==23:
                data[i]='AREA_WORST'
            if data[i]==24:
                data[i]='SMOOTHNESS_WORST'
            if data[i]==25:
                data[i]='COMPACTNESS_WORST'
            if data[i]==26:
                data[i]='CONCATVITY_WORST'
            if data[i]==27:
                data[i]='CONCAVE_POINTS_WORST'
            if data[i]==28:
                data[i]='SYMMETRY_WORST'
            if data[i]==29:
                data[i]='FRACTAL_DIMENSION_WORST'
            
        alldataforid = {}
        newid=int(name)
        myid=df.loc[df[0]==newid].index
        print(myid)
        z=myid[0]
        alldataforid=df.loc[z,2:]
        data2=alldataforid.values.tolist()
        converted2d=[np.asarray(alldataforid)]
        print(data2)

        #TRAINING DATA
        X = df.loc[:, 2:].values
        y = df.loc[:, 1].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)    
        classifier = LogisticRegression()
        classifier.fit(X_train, y_train)
        classifier.score(X_test,y_test)*100
        #PREDICTING DATA
        y_pred=classifier.predict(converted2d)
        print(y_pred)
        flag=10
        if y_pred[0]=='B':
            flag=0
        else:
            flag=1

        
        
        # for i in range(32):
        #     data2[i] = i
        finaldata = {
            "data":data,
            "data2":data2,
            "name":name,
            "result":flag,
            "score":flag 

        }
        # for i in range(30):
        #     data[i] = i
        return JsonResponse(finaldata)
