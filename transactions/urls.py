from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.transactions_index, name="transactions_index"),
    path("deposit/", views.transactions_deposit, name="transactions_deposit"),
    path("deposit/save/", views.transactions_depositsave, name="transactions_depositsave"),
    path("extraction/", views.transactions_extraction, name="transactions_extraction"),
    path("extraction/save/", views.transactions_extractionsave, name="transactions_extractionsave"),
    path("exchange/", views.transactions_exchange, name="transactions_exchange"),
    path("exchange/save/", views.transactions_exchangesave, name="transactions_exchangesave"),
    path("transference/", views.transactions_transference, name="transactions_transference"),
    path("transference/save/", views.transactions_transferencesave, name="transactions_transferencesave"),
]