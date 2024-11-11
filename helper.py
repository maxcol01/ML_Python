
def print_version_library(*args):
    for item in args:
        print(f"the version of {item.__name__} is {item.__version__}")
    print("Finish !")


def convert_wage(value):
    if 'K' in value:
        return int(float(value.replace('€', '').replace('K', '').strip()) * 1000)
    elif 'M' in value:
        return int(float(value.replace('€', '').replace('M', '').strip()) * 1000000)
    else:
        return int(value.replace('€', '').strip())  # In case there are any values without K or M

def test():
    print("ok it worked")

def test2():
    print("this works too !")


 