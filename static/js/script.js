function login(username, password) {
    $.ajax({
        type: 'POST',
        url: '/login',
        data: JSON.stringify({ "username": username, "password": password }),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        complete: function() {
            console.log(this.url);
        },
        success: function(response) {
            console.log('in ajax login user');
            console.log(response);
            alert(response);
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
            console.log(this.url);
            console.log(data);
        },
        success: function(response) {
            console.log('in ajax create user');
            console.log(response);
            alert(response);

        }
    });
}
