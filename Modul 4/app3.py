# problema cos de cumparaturi
cart = {'apple': 10, 'plums': 15, 'bananas': 5}

shop_K = {'apple': 1.2, 'plums': 4, 'bananas': 5.5}
shop_P = {'apple': 1.3, 'plums': 3, 'bananas': 8}
shop_L = {'apple': 1.4, 'plums': 2, 'bananas': 10}

shop = {'pro': shop_P, 'lil':shop_L, 'kau':shop_K}

for cart_product, cart_quantity in cart.items():
    print(cart_product,cart_quantity)
    for shop_name,shop_products in shop.items():
        #print(shop_name,shop_products[cart_product])
        print(shop_name, shop_products[cart_product]* cart_quantity) # doar pentru mere

#extragere cheie

