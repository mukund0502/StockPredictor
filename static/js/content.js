var profile = document.getElementById("profilebtn");
var profilebox = document.getElementsByClassName("profile")
var close = document.getElementById("close")
var edit = document.getElementsByClassName("edit")
var fname = document.getElementById("fname")
var lname = document.getElementById('lname')
var email = document.getElementById("email");
var uname = document.getElementById("uname");
var password = document.getElementById("password");
var buttons = document.getElementsByClassName("buttons");



edit[0].addEventListener('click', ()=>{
    if(edit[0].defaultValue =="Edit info"){
        const fna = fname.innerHTML;
        const lna = lname.innerHTML;
        const ema = email.innerHTML;
        const una = uname.innerHTML;
        const cpass = password.innerHTML;

        fname.innerHTML = `<input type="text" name="cfname" id="cfname" size="10" class = "abc" value = "${fna}">`;
        lname.innerHTML = `<input type="text" name="clname" id="clname" size="10" class = "abc"  value = "${lna}">`;
        email.innerHTML = `<input type="email" name="cemail" id="cemail" class = "abc"  value = "${ema}">`;
        uname.innerHTML = `<input type="text" name="cuname" id="cuname" class = "abc"  value = "${una}">`;
        password.innerHTML = `<input type="password" name="cpassword" class = "abc"  id="cpassword" value = "${cpass}">`;


        buttons[0].innerHTML = `<input type="submit" value="save changes" id="save">`
    }else{

        const cfname = document.getElementById("cfname").value;
        const clname = document.getElementById("clname").value;
        fname.innerHTML = `${cfname}`;
        lname.innerHTML = `${clname}`;
        edit[0].defaultValue = "edit"
    }
    
})

// edit[1].addEventListener('click', ()=>{

//     if(edit[1].defaultValue =="edit"){
//         const ema = email.innerHTML;
//         email.innerHTML = `<input type="email" name="cemail" id="cemail" value = "${ema}">`;
//         edit[1].defaultValue = "save"
//     }else{

//         const cemail = document.getElementById("cemail").value;
//         email.innerHTML = `${cemail}`;
//         edit[1].defaultValue = "edit"
//     }
    
// })
// edit[2].addEventListener('click', ()=>{

//     if(edit[2].defaultValue =="edit"){
//         const una = uname.innerHTML;
//         uname.innerHTML = `<input type="text" name="cuname" id="cuname" value = "${una}">`;
//         edit[2].defaultValue = "save"
//     }else{

//         const cuname = document.getElementById("cuname").value;
//         uname.innerHTML = `${cuname}`;
//         edit[2].defaultValue = "edit"
//     }
    
// })

// edit[3].addEventListener('click', ()=>{

//     if(edit[3].defaultValue =="edit"){
//         const cpass = password.innerHTML;
//         password.innerHTML = `<input type="password" name="cpassword" id="cpassword" value = "${cpass}">`;
//         edit[3].defaultValue = "save"
//     }else{

//         const cpassword = document.getElementById("cpassword").value;
//         password.innerHTML = `${cpassword}`;
//         edit[3].defaultValue = "edit"
//     }
    
// })



close.addEventListener('click', ()=>{
    profilebox[0].style.top = "-900px"
})

profile.addEventListener('click', ()=>{
    profilebox[0].style.top = "100px"

})