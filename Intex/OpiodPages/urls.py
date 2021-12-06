from django.urls import path
from .views import displayTopPre, sqlDisplayPageView, editPageView, displayAvgPageView, preDetailsPageView, updatePageView, deletePageView, createPrescriberPageView, addPrescriberPageView, indexPageView, drugFindPageView, prescriberFindPageView, analysis1PageView, analysis2PageView, analysisLandingView, drugSearchView, educationLandingView, predictorPageView, prescriberSearchView, recommenderPageView, searchLandingView 


urlpatterns = [
    path("", indexPageView, name = "index"),
    path("predictordisplay/", analysis1PageView, name = "predictordisplay"),
    path("recommenderdisplay/", analysis2PageView, name = "recommenderdisplay"),
    path("analysislanding/", analysisLandingView, name = "analysislanding"),
    path("drugsearch/", drugSearchView, name = "drugsearch"),
    path("drugfind/", drugFindPageView, name = 'drugfind'),
    path("educationlanding/", educationLandingView, name = "educationlanding"),
    path("predictor/", predictorPageView, name = "predictor"),
    path("prescribersearch/", prescriberSearchView, name = "prescribersearch"),
    path("prescriberfind/", prescriberFindPageView, name = 'prescriberfind'),
    path("recommender/", recommenderPageView, name = "recommender"),
    path("searchlanding/", searchLandingView, name = "searchlanding"), 
    path("addprescriber/", addPrescriberPageView, name="addprescriber"),
    path("createprescriber/", createPrescriberPageView, name="createprescriber"),
    path("edit/<int:npi>", editPageView, name="edit"),
    path("delete/<int:npi>", deletePageView, name="delete"),
    path("updateit/", updatePageView, name="updateit"),
    path("predetails/<int:npi>", preDetailsPageView, name='predetails'),
    path("displayavg/<str:drugid>", displayAvgPageView, name='displayavg'),
    path("displaytoppre/<int:drugid>", displayTopPre, name="displaytoppre"),
    path("sqldisplay/", sqlDisplayPageView, name="sqldisplay"),
]