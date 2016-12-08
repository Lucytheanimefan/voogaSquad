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

function setLogoutClick() {
    $(".glyphicon-off").click(function() {
        console.log("glyphicon-off clicked");
        logout();
    });
}

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


function populateDataToDashboard() {
    console.log("populateDataToDashboard called")
    $.ajax({
        type: 'GET',
        url: '/getgamescores',
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(response) {
            console.log("Success populateDataToDashboard");
            console.log(response);
            var data = response["result"];
            var newdata = eval("(" + data + ")");
            createLineChart("blah",newdata["gold"])

        }
    });
}

/**
 * [createLineChart description]
 * @param  {[type]} divElementID [description]
 * @param  {[type]} data         first element should be string description (would go in the legend/key)
 * @param  {[type]} dates        [description]
 * @return {[type]}              [description]
 */
function createLineChart(divElementID, data, dates) {
    var chart = c3.generate({
        bindto: "#" + divElementID,
        data: {
            columns: [
                data
            ]
        },
        axis: {
            x: {
                type: 'category',
                categories: dates
            }
        }
    });

    return chart;
}
