grocer_list = {'蛋白石': {'单价': 11, '库存': 3, },
               '木箭': {'单价': 10.5, '库存': 11},
               '王京': {'单价': 3.2, '库存': 36}
               }

amount = int(input('要多少份？'))


def order(list, price):
    for goods in list:
        unit_price = list[goods][price]

    total_price = amount*unit_price
    return(total_price)


print(order(grocer_list, '单价'))
print('购买成功，总价{}'.format(order(grocer_list, '单价')))
