
var cart = localStorage.getItem("cart")
if (cart == null) {
    console.log("when cart is null")
    cart = []
} else {
    cart = JSON.parse(cart);
    cc = []
    for (var item of cart) {
        console.log(item)
        // i = item.replace(/'/g, '"');
        cc.push(item)
    }
    cart = cc
}
function calculatetotal() {
    sum = 0
    for (var item of cart) {
        sum += item["price"]*item["count"]
    }
    console.log(sum)
    return sum
}
var total = 0
if (cart.length == 0) {
    document.write("No Items in the cart")
}
else {
    total = calculatetotal()
    document.write(`
        <tr>
            <tr>
                <th>Item Code</th>
                <th>Name</th>
                <th>Quantity</th>
                <th>Price</th>
            </tr>
        </tr>
            `)
    for (var item of cart) {
        document.write(`
            <tr>
            <td>`+ item["itemId"] + `</td>
            <td>`+ item["name"] + `</td>
            <td>`+ item["count"] + `</td>
            <td>`+ item["count"]*item["price"] + `$</td>
            </tr>
            `)
    }
    document.write(`
            <tr>
            <td></td>
            <td></td>
            <td>Total:</td>
            <td>`+ total + `$</td>
            </tr>
            `)
    document.write(`
    <button type="button" class="btn btn-primary" onclick="deletecart()" style="position:relative;right:-35%">Delete cart</button>

    <a class="nav-link active" onclick="placeorder(`+total+`)"  href="/placeOrder" style="position: relative;
    left: 35%; background-color:"blue"">Place Order</a>
    </br></br>
    
    `)



}

