from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("siren", views.siren, name="siren"),
    path("reglementations", views.reglementations, name="reglementations"),
    path("result", views.result, name="result"),
    path("bdese/<str:siren>", views.bdese, name="bdese"),
]
