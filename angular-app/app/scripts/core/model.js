(function () {

    'use strict';

    angular.module('myApp')
        .factory('myModel', myModel);

    function myModel() {
        var products = [];

        return {
            populateProducts: populateProducts,
            getProducts: getProducts
        };

        function populateProducts(newProducts) {
            products.length = 0;

            for (var i= 0; i < newProducts.length; i ++) {
                products.push(newProducts[i]);
            }
        }

        function getProducts() {
            return products;
        }
    }

}());