from django.shortcuts import render
from rest_framework.decorators import api_view

from django.core.mail import send_mail
from rest_framework.request import Request
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from companies.models import Company
from companies.serializers import CompanySerializer



class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer  # (1)
    queryset = Company.objects.all().order_by("-last_update")  # (2)
    pagination_class = PageNumberPagination  # (3)


@api_view(http_method_names=["POST"])
def send_company_email(request: Request) -> Response:
#     """
#     Function that will send email with request payload. With the help of REST FRAMEWORK decorator `@api_view()` we will treat our function as POST endpoint.
#     sender: python.testme@gmail.com
#     receiver: python.testme@gmail.com
#     """
#     # sent_mail will be mocked in test_email_unittest.py

    send_mail(
        subject=request.data.get("subject"),
        message=request.data.get("message"),
        from_email="python.test123@gmail.com",
        recipient_list=["python.test123@gmail.com"],
    )

    return Response({"status": "success", "info": "email sent successfully"}, status=200)




