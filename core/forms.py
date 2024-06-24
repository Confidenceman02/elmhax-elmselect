from django import forms
from core.models import Course, Extra


class PromotionForm(forms.ModelForm):
    courses = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        template_name="elm_programs/modelChoiceFieldWidget.html",
        empty_label=None,
    )

    extras = forms.ModelMultipleChoiceField(
        queryset=Extra.objects.all(),
        template_name="elm_programs/modelMultipleChoiceFieldWidget.html",
    )

    class Meta:
        model = Course
        fields = ["courses", "extras"]
