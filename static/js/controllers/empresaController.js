(function() {
 'use strict';
 angular.module('app').controller('EmpresaCtrl', function($scope, $stateParams, $filter, $http, $state, ordemService) {
    var vm = this;
    vm.ordem = {};
    vm.ordemDelegada = false;

    if($stateParams.id){
        ordemService.getOrdemPrecos({id: $stateParams.id})
            .then(function(response){
                vm.ordem = response.data;
                if(vm.ordem.status !== 'Criada'){
                    vm.ordemDelegada = true;
                    vm.preco = $filter('filter')(vm.ordem.preco_advogado, {delegada: true})[0];
                }
            });
    }

    vm.finalizarOrdem = function(id){
        ordemService.finalizaOrdem(id).then(function (response){
            ordemService.getOrdem(response.data.id).then(function (response){
                vm.ordem = response.data;
            })
        })
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

    vm.delegaOrdem = function(id, nome){
        ordemService.delegaOrdem({id: vm.ordem.id, advogado: id})
            .then(function(response){
                vm.ordemDelegada = true;
            });
    }
 });
})();