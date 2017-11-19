from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView, View

from seudireito.forms import UserLoginForm


class LoginView(View):
    form_class = UserLoginForm
    template_name = 'seudireito/login.html'

    def get(self, request):
        form = self.form_class(None)

        if request.user.is_authenticated():
            return redirect('ambienteview')
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST or None)
        if request.POST and form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = form.authenticate_user(
                username=username, password=password)
            if user:
                login(request, user)
                if user.user_type == 'EMP':
                    return redirect('empresaview')
                else:
                    return redirect('advogadoview')

        return render(request, self.template_name, {'form': form})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("loginview")


class IndexView(TemplateView):
    template_name = 'seudireito/index.html'


class CadastroView(TemplateView):
    template_name = 'seudireito/cadastro.html'


class EmpresaView(TemplateView):
    template_name = 'seudireito/empresa.html'

    def get(self, request, *args, **kwargs):
        if request.user.user_type == "ADV":
            return redirect('advogadoview')
        else:
            return render(request, self.template_name)


class AdvogadoView(TemplateView):
    template_name = 'seudireito/advogado.html'

    def get(self, request, *args, **kwargs):
        if request.user.user_type == "EMP":
            return redirect('empresaview')
        else:
            return render(request, self.template_name)
