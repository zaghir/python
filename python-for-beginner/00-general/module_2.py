def method_2() :
    print("method 2")

class ClassB:
    def class_method_2(self):
        print("class_method_2")


print(f"__name__ {__name__}")

# execute this code only if we execute this module
# if other module use this one the rest of code is not executed after main
if __name__ == '__main__':
    method_2()
    ClassB().class_method_1()

