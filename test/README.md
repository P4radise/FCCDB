# Test 

### Import Test

To test the Imports you can run CSV files from "data" folder.
- [Import] - [File]
- FCC (Reg) Registration Import - 1_RA-REG.csv
- FCC (Reg) Coordinate Tower Import - 2_CO-Tower-REG.csv
- FCC (Reg) Coordinate Array Import - 3_CO-Array-REG.csv
- FCC (Reg) Entity Import - 4_EN-REG.csv
- FCC (Reg) History Import - 5_HS-REG.csv
- FCC (Reg) Remarks Import - 6_RE-REG.csv
- FCC (Reg) Special Condition - 7_SC-REG.csv

### Integration Test

You can check count of new records by this SQL.
If count of records is 0, it means you have no new records and you need to check the Integration.

```sql
select count(*)
  from config_value_date
 where trunc(ts) between current_date - 7 and current_date
   and config_field_id = (select config_field_id from config_field where config_field_name = 'RA_DATE_CONSTRUCTED')
   and trunc(value_date) between current_date - 7 and current_date;
```

Also you can use **a Rule** from components.xml to run an automated test. **The Rule** checks the number of new records and sends a notification to the specified email.
