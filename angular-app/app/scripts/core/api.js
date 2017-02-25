(function () {

    /**
     * myApi is the only way to connect to the API
     * make the CRUD, and return what is returns the API
     */

    'use strict';

    angular.module('myApp')
        .factory('myApi', myApi);

    function myApi($http, myConfig) {
        return {
            getItems: getItems,
            getItem: getItem
        };

        function getItems() {
            var endpoint = myConfig.API_ROOT + '/items';
            var p = $http.get(endpoint);

            p = p.then(
                function (response) {
                    return response.data;
                }
            );

            return p;
        }

        function getItem(itemId) {
            var endpoint = myConfig.API_ROOT + '/item';
            var params = {
                itemId: itemId
            };
            var p = $http.get(endpoint, {params: params});

            p = p.then(
                function (response) {
                    return response.data;
                }
            );

            return p;
        }
    }
}());