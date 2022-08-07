class Student:
    college='Quantum University Roorkee' #class attribute
    def about(self):                #fuction
        print('Welcome Everyone!')

    @staticmethod
    def greet():
        print('Nice Day')
Ashish=Student()
Ashish.course='BCA' #object attribute
Ashish.about()
Ashish.greet()
#print(Ashish.college)
#print(Ashish.course)