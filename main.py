def test_function():
    def inner_function():
        global a
        print(a)
    inner_function()


a=str("Я в области видимости функции test_function")
test_function()
