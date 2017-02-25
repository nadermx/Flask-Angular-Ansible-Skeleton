(function () {

    'use strict';

    angular.module('myApp')
        .controller('homeCtrl', homeCtrl);

    function homeCtrl(myUtils) {
        var vm = this;
        vm.title = 'Home Page';
        vm.subtitle = myUtils.getTrustedHtml('This is a subtitle'); // testing myUtils functionality
    }

}());