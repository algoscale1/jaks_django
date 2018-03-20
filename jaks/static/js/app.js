$('.input-file').click(function(e){
    e.preventDefault();
    alert('Please Login Before File Select');
    window.location = "/api/subject/login";
});

$('#myModal').blur(function(e){
    e.preventDefault();
});

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
                console.log(obj.id);
                $('.generated-id').val(obj.id);
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

$('.package-form').submit(function(e){
    var jsonObj = JSON.parse(JSON.stringify($(this).serializeArray()));
    var str = jsonObj[0].name+"="+jsonObj[0].value+"&"+jsonObj[1].name+"="+jsonObj[1].value;
    $.ajax({
        type: 'POST',
        url: '/api/save_package',
        data: str,
        success: function (data) {
            var obj = JSON.parse(data);
            window.location = "/api/api_generator?key="+obj.key
        },
    });
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
