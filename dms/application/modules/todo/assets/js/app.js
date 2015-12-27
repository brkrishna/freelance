/**
* Created with app.
* User: ramakrishna
* Date: 2014-11-10
* Time: 10:10 AM
* To change this template use Tools | Templates.
*/
var app = angular.module('SristiBio', ['ui.bootstrap']);

app.filter('startFrom', function() {
    return function(input, start) {
        if(input) {
            start = +start; //parse to int
            return input.slice(start);
        }
        return [];
    }
});

app.controller('TodoCtrl', function($scope, $http, $timeout){
    $http.get('http://mentor-stereo.codio.io:3000/app/public/index.php/admin/content/todo/get_json').success(function(data){
        $scope.list = data;
        $scope.currentPage = 1;
        $scope.entryLimit = 10;
        $scope.filteredItems = $scope.list.length;
        $scope.totalItems = $scope.list.length;
        console.log(data);
    });
    
    $scope.setPage = function(pageNo){
      $scope.currentPage = pageNo;  
    };
    
    $scope.filter = function() {
        $timeout(function() { 
            $scope.filteredItems = $scope.filtered.length;
        }, 10);
    };
    
    $scope.sort_by = function(predicate) {
        $scope.predicate = predicate;
        $scope.reverse = !$scope.reverse;
    };    
    
});