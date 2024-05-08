from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from core.forms import PromotionForm


# Create your views here.
def promotion_form(request: HttpRequest) -> HttpResponse:
    context = {"form": PromotionForm()}

    return render(request, "core/promotion_form.html", context)
