function subscribe(){
    email=document.getElementById("subscribe_id").value
    console.log(typeof email)
    if(email.length<1){
        alert("Please enter valid emailId")
    }else{
        alert("Hurray!! Thank you for Subscribing")
    }
}

function deletecart(){
    console.log("in deletecart")
    cart=[]
    localStorage.setItem("cart",JSON.stringify(cart))
    // localStorage.setItem("placeOrder",JSON.stringify(false))
    location.reload() 
}

function placeorder(total){
    console.log("in place order method")
    console.log(total)
    localStorage.setItem("total",JSON.stringify(total))
    location.reload() 
}