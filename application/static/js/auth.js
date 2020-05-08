document.addEventListener('DOMContentLoaded', () => {


    var valid_username = false;
    var valid_email = false;
    var valid_password = false;

    // hide error messages and disable register button
    document.querySelector('#usernameTaken').style.visibility = "hidden";
    document.querySelector('#emailTaken').style.visibility = "hidden";
    document.querySelector('#passwordError').style.visibility = "hidden"
    document.querySelector('#register').disabled = false;


    // Connect to websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
    socket.on('connect', () => {
        document.querySelector('#username').onblur = () => {
            const username = document.querySelector('#username').value;
            socket.emit('check username', {'username': username});
        };
    });
    socket.on('connect', () => {
        document.querySelector('#email').onblur = () => {
            const email = document.querySelector('#email').value;
            socket.emit('check email', {'email': email});
        };
    });

    socket.on('valid username', data => {
        if(data===false){
            document.querySelector('#usernameTaken').style.visibility = "visible";
        } else {
            document.querySelector('#usernameTaken').style.visibility = "hidden";
            valid_username = true;
            if (valid_username && valid_email && valid_password) {
                document.querySelector('#register').disabled = false;
            }
        }
    });

    socket.on('valid email', data => {
        if(data===false){
            document.querySelector('#emailTaken').style.visibility = "visible";
        } else {
            document.querySelector('#emailTaken').style.visibility = "hidden";
            valid_email = true;
            if (valid_username && valid_email && valid_password) {
                document.querySelector('#register').disabled = false;
            }
        }
    });

    document.querySelector('#confirmPassword').onblur = () => {
        let password = document.querySelector('#password').value;
        let confPassword = document.querySelector('#confirmPassword').value;
        if(password !== confPassword) {
            valid_password = false;
            document.querySelector('#passwordError').style.visibility = "visible"
        } else {
            document.querySelector('#passwordError').style.visibility = "hidden"
            valid_password = true;
            if (valid_username && valid_email && valid_password) {
                document.querySelector('#register').disabled = false;
            }
        }
    };

});
