# Main-Flow-Services-Technologies
TITLE:
Main Flow Services and Technologies Internship - Task Documentation: “Python Basics” Using Python (Jupyter Notebook).

INTRODUCTION
In the realm of programming, data structures are fundamental tools that enable efficient data management and manipulation. Understanding and utilizing these structures effectively is crucial for solving complex problems and optimizing code performance. This code provides a practical demonstration of basic operations on four essential data structures in Python: lists, dictionaries, sets, and tuples.

The list is a versatile and commonly used data structure that allows for dynamic resizing and supports a variety of operations, such as appending, removing, and modifying elements. The given code snippet showcases how to create a list, add an element using append, remove an element with remove, and modify an element by directly accessing its index.

Dictionaries, another key data structure, are ideal for storing data pairs and provide fast lookup times. The code illustrates how to create a dictionary, add a new key-value pair, remove an existing key, and modify the value of an existing key.

Sets are used for storing unique elements and support operations such as addition, removal, and set-specific methods like union and intersection. The code example demonstrates creating a set, adding an element with add, removing an element with remove, and modifying the set by removing and adding elements.

Lastly, tuples are immutable sequences, typically used to store collections of heterogeneous data. While they cannot be modified directly, this code shows how to access a tuple's element and update it by converting the tuple to a list, modifying the list, and converting it back to a tuple.

Through these examples, the code provides a comprehensive overview of basic operations on lists, dictionaries, sets, and tuples, equipping you with foundational skills for effective data manipulation in Python.

Implementation
• Python Lists: Utilize Python's built-in list data structure for creating and manipulating ordered collections of items.

• Python Dictionaries: Use Python dictionaries to store and manage key-value pairs, enabling efficient data retrieval and updates.

• Python Sets: Implement Python sets for handling collections of unique items, providing efficient membership tests and set operations.

• Python Tuples: Employ Python tuples to store immutable sequences of elements, useful for fixed collections of items.

CODE EXPLANATION
Python Lists:
Creating and Modifying Lists:
• Creating a List:
my_list = [1, 2, 3, 4, 5]

• Initializes a list named my_list with elements 1, 2, 3, 4, and 5.

• Adding an Element:
my_list.append(6)

• Adds the element 6 to the end of my_list.

• Removing an Element:
my_list.remove(3)

• Removes the first occurrence of the element 3 from my_list.

• Modifying an Element:
my_list[0] = 10

• Changes the first element of my_list from 1 to 10.

Output:
print("Updated list:", my_list)

• Displays the updated list: [10, 2, 4, 5, 6].

Python Dictionaries:
Creating and Modifying Dictionaries:
• Creating a Dictionary:
my_dict = {'name': 'John', 'age': 25, 'city': 'Delhi'}

• Initializes a dictionary named my_dict with keys 'name', 'age', and 'city'.

• Adding a Key-Value Pair:
my_dict['gender'] = 'Male'

• Adds a new key-value pair 'gender': 'Male' to my_dict.

• Removing a Key-Value Pair:
del my_dict['age']

• Removes the key-value pair with the key 'age' from my_dict.

• Modifying a Value:
my_dict['city'] = 'Mumbai'

• Changes the value associated with the key 'city' from 'Delhi' to 'Mumbai'.

Output:
print("Updated Dictionary:", my_dict)

• Displays the updated dictionary: {'name': 'John', 'city': 'Mumbai', 'gender': 'Male'}.

Python Sets:
Creating and Modifying Sets:
• Creating a Set:
my_set = {1, 2, 3, 4, 5}

• Initializes a set named my_set with elements 1, 2, 3, 4, and 5.

• Adding an Element:
my_set.add(6)

• Adds the element 6 to my_set.

• Removing an Element:
my_set.remove(3)

• Removes the element 3 from my_set.

• Modifying the Set:
my_set.discard(1) my_set.add(10)

• Discards the element 1 and adds the element 10 to my_set.

Output:
print("Updated Set:", my_set)

• Displays the updated set: {2, 4, 5, 6, 10}.

Python Tuples:
Creating and Modifying Tuples:
• Creating a Tuple:
my_tuple = (1, 2, 3, 4, 5)

• Initializes a tuple named my_tuple with elements 1, 2, 3, 4, and 5.

• Accessing an Element:
print(my_tuple[2])

• Prints the third element of my_tuple: 3.

• Updating a Tuple:
new_my_tuple = list(my_tuple) new_my_tuple[1] = 6 my_tuple = tuple(new_my_tuple)

• Converts my_tuple to a list, modifies the second element to 6, and converts it back to a tuple.

Output:
print("Updated Tuple:", my_tuple)

• Displays the updated tuple: (1, 6, 3, 4, 5).

USAGE
Adding an Element to the List: Users can add an element to the list my_list by using the append method, which places the new element at the end of the list.

Removing an Element from the List: Users can remove an element from the list my_list by using the remove method, which deletes the first occurrence of the specified element.

Modifying an Element in the List: Users can change an existing element in the list my_list by accessing the element via its index and assigning a new value.

Adding a Key-Value Pair to the Dictionary: Users can add a new key-value pair to the dictionary my_dict by assigning a value to a new key.

Removing a Key-Value Pair from the Dictionary: Users can delete an existing key-value pair from the dictionary my_dict by using the del statement with the key they want to remove.

Modifying a Value in the Dictionary: Users can change the value associated with an existing key in the dictionary my_dict by reassigning the value to that key.

Adding an Element to the Set: Users can add an element to the set my_set by using the add method, which ensures the element is unique within the set.

Removing an Element from the Set: Users can remove an element from the set my_set by using the remove method, which deletes the specified element if it exists in the set.

Modifying the Set: Users can modify the set my_set by discarding an element using the discard method and adding a new element with the add method.

Accessing an Element in the Tuple: Users can access an element in the tuple my_tuple by using its index to retrieve the value.

Updating a Tuple: Since tuples are immutable, users can update a tuple my_tuple by converting it to a list, modifying the desired element, and converting it back to a tuple.

CONCLUSION
In conclusion, this Python code example effectively demonstrates the basic operations on four fundamental data structures: lists, dictionaries, sets, and tuples. By providing clear and concise examples of how to create, modify, and manipulate these data structures, the code serves as a valuable resource for both beginners and experienced programmers looking to reinforce their understanding of these essential concepts. Through the use of Python's versatile built-in functions and methods, users can efficiently manage and manipulate data, laying the groundwork for more complex and advanced programming tasks. With continued practice and exploration of these data structures, programmers can enhance their coding proficiency and develop robust, efficient solutions to a wide range of problems.

OUTPUT
Python List and Dictionary Data Structure and its Operations
This is about the tasks of Data science with python ,Doing internship in Main Flow Services & Technologies,the screenshot of task-01,is here below

![Screenshot (14)](https://github.com/Ishwarya200430/Main-Flow-Services-Technologies/assets/164725009/825fe594-98dd-47d7-a7f7-16af63c030da)

This is about the tasks of Data science with python,Doing internship in Main Flow Services & Technologies,the screenshot of task-02,is here below
![Untitled6 - Jupyter Notebook - Avast Secure Browser 29-05-2024 22_25_10](https://github.com/Ishwarya200430/Main-Flow-Services-Technologies/assets/164725009/39b24651-7d8a-41f3-80ce-776a49cc5027)

![Untitled6 - Jupyter Notebook - Avast Secure Browser 29-05-2024 22_25_37](https://github.com/Ishwarya200430/Main-Flow-Services-Technologies/assets/164725009/20a36d58-4d01-4346-9057-ae0d4d5ff93d)

![Untitled6 - Jupyter Notebook - Avast Secure Browser 29-05-2024 22_25_57](https://github.com/Ishwarya200430/Main-Flow-Services-Technologies/assets/164725009/406cf59c-7a27-4c7f-ae3b-2bbbc2a2da52)

![Untitled6 - Jupyter Notebook - Avast Secure Browser 29-05-2024 22_26_19](https://github.com/Ishwarya200430/Main-Flow-Services-Technologies/assets/164725009/a55363f3-880f-49d5-a02e-0f90fa94e4f5)

![Untitled6 - Jupyter Notebook - Avast Secure Browser 29-05-2024 22_26_34](https://github.com/Ishwarya200430/Main-Flow-Services-Technologies/assets/164725009/4a4c1ffc-5fe7-4240-a5c3-b207dd5b15ff)

![Untitled6 - Jupyter Notebook - Avast Secure Browser 29-05-2024 22_26_58](https://github.com/Ishwarya200430/Main-Flow-Services-Technologies/assets/164725009/4f10e494-5493-4cca-b033-ee2d9703a932)

![Untitled6 - Jupyter Notebook - Avast Secure Browser 29-05-2024 22_27_13](https://github.com/Ishwarya200430/Main-Flow-Services-Technologies/assets/164725009/845bfdb6-9639-4343-bf4d-8bae43bb5072)

![Untitled6 - Jupyter Notebook - Avast Secure Browser 29-05-2024 22_27_27](https://github.com/Ishwarya200430/Main-Flow-Services-Technologies/assets/164725009/bef7204c-f6d7-4c6e-b259-b96eb58f7355)

![Untitled6 - Jupyter Notebook - Avast Secure Browser 29-05-2024 22_27_54](https://github.com/Ishwarya200430/Main-Flow-Services-Technologies/assets/164725009/d48c8a8f-82e2-4a69-9d9f-9a6303c0fc5e)

![Untitled6 - Jupyter Notebook - Avast Secure Browser 29-05-2024 22_27_54](https://github.com/Ishwarya200430/Main-Flow-Services-Technologies/assets/164725009/edf8ffd8-1616-4e66-b974-e83e8be01ddc)

![Untitled6 - Jupyter Notebook - Avast Secure Browser 29-05-2024 22_28_52](https://github.com/Ishwarya200430/Main-Flow-Services-Technologies/assets/164725009/5ef517e5-4c59-4757-abcb-ea1615f79811)

![Untitled6 - Jupyter Notebook - Avast Secure Browser 29-05-2024 22_28_52](https://github.com/Ishwarya200430/Main-Flow-Services-Technologies/assets/164725009/904ded54-3ebe-4a92-94a3-63574ec25714)

![Untitled6 - Jupyter Notebook - Avast Secure Browser 29-05-2024 22_29_22](https://github.com/Ishwarya200430/Main-Flow-Services-Technologies/assets/164725009/5d744b01-19b0-48ea-8305-5cb41f10c672)

![Untitled6 - Jupyter Notebook - Avast Secure Browser 29-05-2024 22_29_34](https://github.com/Ishwarya200430/Main-Flow-Services-Technologies/assets/164725009/e513d46f-5ad3-4c92-a0b6-840c009745f9)

This is about the tasks of Data science with python ,Doing internship in Main Flow Services & Technologies,the screenshot of task-03,is here below
using pandas,numpy,seaborn,matplotlib 

![Untitled8 - Jupyter Notebook - Avast Secure Browser 07-06-2024 18_35_50](https://github.com/Ishwarya200430/Main-Flow-Services-Technologies/assets/164725009/ceef8612-5afa-47ba-931b-69a00b419b23)

![Untitled8 - Jupyter Notebook - Avast Secure Browser 07-06-2024 18_36_31](https://github.com/Ishwarya200430/Main-Flow-Services-Technologies/assets/164725009/4b2411a8-b6a0-4ea3-87c4-61148f19c296)

![Untitled8 - Jupyter Notebook - Avast Secure Browser 07-06-2024 18_36_47](https://github.com/Ishwarya200430/Main-Flow-Services-Technologies/assets/164725009/efc7fc5e-645e-4422-b954-b2f1aa9cc84f)

![Untitled8 - Jupyter Notebook - Avast Secure Browser 07-06-2024 18_37_03](https://github.com/Ishwarya200430/Main-Flow-Services-Technologies/assets/164725009/3a4be9c9-ed20-4f29-b8cf-c432fb24b442)

![Untitled8 - Jupyter Notebook - Avast Secure Browser 07-06-2024 18_37_14](https://github.com/Ishwarya200430/Main-Flow-Services-Technologies/assets/164725009/90f7b8ea-4b80-4051-9719-4a3850d35cd3)














