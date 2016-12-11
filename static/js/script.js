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

function getAllGameTimes() {
    console.log("getAllGameTimes called");
    $.ajax({
        type: 'GET',
        url: '/getgametimes',
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(response) {
            console.log("Success get game times");
            var data = response["result"];
            var newdata = eval("(" + data + ")");
            console.log(newdata);
            for (var i = 0; i < newdata["time"].length; i++) {
                console.log("Iterate through newdata['time']");
                gameTime=newdata["time"][i].toString();
                console.log(gameTime);
                populateDataToDashboard(gameTime)
            }
        }
    });
}



function populateDataToDashboard(gameTime) {
    console.log("populateDataToDashboard called")
    $.ajax({
        type: 'POST',
        url: '/get_game_for_time',
        data: JSON.stringify({ "game_time": gameTime}),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(response) {
            console.log("Success populateDataToDashboard");
            console.log(response);
            var data = response;
            console.log(data);
            //var newdata = eval("(" + data + ")");
            //console.log(newdata);
            createGoldGraph("goldgraph", data);
            createLifeGraph("lifegraph", data);
        }
    });
}

function createGoldGraph(divElementID, newdata) {
    var dat = ["Gold"];
    var time = [];
    for (var i = 0; i < newdata["gold"].length; i++) {
        dat.push(parseInt(newdata["gold"][i][0]));
        time.push(newdata["gold"][i][1]);
    }
    createLineChart(divElementID, dat, time);
}

function createLifeGraph(divElementID, newdata) {
    var dat = ["Lives"];
    var time = [];
    for (var i = 0; i < newdata["lives"].length; i++) {
        dat.push(parseInt(newdata["lives"][i][0]));
        time.push(newdata["lives"][i][1]);
    }
    createLineChart(divElementID, dat, time);
}


/**
 * [createLineChart description]
 * @param  {[type]} divElementID [description]
 * @param  {[type]} data         first element should be string description (would go in the legend/key)
 * @param  {[type]} dates        [description]
 * @return {[type]}              [description]
 */
function createLineChart(divElementID, values, times) {
    console.log($("#" + divElementID));
    var chart = c3.generate({
        bindto: "#" + divElementID,
        data: {
            columns: [
                values
            ],
            type: 'bar'
        },
        axis: {
            x: {
                type: 'category',
                categories: times
            }
        }
    });

    return chart;
}
