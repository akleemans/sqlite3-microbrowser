angular.module('app', ['ngMaterial'])
.controller('ContentCtrl', ['$scope', 'TableService', function($scope, TabService) {
    // $scope.tables

    $scope.myfunction = function(lulz) {
        // test
    };
    TableService.fetchTab().then(function successCallback(response) {
        $scope.tables = TabService.getTabs();
        $route.reload();
    });

}])
.factory('TableService', ['$http', function ($http) {
    var tables = [];
    return {
        fetchTables: function () {
            return $http.get("/tables/").success(function (data) {
                tables = data;
            });
        },
        getTables: function () {
            return tables;
        }
    }
}]);
