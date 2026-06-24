"""
* Users: 
    id : autonumbered (primary key),
    name : varchar(60),
    email : varchar(60),
    password : varchar(60)
"""
query_1 = """
CREATE TABLE users (
    id serial primary key,
    name varchar(60),
    email varchar(60) UNIQUE,
    password varchar(60)
    )
"""

"""
* Messages:
    id : autonumbered (primary key),
    user_id: int,
    message : text
"""
query_2 = """
CREATE TABLE messages (
    id serial primary key,
    user_id int,
    message text,
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
    )
CREATE INDEX messages_user_id_idx ON messages (user_id)
"""

"""
* Items:
    id : autonumbered (primary key),
    name : varchar(40),
    description : text,
    price : decimal(7,2)
"""
query_3 = """
CREATE TABLE items (
    id serial primary key,
    name varchar(40),
    description text,
    price decimal(7,2)
    )
"""

"""
* Orders: 
    id : autonumbered (primary key),
    description : text
"""
query_4 = """
CREATE TABLE orders (
    id serial primary key,
    description text
    )
"""

query_5 = """
CREATE TABLE itemsorders (
    id       serial PRIMARY KEY,
    item_id  int,
    order_id int,
    FOREIGN KEY (item_id) REFERENCES items (id) ON DELETE CASCADE,
    FOREIGN KEY (order_id) REFERENCES orders (id) ON DELETE CASCADE 
)
"""
query_6 = """
SELECT name,price,description,id
FROM items
WHERE price > 13
ORDER BY name
"""

query_7 = """
INSERT INTO orders (description)
VALUES ('sample description')
"""
query_8 = """
DELETE FROM users WHERE id = 7
"""
query_9 = """
SELECT name,email,id
FROM users WHERE id IN (SELECT user_id FROM messages GROUP BY user_id)
ORDER BY name, email
"""
query_10 = """
ALTER TABLE messages
   ADD date_of_created date DEFAULT current_date
"""