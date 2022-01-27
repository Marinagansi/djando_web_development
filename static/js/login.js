var name1=document.forms['form']['customer_name'];
var pass=document.forms['form']['customer_password'];


var error1=document.getElementById('name_message');
var error2=document.getElementById('password_message');


function validated(){
 if(name1.value.length <2){
        
        error1.style.display="block";
        name1.focus();
        return false;
    }

    if(pass.value.length <2){
       
        error2.style.display="block";
        pass.focus();
        return false;
    }
}