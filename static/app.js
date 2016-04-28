angular.module('app', ['ngMaterial', 'ngRoute'])
.controller('ContentCtrl', ['$scope', 'TableService', '$route', function($scope, TableService, $route) {
    // $scope.tables

    $scope.myfunction = function(lulz) {
        // test
    };
    TableService.fetchTables().then(function successCallback(response) {
        $scope.tables = TableService.getTables();
        $route.reload();
    });

}])
.factory('TableService', ['$http', function ($http) {
    var tables = [];
    return {
        fetchTables: function () {
            return $http.get("/tables/").success(function (data) {
                tables = data['results'];
            });
        },
        getTables: function () {
            return tables;
        }
    }
}]);
