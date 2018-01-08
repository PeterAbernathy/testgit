while True:
    print('请输入纯数字')
    price = input('商品售价：')
    net = input('含量（以克或者毫升为单位）：')
    x = float(price) / float(net) * 500
    print('--此商品，每500 克/毫升：\n' + str(round(x,4)) + '元')
    keep_running = input('\n此处输入 n 退出程序')
    if keep_running == 'n':
        break

