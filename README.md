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

- Add a new integration on Integration page using repository URL: https://github.com/ov-integrations/FCCDB
- Recommended schedule for daily sync is 0 0 3 * * ?
- Specify installation url and credentials in settings 

settings:
```
SET=daily
USERNAME=username
PWD=password
URL=https://name.onevizion.com
FULL=ftp://wirelessftp.fcc.gov/pub/uls/complete/r_tower.zip
SUN=ftp://wirelessftp.fcc.gov/pub/uls/daily/r_tow_sun.zip
MON=ftp://wirelessftp.fcc.gov/pub/uls/daily/r_tow_mon.zip
TUE=ftp://wirelessftp.fcc.gov/pub/uls/daily/r_tow_tue.zip
WED=ftp://wirelessftp.fcc.gov/pub/uls/daily/r_tow_wed.zip
THU=ftp://wirelessftp.fcc.gov/pub/uls/daily/r_tow_thu.zip
FRI=ftp://wirelessftp.fcc.gov/pub/uls/daily/r_tow_fri.zip
SAT=ftp://wirelessftp.fcc.gov/pub/uls/daily/r_tow_sat.zip
```

- SET is type of the integration.
- USERNAME - API user name
- PWD - API password
- FULL, SUN, MON, TUE, WED, THU, FRI, SAT - URLs of the databases

Set “full” instead of “daily” for Full import.
