from django.shortcuts import render
from .models import Drug, Triple, pd_prescriber, Credential, State, Prescriber_Credential
from django.db.models import  Avg, Max, Count, Sum


# Create your views here.
import json
from pip._vendor import requests 

def indexPageView(request):
    return render(request, 'OpiodPages/index.html')

def analysis1PageView(request):
    return render(request, 'OpiodPages/analysis1.html')

def analysis2PageView(request):
    return render(request, 'OpiodPages/analysis2.html')

def analysisLandingView(request):
    credentials = Credential.objects.all() 
    locations = State.objects.all()
    prescriber = pd_prescriber.objects.all()
    context = {
        "Credentials": credentials,
        "Locations" : locations,
        "Prescriber" : prescriber,
    }   
    return render(request, 'OpiodPages/analysislanding.html', context)

def drugSearchView(request):
    return render(request, 'OpiodPages/drugsearch.html')

def drugFindPageView(request):
    data = ''
    sName = request.GET['drugName']
    sName = sName.upper()
    bOpioid = request.GET['bOpioid']
    if (sName == '') :
        if (bOpioid == 'True') :
            data = Drug.objects.filter(isopioid=True)
        else :
            data = Drug.objects.filter(isopioid=False)
    else :
        if (bOpioid == " " or bOpioid == None or bOpioid == "") :
            data = Drug.objects.filter(drugname=sName)
        else :
            data = Drug.objects.filter(drugname=sName, isopioid=bOpioid)
    try :
        context = {
            "drugs" : data
        }
        if data.count() > 0 :
            return render(request, 'OpiodPages/displaydrugs.html', context)
        else :
            return render(request, 'OpiodPages/notfound.html')
    except : 
        return render(request, 'OpiodPages/notfound.html')

def educationLandingView(request):
    return render(request, 'OpiodPages/educationlanding.html')

def prescriberSearchView(request):
    credentials = Credential.objects.all() 
    locations = State.objects.all()
    context = {
    "Credentials": credentials,
    "Locations" : locations,
}  
    return render(request, 'OpiodPages/prescribersearch.html', context)

def prescriberFindPageView(request) :
    dictCreds = {
        'ACNP' : 2,
        'ACNP-BC' : 3,
        'AGACNP' : 4,
        'ANP' : 5,
        'ANP-BC' : 6,
        'ANP-C' : 7,
        'ANP-FNP-BC' : 8,
        'APN' : 9,
        'APN-C' : 10,
        'APNP' : 11,
        'APRN' : 12,
        'APRN-BC' : 13,
        'ARANP' : 14,
        'ARNP' : 15,
        'ARNP-BC' : 16,
        'ARNP-C' : 17,
        'BC' : 18,
        'BCFNP' : 19,
        'BC-GNP' : 20,
        'BS' : 21,
        'BSN' : 22,
        'CANP' : 23,
        'CCNS' : 24,
        'CCRN' : 25,
        'CFNP' : 26,
        'C-FNP' : 27,
        'CNM' : 28,
        'CNNP' : 29,
        'CNP' : 30,
        'C-NP' : 31,
        'CNS' : 32,
        'CRNA' : 33,
        'CRNP' : 34,
        'CS' : 35,
        'DCNP' : 36,
        'DDS' : 37,
        'DMD' : 38,
        'DNP' : 39,
        'DO' : 40,
        'DP' : 41,
        'DPM' : 42,
        'DVM' : 43,
        'FAAFP' : 44,
        'FACA' : 45,
        'FACC' : 46,
        'FACE' : 47,
        'FACG' : 48,
        'FACP' : 49,
        'FACS' : 50,
        'FCCP' : 51,
        'FNP' : 52,
        'FNP-BC' : 53,
        'FNPC' : 54,
        'FNP-C' : 55,
        'FP' : 56,
        'FPMHNP' : 57,
        'FSCAI' : 58,
        'FSVM' : 59,
        'GNP' : 60,
        'GNP-BC' : 61,
        'LACC' : 62,
        'LP' : 63,
        'MA' : 64,
        'MB' : 65,
        'MBA' : 66,
        'MBBCH' : 67,
        'MBBS' : 68,
        'MD' : 69,
        'MDFACP' : 70,
        'MDPA' : 71,
        'MDPHD' : 72,
        'MHS' : 73,
        'MMS' : 74,
        'MNS' : 75,
        'MPAS' : 76,
        'MPH' : 77,
        'MRCP' : 78,
        'MS' : 79,
        'MSC' : 80,
        'MSHS' : 81,
        'MSN' : 82,
        'NASPE' : 83,
        'ND' : 84,
        'NP' : 85,
        'NPC' : 86,
        'NP-C' : 87,
        'NPF' : 88,
        'NPP' : 89,
        'OD' : 90,
        'PA' : 91,
        'PAC' : 92,
        'PA-C' : 93,
        'PC' : 94,
        'PHARMD' : 95,
        'PHD' : 96,
        'PHP' : 97,
        'PMHHNP' : 98,
        'PMHNP' : 99,
        'PMHNP-BC' : 100,
        'PMHNP-C' : 101,
        'PSYNP' : 102,
        'PT' : 103,
        'RN' : 104,
        'RN-C' : 105,
        'RNCS' : 106,
        'RPAC' : 107,
        'RPA-C' : 108,
        'RPH' : 109,
        'WHNP' : 110,
        ' ' : 1
    }
    sFirst = request.GET['firstName']
    sFirst = sFirst.lower()
    sFirst = sFirst.capitalize()
    sLast = request.GET['lastName']
    sLast = sLast.lower()
    sLast = sLast.capitalize()
    sGender = request.GET['gender']
    sGender = sGender.upper()
    sLocation = request.GET['location']
    sCredentials = request.GET['credentials']
    sSpecialty = request.GET['specialty']
    sSpecialty = sSpecialty.lower()
    sSpecialty = sSpecialty.title()
    iCred = dictCreds.get(sCredentials)
    print(iCred)
    if (sFirst == '') :
        if (sLast == '') : 
            if (sGender == '') :
                if (sLocation == '') :
                    if (sSpecialty == '') :
                            creds = Prescriber_Credential.objects.filter(credid=iCred)
                            for iCount in range(0, len(creds)) :
                                data = pd_prescriber.objects.filter(npi = creds[iCount].npi)
                            return render(request, 'OpiodPages/notfound.html')
                    else :
                        data = pd_prescriber.objects.filter(specialty = sSpecialty)
                else :
                    data = pd_prescriber.objects.filter(state=sLocation)
            else :
                data = pd_prescriber.objects.filter(gender=sGender)
        else :
            data = pd_prescriber.objects.filter(lname = sLast)
    elif (sLast == '') :
        data = pd_prescriber.objects.filter(fname=sFirst)
    elif (sLast != '') :
        if (sGender == '' or sLocation == '' or sSpecialty == '') :
            data = pd_prescriber.objects.filter(fname=sFirst, lname=sLast)
        else :
            data = pd_prescriber.objects.filter(fname=sFirst, lname=sLast, gender=sGender, state=sLocation, specialty=sSpecialty)
    try :
        if data.count() > 0 :
            context = {
                    'prescribers' : data,
                }
            return render(request, 'OpiodPages/prescriberdisplay.html', context)
        else :
            return render(request, 'OpiodPages/notfound.html')
    except :
        return render(request, 'OpiodPages/notfound.html')

def searchLandingView(request):
    return render(request, 'OpiodPages/searchlanding.html')

def addPrescriberPageView(request) :
    data = State.objects.all()
    context = {
        'Locations' : data
    }
    return render(request, 'OpiodPages/addprescriber.html', context)

def createPrescriberPageView(request) :
    if request.method == 'POST':
        new_prescriper = pd_prescriber()
        #Store the data from the form to the new object's attributes (like columns)
        new_prescriper.npi = request.POST.get('npi')
        new_prescriper.fname = request.POST.get('fname')
        new_prescriper.lname = request.POST.get('lname')
        new_prescriper.gender = request.POST.get('gender')
        new_prescriper.specialty = request.POST.get('specialty')
        new_prescriper.isopioidprescriber = request.POST.get('bPrescriber')
        new_prescriper.totalprescriptions = request.POST.get('total')
        new_prescriper.state = State.objects.get(state=request.POST.get('location'))
        new_prescriper.save()
        
    return render(request, 'OpiodPages/prescribersearch.html')

def deletePageView(request, npi) :
    if request.method == 'POST':
        oDelete = pd_prescriber.objects.get(npi=npi)
        oDelete.delete()
    return render(request, 'OpiodPages/prescribersearch.html')

def editPageView(request, npi) :
    data = pd_prescriber.objects.filter(npi=npi)
    context = {
        "edit" : data
    }
    return render(request, 'OpiodPages/edit.html', context)

def updatePageView(request) :
    if request.method == 'POST':
        iUpdateID = request.POST.get('npihidden')
        oUpdate = pd_prescriber.objects.get(npi=iUpdateID)
        oUpdate.totalprescriptions = request.POST.get('updatenumber')
        oUpdate.save()
    return render(request, 'OpiodPages/prescribersearch.html')

def predictorPageView(request):
    url = "http://d912db94-d8bb-4e07-aafd-02aebb477c22.eastus2.azurecontainer.io/score"

    if request.method == 'POST' :
        state = request.POST['location']
        gender = request.POST['gender']
        specialty = request.POST['specialty']
        isoppresc = request.POST['bOpioid']
    
    payload = json.dumps({  
    
    "Inputs": {
        "WebServiceInput0": [
        {
            "state": state,
            "gender": gender,
            "specialty": specialty,
            "isopioidprescriber": isoppresc,
            "Cuberoot(totalprescriptions)": 5.180101467380292
        }
        ]
    },
    "GlobalParameters": {}
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer MVwu3oumhzszRBfTwWb9aur5UZYac6hm'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    json_data = json.loads(response.text)

    items = (json_data['Results']['WebServiceOutput0'][0])
    
    iCount = 0
    mydict = {}
    import math 
    print("Total Prescriptions: ")
    for item in items :
        mydict[iCount] = math.trunc(items[item]*items[item]*items[item])
    new = str(mydict[0])
    
    context = {
        "test" : new
    }

    return render(request, 'OpiodPages/predictordisplay.html', context)
    
def recommenderPageView(request): 
    if request.method == 'POST' :
        prescriberid = request.POST['npi']
        fname = str(pd_prescriber.objects.filter(npi=prescriberid).only("fname"))
        print(fname)
        lname = str(pd_prescriber.objects.filter(npi=prescriberid).only("lname"))
        state = str(pd_prescriber.objects.filter(npi=prescriberid).only("state"))
        gender = str(pd_prescriber.objects.filter(npi=prescriberid).only("gender"))
        specialty = str(pd_prescriber.objects.filter(npi=prescriberid).only("specialty"))
        isoppresc = str(pd_prescriber.objects.filter(npi=prescriberid).only("isopioidprescriber"))
        totpresc = 10
        # if time, fix totpresc - the problem being that we cannot convert a query set to an integer
        
    url = "http://65a45df2-2b8f-4b35-a262-d56b3933e309.eastus2.azurecontainer.io/score"
    payload = json.dumps({
    "Inputs": {
        "input1": [
        {
            "prescriberid": prescriberid,
            "drugname": "LANTUS.SOLOSTAR",
            "Cuberoot(qty)": 3.6593057100229713
        }
        ],
        "WebServiceInput0": [
        {
            "npi": prescriberid,
            "fname": fname,
            "lname": lname,
            "gender": gender,
            "state": state,
            "specialty": specialty,
            "isopioidprescriber": isoppresc,
            "Cuberoot(totalprescriptions)": totpresc
        }
        ],
        "WebServiceInput1": [
        {
            "drugname": "ABILIFY",
            "isopioid": "False"
        }
        ]
    },
    "GlobalParameters": {}
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ry7SQKtAr9CuX3mtzEdgEnaNoZfF496f'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    json_data = json.loads(response.text)
    
    items = (json_data['Results']['WebServiceOutput0'][0])
   
    iCount = 0
    mydict = {}
    print("Total Prescriptions: ")
    for item in items :
        mydict[iCount] = items[item]
        iCount += 1
    
    rec1 = mydict[0]
    rec2 = mydict[1]
    rec3 = mydict[2]
    rec4 = mydict[3]
    rec5 = mydict[4]
    
    print(mydict)
    context = {
        "rec1" : rec1,
        "rec2" : rec2,
        "rec3" : rec3,
        "rec4" : rec4,
        "rec5" : rec5,
    }
    
    return render(request, 'OpiodPages/recommenderdisplay.html', context)

def preDetailsPageView(request, npi) :
    data = pd_prescriber.objects.filter(npi=npi)
    for iCount in range(0, len(data)) :
        data2 = Prescriber_Credential.objects.filter(npi=data[iCount].npi).only("credid")
        data3 = Triple.objects.filter(pd_prescriber=data[iCount].npi).exclude(qty=0).only("drug")
    context = {
        'prescribers' : data,
        'credentials' : data2,
        'triple' : data3,
    }
    return render(request, 'OpiodPages/predetails.html', context)

def displayAvgPageView(request, drugid) :
    data = Drug.objects.filter(drugname=drugid)
    data2 = Triple.objects.filter(drug=data[0].drugid).exclude(qty=0).aggregate(Avg('qty'))
    context = {
        "drug" : data,
        "avg" : data2
    }
    return render(request, "OpiodPages/predetailsavg.html", context)

def displayTopPre(request, drugid) :
    # data2 = ''
    data = Triple.objects.filter(drug=drugid).order_by(('qty'))
    data = data.reverse()[:10]
    data2 = pd_prescriber.objects.all()
    for iCount in range(0, len(data2)) :
        data2[iCount].npi = str(data2[iCount].npi)
        print(data2[iCount].npi + ' is a string')
    # lstPres = []
    # for iCount in range(0, len(data)) :
    #     sNpi = data[iCount].pd_prescriber
    #     iNpi = int(str(sNpi))
    #     data2 = pd_prescriber.objects.filter(npi=iNpi)
    #     lstPres.append(data2)
    #     print(str(iCount))
    #     print(data2)
    # print("final data2")
    # print(data2)
    # print(lstPres)
    # try :
    print('data')
    print(data)
    print('data2')
    print(data2)
    context = {
        'npis' : data,
        'pres' : data2
    }
    return render(request, 'OpiodPages/displaytop.html', context)
    # except :
    #     return render(request, 'OpiodPages/notfound.html')

def sqlDisplayPageView(request) :
    qOpioids = Drug.objects.filter(isopioid = 'True')
    iTotal = 0
    data = State.objects.all().order_by('deaths')
    data = data.reverse()[:10]
    for iCounting in range(0, len(qOpioids)) :
        data2 = Triple.objects.filter(drug=qOpioids[iCounting].drugid).values('drug').annotate(Sum("qty")).order_by('qty__sum')
    data2 = data2.reverse()[:1]
    data3 = Drug.objects.get(drugid= data2[0]['drug'])
    print(qOpioids)
    for iCount in range(0, len(qOpioids)) :
        data4 = Triple.objects.filter(drug=qOpioids[iCount].drugid).aggregate(Sum('qty'))
        iTotal = iTotal + data4['qty__sum']
    context = {
        "states" : data,
        "opioid" : data2,
        'dname' : data3,
        'numop' : iTotal
    }
    # try :
    return render(request, 'OpiodPages/sqldisplay.html', context)
    # except : 
    #     return render(request, "OpiodPages/notfound.html")    