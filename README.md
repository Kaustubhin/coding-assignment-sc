## Scenario 

https://github.com/codingo/Ransomware-Json-Dataset/blob/master/ransomware_overview.json
 
1. Given this JSON as a sample, how will you write a short script/program to process this json and store into databases
2. Explain selection of coding language and DB of your choice.
3. Given that its large set of data, how will you ensure that no records are missed when writing into the DB
4. In the case of duplicate entries, how will you handle them?
======================================================================
### Possible solution for given scenario
* **ransomware.sql** - To run SQL quries
* **data.json**  - Local copy of json file mentioned in above github link.
* **createdbfromjson.py** - To extract the key and insert data using data.json file
