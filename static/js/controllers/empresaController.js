(function() {
 'use strict';
 angular.module('app').controller('EmpresaCtrl', function($scope, $stateParams, $http, $state, ordemService) {

    var vm = this;
    vm.ordem = {};

    if($stateParams.id){
        ordemService.getOrdemPrecos({id: $stateParams.id})
            .then(function(response){
                vm.ordem = response.data;
            });
    }

    ordemService.getOrdens()
        .then(function(response){
            vm.ordens = response.data;
        });

    vm.createOrder = function(){
        ordemService.saveOrdem(vm.ordem)
            .then(function(response){
                $state.transitionTo('ordens');
            });
    }

    vm.delegaOrdem = function(id){
        ordemService.delegaOrdem({id: vm.ordem.id, advogado: id})
            .then(function(response){

            });
    }

 });
})();