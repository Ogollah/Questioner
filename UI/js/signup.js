//event listeners
function eventListeners() {
    const ui = new UI();
    // nav btn
    document.querySelector('.cf-nav_btn').addEventListener('click', function () {
        ui.showNav();
    })

    //submit the signup form
    document.querySelector('.cf-signup_form').addEventListener('submit', function(event){
        event.preventDefault();
        const username = document.querySelector('.cf-input_username').value;
        const password = document.querySelector('.cf-input_password').value;
        const email = document.querySelector('.cf-input_email').value;

        let value = ui.checkEmpty(username, password, email);
        if(value){
            let user = new User(username, password, email);
            console.log(user);
            ui.showFeedback('You have successfully registered', 'success')
            ui.clearFields()
        }
        else{
            ui.showFeedback('Kindly fill all the fields', 'error')
        }
    })
}

// constructor function
function UI(){  

}
//show nav
UI.prototype.showNav = function(){
    document.querySelector('.cf-nav').classList.toggle('cf-nav_show')
}
//check empty values
UI.prototype.checkEmpty = function(username, password, email){
    let result;
    if(username ==='' || password ==='' || email ===''){
        result = false;
    }  
    else{
        result = true; 
    }
    return result;
}

//show feedback
UI.prototype.showFeedback = function(text, type){
    const feedback = document.querySelector('.cf-signup_form_feedback');
    if(type === 'success'){ 
        feedback.classList.add('success');
        feedback.innerText = text; 
        this.removeAlert('success');

    }
    else if(type === 'error'){
        feedback.classList.add('error');
        feedback.innerText = text; 
        this.removeAlert('error');
    }
}

//remove alert
UI.prototype.removeAlert = function(type){
    setTimeout(function(){
        document.querySelector('.cf-signup_form_feedback').classList.remove(type)
    }, 3000)
}

//clear fields
UI.prototype.clearFields = function(){
    document.querySelector('.cf-input_username').value = '';
    document.querySelector('.cf-input_password').value = '';
    document.querySelector('.cf-input_email').value = '';
} 

// User
function User(username, password, email){
    this.username = username;
    this.password = password;
    this.email = email
}
// call event listener
eventListeners();  