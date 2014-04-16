angular.module("ConAudioApp.Auth", [
    "ConAudioApp.Common",
]).controller('LoginController', function($rootScope, $scope, $state, $http, localStorageService){
    if ((typeof $rootScope.conaudioAuthToken === 'string') && ($rootScope.conaudioAuthToken.length > 0)) {
        $rootScope.conaudioAuthToken = localStorageService.get("token");
        $state.go('index');
        return;
    }
    $scope.authenticate = function(){
        $rootScope.conaudioAuthToken = $scope.token;
        localStorageService.add("token", $scope.token);
        $state.go('index');
    };
});
