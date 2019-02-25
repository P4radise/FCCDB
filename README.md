# FCCDB

Pull FCC data from https://wireless.fcc.gov to Onevizion and keep it in sync

## Requirements (scripts and schedule)

- Bash
- GNU Awk (gawk) 3.1.7+
- wget
- curl
- split (GNU coreutils) 8.22+
- python 2/3 (parse json values, run q tool)

## Third party software

* q (https://github.com/harelba/q)

## Manual installation

Run components import with ComponentsPackage.xml 

Add new trackors to Trackor Tree.
 
 Trackor Tree:
 ```
	Registration -> History
	Registration -> Entity
	Registration -> FCC Remarks
	Registration -> FCC Special Conditions
```

Setup import parameters at new Imports.

- Add a new integration on Integration page using repository URL: https://github.com/IKAMTeam/FCCDBintHub
- Recommended schedule for daily sync is 0 0 3 * * ?
- Specify instllation url and credentials in SettingsFile.integration 

SettingsFile.integration:
```
SET=daily
UN=username
PWD=password
URL=https://name.onevizion.com
```

- SET is type of the integration.
- UN - API user name
- PWD - API password

Set “full” instead of “daily” for Full import.
