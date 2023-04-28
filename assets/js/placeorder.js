document.getElementById('total').value = localStorage.getItem("total");
console.log(localStorage.getItem("total"))

function clearcart(){
    console.log("cart cleared")
    cart=localStorage.getItem("cart")
    cart = JSON.parse(cart);
    fetch('/myendpoint', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(cart)
    })
    .then(response => response.text())
    .then(result => {
        console.log('Success:', result);
    })
    .catch(error => {
        console.error('Error:', error);
    });

    cart=[]
    localStorage.setItem("cart",JSON.stringify(cart))
}

