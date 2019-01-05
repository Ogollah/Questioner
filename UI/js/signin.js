//event listeners
function eventListeners() {
    const ui = new UI();
    // nav btn
    document.querySelector('.cf-nav_btn').addEventListener('click', function () {
        ui.showNav();
    })

    // admin
    document.querySelector('.cf-signin_users').addEventListener('click', function(){
        ui.showAdmin();
    })

    // user
    document.querySelector('.cf-signin_admins').addEventListener('click', function(){
        ui.showUser();
    })

    // comment box
    document.querySelector('.cf-display_btn').addEventListener('click', function(){
        ui.showComment();
    })
}

// constructor function
function UI(){  

}

//show nav
UI.prototype.showNav = function(){
    document.querySelector('.cf-nav').classList.toggle('cf-nav_show')
}

// show admin
UI.prototype.showAdmin = function(){
    document.querySelector('.cf-signin_user').style.display = 'none';
    document.querySelector('.cf-signin_admin').style.display = 'block';
    console.log("hey");
}

// show user
UI.prototype.showUser = function(){
    document.querySelector('.cf-signin_user').style.display = 'block';
    document.querySelector('.cf-signin_admin').style.display = 'none';
}

UI.prototype.showComment = function(){
    document.querySelector('.cf-comment_form').style.display = 'inline';
    console.log("hey there");
}

// call event listener
eventListeners();  
