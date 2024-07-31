def scope_test():
    def do_local():
        spam="local spam"
    def do_nonlocal(): #üstteki fonksiyonda da tanımlo
        nonlocal spam
        spam="nonlocal spam"
    def do_global(): #tüm kodda tanımlı
        global spam
        spam = "global spam"
    spam="test spam"
    do_local()
    print("Localdan sonra :",spam)
    do_nonlocal()
    print("nonlocaldan sonra :",spam)
    do_global()
    print("Globaldan sonra :",spam)

scope_test()
print("Global skop: ", spam)
