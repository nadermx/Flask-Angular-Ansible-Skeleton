(function () {
    
    'use strict';
    
    angular.module('myApp')
        .config(myRoutes);
    
    function myRoutes($stateProvider, $urlRouterProvider, $locationProvider) {
        $urlRouterProvider.otherwise('/');
        $locationProvider.html5Mode({
            enabled: false, // change to true to remove /!#/ from URL
            requireBase: false
        });

        $stateProvider
            .state('main', {
                abstract: true,
                templateUrl: 'scripts/views/main-template.html'
            })
            .state('main.Home', {
                url: '/',
                templateUrl: 'scripts/views/home/home.html',
                controller: 'homeCtrl',
                controllerAs: 'vm'
            });
    }
    
}());