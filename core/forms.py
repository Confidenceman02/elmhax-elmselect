from django import forms
from core.models import Course


class PromotionForm(forms.ModelForm):
    courses = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        template_name="elm_programs/modelChoiceFieldWidget.html",
        empty_label=None,
    )

    class Meta:
        model = Course
        fields = ["courses"]
