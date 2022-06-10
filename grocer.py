grocer_list = {'蛋白石': {'单价': 11, '库存': 3}, '木箭': {
    '单价': 10.5, '库存': 11}, '禽蛋': {'单价': 3.2, '库存': 36}}

item = input('亲，您要点什么?')
if item in grocer_list:
    amount = int(input('请问要多少份呢？'))

    def order(list, price):
        for goods in list:
            unit_price = list[goods][price]
        total_price = amount*unit_price
        return(total_price)
    print('购买成功，总价{}'.format(order(grocer_list, '单价')))


else:
    print('很抱歉，您要的商品还没有到货。')
