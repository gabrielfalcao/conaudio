angular.module("ConAudioApp.Common", [
]).directive('navbar', function(localStorageService, $rootScope, $state) {
    return {
        restrict: 'E',
        templateUrl: "{{ angular_template('navbar.html') }}",
        link: function (scope, element, attrs) {
            scope.login = function(){
                $state.go('login');
            };
            scope.logout = function(){
                localStorageService.clearAll();
                $rootScope.conaudioAuthToken = null;
                $state.go('login');
            };
        }
    }
});
