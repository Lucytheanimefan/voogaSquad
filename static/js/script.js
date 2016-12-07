function login(username, password) {
    $.ajax({
        type: 'POST',
        url: '/login',
        data: JSON.stringify({ "username": username, "password": password }),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        complete: function() {
            console.log(this.url);
            window.location.href = "/home";
        },
        success: function(response) {
            console.log('in ajax login user');
            console.log(response);
            
        }
    });

}

$(".glyphicon-off").click(function(){
    logout();
});

function logout() {
    $.ajax({
        type: 'POST',
        url: '/logout',
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        complete: function() {
            console.log(this.url);
            window.location.href = "/";
        },
        success: function(response) {
            console.log('in ajax login user');
            console.log(response);
            
        }
    });

}

function createUser(username, password) {
    console.log("Username: " + username);
    console.log("password: " + password);
    $.ajax({
        type: 'POST',
        url: '/createaccount',
        data: JSON.stringify({ "username": username, "password": password }),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        complete: function() {
            //window.location.href = "/home";
        },
        success: function(response) {
            console.log('in ajax create user');
            console.log(response);
            alert(response);

        }
    });
}
