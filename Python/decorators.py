def ann(f):
    print("hey")
    def kiran():
        print("About to run the function...")
        f()
        print("Done running the function.")
    print("hooo")
    return kiran


@ann
def hello():
    print("Hello, world!")

hello()
