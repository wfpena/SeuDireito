(function() {
 'use strict';
 angular.module('app').controller('AdvogadoCtrl', function($scope, $state, $http, $stateParams, ordemService) {

    var vm = this;

    if($stateParams.id){
        ordemService.getOrdem($stateParams.id)
            .then(function (response){
                vm.ordem = response.data;
            })
    }

    ordemService.getOrdens()
        .then(function(response){
            vm.ordens = response.data;
        });

    ordemService.ordensEnviadas()
        .then(function(response){
            vm.ordensEnviadas = response.data;
        });

    vm.setPrecoOrdem = function(){
        ordemService.setPreco({ordem: vm.ordem.id, preco: vm.preco})
            .then(function (response){
                $state.transitionTo('ordensAdvogado');
            })
    }

 });
})();