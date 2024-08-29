# from django.contrib.auth.models import Group, User
# from courses.models import Course, Module
# from users.models import Profile

# # Create some groups to represent courses
# course1 = Group.objects.create(name="Introduction to Programming")
# course2 = Group.objects.create(name="Advanced Data Science")

# # Create modules for the first course
# module1 = Module.objects.create(course=course1, name="Python Basics", description="Learn Python from scratch.")
# module2 = Module.objects.create(course=course1, name="Introduction to Algorithms", description="Learn basic algorithms.")

# # Create modules for the second course
# module3 = Module.objects.create(course=course2, name="Machine Learning", description="Introduction to machine learning.")
# module4 = Module.objects.create(course=course2, name="Data Visualization", description="Learn how to visualize data effectively.")

# # Register a student for a module
# student = Profile.objects.create(user=User.objects.create(username='student1'))
# student.register_module(module1)
# student.register_module(module3)

# # Unregister a student from a module
# student.unregister_module(module1)
