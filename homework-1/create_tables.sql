-- SQL-команды для создания таблиц

CREATE TABLE customers (
    customer_id char(5) PRIMARY KEY,
	company_name VARCHAR(100) NOT NULL,
	contact_name VARCHAR(50) NOT NULL
);


CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    title VARCHAR(100) NOT NULL,
    birth_date DATE NOT NULL
);


CREATE TABLE orders (
    order_id INT PRIMARY KEY,
	customer_id char(5) REFERENCES customers(customer_id),
	employee_id INT REFERENCES employees(employee_id),
	order_date DATE NOT NULL,
	ship_city VARCHAR(50) NOT NULL
);
