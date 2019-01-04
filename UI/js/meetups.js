//event listeners
function eventListeners() {
    const ui = new UI();
    // nav btn
    document.querySelector('.cf-nav_btn').addEventListener('click', function () {
        ui.showNav();
    })
}

// constructor function
function UI(){  

}

//show nav
UI.prototype.showNav = function(){
    document.querySelector('.cf-nav').classList.toggle('cf-nav_show')
}
// call event listener
eventListeners();  
