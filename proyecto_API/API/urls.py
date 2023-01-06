from django.urls import path
from .views import companyview

urlpatterns = [
    path('companies/', companyview.as_view(), name='companies'),
    path('companies/<int:id>', companyview.as_view(), name='one_company')

]