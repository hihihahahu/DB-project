DROP TABLE IF EXISTS UnemploymentStat;
DROP TABLE IF EXISTS CrimeStat;
DROP TABLE IF EXISTS Population;
DROP VIEW IF EXISTS CrimeTotal
DROP VIEW IF EXISTS CrimeRate

CREATE TABLE UnemploymentStat(
	County VARCHAR(255),
	Year INTEGER,
	Month INTEGER,
	--LaborForce INTEGER, --will be accessed via view
	Employed INTEGER,
	Unemployed INTEGER,
	--UnemploymentRate FLOAT, --will be accessed via view
	PRIMARY KEY(County, Year, Month)
);

CREATE TABLE CrimeStat(
        County VARCHAR(255),
		Agency VARCHAR(255),
        Year INTEGER,
		--IndexTotal INTEGER, --will be accessed via view
		--ViolentTotal INTEGER, --will be accessed via view
        Murder INTEGER,
        Rape INTEGER,
        Robbery INTEGER,
        AggravatedAssualt INTEGER,
		--PropertyTotal INTEGER, --will be accessed via view
        Bulglary INTEGER,
        Larceny INTEGER,
        MotorTheft INTEGER,
		Region VARCHAR(255),
        PRIMARY KEY(County, Agency, Year)
);

CREATE TABLE Population(
		County VARCHAR(255),
		Year INTEGER,
		Population INTEGER,
		PRIMARY KEY(County, Year)
);

CREATE VIEW CrimeTotal AS 
	SELECT County, Agency, Year,
   		   Murder + Rape + Robbery + AggravatedAssualt AS ViolentTotal,
           Bulglary + Larceny + MotorTheft AS PropertyTotal,
           Murder + Rape + Robbery + AggravatedAssualt + Bulglary + Larceny + MotorTheft AS IndexTotal
	FROM crimeStat

CREATE VIEW CrimeRate AS
	SELECT County, Year, ViolentTotal/(Population/100000) AS ViolentRate, PropertyTotal/(Population/100000) AS PropertyRate, IndexTotal/(Population/100000) AS IndexRate
	FROM Population NATURAL JOIN
		(SELECT County, Year,
			    SUM(ViolentTotal) AS ViolentTotal,
			    SUM(PropertyTotal) AS PropertyTotal,
			    SUM(IndexTotal) AS IndexTotal
		 FROM CrimeTotal
		 GROUP BY County, Year) CrimeCount

