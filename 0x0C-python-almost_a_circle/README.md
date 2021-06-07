0. All your files, classes, and methods must be unit tested and PEP 8 validated. 
1. Create empty init file, and Base file with private class attribute nb objects and class constructor. If id is not None, assign id with argument value, and can assume it is an integer and does not need to be tested. Otherwise increment nb objects and assign the new value to public instance attribute id. 
2. Write the class Rectangle which inherits from Base. Give it private instance attributes with getters and setters: width, height, x, and y, as well as a class constructor. Call super class with id, and assign each argument width, height, x and y to the right attribute. 
3. Update rectangle class by adding validation of all setter methods and instantiation. Raise type error if input is not an integer. Raise value error is width or height is less than or equal to zero, likewise with x and y (but x/y can be equal to zero). 
4. Update the rectangle class by adding the public method def area (self). 
5. Update the rectangle class by adding public method def display (self) that prints with #, but does not need to handle x & y. 
6. Update rectangle class by overriding str so it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>. 
7. Add x and y in the display method. 
8. Add public method update(self, *args)* that assigns and argument to the attributes id, width, height, x, and y. Argument order is important, it's a no-keyword argument. 
9. Add ability to assign key/value argument to attributes listed above. 
10. Write a class square that inherits from rectangle. 
11. Update square by adding public getter and setter size. 
12. Add update keyword arguments to square. 
13. Update rectangle class by adding public method which returns the dictionary representation of a rectangle, containing id, width, height, x and y. 
14. Update the square class with the dictionary representation method. 
15. Update the base class by adding static method that returns the JSON string representation of list dictionaries. 
16. Update the base class to add class method that writes the JSON string representation of list objects to a file. 
17. Update base class to add static method that returns the list of JSON string representations
18. Update base class by adding class method create that returns an instance with attributes already set. 
19. Update the base class by adding load from file class method that returns a list of instances. 
