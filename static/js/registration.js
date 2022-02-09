// Getting inputData from user input
var inputData=document.getElementsByTagName("input");
// Getting form elements
var Form = document.getElementsByTagName("form")[0];
// Getting message class
var message = document.getElementsByClassName("message");

//function for form validation
function validate(){
  var fullname=inputData['customer_name'].value;
  var email=inputData['customer_email'].value;
  var address=inputData['customer_address'].value;
  var password=inputData['customer_password'].value;
  var confirm_password=inputData['confirm_password'].value;

// conditions for register form validation and message display

// fullname validation
	if(fullname===""){
	  message[0].innerText="**Full Name Required";
	}else{
	  message[0].innerText="";
  }

// Email validation
  if(email===""){
     message[1].innerText="**Email Address Required";
  }else{
     message[1].innerText="";
  }
// Address validation
  if(address===""){
     message[2].innerText="**Address Required";
  }else{
     message[2].innerText="";
  }

// Password validation
  if(password===""){
    message[3].innerText="**Password Required";
  }
  else if(password.length != "8"){
    message[3].innerText="**Password must be 8 digits";
  }else{
    message[3].innerText="";
  }


  if(fullname===""||email==="" ||address==="" || password===""){
	  return false;
	}
	return true;
  }