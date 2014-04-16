angular.module("ConAudioApp.Index", [
    "ConAudioApp.Common",
]).controller('IndexController', function($rootScope, $scope, $state, $http){
    $rootScope.isAuthenticated();


});
