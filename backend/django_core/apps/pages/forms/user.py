from apps.user.models import CustomUser
from apps.user.validators import username_validator
from django import forms
from django.conf import settings
from django.core.validators import RegexValidator


class FirstRegisterForm(forms.Form):
    email = forms.EmailField(
        label="Email:",
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "placeholder": "sora_amamiya@coreproject.moe",
                "class": "h-12 w-full rounded-xl border-2 bg-transparent pl-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:pl-[1vw] md:text-[1.1vw]",
            }
        ),
        help_text="we’ll send you a verification email, so please ensure it’s active",
    )
    password = forms.CharField(
        label="Password:",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "enter your existing password",
                "class": "h-12 w-full rounded-xl border-2 bg-transparent pl-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:pl-[1vw] md:text-[1.1vw]",
                "_": """
                    on keyup
                        set global password to my.value
                        js(password)
                            try{
                                return window.get_password_strength(password).score;
                            } catch (e) {
                                console.log("Silenced errors")
                                return null
                            }
                        end
                        send hyperscript:password_strength(strength:it) to <password-strength/>
                """,
            },
            render_value=True,
        ),
    )
    confirm_password = forms.CharField(
        label="Confirm Password:",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "re-enter your password",
                "class": "h-12 w-full rounded-xl border-2 bg-transparent pl-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:pl-[1vw] md:text-[1.1vw]",
            }
        ),
        help_text="Please make sure you enter the same password in both fields",
    )

    def clean(self) -> None:
        cleaned_data = self.cleaned_data
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error(
                "confirm_password",
                error="**Password** and **Confirm Password** does not match",
            )


class SecondRegisterForm(forms.Form):
    username = forms.CharField(
        label="Username:",
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "placeholder": "choose any username",
                "class": "h-12 w-full rounded-xl border-2 border-primary-500 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]",
            }
        ),
        validators=[
            username_validator,
            RegexValidator(
                rf"^[a-zA-Z0-9_-]+#[0-9]{{{settings.DISCRIMINATOR_LENGTH}}}$",
                message="**Username** is not valid for this regex `^[a-zA-Z0-9_-]+#[0-9]{4}$`",
            ),
        ],
        help_text="you can change username in your user settings later, so go bonkers!",
    )

    otp = forms.CharField(
        label="One Time Verification Code:",
        widget=forms.TextInput(
            attrs={
                "placeholder": "enter the code",
                "class": "h-12 w-full rounded-xl border-2 border-primary-500 bg-transparent px-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 focus:border-primary-400 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:px-[1vw] md:text-[1.1vw]",
            }
        ),
        help_text="if you didn’t receive the code, check your spam folder. Or use the resend button",
    )

    def clean(self) -> None:
        cleaned_data = self.cleaned_data

        if username := cleaned_data.get("username"):
            if CustomUser.objects.filter(username=username).exists():
                self.add_error(
                    "username", error="**Username** already taken! try another one"
                )


class ResetPasswordForm(forms.Form):
    email = forms.EmailField(
        label="Email:",
        widget=forms.TextInput(
            attrs={
                "autofocus": True,
                "placeholder": "sora_amamiya@coreproject.moe",
                "class": "h-12 w-full rounded-xl border-2 bg-transparent pl-5 text-base font-medium outline-none !ring-0 transition-all placeholder:text-white/50 md:h-[3.125vw] md:rounded-[0.75vw] md:border-[0.2vw] md:pl-[1vw] md:text-[1.1vw]",
            }
        ),
        help_text=" we’ll send you a reset password link on your registered email address",
    )

    def clean(self) -> None:
        email = self.cleaned_data.get("email")

        if not CustomUser.objects.filter(email=email).exists():
            self.add_error(
                "email",
                error="**Email** not registered! please enter a registered email address",
            )
