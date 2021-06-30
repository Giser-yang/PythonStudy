def deco(func):
    def inner():
        print("runing inner!")
    return inner

@ deco
def target():
    print("running target!")


a =target()