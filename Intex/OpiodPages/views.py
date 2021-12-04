from django.shortcuts import render
from django.http import HttpResponse
from .models import Drug, Triple, pd_prescriber, Credential, State, Prescriber_Credential
from django.db import connection

# Create your views here.
import json
from pip._vendor import requests 

def test(request) :
    data = Drug.objects.filter(isopioid = True)
    context = {
        'Drugs' : data
    }
    return render(request, 'OpiodPages/test.html', context)

def indexPageView(request):
    return render(request, 'OpiodPages/index.html')

def analysis1PageView(request):
    return render(request, 'OpiodPages/analysis1.html')

def analysis2PageView(request):
    return render(request, 'OpiodPages/analysis2.html')

def analysis3PageView(request):
    return render(request, 'OpiodPages/analysis3.html')

def analysisLandingView(request):
    return render(request, 'OpiodPages/analysislanding.html')

def drugSearchView(request):
    return render(request, 'OpiodPages/drugsearch.html')

def drugFindPageView(request):
    data = ''
    sName = request.GET['drugName']
    sName = sName.upper()
    bOpioid = request.GET['bOpioid']
    context = 0
    if (sName == '') :
        if (bOpioid == 'True') :
            data = Drug.objects.filter(isopioid=True)
        else :
            data = Drug.objects.filter(isopioid=False)
        context = {
            "drugs" : data
        }
    else :
        data = Drug.objects.filter(drugname=sName, isopioid=bOpioid)
        context = {
            "drugs" : data
        }
    if data.count() > 0 :
        return render(request, 'OpiodPages/displaydrugs.html', context)
    else :
        return render(request, 'OpiodPages/notfound.html')

def educationLandingView(request):
    return render(request, 'OpiodPages/educationlanding.html')

def predictorPageView(request):
    return render(request, 'OpiodPages/predictor.html')

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
    lstcred = []
    lstcred1 = []
    lstdrug = []
    data= ''
    data2 = ''
    data3 = ''
    sFirst = request.GET['firstName']
    sLast = request.GET['lastName']
    sGender = request.GET['gender']
    sGender = sGender.upper()
    sLocation = request.GET['location']
    sCredentials = request.GET['credentials']
    sSpecialty = request.GET['specialty']
    sCred = dictCreds.get(sCredentials)
    if (sFirst == '') :
        if (sLast == '') : 
            if (sGender == '') :
                if (sLocation == '') :
                    if (sSpecialty == '') :
                        data = Prescriber_Credential.objects.filter(credid=sCred)
                    else :
                        data = pd_prescriber.objects.filter(specialty = sSpecialty)
                        for iCount in range(0, len(data)) :
                            lstcred.append(Prescriber_Credential.objects.filter(npi=data[iCount].npi))
                            lstdrug.append(Triple.objects.filter(pd_prescriber=data[iCount].npi))
                else :
                    data = pd_prescriber.objects.filter(state=sLocation)
                    for iCount in range(0, len(data)) :
                        lstcred.append(Prescriber_Credential.objects.filter(npi=data[iCount].npi))
                        lstdrug.append(Triple.objects.filter(pd_prescriber=data[iCount].npi))
            else :
                data = pd_prescriber.objects.filter(gender=sGender)
                for iCount in range(0, len(data)) :
                    lstcred.append(Prescriber_Credential.objects.filter(npi=data[iCount].npi))
                    lstdrug.append(Triple.objects.filter(pd_prescriber=data[iCount].npi))
        else :
            data = pd_prescriber.objects.filter(lname = sLast)
            for iCount in range(0, len(data)) :
                lstcred.append(Prescriber_Credential.objects.filter(npi=data[iCount].npi))
                lstdrug.append(Triple.objects.filter(pd_prescriber=data[iCount].npi))
    elif (sLast == '') :
        data = pd_prescriber.objects.filter(fname=sFirst)
        for iCount in range(0, len(data)) :
            lstcred.append(Prescriber_Credential.objects.filter(npi=data[iCount].npi))
            lstdrug.append(Triple.objects.filter(pd_prescriber=data[iCount].npi))
    elif (sLast != '') :
        if (sGender == '' or sLocation == '' or sSpecialty == '') :
            data = pd_prescriber.objects.filter(fname=sFirst, lname=sLast)
            for iCount in range(0, len(data)) :
                data2 = Prescriber_Credential.objects.filter(npi=data[iCount].npi)
                data3 = Triple.objects.filter(pd_prescriber=data[iCount].npi)

        else :
            data = pd_prescriber.objects.filter(fname=sFirst, lname=sLast, gender=sGender, state=sLocation, specialty=sSpecialty)
            for iCount in range(0, len(data)) :
                oCred = Prescriber_Credential.objects.get(npi=data[iCount].npi)
                lstcred.append(oCred.credid)
                for iCount1 in range(0, len(lstcred)) :
                    lstcred1.append(lstcred[iCount])
                oDrug = Triple.objects.filter(pd_prescriber=data[iCount].npi)
                lstdrug.append(oDrug.drug)
    print(data3)
    if data.count() > 0 :
        context = {
                'prescribers' : data,
                'credentials' : data2,
                'triple' : data3
            }
        return render(request, 'OpiodPages/prescriberdisplay.html', context)
    else :
        return render(request, 'OpiodPages/notfound.html')

def recommenderPageView(request):
    return render(request, 'OpiodPages/recommender.html')

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
        state = request.POST['state']
        gender = request.POST['gender']
        specialty = request.POST['specialty']
        isoppresc = request.POST['isop']
    
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
    print(mydict)
    context = {
        "test" : new
    }
    
    return render(request, 'something,html', context)