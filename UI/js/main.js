
//event listeners
function eventListeners() {
    const ui = new UI();

    // nav btn
    document.querySelector('.cf-nav_btn').addEventListener('click', function () {
        ui.showNav();
    })

    //video control 
    document.querySelector('.cf-video_switch').addEventListener('click', function(){
        ui.videoControls();  
    })

}

// constructor function
function UI(){  

}
//show nav
UI.prototype.showNav = function(){
    document.querySelector('.cf-nav').classList.toggle('cf-nav_show')
}

//play/pause video
UI.prototype.videoControls = function(){
    let btn = document.querySelector('.cf-video_switch_btn');
    if(!btn.classList.contains('cf-btn_slide')){
        btn.classList.add('cf-btn_slide')
        document.querySelector('.cf-video_item').pause()
        document.querySelector('.cf-header').style.background = "rgba(0,0,0,0.5)";
    }
    else{
        btn.classList.remove('cf-btn_slide')
        document.querySelector('.cf-video_item').play()
        document.querySelector('.cf-header').style.background = "";
    }
}

//calling event listeners
eventListeners();  