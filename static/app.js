angular.module('app', ['ngMaterial', 'ngRoute'])
.controller('ContentCtrl', ['$scope', 'TableService', '$route', function($scope, TableService, $route) {
    TableService.fetchOverview().then(function successCallback(response) {
        $scope.overview = TableService.getOverview();
        $route.reload();
    });
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
        },
        fetchOverview: function () {
            return $http.get("/overview/").success(function (data) {
                overview = data['results'];
            });
        },
        getOverview: function () {
            return overview;
        }

    }
}]);
