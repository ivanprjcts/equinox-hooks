app.controller('ApplicationDetailCtrl', ['$scope', '$sce', 'api', function ($scope, $sce, api)
{
    $scope.application = {};

    var reloadUrlApplication = function() {
        var pathArray = window.location.pathname.split( '/' );
        var id = pathArray[pathArray.length-2];

        api.getApplication(id).then(function(response) {
            $scope.application = response.data;
        });
    };

    $scope.initDetail = function() {
        reloadUrlApplication();
    };


    $scope.removeApplication = function(id) {
        api.deleteApplication(id).then(function(response) {
                reloadApplications();
            });
    };

    $scope.saveApplication = function(id, name, appId, secret) {
        api.updateApplication(id, name, appId, secret)
            .then(function(response) {
                reloadApplications();
        });
    };

    $scope.createApplication = function(name, appId, secret) {

        api.createApplication(name, appId, secret).then(function(response) {
            $scope.show_new_application = false;
            reloadApplications();
        });


    };

}]);