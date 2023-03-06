CREATE TABLE SQLBackupRestoreTest (
	ID INT NOT NULL PRIMARY KEY,
	loginname VARCHAR(100) NOT NULL,
	logindate DATETIME NOT NULL DEFAULT getdate()
)
GO
select *  from SQLBackupRestoreTest
insert into SQLBackupRestoreTest (ID,loginname) values (1, 'test1')
insert into SQLBackupRestoreTest (ID,loginname) values (2, 'test2')
insert into SQLBackupRestoreTest (ID,loginname) values (3, 'test3')
insert into SQLBackupRestoreTest (ID,loginname) values (4, 'test4')
insert into SQLBackupRestoreTest (ID,loginname) values (5, 'test5')
insert into SQLBackupRestoreTest (ID,loginname) values (6, 'test6')

insert into SQLBackupRestoreTest (ID,loginname) values (7, 'test7')
insert into SQLBackupRestoreTest (ID,loginname) values (8, 'test8')
insert into SQLBackupRestoreTest (ID,loginname) values (9, 'test9')
insert into SQLBackupRestoreTest (ID,loginname) values (10, 'test10')

insert into SQLBackupRestoreTest (ID,loginname) values (11, 'test11')
insert into SQLBackupRestoreTest (ID,loginname) values (12, 'test12')
insert into SQLBackupRestoreTest (ID,loginname) values (13, 'test13')
USE [master]
RESTORE DATABASE [AdventureWorks2016] FROM  DISK = N'C:\SQL_BACKUPS\AdventureWorks2016_full.BAK' WITH  FILE = 1,  NORECOVERY,  NOUNLOAD,  STATS = 5