(function() {
    'use strict';
    angular.module('app').factory('userService', function($http) {
        return {
            getGroups: function(params) {
                 return $http.get('/api/grupos/list_grupos/', {
                    params : params
                });
            },
            authUser: function(params, user, pass) {
                 return $http.post('/api/auth/', {headers:{'Authorization': 'Token ' + window.btoa(user + ':' + pass)}});
            },
            saveUser: function(params) {
                 return $http.post('/api/empresa/',
                    params
                );
            },
            userLogin: function(params) {
                 return $http.get('/login/');
            }
        }
    });

    angular.module('app').factory('ordemService', function($http) {
        return {
            getOrdens: function() {
                 return $http.get('/api/ordem/');
            },
            saveOrdem: function(params) {
                 return $http.post('/api/ordem/', params);
            },
            getOrdem: function(id) {
                return $http.get('/api/ordem/' + id);
            },
            setPreco: function(params) {
                return $http.post('/api/preco/', params);
            },
            getOrdemPrecos: function(params) {
                return $http.get('/api/preco/list_precos/', {params});
            },
            delegaOrdem: function(params) {
                return $http.post('/api/ordem/delegate_ordem/', params);
            },
            ordensEnviadas: function() {
                return $http.get('/api/preco/ordens_advogado/');
            }

        }
    });

})();