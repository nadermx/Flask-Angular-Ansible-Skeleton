(function () {

    /**
     * myPersist will persist the data across the entire application session
     * This will be helpfull to work with user sessions
     */

    'use strict';

    angular.module('myApp')
        .factory('myPersist', myPersist);

    function myPersist() {
        var lc = window.localStorage;

        return {
            get: get,
            set: set,
            clear: clear
        };

        function get(index) {
            return lc[index];
        }

        function set(index, value) {
            lc[index] = value;
        }

        function clear() {
            lc.clear();
        }
    }
}());