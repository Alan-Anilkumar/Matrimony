from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateInput

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = (
            "username",
            "email",
            "phone_number",
            "profile_picture",
            "first_name",
            "last_name",
            "date_of_birth",
            "gender",
            "hobbies",
            "qualification",
            "smoking_habits",
            "interests",

        )
        widgets = {
            "date_joined": DateInput(attrs={"class": "form-control", "type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field not in self.Meta.widgets:
                self.fields[field].widget.attrs.update({"class": "form-control"})
