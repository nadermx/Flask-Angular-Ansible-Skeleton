(function () {

    'use strict';

    var myConfig = {
        API_ROOT: 'http://my-api.domain'
    };

    angular.module('myApp')
        .constant('myConfig', myConfig);

}());