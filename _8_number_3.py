def new_decorator(transform):
      def the_original_function():
          transform() 
      yield the_original_function
a = new_decorator(transform([1,2,3,4,5],[6,7,8,9,10]))
print(list(a))
#попыталась сделать хоть какой-то декоратор, но особо не понимаю алгорим,буду дальше разбирать