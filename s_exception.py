
def log_func(msg):
    print(msg)
    return msg

class myException(Exception):
    def __init__(self):
        log_func("myEception raise")



def test_function(x:int, y:int):
    if x == 0 or y == 0:
        raise myException
    return x * y


if __name__ == "__main__":
    try:
        print(test_function(5, 5))
        print(test_function(0, 5))
        print(test_function(5, 0))
        print(test_function(0, 0))
    except myException:
        print("Raised my exception")
