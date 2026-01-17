CREATE DATABASE Odev_db

CREATE TABLE Books (
book_id INT IDENTITY (1,1) PRIMARY KEY,
title NVARCHAR(50) NOT NULL,
author NVARCHAR(50) NOT NULL,
genre NVARCHAR(50),
price DECIMAL(8,2) CHECK (price >= 0),
stock INT CHECK (stock >= 0),
published_year INT CHECK (published_year >= 0),
added_at INT CHECK (added_at >= 0)
);

INSERT INTO Books (title,author,genre,price,stock,published_year,added_at) values
('Kayýp Zamanýn Ýzinde','M. Proust','roman', 129.90, 25, 1913, 2025-08-20),
('Simyaci','P. Coelho','roman',89.50, 40, 1988, 2025-08-21),
('Sapiens', 'Y.N. Harari', 'tarih', 159.00, 18, 2011, 2025-08-25),
('Ýnce Memed','Y. Kemal','roman',99.90,12,1955,2025-08-22),
('Körlük','J. Saramago','roman',119.00,7,1995,2025-08-28),
('Dune','F. Herbert','bilim',149.00,30,1965,2025-09-01),
('Hayvan Çiftliði','G. Orwell','roman',79.90,55,1945,2025-08-23),
('1984','G. Orwell','roman',99.00,35,1949,2025-08-24),
('Nutuk','M. K. Atatürk','tarih',139.00,20,1927,2025-08-27),
('Küçük Prens','A. de Saint-Exupéry','çocuk',69.90,80,1943,2025-08-26),
('Baþlangýç','D. Brown','roman',109.00,22,2017,2025-09-02),
('Atomik Alýþkanlýklar','J. Clear','kiþisel geliþim',129.00,28,2018,2025-09-03),
('Zamanýn Kýsa Tarihi','S. Hawking','bilim',119.50,16,1988,2025-08-29),
('Þeker Portakalý','J. M. de Vasconcelos','roman',84.90,45,1968,2025-08-30),
('Bir Ýdam Mahkûmunun Son Günü','V. Hugo','roman',74.90,26,1829,2025-08-31);

---3.GÖREVLER---

--3.1--
SELECT title,author,price from Books
ORDER BY title ASC;

SELECT title,author,price from Books
ORDER BY author ASC;

SELECT title,author,price from Books
ORDER BY price ASC;

--3.2--
SELECT * FROM Books WHERE genre = 'roman'
ORDER BY genre ASC;

--3.3--
SELECT * FROM Books
WHERE price BETWEEN 80.00 AND 120.00
ORDER BY price ASC;

--3.4--
SELECT * FROM Books
WHERE stock < 20
ORDER BY stock ASC;

--3.5--
SELECT * FROM Books
WHERE title LIKE '%zaman%';

--3.6--
SELECT * FROM Books
WHERE genre IN ('roman', 'bilim');

--3.7--
SELECT * FROM Books
WHERE published_year >= 2000
ORDER BY published_year DESC;

--3.8--
SELECT * FROM Books
WHERE added_at >= DATEADD(DAY, -10, GETDATE());

--3.9--
SELECT TOP 5 * FROM Books
ORDER BY price DESC;

--3.10--
SELECT * FROM Books
WHERE stock BETWEEN 30 AND 60
ORDER BY price ASC;