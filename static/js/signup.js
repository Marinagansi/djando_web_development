const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container=document.querySelector(".container");


const user=document.getElementById('usertxt')
const password=document.getElementById('passwordtxt')
const form1=document.getElementById('form1') 
const errorElement=document.getElementById('error1')

const user1=document.getElementById('nametxt')
const password1=document.getElementById('passtxt')
const email=document.getElementById('emailtxt')
const form2=document.getElementById('form2') 
const errorElement1=document.getElementById('error2')


form1.addEventListener('submit', (e) => {
        
    let messages = []
    if(user.value==''){
        messages.push('Email is required')
    }

 
    if(password.value.length <=6){
        messages.push('Invalid password')
    }
 
    if (password.value.length >=20){
        messages.push("Less than 20 character")
    }
    if(messages.length > 0) {
     e.preventDefault()
     errorElement.innerText= messages.join(' / ')
    }
   
         
   
 })

 form2.addEventListener('submit', (e) => {
        
    let messages1 = []
    
    if(user1.value=='' || email.value=='' || password1.value==""){
        messages1.push("All data required")
    }
    if(user1.value=='' && email.value!='' && password1.value!="" ){
        messages1.push('Username is required')
    }
    if(email.value==''  && password1.value!="" && user1.value!='' ){
        messages1.push('Email is required')
    }

    if(  email.value!='' && password1.value.length <=6 && user1.value!=''){
        messages1.push(' Password required more than 6 char required')
    }
 
    if (password1.value.length >=20){
        messages1.push(" password required Less than 20 character")
    }
    if(messages1.length > 0) {
     e.preventDefault()
     errorElement1.innerText= messages1.join(' / ')
    }
   
         
   
 })


sign_up_btn.addEventListener('click',()=>{
container.classList.add("sign-up-mode");
});
sign_in_btn.addEventListener('click',()=>{
    container.classList.remove("sign-up-mode");
    });


    
