from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect


class UserOnlyEditThemselfPermissionMixin(AccessMixin):
    fail_url = "/"
    fail_message = ""
    no_auth_message = ""

    def dispatch(self, request, pk, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.no_auth_message)
        elif request.user.id != pk:
            messages.error(request, self.fail_message)
        else:
            return super().dispatch(request, pk, *args, **kwargs)
        return redirect(to=self.fail_url, request=request)

class LoginRequiredWithMessageMixin(LoginRequiredMixin):
    no_auth_message = ""

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.no_auth_message)
            return super().handle_no_permission()
        return super().dispatch(request, *args, **kwargs)