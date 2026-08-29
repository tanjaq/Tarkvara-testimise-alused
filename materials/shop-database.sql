-- =====================================================================
-- Software Testing Fundamentals - Lesson 11 - sample shop database
--
-- HOW TO USE
--   1. Open https://sqliteonline.com  (or any SQLite client / DB Fiddle)
--   2. Paste this whole file and run it
--   3. Write one query per requirement below and check whether the data
--      actually honours it
--
-- THE REQUIREMENTS THE APPLICATION IS SUPPOSED TO GUARANTEE
--   R1  Every customer has an email address, and it is unique.
--   R2  Every order belongs to an existing customer.
--   R3  Every order item refers to an existing product.
--   R4  An order item quantity is at least 1.
--   R5  A product price is greater than 0.
--   R6  An order status is one of: NEW, PAID, SHIPPED, CANCELLED.
--   R7  An order total equals the sum of its items (quantity * unit_price),
--       rounded to 2 decimals.
--   R8  A cancelled order that was paid must have a refund row.
--   R9  No order is created with a date in the future.
--
-- There are AT LEAST SIX defects in the data below.
-- For each one: which requirement does it break, what severity would you
-- give it, and which database constraint would have prevented it?
-- =====================================================================

DROP TABLE IF EXISTS refunds;
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS customers;

-- Note: no FOREIGN KEY, UNIQUE or CHECK constraints are declared.
-- That is part of what you are evaluating.
CREATE TABLE customers (
  id          INTEGER PRIMARY KEY,
  name        TEXT,
  email       TEXT,
  created_at  TEXT
);

CREATE TABLE products (
  id          INTEGER PRIMARY KEY,
  name        TEXT,
  price       REAL,
  active      INTEGER
);

CREATE TABLE orders (
  id           INTEGER PRIMARY KEY,
  customer_id  INTEGER,
  status       TEXT,
  total        REAL,
  created_at   TEXT,
  refunded_at  TEXT
);

CREATE TABLE order_items (
  id          INTEGER PRIMARY KEY,
  order_id    INTEGER,
  product_id  INTEGER,
  quantity    INTEGER,
  unit_price  REAL
);

CREATE TABLE refunds (
  id         INTEGER PRIMARY KEY,
  order_id   INTEGER,
  amount     REAL,
  created_at TEXT
);

INSERT INTO customers (id, name, email, created_at) VALUES
  (1, 'Anna Tamm',      'anna.tamm@example.com',    '2026-01-04 09:12:00'),
  (2, 'Peeter Kask',    'peeter.kask@example.com',  '2026-01-07 14:03:00'),
  (3, 'Mari Lepik',     'mari.lepik@example.com',   '2026-02-11 08:44:00'),
  (4, 'Jaan Saar',      NULL,                       '2026-02-19 17:21:00'),
  (5, 'Liis Oja',       'mari.lepik@example.com',   '2026-03-02 11:05:00'),
  (6, 'Tonu Ilves',     'tonu.ilves@example.com',   '2026-03-15 19:37:00');

INSERT INTO products (id, name, price, active) VALUES
  (10, 'Keyboard',        49.90, 1),
  (11, 'Mouse',           19.99, 1),
  (12, 'Monitor 24"',    189.00, 1),
  (13, 'USB-C cable',      9.95, 1),
  (14, 'Laptop stand',    39.50, 1),
  (15, 'Webcam',           0.00, 1),
  (16, 'Headset',         79.00, 0);

INSERT INTO orders (id, customer_id, status, total, created_at, refunded_at) VALUES
  (100, 1,   'PAID',      69.89,  '2026-03-01 10:00:00', NULL),
  (101, 2,   'SHIPPED',  189.00,  '2026-03-03 12:30:00', NULL),
  (102, 3,   'NEW',       19.99,  '2026-03-05 08:15:00', NULL),
  (103, 99,  'PAID',      39.50,  '2026-03-06 16:45:00', NULL),
  (104, 1,   'CANCELLED', 99.85,  '2026-03-08 09:05:00', NULL),
  (105, 5,   'PAYED',     49.90,  '2026-03-09 13:20:00', NULL),
  (106, 6,   'PAID',      59.70,  '2027-01-02 10:00:00', NULL),
  (107, 2,   'PAID',      19.99,  '2026-03-12 15:00:00', NULL);

INSERT INTO order_items (id, order_id, product_id, quantity, unit_price) VALUES
  (1000, 100, 10,  1, 49.90),
  (1001, 100, 11,  1, 19.99),
  (1002, 101, 12,  1, 189.00),
  (1003, 102, 11,  1, 19.99),
  (1004, 103, 14,  1, 39.50),
  (1005, 104, 12,  1, 189.00),
  (1006, 104, 13, -1,  9.95),
  (1007, 105, 10,  1, 49.90),
  (1008, 106, 13,  6,  9.95),
  (1009, 107, 42,  1, 19.99);

INSERT INTO refunds (id, order_id, amount, created_at) VALUES
  (5000, 999, 12.00, '2026-03-10 10:00:00');

-- =====================================================================
-- STARTER QUERIES - run these first to get your bearings
-- =====================================================================
-- SELECT * FROM customers;
-- SELECT * FROM orders;
-- SELECT o.id, c.name, o.status, o.total
--   FROM orders o JOIN customers c ON c.id = o.customer_id;
--
-- Notice how many rows that last query returns, then run it again as a
-- LEFT JOIN and compare the count. The difference is a defect.
-- =====================================================================
