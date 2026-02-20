# def method_decorator(func):
#     def wrapper(self, *args, **kwargs):
#         print("Before method execution")
#         res = func(self, *args, **kwargs)
#         print("After method execution")
#         return res
#     return wrapper

# class MyClass:
#     @method_decorator
#     def say_hello(self):
#         print("Hello!")
# obj = MyClass()
# obj.say_hello()


class LogErrorIterator:
    def __init__(self, file_path):
        # Open the file, but don't read the contents yet
        self.file = open(file_path, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        # Read strictly ONE line into memory at a time
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration # Tells Python the iteration is over
        return line

# Usage:
error_count = 0
# The for loop automatically calls __next__() on our iterator under the hood
for line in LogErrorIterator('server_logs.txt'):
    if "404 Not Found" in line:
        error_count += 1