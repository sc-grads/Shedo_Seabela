CREATE TABLE [AdventureWorks2019].[sales].[visits1](
visit_id INT PRIMARY KEY IDENTITY (1,1),
first_name VARCHAR (50) NOT NULL,
last_name VARCHAR (50) NOT NULL,
visited_at DATETIME,
phone VARCHAR (20),
store_id INT NOT NULL,
FOREIGN KEY (store_id) REFERENCES sales.storenew11(store_id)
)

CREATE TABLE [AdventureWorks2019].[sales].[storenew11](

store_id INT PRIMARY KEY NOT NULL,
sales INT)

SELECT * FROM sales.storenew11