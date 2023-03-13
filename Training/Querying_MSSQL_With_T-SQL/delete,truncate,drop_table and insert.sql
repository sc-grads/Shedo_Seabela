CREATE TABLE tblPrimeNumbers (
intField int);

INSERT INTO tblPrimeNumbers
VALUES (2),(3),(5),(7);

INSERT INTO tblPrimeNumbers
VALUES (11)

 Select * from tblPrimeNumbers
 where intField >= 3
GO

SELECT * FROM tblPrimeNumbers;

Delete from tblPrimeNumbers

TRUNCATE TABLE tblPrimeNumbers

DROP TABLE tblPrimeNumbers
