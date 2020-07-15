def method_1():
    print("method 1")

class ClassA:
    def class_method_1(self):
        print("class_method_1 method_1")

print(f"__name__ {__name__}")

# execute this code only if we execute this module
# if other module use this one the rest of code is not executed after main
if __name__ == '__main__':
    method_1()
    ClassA().class_method_1()

