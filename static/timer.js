function timer() {
    console.log("inside timer")
//    document.location.href = 'templates/Enter_Login.html'
    var time = document.getElementById("eEnd").value;
    // console.log(new Date(time))
    endTime = new Date(time);
    document.getElementById("election-mention").innerHTML = "Election ends at ",endTime;

    // console.log(new Date(time).getSeconds())
    setInterval(function() {
        var dSec = 60 - new Date().getSeconds();
        var dMin = endTime.getMinutes() - new Date().getMinutes()
        var dHour = endTime.getHours() - new Date().getHours()
        if (dSec <= 1 && dMin <= 0 && dHour <= 0) {
            console.log("Zero");
            document.getElementById("timer").innerHTML = "Expired";
            document.getElementById("results").removeAttribute("disabled")
            document.getElementById("login").setAttribute("disabled", "disabled");
        }
        // console.log(dSec);
        else if (dMin >= 0 && dHour >= 0) {
            console.log(dHour + " " + dMin + " " + dSec);
            document.getElementById("timer").innerHTML = (dHour + " " + dMin + " " + dSec);
            document.getElementById("login").removeAttribute("disabled")
        }
    }, 1000)

}
