from django.shortcuts import render

# Create your views here.

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

def educationLandingView(request):
    return render(request, 'OpiodPages/educationlanding.html')

def predictorPageView(request):
    return render(request, 'OpiodPages/predictor.html')

def prescriberSearchView(request):
    return render(request, 'OpiodPages/prescribersearch.html')

def recommenderPageView(request):
    return render(request, 'OpiodPages/recommender.html')

def searchLandingView(request):
    return render(request, 'OpiodPages/searchlanding.html')

def indexRenamePageView(request):
    return render(request, 'OpiodPages/indexRename.html')