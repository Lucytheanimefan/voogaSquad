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
                gameTime = newdata["time"][i].toString();
                console.log(gameTime);
                $(".games").append('<button class = "accordion">Game: ' + gameTime + '</button>' +
                    '<div class="panel">' +
                    '<p>' +
                    '<div class="x_content">' +
                    '<div class="demo-container" style="height:250px">' +
                    '<div id="goldgraph' + i + '" style="width: 100%; height:250px;"></div>' +
                    '</div></div>' +
                    '<div class="x_content">' +
                    '<div class="demo-container" style="height:250px">' +
                    '<div id="lifegraph' + i + '" style="width: 100%; height:250px;"></div>' +
                    '</div></div></p></div>')
                populateDataToDashboard(gameTime, i);
            }

            dropDownInteractivity();
        }
    });
}

function getActualScores() {
    console.log("get actual scores called");
    $.ajax({
        type: 'GET',
        url: '/get_actual_score',
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(response) {
            console.log("Success get game times");
            var data = response["result"];
            var newdata = eval("(" + data + ")");
            console.log(newdata);
            var timeArr = [];
            var scores = ["Scores"];
            for (var i = 0; i < newdata["data"].length; i++) {
                timeArr.push(newdata["data"][i][0]);
                scores.push(newdata["data"][i][1]);
            }

            createLineChart("topScores", scores,timeArr);
        }
    });
}



function dropDownInteractivity() {

    var acc = document.getElementsByClassName("accordion");
    var i;

    for (i = 0; i < acc.length; i++) {
        acc[i].onclick = function() {
            console.log("Accordion clicked");
            this.classList.toggle("active");
            this.nextElementSibling.classList.toggle("show");
        }
    }
}



function initDropDown() {
    console.log($(".header"));
    $(".header").click(function() {

        console.log("header clicked");
        $header = $(this);
        //getting the next element
        $content = $header.next();
        //open up the content needed - toggle the slide- if visible, slide up, if not slidedown.
        $content.slideToggle(500, function() {
            //execute this after slideToggle is done
            //change text of header based on visibility of content div
            $header.text(function() {
                //change text based on condition
                return $content.is(":visible") ? "Collapse" : "Expand";
            });
        });

    });
}

function getNumGames(){
     $.ajax({
        type: 'GET',
        url: '/num_games',
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(response) {
            console.log("Success get num games");
            console.log(response);
            $("#numPlays").html(response);
            
        }
    });

}

function getEndScores() {
    $.ajax({
        type: 'GET',
        url: '/get_end_scores',
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(response) {
            console.log("Success getEndScores");
            var data = response["result"];
            var newdata = eval("(" + data + ")");
            var dat = newdata["data"];
            console.log(dat);
            var topScores = findTopScores(dat);
            console.log(topScores);
            populateTopScores(topScores);
        }
    });
}

function findTopScores(dat) {
    var topGold = 0;
    var topGoldTime = "";
    var topLevel = 0;
    var topLevelTime = "";
    var topLives = 0;
    var topLivesTime = "";
    for (var i = 0; i < dat.length; i++) {
        if (parseInt(dat[i]["gold"]) >= topGold) {
            topGold = parseInt(dat[i]["gold"]);
            topGoldTime = dat[i]["timestamp"]
            console.log("topGoldTIme: " + topGoldTime)
        }
        if (parseInt(dat[i]["level"]) >= topLevel) {
            console.log("In leve lif statement");
            topLevel = parseInt(dat[i]["level"]);
            topLevelTime = dat[i]["timestamp"]
            console.log("topLevelTime: " + topLevelTime);
        }
        if (parseFloat(dat[i]["lives"]) >= topLives) {
            console.log("in lives if statement");
            topLives = parseInt(dat[i]["lives"]);
            topLivesTime = dat[i]["timestamp"];
            console.log("topLivesTime: " + topLivesTime);
        }
        console.log("Looping in findTopScores");
    }

    var data = { "topGold": [topGold, topGoldTime], "topLevel": [topLevel, topLevelTime], "topLives": [topLives, topLivesTime] }

    return data;
}


function populateTopScores(scores) {
    $("#highestgold").html(scores['topGold'][0]);
    $("#highestlevel").html(scores['topLevel'][0]);
    $("#highestlives").html(scores['topLives'][0]);
    $("#goldtime").html(scores['topGold'][1]);
    $("#leveltime").html(scores['topLevel'][1]);
    $("#livestime").html(scores['topLives'][1]);
}

function populateDataToDashboard(gameTime, id_num) {
    console.log("populateDataToDashboard called")
    $.ajax({
        type: 'POST',
        url: '/get_game_for_time',
        data: JSON.stringify({ "game_time": gameTime }),
        contentType: 'application/json; charset=utf-8',
        dataType: 'json',
        success: function(response) {
            console.log("Success populateDataToDashboard");
            var data = response;

            createGoldGraph("goldgraph" + id_num, data);
            createLifeGraph("lifegraph" + id_num, data);
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
    createBarChart(divElementID, dat, time);
}

function createLifeGraph(divElementID, newdata) {
    var dat = ["Lives"];
    var time = [];
    for (var i = 0; i < newdata["lives"].length; i++) {
        dat.push(parseInt(newdata["lives"][i][0]));
        time.push(newdata["lives"][i][1]);
    }
    createBarChart(divElementID, dat, time);
}


/**
 * [createBarChart description]
 * @param  {[type]} divElementID [description]
 * @param  {[type]} data         first element should be string description (would go in the legend/key)
 * @param  {[type]} dates        [description]
 * @return {[type]}              [description]
 */
function createBarChart(divElementID, values, times) {
    console.log($("#" + divElementID));
    var chart = c3.generate({
        bindto: "#" + divElementID,
        data: {
            columns: [
                values
            ],
            type: 'bar',
            types: {
                gold: 'line',
                lives: 'line'
            },
        },
        axis: {
            x: {
                type: 'category',
                categories: times,
                show:false
            }
        }
    });

    return chart;
}


//lol

function createLineChart(divElementID, values, times) {
    console.log($("#" + divElementID));
    var chart = c3.generate({
        bindto: "#" + divElementID,
        data: {
            columns: [
                values
            ],
            types: {
                gold: 'line',
                lives: 'line'
            },
        },
        axis: {
            x: {
                type: 'category',
                categories: times,
                show:false
            }
        }
    });

    return chart;
}