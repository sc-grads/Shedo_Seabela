CREATE TABLE [dbo].[Course](
	[CourseID] [int] NULL,
	[RollNO] [int] NULL
) ON [PRIMARY

CREATE TABLE [dbo].[Student](
	[RollNo] [int] NOT NULL,
	[StudentName] [nvarchar](50) NULL,
	[StudentCity] [nvarchar](20) NULL,
	[StudentPhoneNo] [nvarchar](50) NULL,
	[StuentAge] [int] NULL,
 CONSTRAINT [PK_Student] PRIMARY KEY CLUSTERED 
(
	[RollNo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

select * from [dbo].[Student]

select * from [dbo].[Course]

select * from [dbo].[Student] s
inner join [dbo].[Course] c 
on s.RollNo = c.RollNO

create table salesstaff
(
staffid int not null primary key,
firstname nvarchar(50) not null,
lastname nvarchar(50) not null,
countryregion nvarchar(50) not null
)
 DELETE Salesstaff
 drop table salesstaff
 insert into salesstaff
select [BusinessEntityID],[FirstName],[LastName],[CountryRegionName] from [Sales].[vSalesPerson]
delete from salesstaff where countryregion =  'united states'

begin tran
delete from salesstaff where countryregion =  'united states'

rollback tran
select * from [Sales].[vSalesPerson]

delete from salesstaff where staffid in (select [BusinessEntityID] from [Sales].[vSalesPerson] where SalesLastYear = 0)

CREATE TABLE [dbo].[salesstaff1](
	[staffid] [int] NOT NULL PRIMARY KEY,
	[fName] [nvarchar](30) NULL,
	[lName] [nvarchar](30) NULL
	)
	INSERT INTO [dbo].[salesstaff1] (STAFFID,FNAME,LNAME) VALUES (200,'Abbas','Mehmood')
	select * from [dbo].[salesstaff1] 
	INSERT INTO [dbo].[salesstaff1] (STAFFID,FNAME,LNAME) VALUES (300,'Imran','Afzal'),(325,'John','Vick'),(314,'James','Dino')

	CREATE TABLE [dbo].[nameOnlyTable](
	
	[fName] [nvarchar](30),
	[lName] [nvarchar](30)
	)
	
	select firstname + ' ' + Lastname AS Fullname,
[TerritoryName],
[TerritoryGroup],
[SalesQuota],
[SalesYTD],[SalesLastYear]
 into salesstaff2
 from sales.vSalesPerson

 
select * from salesstaff2


update salesstaff2 set [SalesQuota] = 50000 

update salesstaff2 set [SalesQuota] = SalesQuota + 1550000 