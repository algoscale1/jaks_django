$('.input-file').change(function(e){
    $('.input-text').val(e.target.files[0].name);
    $('.file-selector').submit();
    $('.input-text').val('');
});

$('.user-img').click(function(){
    if($(this).hasClass('show')){
        $(this).removeClass('show');
        $(this).next('.user-options').hide();
    } else {
        $(this).addClass('show');
        $(this).next('.user-options').show();
    }
});

$.validator.messages.required = '';

var myApp = angular.module('myApp',[]);

//myApp.config(function($interpolateProvider) {
//    $interpolateProvider.startSymbol('//').endSymbol('//');
//});

//myApp.controller('baseController',['$scope',function($scope){
//    $scope.title = "testing";
//}]);

//myApp.config(function($stateProvider, $urlRouterProvider,$locationProvider) {
//    $locationProvider.html5Mode(true);
//    $urlRouterProvider.otherwise('/index');
//    $stateProvider
//        .state('index',{
//            url : '/index',
//            templateUrl : '/templates/home.html'
//        })
//        .state('login',{
//            url : '/login',
//            templateUrl : '/templates/login.html'
//        })
//        .state('signup',{
//            url : '/signup',
//            templateUrl : '/templates/signup.html'
//        })
//});