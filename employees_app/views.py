from django.shortcuts import render
from .models import Employee
from django.db.models import Avg, Q
from datetime import date


def employee_overview(request):

    # Alle Mitarbeiter:
    all_employees = Employee.objects.all()
    # Gehalt über 3000:
    over_3000 = Employee.objects.filter(salary__gt=3000)
    # MA mit Gehalt >= 5000
    count_5000 = Employee.objects.filter(salary__gte=5000).count()
    #Durscchnitt Sales
    average_sales = Employee.objects.filter(department__name="Sales").aggregate(avg=Avg("salary"))["avg"]
    #Vor 2022 eingestellt, nicht HR
    before_2022_not_hr = Employee.objects.filter(hire_date__lt=date(2022, 1, 1)).exclude(department__name="HR")

    context = {
        "all_employees": all_employees,
        "over_3000": over_3000,
        "count_5000":count_5000,
        "average_sales":average_sales,
        "before_2022_not_hr":before_2022_not_hr
    }

    return render(request, 'employee_list.html', context)
