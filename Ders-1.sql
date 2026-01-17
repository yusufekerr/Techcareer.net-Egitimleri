CREATE DATABASE PERSONEL

CREATE TABLE KULLANICILAR (
id INT IDENTITY(1,1) PRIMARY KEY ,
ad NVARCHAR(50) ,
soyad NVARCHAR(50) ,
yas INT ,
);


select * from KULLANICILAR --deneme 123

select ad from KULLANICILAR

select ad , soyad from KULLANICILAR

INSERT INTO KULLANICILAR (ad, soyad, yas) values ('kemal', 'tas', 36)

UPDATE KULLANICILAR
SET yas = 25
where ad = 'ayse'


DELETE FROM KULLANICILAR
where id=1

select DISTINCT ad 
from KULLANICILAR

select top 2 ad
from KULLANICILAR
