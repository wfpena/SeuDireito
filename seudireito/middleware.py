# -*- coding: utf-8 -*-

import re
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

from .settings import LOGIN_NOT_REQUIRED


class LoginRequiredMiddleware(MiddlewareMixin):

    def __init__(self, get_response=None, *args, **kwargs):
        self.exceptions = tuple(re.compile(url) for url in LOGIN_NOT_REQUIRED)
        self.get_response = get_response

        return super(LoginRequiredMiddleware, self).__init__(
            get_response, *args, **kwargs)

    def process_view(self, request, view_func, view_args, view_kwargs):
        # if request.user.is_authenticated():
        #     if request.user.user_type != 'EMP':
        #         return redirect('advogadoview')
        #
        # if request.user.is_authenticated():
        #     if request.user.user_type != 'ADV':
        #         return redirect('empresaview')

        # Caso o user ja esteja logado:
        if request.user.is_authenticated():
            for url in self.exceptions:
                if url.match(request.path):
                    if request.user.user_type == 'EMP':
                        return redirect('empresaview')
                    if request.user.user_type == 'ADV':
                        return redirect('advogadoview')
            return None


        for url in self.exceptions:
            if url.match(request.path):
                return None

        return redirect('loginview')
