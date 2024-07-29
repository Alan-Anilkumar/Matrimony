from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import DateInput

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):  
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "phone_number",
            "date_of_birth",
            "gender",
            "profile_picture",
            "hobbies",
            "qualification",
            "smoking_habits",
            "interests",
            "short_reel",
            "user_image_1",
            "user_image_2",
            "user_image_3",
            "user_image_4",
        )
        widgets = {
            "date_of_birth": DateInput(attrs={"class": "form-control", "type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field not in self.Meta.widgets:
                self.fields[field].widget.attrs.update({"class": "form-control"})
