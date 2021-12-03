from django.urls import path
from .views import indexPageView, analysis1PageView, analysis2PageView, analysis3PageView, analysisLandingView, drugSearchView, educationLandingView, predictorPageView, prescriberSearchView, recommenderPageView, searchLandingView, indexRenamePageView 


urlpatterns = [
    path("", indexPageView, name = "index"),
    path("analysis1/", analysis1PageView, name = "analysis1"),
    path("analysis2/", analysis2PageView, name = "analysis2"),
    path("analysis3/", analysis3PageView, name = "analysis3"),
    path("analysislanding/", analysisLandingView, name = "analysislanding"),
    path("drugsearch/", drugSearchView, name = "drugsearch"),
    path("educationlanding/", educationLandingView, name = "educationlanding"),
    path("predictor/", predictorPageView, name = "predictor"),
    path("prescribersearch/", prescriberSearchView, name = "prescribersearch"),
    path("recommender/", recommenderPageView, name = "recommender"),
    path("searchlanding/", searchLandingView, name = "searchlanding"),  
    #Remove this later the one under this comment
    path("indexRename/", indexRenamePageView, name = "indexRename"),
]