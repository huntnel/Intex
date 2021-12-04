from django.urls import path
from .views import test, editPageView, updatePageView, deletePageView, createPrescriberPageView, addPrescriberPageView, indexPageView, drugFindPageView, prescriberFindPageView, analysis1PageView, analysis2PageView, analysis3PageView, analysisLandingView, drugSearchView, educationLandingView, predictorPageView, prescriberSearchView, recommenderPageView, searchLandingView 


urlpatterns = [
    path("", indexPageView, name = "index"),
    path("predictordisplay/", analysis1PageView, name = "predictordisplay"),
    path("analysis2/", analysis2PageView, name = "analysis2"),
    path("analysis3/", analysis3PageView, name = "analysis3"),
    path("analysislanding/", analysisLandingView, name = "analysislanding"),
    path("drugsearch/", drugSearchView, name = "drugsearch"),
    path("drugfind/", drugFindPageView, name = 'drugfind'),
    path("educationlanding/", educationLandingView, name = "educationlanding"),
    path("predictor/", predictorPageView, name = "predictor"),
    path("prescribersearch/", prescriberSearchView, name = "prescribersearch"),
    path("prescriberfind/", prescriberFindPageView, name = 'prescriberfind'),
    path("recommender/", recommenderPageView, name = "recommender"),
    path("searchlanding/", searchLandingView, name = "searchlanding"), 
    path("test/", test, name="test"),
    path("addprescriber/", addPrescriberPageView, name="addprescriber"),
    path("createprescriber/", createPrescriberPageView, name="createprescriber"),
    path("edit/<int:npi>", editPageView, name="edit"),
    path("delete/<int:npi>", deletePageView, name="delete"),
    path("updateit/", updatePageView, name="updateit"),
    path("predictor/", predictorPageView, name="predictor"),
]