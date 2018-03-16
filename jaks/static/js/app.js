$('.input-file').change(function(e){
    $('.input-model').val(e.target.files[0].name);
    $('.file-selector').submit();
    $('.input-model').val('');
});

$('#myModal').blur(function(e){
    e.preventDefault();
})

$('.packages.disabled .package-btn a').click(function(e){
    e.preventDefault();
});

$('.signin-form').submit(function(e){
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/api/save_userdata',
        data: $('.signin-form').serialize(),
        success: function (data) {
            var obj = JSON.parse(data);
            if(obj.flag === true){
                $('#myModal').modal(
                    {
                        'backdrop': false,
                        'show': true,
                        'keyboard': false
                    }
                );
            } else if(obj.flag === false) {
                alert(obj.msg)
            }
        },
    });
});

//$('.signin-btn').click(function(){
//    var form = $('.signin-form');
//    if(form.valid()){
//        console.log('form valid btn');
//        $('#myModal').modal(
//            {
//                'backdrop': false,
//                'show': true,
//                'keyboard': false
//            }
//        );
//    } else {
//        console.log('form invalid btn')
//    }
//});

$.validator.messages.required = '';

var myApp = angular.module('myApp',[]);

//myApp.config(function($interpolateProvider) {
//    $interpolateProvider.startSymbol('//').endSymbol('//');
//});

//myApp.controller('baseController',['$scope',function($scope){
//    $scope.title = "testing";
//}]);
//
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
