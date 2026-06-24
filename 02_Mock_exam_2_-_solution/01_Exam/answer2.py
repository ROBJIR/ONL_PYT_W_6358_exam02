query_1 = """CREATE TABLE Users(
  id serial PRIMARY KEY,
  name varchar(60),
  email varchar(60) UNIQUE,
  password varchar(60)
)"""

query_2 = """CREATE TABLE Messages(
  id serial PRIMARY KEY,
  user_id int REFERENCES Users(id),
  message text
)"""

query_3 = """CREATE TABLE Items(
  id serial PRIMARY KEY,
  name varchar(40),
  description text,
  price decimal(7,2)
)"""

query_4 = """CREATE TABLE Orders(
  id serial,
  description text,
  PRIMARY KEY(id)
)"""

query_5 = """CREATE TABLE ItemsOrders(
    id serial PRIMARY KEY,
    item_id int REFERENCES Items (id) ON DELETE CASCADE,
    order_id int REFERENCES Orders (id) ON DELETE CASCADE
)"""

query_6 = "SELECT * FROM Items WHERE price > 13"
query_7 = "INSERT INTO Orders(description) VALUES ('example description')"
query_8 = "DELETE FROM Users WHERE id = 7"
query_9 = """SELECT Users.name AS user_name, Users.id AS user_id, Messages.message AS u_message
    FROM Users JOIN Messages on Users.id=Messages.user_id
"""

query_10 = "ALTER TABLE Messages ADD date_of_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
