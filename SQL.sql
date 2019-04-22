DROP TABLE IF EXISTS UnemploymentStat;DROP TABLE IF EXISTS CrimeStat;DROP TABLE IF EXISTS Population;DROP VIEW IF EXISTS CrimeTotal;DROP VIEW IF EXISTS CrimeRate;CREATE TABLE UnemploymentStat(	County VARCHAR(255),	Year INTEGER,	Month INTEGER,	--LaborForce INTEGER, --will be accessed via view	Employed INTEGER,	Unemployed INTEGER,	--UnemploymentRate FLOAT, --will be accessed via view	PRIMARY KEY(County, Year, Month));CREATE TABLE CrimeStat(        County VARCHAR(255),		Agency VARCHAR(255),        Year INTEGER,		--IndexTotal INTEGER, --will be accessed via view		--ViolentTotal INTEGER, --will be accessed via view        Murder INTEGER,        Rape INTEGER,        Robbery INTEGER,        AggravatedAssualt INTEGER,		--PropertyTotal INTEGER, --will be accessed via view        Bulglary INTEGER,        Larceny INTEGER,        MotorTheft INTEGER,		Region VARCHAR(255),        PRIMARY KEY(County, Agency, Year));CREATE TABLE Population(		County VARCHAR(255),		Year INTEGER,		Population INTEGER,		PRIMARY KEY(County, Year));CREATE VIEW CrimeTotal AS 	SELECT County, Year,   		   SUM(Murder + Rape + Robbery + AggravatedAssualt) AS ViolentTotal,           SUM(Bulglary + Larceny + MotorTheft) AS PropertyTotal,           SUM(Murder + Rape + Robbery + AggravatedAssualt + Bulglary + Larceny + MotorTheft) AS IndexTotal	FROM CrimeStat    GROUP BY County, Year;CREATE VIEW CrimeRate AS	SELECT County, Year, 	cast(ViolentTotal/(cast(Population AS decimal)/100000) AS DECIMAL(16,2)) AS ViolentRate, 	cast(PropertyTotal/(cast(Population AS decimal)/100000) AS DECIMAL(16,2)) AS PropertyRate, 	cast(IndexTotal/(cast(Population AS decimal)/100000)  AS DECIMAL(16,2)) AS IndexRate	FROM Population NATURAL JOIN		(SELECT County, Year,			    SUM(ViolentTotal) AS ViolentTotal,			    SUM(PropertyTotal) AS PropertyTotal,			    SUM(IndexTotal) AS IndexTotal		 FROM CrimeTotal		 GROUP BY County, Year) CrimeCount;		 --CREATE VIEW UnemploymentTable AS--		 SELECT County, Year, cast(cast(total_unemployed AS decimal)/cast(LaborForce AS decimal)AS DECIMAL(16,3)) * 100 AS UnemploymentRate--		 FROM (SELECT County, Year, SUM(Employed) + SUM(Unemployed) AS LaborForce,--		 	   SUM(Employed) AS total_employed, SUM(Unemployed) AS total_unemployed--			   FROM Unemploymentstat--			   GROUP BY County, Year--		 ) AS temp;CREATE VIEW UnemploymentTable AS	SELECT County, Year, CAST((CAST(AVG(MonthlyRate) AS DECIMAL(16,3)) * 100) AS DECIMAL(16,1)) AS UnemploymentRate		FROM ( 			SELECT CAST((CAST(Unemployed AS DECIMAL)/CAST((Employed+Unemployed) AS DECIMAL)) AS DECIMAL(10,2)) AS MonthlyRate, County, Year			FROM UnemploymentStat) AS UnemployedMonthRate			GROUP BY County, Year;