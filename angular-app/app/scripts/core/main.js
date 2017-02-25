(function () {

    /**
     * myMain, is the only way to connect to myApi
     * transform the data from myApi to something readble to the application
     */

    'use strict';

    angular.module('myApp')
        .factory('myMain', myMain);

    function myMain(myApi, myModel) {
        return {
            getProducts: getProducts,
            getProduct: getProduct
        };

        function getProducts() {
            var products = myModel.getProducts();

            if (products.length) {
                return products;
            }

            var p = myApi.getItems();

            p = p.then(
                function (results) {
                    ytModel.populateProducts(results.products);
                    return myModel.getProducts();
                }
            );

            return p;
        }

        function getProduct(productId) {
            var p = myApi.getItem(productId);

            p = p.then(
                function (result) {
                    return result.product;
                }
            );

            return p;
        }
    }

}());