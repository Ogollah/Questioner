//event listeners
function eventListeners() {
    const ui = new UI();
    // nav btn
    document.querySelector('.cf-nav_btn').addEventListener('click', function () {
        ui.showNav();
    })

    // comment box
    document.querySelector('.cf-display_btn').addEventListener('click', function(){
        ui.showComment();
    })

    document.querySelector('.cf-display_btn1').addEventListener('click', function(){
        ui.showComment();
    })

    document.querySelector('.cf-display_btn2').addEventListener('click', function(){
        ui.showComment();
    })

    document.querySelector('.cf-display_btn3').addEventListener('click', function(){
        ui.showComment();
    })

    // submite comment
    document.querySelector('.cf-btn_submit').addEventListener('submit', function(event){
        event.preventDefault();
        ui.hideComment();
    })

    document.querySelector('.cf-btn_reject').addEventListener('submit', function(event){
        event.preventDefault();
        ui.hideComment();
    })
}

// constructor function
function UI(){  

}

//show nav
UI.prototype.showNav = function(){
    document.querySelector('.cf-nav').classList.toggle('cf-nav_show')
}

UI.prototype.showComment = function(){
    document.querySelector('.cf-comment_form').style.display = 'block';
    
}

UI.prototype.hideComment = function(){
    document.querySelector('.cf-comment_form').style.display = 'none';
    console.log("hey there");
}

// call event listener
eventListeners();  
