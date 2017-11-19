(function() {
    'use strict';
    angular.module('app').controller('UserCtrl', function($scope, $window,  $state, userService) {

    var vm = this;

    vm.tab = 1;
    vm.pass = null;
    vm.user = null;

    vm.empresa = {
        type: 2
    };
    vm.advogado = {
        type: 1
    };

    vm.registerUser = function(){
        if(vm.tab === 1){
            userService.saveUser(vm.advogado)
                .then(function(response){
                   if(response.status === 200){
                       $window.location.href = '/advogado';
                   }
                })
        }else{
            userService.saveUser(vm.empresa)
                .then(function(response){
                    if(response.status === 200){
                        $window.location.href = '/empresa';
                    }
                })
        }

    }

    });
})();