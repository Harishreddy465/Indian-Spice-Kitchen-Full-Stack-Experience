cart=localStorage.getItem("cart")

if(cart==null){
    cart=[]
}else{
    cart = JSON.parse(cart);
}
function addToCart(p){

    p=p.replace(/'/g, '"');
    const curr=JSON.parse(p)
    alert(curr.name +" added to the cart")
    checkb=true
    for (let i of cart){
        console.log(i)
        if(i["name"]==curr.name){
            i.count+=1
            checkb=false
            break
        }
    }
    if(checkb==true){
        curr.count=1
        cart.push(curr)
    }
    console.log(cart)
    localStorage.setItem("cart",JSON.stringify(cart))    
}