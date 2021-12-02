from django.urls import path
from .views import indexPageView, analysis1PageView, analysis2PageView, analysis3PageView, analysisLandingView, drugSearchView, educationLandingView, predictorPageView, prescriberSearchView, recommenderPageView, searchLandingView, indexRenamePageView 


urlpatterns = [
    path("", indexPageView, name = "index"),
    path("analysis1/", indexPageView, name = "analysis1"),
    path("analysis2/", indexPageView, name = "analysis2"),
    path("analysis3/", indexPageView, name = "analysis3"),
    path("analysislanding/", indexPageView, name = "analysislanding"),
    path("drugsearch/", indexPageView, name = "drugsearch"),
    path("educationlanding/", indexPageView, name = "educationlanding"),
    path("predictor/", indexPageView, name = "predictor"),
    path("prescribersearch/", indexPageView, name = "prescribersearch"),
    path("recommender/", indexPageView, name = "recommender"),
    path("searchlanding/", indexPageView, name = "searchlanding"),  
    #Remove this later the one under this comment
    path("indexRename/", indexRenamePageView, name = "indexRename"),
]