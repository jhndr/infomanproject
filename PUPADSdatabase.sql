/* Create the database */
CREATE DATABASE  dtbPUPADS;

/* Use the created database */
USE dtbPUPADS;

/* Create the tables */
CREATE TABLE tblCourses (
  strCourseID varchar(10) PRIMARY KEY NOT NULL,
  strCourseName varchar(50) NOT NULL,
  intUnits integer(2) NOT NULL,
  strdeptCollege varchar(5) NOT NULL CHECK (strdeptCollege IN('CSC', 'CED', 'CSD', 'CEN', 'CCIS', 'CAB'))
);

CREATE TABLE tblScholars (
  strMembID varchar(10) PRIMARY KEY NOT NULL,
  strScholarID varchar(15) NOT NULL,
  strScholarType varchar(7) NOT NULL CHECK (strScholarType IN('Merit', 'RA10612', 'RA7687')),
  strFirstName varchar(50) NOT NULL,
  strMidName varchar(50),
  strLastName varchar(50) NOT NULL,
  datBirthdate DATE NOT NULL,
  strEmailAdd varchar(50) NOT NULL UNIQUE, 
  strPhoneNum char(11) NOT NULL,
  strAddress varchar(50) NOT NULL,
  strSchoolID varchar(15) NOT NULL,
  strCourseID varchar(10) NULL,
  intYearLvl integer(1) NULL,
  strStrtTerm DATE NOT NULL,
  strEndTerm DATE,
  FOREIGN KEY (strCourseID) REFERENCES tblCourses(strCourseID)
  ON UPDATE CASCADE
  ON DELETE CASCADE
);

CREATE TABLE tblExecutives (
  strComID varchar(10) PRIMARY KEY NOT NULL,
  strMembID varchar(10) NOT NULL,
  strComName varchar(30) NOT NULL CHECK (strComName IN('Operations', 'Communication', 'Finance')),
  strRoleName varchar(30) NOT NULL,
  FOREIGN KEY (strMembID) REFERENCES tblScholars(strMembID)
  ON UPDATE CASCADE
  ON DELETE CASCADE
);

CREATE TABLE tblOrgProjects (
  strProjID varchar(10) PRIMARY KEY NOT NULL,
  strProjName varchar(30) NOT NULL,
  strProjStatus varchar(2) NOT NULL CHECK (strProjStatus IN('NS','OG','CT')),
  decProjBudget decimal(7,2) NOT NULL,
  datProjStart DATE NOT NULL,
  datProjEnd DATE NOT NULL,
  strProjAddress varchar(50) NOT NULL,
  strComID varchar(10) NOT NULL,
  FOREIGN KEY (strComID) REFERENCES tblExecutives(strComID)
  ON UPDATE CASCADE
  ON DELETE CASCADE
);

CREATE TABLE tblOrgEvents (
  strEventID varchar(10) PRIMARY KEY NOT NULL,
  strEventName varchar(30) NOT NULL,
  strPrtcpntID varchar(10) NOT NULL,
  strPrtcpntName varchar(50) NOT NULL,
  datEvent DATE NOT NULL,
  strEventAdd varchar(50) NOT NULL, 
  strEventStatus varchar(2) NOT NULL CHECK (strEventStatus IN('NS','OG','CT')),
  decEventBudget decimal(7,2) NOT NULL,
  strComID varchar(10) NOT NULL,
  FOREIGN KEY (strComID) REFERENCES tblExecutives(strComID)
  ON UPDATE CASCADE
  ON DELETE CASCADE
);

CREATE TABLE tblOperations (
  strOpID varchar(10) PRIMARY KEY NOT NULL,
  strSubCom varchar(50) NOT NULL CHECK (strSubCom IN('Councilor', 'Technicals', 'Research and Development', 'Student Trainee Officers', 'Creatives')),
  strComID varchar(10) NOT NULL,
  FOREIGN KEY (strComID) REFERENCES tblExecutives(strComID)
  ON UPDATE CASCADE
  ON DELETE CASCADE
);

CREATE TABLE tblCommunications (
  strCmcID varchar(10) PRIMARY KEY NOT NULL,
  strSubCom varchar(50) NOT NULL CHECK (strSubCom IN('Councilor', 'Technicals', 'Research and Development', 'Student Trainee Officers', 'Creatives')),
  strComID varchar(10) NOT NULL,
  FOREIGN KEY (strComID) REFERENCES tblExecutives(strComID)
  ON UPDATE CASCADE
  ON DELETE CASCADE
);

CREATE TABLE tblFinance (
  strFinID varchar(10) PRIMARY KEY NOT NULL,
  strSubCom varchar(50) NOT NULL CHECK (strSubCom IN('Councilor', 'Technicals', 'Research and Development', 'Student Trainee Officers', 'Creatives')),
  strComID varchar(10) NOT NULL,
  FOREIGN KEY (strComID) REFERENCES tblExecutives(strComID)
  ON UPDATE CASCADE
  ON DELETE CASCADE
);

CREATE TABLE tblAdvisers (
  strAdvID varchar(10) PRIMARY KEY NOT NULL,
  datAdvStrt DATE NOT NULL,
  datAdvEnd DATE NOT NULL,
  strMembID varchar(10) NOT NULL,
  FOREIGN KEY (strMembID) REFERENCES tblScholars(strMembID)
  ON UPDATE CASCADE
  ON DELETE CASCADE
);

CREATE TABLE tblPartnerships (
  strPrtID varchar(10) PRIMARY KEY NOT NULL,
  strPrtName varchar(50) NOT NULL,
  strPrtEmail varchar(50) NOT NULL UNIQUE,
  strPrtPhoneNum char(11) NOT NULL,
  datPtr DATE NOT NULL,
  strComID varchar(10) NOT NULL,
  strProjID varchar(10),
  strEventID varchar(10),
  FOREIGN KEY (strComID) REFERENCES tblExecutives(strComID),
  FOREIGN KEY (strProjID) REFERENCES tblOrgProjects(strProjID),
  FOREIGN KEY (strEventID) REFERENCES tblOrgEvents(strEventID)
  ON UPDATE CASCADE
  ON DELETE CASCADE
);

 CREATE TABLE tblSponsorships (
  strSpnsrID varchar(10) PRIMARY KEY NOT NULL,
  strSpnsrName varchar(50) NOT NULL,
  strSpnsrEmail varchar(50) NOT NULL UNIQUE,
  strSpnsrPhoneNum char(11) NOT NULL,
  datSpnsr DATE NOT NULL,
  strComID varchar(10),
  strProjID varchar(10),
  strEventID varchar(10),
  FOREIGN KEY (strComID) REFERENCES tblExecutives(strComID),
  FOREIGN KEY (strProjID) REFERENCES tblOrgProjects(strProjID),
  FOREIGN KEY (strEventID) REFERENCES tblOrgEvents(strEventID)
  ON UPDATE CASCADE
  ON DELETE CASCADE
 );

/* Use the created database */
USE dtbPUPADS;

/* Insert sample values into tblCourses */
INSERT INTO tblCourses (strCourseID, strCourseName, intUnits, strdeptCollege) VALUES
('CSC101', 'Computer Science 101', 3, 'CSC'),
('CED102', 'Education 102', 3, 'CED'),
('CSD103', 'Science 103', 3, 'CSD'),
('CEN104', 'Engineering 104', 3, 'CEN'),
('CCIS105', 'Information Systems 105', 3, 'CCIS'),
('CAB106', 'Business 106', 3, 'CAB');

/* Insert sample values into tblScholars */
INSERT INTO tblScholars (strMembID, strScholarID, strScholarType, strFirstName, strMidName, strLastName, datBirthdate, strEmailAdd, strPhoneNum, strAddress, strSchoolID, strCourseID, intYearLvl, strStrtTerm, strEndTerm) VALUES
('M001', 'S001', 'Merit', 'John', 'A', 'Doe', '2000-01-01', 'john.doe@example.com', '09123456789', '123 Main St', 'STU001', 'CSC101', 1, '2023-06-01', NULL),
('M002', 'S002', 'RA10612', 'Jane', 'B', 'Smith', '2001-02-02', 'jane.smith@example.com', '09234567890', '456 Elm St', 'STU002', 'CED102', 2, '2023-06-01', NULL),
('M003', 'S003', 'RA7687', 'Alice', 'C', 'Johnson', '2002-03-03', 'alice.johnson@example.com', '09345678901', '789 Pine St', 'STU003', 'CSD103', 2, '2023-06-01', NULL),
('M004', 'S004', 'RA7687', 'Risa', 'M', 'Hontiveros', '1999-05-08', 'risahonti@example.com', '09874390254', '897 Cone Avenue', 'TEA004', NULL, NULL, '2023-06-01', NULL);


/* Insert sample values into tblExecutives */
INSERT INTO tblExecutives (strComID, strMembID, strComName, strRoleName) VALUES
('C001', 'M001', 'Operations', 'Manager'),
('C002', 'M002', 'Communication', 'Lead'),
('C003', 'M003', 'Finance', 'Treasurer');

/* Insert sample values into tblOrgProjects */
INSERT INTO tblOrgProjects (strProjID, strProjName, strProjStatus, decProjBudget, datProjStart, datProjEnd, strProjAddress, strComID) VALUES
('P001', 'Project Alpha', 'NS', 1000.00, '2024-01-01', '2024-06-01', '123 Project St', 'C001'),
('P002', 'Project Beta', 'OG', 2000.00, '2024-02-01', '2024-07-01', '456 Project St', 'C002'),
('P003', 'Project Gamma', 'CT', 1500.00, '2024-03-01', '2024-08-01', '789 Project St', 'C003');

/* Insert sample values into tblOrgEvents */
INSERT INTO tblOrgEvents (strEventID, strEventName, strPrtcpntID, strPrtcpntName, datEvent, strEventAdd, strEventStatus, decEventBudget, strComID) VALUES
('E001', 'Event Alpha', 'P001', 'John Doe', '2024-01-15', '123 Event St', 'NS', 500.00, 'C001'),
('E002', 'Event Beta', 'P002', 'Jane Smith', '2024-02-15', '456 Event St', 'OG', 1000.00, 'C002'),
('E003', 'Event Gamma', 'P003', 'Alice Johnson', '2024-03-15', '789 Event St', 'CT', 750.00, 'C003');

/* Insert sample values into tblOperations */
INSERT INTO tblOperations (strOpID, strSubCom, strComID) VALUES
('O001', 'Councilor', 'C001');

/* Insert sample values into tblCommunications */
INSERT INTO tblCommunications (strCmcID, strSubCom, strComID) VALUES
('CM001', 'Technicals', 'C002');

/* Insert sample values into tblFinance */
INSERT INTO tblFinance (strFinID, strSubCom, strComID) VALUES
('F001', 'Research and Development', 'C003');

/* Insert sample values into tblAdvisers */
INSERT INTO tblAdvisers (strAdvID, datAdvStrt, datAdvEnd, strMembID) VALUES
('A001', '2024-01-01', '2024-12-31', 'M004');

/* Insert sample values into tblPartnerships */
INSERT INTO tblPartnerships (strPrtID, strPrtName, strPrtEmail, strPrtPhoneNum, datPtr, strComID, strProjID, strEventID) VALUES
('PR001', 'Partner Alpha', 'partner.alpha@example.com', '09123456789', '2024-01-01', 'C001', 'P001', 'E001'),
('PR002', 'Partner Beta', 'partner.beta@example.com', '09234567890', '2024-02-01', 'C002', 'P002', 'E002'),
('PR003', 'Partner Gamma', 'partner.gamma@example.com', '09345678901', '2024-03-01', 'C003', 'P003', 'E003');

/* Insert sample values into tblSponsorships */
INSERT INTO tblSponsorships (strSpnsrID, strSpnsrName, strSpnsrEmail, strSpnsrPhoneNum, datSpnsr, strComID, strProjID, strEventID) VALUES
('S001', 'Sponsor Alpha', 'sponsor.alpha@example.com', '09123456789', '2024-01-01', 'C001', 'P001', 'E001'),
('S002', 'Sponsor Beta', 'sponsor.beta@example.com', '09234567890', '2024-02-01', 'C002', 'P002', 'E002'),
('S003', 'Sponsor Gamma', 'sponsor.gamma@example.com', '09345678901', '2024-03-01', 'C003', 'P003', 'E003');

