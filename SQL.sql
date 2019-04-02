DROP TABLE IF EXISTS UnemploymentStat;
DROP TABLE IF EXISTS CrimeStat;
DROP TABLE IF EXISTS CrimeByPopulation;


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
        Firearm INTEGER,
		Region VARCHAR(255),
        PRIMARY KEY(County, Agency, Year)
);

CREATE TABLE CrimeByPopulation(
		County VARCHAR(255),
		Year INTEGER,
		Population INTEGER,
		PRIMARY KEY(County, Year)
);


