![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709394-2cabee80-571f-11eb-9518-ea6a794e558e.png)


# Python and databases &ndash; mock exam

Before you start solving the tasks, read the following tips.

##### Put the answers to the programming questions in the appropriate files *answer1.py* &ndash; *answer5.py*.

**Good luck!**

----------------------------------------------------------------------------------------

## Task 1 (3 points)

Write a script (program) in Python that creates a database.
* It should create a database named `exam2`.
* It should be resilient to connection errors.
* It should inform the user if such a database already exists.

Put the solution in file `answer1.py`.

---

## Task 2 (5 points)

We want to have the following tables in a database:

```SQL
* Users: 
    id : autonumbered (primary key),
    name : varchar(60),
    email : varchar(60),
    password : varchar(60)
* Messages:
    id : autonumbered (primary key),
    user_id: int,
    message : text
* Items: 
    id : autonumbered (primary key),
    name : varchar(40),
    description : text,
    price : decimal(7,2)
* Orders: 
    id : autonumbered (primary key),
    description : text
```

Look in the file **answer2.py**, you will find there the following variables defined: `query_1`, `query_2` ... `query_10`.
Place the following SQL queries in the variables:

* **query_1**: Creating table `Users` (email must be unique).
* **query_2**: Creating table `Messages` (remember the one-to-many relationship with table `Users`).
* **query_3**: Creating table `Items`.
* **query_4**: Creating table `Orders`.
* **query_5**: Creating a many-to-many relationship between tables `Items` and `Orders` (the table should be named `ItemsOrders`, and the relationship fields are `item_id` and `order_id`).
* **query_6**: Selecting all elements (Item) with a price greater than 13.
* **query_7**: Inserting a new order with the description "sample description" into the table `Orders`.
* **query_8**: Deleting the user with `id` 7.
* **query_9**: Selecting all users in table `Users` who have some message assigned in table `Messages`.
* **query_10**: Adding to table `Messages` a field named `date_of_created` that stores the date the message was created. It should be completed automatically when a row is added to the database. It can take the value `null` (for messages entered into the database before its addition).

Half a point is given for each query.

**Note 1:** When writing queries, do not use the database name in the query.
**Note 2:** Keep your table names, field names, and data types accurate!

---

## Task 3 (3 points)

Write a **generator** named `dividers` that takes one argument: `number`.
The generator should generate successive divisors of the number passed as an argument.

##### Example of use:
```python
for i in dividers(6):
    print(i)
```

##### Result:
```
1
2
3
6
```

Put the solution in the file `answer3.py`.

---

## Task 4 (4 points)

Using the **Flask** framework, write a page available at `/add_product`,
which will meet the following assumptions:

1. When accessed using the GET method, it will display an empty form that contains the following fields:
    * `name`: product name,
    * `description`: product description,
    * `price`: product price.

    Remember: name the fields exactly as in the exercise instruction (set the `name` attribute of the `<input>` tag accordingly)

2. When accessed using the POST method:
    * will verify data correctness,
    * will write this data to the table `Items` (the same table as in task 1) in the database and display the message `Product added!`,
    * if any value is incorrect, it will display the message `Invalid data!` on the page instead of writing to the database.

Remember to connect to the database correctly and close the connection afterwards.

Put the solution in file `answer4.py`.

## Task 5 (5 points)
Write a class `VIPUser` in Python. The class should have the following properties:

1. Inherit from the `User` class (look in the **exam_lib** module) and have an additional attribute: ```_vip_card_number```.
    This attribute should not be accessible outside the class (remember the proper naming convention).

2. Have an `__init__` method that takes the following data:
    * name,
    * surname,
    * email,
    * VIP card number.
    Name, surname and email should be passed to the appropriate method of the parent class. This method must check if the given number is valid.
    * If it is &ndash; then set it.
    * If not &ndash; then the number should be set to ```None```.

3. Have a static method ```_check_card(new_number)``` &ndash; number is valid if it is:
    * greater than 999,
    * divisible by 2.
    The method has to return a boolean value. The method should not be accessible from outside the class.

4. Have a static method ```use_vip_card()``` &ndash; the method body can be left empty (or return the value `None`).
5. Have a setter and a getter (`@property`) for the ```_vip_card_number``` attribute.
    * Setter should set the variable `_vip_card_number` (if the specified new number meets the assumptions).
    * Getter (property) should simply return the value of the attribute.

Put the solution to the task in the file `answer5.py`.
