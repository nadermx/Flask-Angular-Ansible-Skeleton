(function () {

    /**
     * myUtils, contains all logic that will be used in the app
     * this logic doesnt connect to myApi or myMain
     */

    'use strict';

    angular.module('myApp')
        .factory('myUtils', myUtils);

    function myUtils($sce) {
        return {
            scrollTop: scrollTop,
            getTrustedHtml: getTrustedHtml
        };
        
        function scrollTop() {
            angular.element("html, body").animate({ scrollTop: 0 }, 200);
        }

        function getTrustedHtml(html) {
            return $sce.trustAsHtml(html);
        }
    }

}());