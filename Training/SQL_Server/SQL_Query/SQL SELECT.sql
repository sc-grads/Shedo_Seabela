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

SELECT        TOP (100) PERCENT Person.Person.Title, Person.Person.FirstName, Person.Person.LastName, Person.PersonPhone.PhoneNumber, Person.PhoneNumberType.Name AS PhoneType
FROM            Person.Person INNER JOIN
                         Person.PersonPhone ON Person.Person.BusinessEntityID = Person.PersonPhone.BusinessEntityID INNER JOIN
                         Person.PhoneNumberType ON Person.PersonPhone.PhoneNumberTypeID = Person.PhoneNumberType.PhoneNumberTypeID
WHERE        (Person.Person.Title = N'Mr.')
ORDER BY Person.Person.FirstName DESC



select * from Person.address;

select AddressID,city,modifieddate from person.address;

select city,addressid,modifieddate from person.address;

select top 10 * from Person.Address;



select * from Person.address where postalcode = '98011'

select * from Person.address where postalcode != '98011'

select * from Person.address where postalcode <> '98011'

select count(*) from Person.address where postalcode <> '98011'

select * from Person.address where ModifiedDate >= '2013-11-08 00:00:00'

select * from Person.address where ModifiedDate <= '2013-11-08 00:00:00'

select * from Person.Person where FirstName like 'mat%'

select * from Person.Person where FirstName like '%ew'

select * from Person.Person where FirstName like '%EW'

select * from [HumanResources].[EmployeePayHistory]

select max(rate) from [HumanResources].[EmployeePayHistory]

select max(rate) AS MaxPayrate from [HumanResources].[EmployeePayHistory]

select min(rate) AS [Min Pay rate] from [HumanResources].[EmployeePayHistory]


select * from [Production].[ProductCostHistory] where startdate = '2013-05-30 00:00:00'


select * from [Production].[ProductCostHistory] where startdate = '2013-05-30 00:00:00' and StandardCost >= 200

select * from [Production].[ProductCostHistory] where( startdate = '2013-05-30 00:00:00' and StandardCost >= 200) or ProductID >800

select * from [Production].[ProductCostHistory] where( startdate = '2013-05-30 00:00:00' and StandardCost >= 200) and ProductID >800

select * from [Production].[ProductCostHistory] where ProductID in (802,803,820,900)

select * from [Production].[ProductCostHistory] where EndDate is null

select * from [Production].[ProductCostHistory] where EndDate is not null

---------------------------------

select * from [HumanResources].[EmployeePayHistory] order by rate 

select * from [HumanResources].[EmployeePayHistory] order by rate asc

select * from [HumanResources].[EmployeePayHistory] order by rate desc


select * from [HumanResources].[EmployeePayHistory] where  ModifiedDate >= '2010-06-30 00:00:00' order by ModifiedDate desc

select * from [HumanResources].[EmployeePayHistory] where  year(ModifiedDate) >= '2014' order by ModifiedDate desc

select * from [HumanResources].[EmployeePayHistory] where  month(ModifiedDate) = '06' order by ModifiedDate desc

---------------------------------------------

select * from Person.address where postalcode = '98011'


select count(*) from Person.address where postalcode = '98011'


select count(*),postalcode from Person.address group by PostalCode

select count(*) as NoOfAddresses,postalcode from Person.address group by PostalCode

select count(*) as NoOfAddresses,postalcode from Person.address group by PostalCode order by PostalCode 

select count(*),City from Person.address group by City

select count(*),City,PostalCode from Person.address group by City,PostalCode
----------------------------------------------

select * from Production.product 

select count(*) countofproduct,Color from Production.product where color = 'yellow' group by Color

select count(*) countofproduct,Color from Production.product group by Color having Color = 'yellow'


select count(*) countofproduct,Color,Size from Production.product group by Color,size having Size >= '44'


















