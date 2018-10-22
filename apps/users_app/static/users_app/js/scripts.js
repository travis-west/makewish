//scripts.js

// display/hide password in registration form
function displayRegPassword() {
    var x = document.getElementById("reg-password");
    var y = document.getElementById("reg-password2")

    if (x.type === "password") {
            x.type = "text";
        } else {
            x.type = "password";
        }

    if (y.type === "password") {
            y.type = "text";
        } else {
            y.type = "password";
        }
}

function displayLoginPassword() {
    var z = document.getElementById("login-password");

    if (z.type === "password") {
            z.type = "text";
        } else {
            z.type = "password";
        }
}