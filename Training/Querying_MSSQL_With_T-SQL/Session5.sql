select A.EmployeeNumber, A.AttendanceMonth, A.NumberAttendance
,sum(A.NumberAttendance) over() as TotalAttendance,
convert(decimal(18,7),A.NumberAttendance) / sum(A.NumberAttendance) over() * 100.0000 as PercentageAttendance
from tblEmployee as E join tblAttendance as A
on E.EmployeeNumber = A.EmployeeNumber

select sum(NumberAttendance) from tblAttendance

select A.EmployeeNumber, A.AttendanceMonth, 
A.NumberAttendance, 
sum(A.NumberAttendance) over(PARTITION BY E.EmployeeNumber) as SumAttendance,
convert(money,A.NumberAttendance) / 
sum(A.NumberAttendance) over(PARTITION BY E.EmployeeNumber) * 100 as PercentageAttendance
from tblEmployee as E join tblAttendance as A
on E.EmployeeNumber = A.EmployeeNumber

select A.EmployeeNumber, A.AttendanceMonth, 
A.NumberAttendance, 
sum(A.NumberAttendance) over(PARTITION BY E.EmployeeNumber, year(A.AttendanceMonth)
 ORDER BY A.AttendanceMonth) as SumAttendance,
convert(money,A.NumberAttendance) / 
sum(A.NumberAttendance) over(PARTITION BY E.EmployeeNumber) * 100 as PercentageAttendance
from tblEmployee as E join tblAttendance as A
on E.EmployeeNumber = A.EmployeeNumber
order by A.EmployeeNumber, A.AttendanceMonth


select A.EmployeeNumber, A.AttendanceMonth, 
A.NumberAttendance, 
SUM(A.NumberAttendance) over(PARTITION BY E.EmployeeNumber ORDER BY A.AttendanceMonth ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) as RollingTotal
from tblEmployee as E join tblAttendance as A
on E.EmployeeNumber = A.EmployeeNumber

select A.EmployeeNumber, A.AttendanceMonth, 
A.NumberAttendance, 
SUM(A.NumberAttendance) over(PARTITION BY E.EmployeeNumber ORDER BY A.AttendanceMonth ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) as RollingTotal
from tblEmployee as E join tblAttendance as A
on E.EmployeeNumber = A.EmployeeNumber

select A.EmployeeNumber, A.AttendanceMonth, 
A.NumberAttendance, 
SUM(A.NumberAttendance) over(PARTITION BY E.EmployeeNumber ORDER BY A.AttendanceMonth ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as RollingTotal
from tblEmployee as E join tblAttendance as A
on E.EmployeeNumber = A.EmployeeNumber

select A.EmployeeNumber, A.AttendanceMonth, 
A.NumberAttendance, 
SUM(A.NumberAttendance) over(PARTITION BY E.EmployeeNumber ORDER BY A.AttendanceMonth ROWS BETWEEN CURRENT ROW AND UNBOUNDED FOLLOWING) as RollingTotal
from tblEmployee as E join tblAttendance as A
on E.EmployeeNumber = A.EmployeeNumber

select A.EmployeeNumber, A.AttendanceMonth, A.NumberAttendance
,sum(A.NumberAttendance) 
over(partition by A.EmployeeNumber, year(A.AttendanceMonth) 
     order by A.AttendanceMonth 
	 rows between current row and unbounded following) as RowsTotal
,sum(A.NumberAttendance) 
over(partition by A.EmployeeNumber, year(A.AttendanceMonth) 
     order by A.AttendanceMonth 
	 range between current row and unbounded following) as RangeTotal
from tblEmployee as E join (select * from tblAttendance UNION ALL select * from tblAttendance) as A
on E.EmployeeNumber = A.EmployeeNumber
--where A.AttendanceMonth < '20150101'
order by A.EmployeeNumber, A.AttendanceMonth


select A.EmployeeNumber, A.AttendanceMonth, A.NumberAttendance
,sum(A.NumberAttendance) over() as TotalAttendance
--,convert(decimal(18,7),A.NumberAttendance) / sum(A.NumberAttendance) over() * 100.0000 as PercentageAttendance
from tblEmployee as E join tblAttendance as A
on E.EmployeeNumber = A.EmployeeNumber

select sum(NumberAttendance) from tblAttendance

select A.EmployeeNumber, A.AttendanceMonth, 
A.NumberAttendance, 
sum(A.NumberAttendance) 
over(PARTITION BY E.EmployeeNumber, year(A.AttendanceMonth)
     ORDER BY A.AttendanceMonth) as SumAttendance
from tblEmployee as E join (select * from tblAttendance UNION ALL Select * from tblAttendance) as A
on E.EmployeeNumber = A.EmployeeNumber
order by A.EmployeeNumber, A.AttendanceMonth


select A.EmployeeNumber, A.AttendanceMonth, 
A.NumberAttendance, 
ROW_NUMBER() OVER(ORDER BY E.EmployeeNumber, A.AttendanceMonth) as TheRowNumber,
RANK() OVER(ORDER BY E.EmployeeNumber, A.AttendanceMonth) as TheRank,
DENSE_RANK() OVER(ORDER BY E.EmployeeNumber, A.AttendanceMonth) as TheDenseRank
from tblEmployee as E join 
(Select * from tblAttendance union all select * from tblAttendance) as A
on E.EmployeeNumber = A.EmployeeNumber

select A.EmployeeNumber, A.AttendanceMonth, 
A.NumberAttendance, 
ROW_NUMBER() OVER(PARTITION BY E.EmployeeNumber
                  ORDER BY A.AttendanceMonth) as TheRowNumber,
RANK()       OVER(PARTITION BY E.EmployeeNumber
                  ORDER BY A.AttendanceMonth) as TheRank,
DENSE_RANK() OVER(PARTITION BY E.EmployeeNumber
                  ORDER BY A.AttendanceMonth) as TheDenseRank
from tblEmployee as E join 
(Select * from tblAttendance union all select * from tblAttendance) as A
on E.EmployeeNumber = A.EmployeeNumber

select *, row_number() over(order by (select null)) from tblAttendance


select A.EmployeeNumber, A.AttendanceMonth, 
A.NumberAttendance, 
NTILE(10) OVER(PARTITION BY E.EmployeeNumber
          ORDER BY A.AttendanceMonth) as TheNTile,
convert(int,(ROW_NUMBER() OVER(PARTITION BY E.EmployeeNumber
                               ORDER BY A.AttendanceMonth)-1)
 / (count(*) OVER(PARTITION BY E.EmployeeNumber 
		          ORDER BY A.AttendanceMonth 
				  ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)/10.0))+1 as MyNTile
from tblEmployee as E join tblAttendance as A
on E.EmployeeNumber = A.EmployeeNumber
where A.AttendanceMonth <'2015-05-01'

select A.EmployeeNumber, A.AttendanceMonth, 
A.NumberAttendance, 
first_value(NumberAttendance)
over(partition by E.EmployeeNumber order by A.AttendanceMonth) as FirstMonth,
last_value(NumberAttendance)
over(partition by E.EmployeeNumber order by A.AttendanceMonth
rows between unbounded preceding and unbounded following) as LastMonth
from tblEmployee as E join tblAttendance as A
on E.EmployeeNumber = A.EmployeeNumber

select A.EmployeeNumber, A.AttendanceMonth, 
A.NumberAttendance, 
lag(NumberAttendance, 1)  over(partition by E.EmployeeNumber 
                            order by A.AttendanceMonth) as MyLag,
lead(NumberAttendance, 1) over(partition by E.EmployeeNumber 
                            order by A.AttendanceMonth) as MyLead,
NumberAttendance - lag(NumberAttendance, 1)  over(partition by E.EmployeeNumber 
                            order by A.AttendanceMonth) as MyDiff
--first_value(NumberAttendance)  over(partition by E.EmployeeNumber 
--                                    order by A.AttendanceMonth
--							        rows between 1 preceding and current row) as MyFirstValue,
--last_value(NumberAttendance) over(partition by E.EmployeeNumber 
--                                  order by A.AttendanceMonth
--								  rows between current row and 1 following) as MyLastValue
from tblEmployee as E join tblAttendance as A
on E.EmployeeNumber = A.EmployeeNumber


select A.EmployeeNumber, A.AttendanceMonth, 
A.NumberAttendance, 
CUME_DIST()    over(partition by E.EmployeeNumber 
               order by A.AttendanceMonth) as MyCume_Dist,
PERCENT_RANK() over(partition by E.EmployeeNumber 
                order by A.AttendanceMonth) as MyPercent_Rank,
cast(row_number() over(partition by E.EmployeeNumber order by A.AttendanceMonth) as decimal(9,5))
/ count(*) over(partition by E.EmployeeNumber) as CalcCume_Dist,
cast(row_number() over(partition by E.EmployeeNumber order by A.AttendanceMonth) - 1 as decimal(9,5))
/ (count(*) over(partition by E.EmployeeNumber) - 1) as CalcPercent_Rank
from tblEmployee as E join tblAttendance as A
on E.EmployeeNumber = A.EmployeeNumber

select A.EmployeeNumber, A.AttendanceMonth, 
A.NumberAttendance, 
CUME_DIST()    over(partition by E.EmployeeNumber 
               order by A.NumberAttendance) as MyCume_Dist,
PERCENT_RANK() over(partition by E.EmployeeNumber 
                order by A.NumberAttendance) * 100 as MyPercent_Rank
from tblEmployee as E join tblAttendance as A
on E.EmployeeNumber = A.EmployeeNumber

SELECT DISTINCT EmployeeNumber,
PERCENTILE_CONT(0.4) WITHIN GROUP (ORDER BY NumberAttendance) OVER (PARTITION BY EmployeeNumber) as AverageCont,
PERCENTILE_DISC(0.4) WITHIN GROUP (ORDER BY NumberAttendance) OVER (PARTITION BY EmployeeNumber) as AverageDisc
from tblAttendance

select E.Department, E.EmployeeNumber, A.AttendanceMonth as AttendanceMonth, sum(A.NumberAttendance) as NumberAttendance
from tblEmployee as E join tblAttendance as A
on E.EmployeeNumber = A.EmployeeNumber
group by E.Department, E.EmployeeNumber, A.AttendanceMonth
--order by Department, EmployeeNumber, AttendanceMonth
UNION
select E.Department, E.EmployeeNumber, null as AttendanceMonth, sum(A.NumberAttendance) as TotalAttendance
from tblEmployee as E join tblAttendance as A
on E.EmployeeNumber = A.EmployeeNumber
group by E.Department, E.EmployeeNumber
union
select E.Department, null, null as AttendanceMonth, sum(A.NumberAttendance) as TotalAttendance
from tblEmployee as E join tblAttendance as A
on E.EmployeeNumber = A.EmployeeNumber
group by E.Department
union
select null, null, null as AttendanceMonth, sum(A.NumberAttendance) as TotalAttendance
from tblEmployee as E join tblAttendance as A
on E.EmployeeNumber = A.EmployeeNumber
order by Department, EmployeeNumber, AttendanceMonth

select E.Department, E.EmployeeNumber, A.AttendanceMonth as AttendanceMonth, sum(A.NumberAttendance) as NumberAttendance,
GROUPING(E.EmployeeNumber) AS EmployeeNumberGroupedBy,
GROUPING_ID(E.Department, E.EmployeeNumber, A.AttendanceMonth) AS EmployeeNumberGroupedID
from tblEmployee as E join tblAttendance as A
on E.EmployeeNumber = A.EmployeeNumber
group by ROLLUP (E.Department, E.EmployeeNumber, A.AttendanceMonth)
order by Department, EmployeeNumber, AttendanceMonth


select E.Department, E.EmployeeNumber, A.AttendanceMonth as AttendanceMonth, sum(A.NumberAttendance) as NumberAttendance,
GROUPING(E.EmployeeNumber) AS EmployeeNumberGroupedBy,
GROUPING_ID(E.Department, E.EmployeeNumber, A.AttendanceMonth) AS EmployeeNumberGroupedID
from tblEmployee as E join tblAttendance as A
on E.EmployeeNumber = A.EmployeeNumber
group by GROUPING SETS ((E.Department, E.EmployeeNumber, A.AttendanceMonth), (E.Department), ())
order by coalesce(Department, 'zzzzzzz'), coalesce(E.EmployeeNumber, 99999), coalesce(AttendanceMonth,'2100-01-01')

select E.Department, E.EmployeeNumber, A.AttendanceMonth as AttendanceMonth, sum(A.NumberAttendance) as NumberAttendance,
GROUPING(E.EmployeeNumber) AS EmployeeNumberGroupedBy,
GROUPING_ID(E.Department, E.EmployeeNumber, A.AttendanceMonth) AS EmployeeNumberGroupedID
from tblEmployee as E join tblAttendance as A
on E.EmployeeNumber = A.EmployeeNumber
group by GROUPING SETS ((E.Department, E.EmployeeNumber, A.AttendanceMonth), (E.Department), ())
order by CASE WHEN Department       IS NULL THEN 1 ELSE 0 END, Department, 
         CASE WHEN E.EmployeeNumber IS NULL THEN 1 ELSE 0 END, E.EmployeeNumber, 
         CASE WHEN AttendanceMonth  IS NULL THEN 1 ELSE 0 END, AttendanceMonth


BEGIN TRAN
CREATE TABLE tblGeom
(GXY geometry,
Description varchar(30),
IDtblGeom int CONSTRAINT PK_tblGeom PRIMARY KEY IDENTITY(1,1))
INSERT INTO tblGeom
VALUES (geometry::STGeomFromText('POINT (3 4)', 0),'First point'),
       (geometry::STGeomFromText('POINT (3 5)', 0),'Second point'),
	   (geometry::Point(4, 6, 0),'Third Point'),
	   (geometry::STGeomFromText('MULTIPOINT ((1 2), (2 3), (3 4))', 0), 'Three Points')

Select * from tblGeom

ROLLBACK TRAN

begin tran
create table tblGeom
(GXY geometry,
Description varchar(20),
IDtblGeom int CONSTRAINT PK_tblGeom PRIMARY KEY IDENTITY(1,1))
insert into tblGeom
VALUES (geometry::STGeomFromText('POINT (3 4)', 0),'First point'),
       (geometry::STGeomFromText('POINT (3 5)', 0),'Second point'),
	   (geometry::Point(4, 6, 0),'Third Point'),
	   (geometry::STGeomFromText('MULTIPOINT ((1 2), (2 3), (3 4))', 0),'Three Points')

SELECT * from tblGeom

select IDtblGeom, GXY.STGeometryType() as MyType
, GXY.STStartPoint().ToString() as StartingPoint
, GXY.STEndPoint().ToString() as EndingPoint
, GXY.STPointN(1).ToString() as FirstPoint
, GXY.STPointN(2).ToString() as SecondPoint
, GXY.STPointN(1).STX as FirstPointX
, GXY.STPointN(1).STY as FirstPointY
, GXY.STNumPoints() as NumberPoints
from tblGeom

DECLARE @g as geometry
DECLARE @h as geometry

select @g = GXY from tblGeom where IDtblGeom = 1
select @h = GXY from tblGeom where IDtblGeom = 3
select @g.STDistance(@h) as MyDistance

ROLLBACK TRAN


begin tran
create table tblGeom
(GXY geometry,
Description varchar(20),
IDtblGeom int CONSTRAINT PK_tblGeom PRIMARY KEY IDENTITY(5,1))
insert into tblGeom
VALUES (geometry::STGeomFromText('LINESTRING (1 1, 5 5)', 0),'First line'),
       (geometry::STGeomFromText('LINESTRING (5 1, 1 4, 2 5, 5 1)', 0),'Second line'),
	   (geometry::STGeomFromText('MULTILINESTRING ((1 5, 2 6), (1 4, 2 5))', 0),'Third line'),
	   (geometry::STGeomFromText('POLYGON ((4 1, 6 3, 8 3, 6 1, 4 1))', 0), 'Polygon'),
	   (geometry::STGeomFromText('CIRCULARSTRING (1 0, 0 1, -1 0, 0 -1, 1 0)', 0), 'Circle')
SELECT * FROM tblGeom
rollback tran

begin tran
create table tblGeom
(GXY geometry,
Description varchar(20),
IDtblGeom int CONSTRAINT PK_tblGeom PRIMARY KEY IDENTITY(5,1))
insert into tblGeom
VALUES (geometry::STGeomFromText('LINESTRING (1 1, 5 5)', 0),'First line'),
       (geometry::STGeomFromText('LINESTRING (5 1, 1 4, 2 5, 5 1)', 0),'Second line'),
	   (geometry::STGeomFromText('MULTILINESTRING ((1 5, 2 6), (1 4, 2 5))', 0),'Third line'),
	   (geometry::STGeomFromText('POLYGON ((4 1, 6 3, 8 3, 6 1, 4 1))', 0), 'Polygon'),
	   (geometry::STGeomFromText('CIRCULARSTRING (1 0, 0 1, -1 0, 0 -1, 1 0)', 0), 'Circle')
SELECT * FROM tblGeom



select IDtblGeom, GXY.STGeometryType() as MyType
, GXY.STStartPoint().ToString() as StartingPoint
, GXY.STEndPoint().ToString() as EndingPoint
, GXY.STPointN(1).ToString() as FirstPoint
, GXY.STPointN(2).ToString() as SecondPoint
, GXY.STPointN(1).STX as FirstPointX
, GXY.STPointN(1).STY as FirstPointY
, GXY.STBoundary().ToString() as Boundary
, GXY.STLength() as MyLength
, GXY.STNumPoints() as NumberPoints
from tblGeom

DECLARE @g as geometry
select @g = GXY from tblGeom where IDtblGeom = 5

select IDtblGeom, GXY.STIntersection(@g).ToString() as Intersection
, GXY.STDistance(@g) as DistanceFromFirstLine
from tblGeom

select GXY.STUnion(@g), Description
from tblGeom
where IDtblGeom = 8 

rollback tran


