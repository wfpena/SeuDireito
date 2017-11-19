(function() {
 'use strict';
 angular.module('app',[
	'ngCookies',
	'ui.router'
 ], function($interpolateProvider){
	// Contorna prroblema de interpolação da renderização de template do django
	$interpolateProvider.startSymbol('{[{');
	$interpolateProvider.endSymbol('}]}');
 })
 .run( function run($http, $cookies ){
	// Evita problemas relacionados ao CSRF
	$http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
 });

 angular.module('app').config(['$httpProvider', '$stateProvider', '$urlRouterProvider', function($httpProvider, $stateProvider, $urlRouterProvider){

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

     $urlRouterProvider.otherwise("/");
     $stateProvider.state('cadastro', {
        url:'/cadastro',
        templateUrl: '/seudireito/cadastro.html'
      })
      .state('empresa', {
        url:'/empresa',
        templateUrl: '/static/views/empresa.html'
      })
      .state('ordens', {
        url:'/ordens',
        controller: 'EmpresaCtrl as vm',
        templateUrl: '/static/views/empresa/ordens.html'
      })
      .state('criarOrdem', {
        url:'/criar',
        controller: 'EmpresaCtrl as vm',
        templateUrl: '/static/views/empresa/criarOrdem.html'
      })
      .state('ordemDefinir', {
        url:'/ordemDefinir/:id',
        controller: 'EmpresaCtrl as vm',
        templateUrl: '/static/views/empresa/precos.html'
      })
      .state('advogado', {
        url:'/advogado',
        templateUrl: '/seudireito/advogado.html'
      })
       .state('ordensAdvogado', {
        url:'/ordensAdvogado',
        controller: 'AdvogadoCtrl as vm',
        templateUrl: '/static/views/advogado/ordens.html'
      })
       .state('ordemPreco', {
        url:'/ordemPreco/:id',
        controller: 'AdvogadoCtrl as vm',
        templateUrl: '/static/views/advogado/criarOrdem.html'
      })
      .state('ordensEnviadas', {
        url:'/ordensEnviadas',
        controller: 'AdvogadoCtrl as vm',
        templateUrl: '/static/views/advogado/ordensEnviadas.html'
      })
      .state('ordensConfirmadas', {
        url:'/ordensConfirmadas',
        controller: 'AdvogadoCtrl as vm',
        templateUrl: '/static/views/advogado/ordensConfirmadas.html'
      });
 }])
})();
