from django.views import View
from .models import company
from django.http import JsonResponse
from django.utils.decorators import method_decorator 
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


class companyview(View): 

    #decorator csrf_exempt
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    #get all companies or one company
    def get(self, request, id=0):
        if(id>0): 
            companies=list(company.objects.filter(id=id).values())
            if len(companies)>0 : 
                comp= companies[0]
                datos= {
                    "message": "company", 
                    "company": comp
                }
            else: 
                datos= {
                    "message": "company not found"
                }
            return JsonResponse(datos)
        else:
            companies= list(company.objects.values())
            if len(companies)>0: 
                datos= {
                    "message": "companies", 
                    "companies": companies
                }
            else: 
                datos= {
                    "message": "companies not found"
                }
            return JsonResponse(datos)

    #post a company
    def post(self, request):
        jsondata= json.loads(request.body)
        # print(jsondata)
        company.objects.create(name=jsondata['name'], website=jsondata['Website'], foundation= jsondata['foundation'])
        return JsonResponse({"message": "sucess"})


    #edit a company
    def put(self, request, id):
        jd= json.loads(request.body)
        companies= list(company.objects.filter(id=id).values())
        if len(companies)>0: 
            comp= company.objects.get(id=id)
            comp.name= jd['name']
            comp.website= jd['website']
            comp.foundation= jd['foundation']
            comp.save()
            datos= {"message": "Update Success"}
        else: 
            datos= {"message": "company not found"}

        return JsonResponse(datos)

    
    def delete(self, request, id):
        companies= list(company.objects.filter(id=id).values())
        if len(companies)>0:
            company.objects.filter(id=id).delete()
            datos= {"message": "Delete Success"}
        else:
            datos= {"message": "company not found"}
        return JsonResponse(datos)