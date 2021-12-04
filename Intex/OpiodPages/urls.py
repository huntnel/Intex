from django.urls import path
from .views import test, indexPageView, drugFindPageView, prescriberFindPageView, analysis1PageView, analysis2PageView, analysis3PageView, analysisLandingView, drugSearchView, educationLandingView, predictorPageView, prescriberSearchView, recommenderPageView, searchLandingView 


urlpatterns = [
    path("", indexPageView, name = "index"),
    path("analysis1/", analysis1PageView, name = "analysis1"),
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
    path("test/", test, name="test")
]