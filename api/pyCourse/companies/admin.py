from django.contrib import admin

# from api.pyCourse.companies.models import Company  # (1)
from .models import Company


@admin.register(Company)  # (2)
class CompanyAdmin(admin.ModelAdmin):
    pass


"""
Notes
(1) Normally, PyCharm use the following way to import Company model:
'from api.coronavstech.companies.models import Company' but it creates
an error. So we manually adjust imports as follows:
'from .models import Company'
(2) admin decorator will register Company model in Django admin
"""
