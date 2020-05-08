document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#sidenav-burger').onclick=() => {
        if (document.querySelector('#sideNav').classList.contains("closeNav")) {
            document.querySelector('#sideNav').classList.remove("closeNav");
        };
        document.querySelector('#sideNav').classList.add("openNav");
        document.querySelector('#sidenav-burger').style.visibility = "hidden";
    };

    document.querySelector('#main-container').onclick = () => {
        document.querySelector('#sideNav').classList.remove("openNav");
        document.querySelector('#sideNav').classList.add("closeNav");
        document.querySelector('#sidenav-burger').style.visibility = "visible";
    };

});
