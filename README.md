# Snowflake-Data-Pipeline-Project-using-DBT-Python-Streams-Tasks
Kelly Anderson test data pipeline project using DBT, Python procedures, streams and tasks  

For this example of setting up a data pipeline in Snowflake using python and dbt.

![image](https://github.com/anderskd12/dbt_snowflake_testing/assets/49698565/77d73a33-2ebb-439e-b77a-acf1d3311d9a)


Overall 
1.  Setup snowflake, python, dbt
2.  Consume large dataset of San Fransisco employee compensation data (source:  https://catalog.data.gov/dataset/employee-compensation)
3.  Create a materialized view that transforms the large raw dataset to the information that we want to use in this project
4.  Add incremental data - this is created by using a Python worksheet in Snowflake and setting this up a procedure
5.  Track and add new rows to the total dataset by adding in our incremental data - mimic a daily or streaming data feed
6.  Combine data from a marketplace source to enhance our full set
7.  Create a final materialized view that creates our final output that we would like to analyze
8.  Add some visualization and metrics with our final dataset

Setup Steps - Snowflake account added - DBT is setup and ran in Github codespaces
1.  Snowflake information
  a. Setup database, schema, roles, and data warehouse - See worksheet for this setup steps
  
2.  Consume large dataset
  a.  Setup Stage (k_stage) - add in file using snowsql - see separate script for details in running this
  b.  Create KA_DB.K_ANALYTICS.EMP_COMP_FULL - Need to create from UI Stage - Column 'UNION' needs to be changed to 'UNIONID' (keyword)
  c.  Validate data and review - Should be 881K rows

3.  DBT Setup - Files are located in this Repo.
  a. Using a GitHub Codespace due to dbt install errors on local.  See files in this Repo for details on models setup

4.  Incremental data - See python worksheet in this repo for details on generating some random data.
 a.  This data adds data for two employee IDs that are already tracked and one new one.  Data added to df_sf.write.mode("append").save_as_table("EMPLOYEE_COMP_NEW_DATA") table
 b.  Setup this as a procedure and can setup as task to run regularly
     CALL Add_Random_Emp_Data();
 c.  Setup Stream to track these changes   
    Stream name:  stream KA_DB.K_ANALYTICS.STREAM_NEW_EMP_DATA

6.  Track incremental changes and merge transformed large dataset with incremental data changes
   For this - we create two tasks - one that runs the procedure to create new records (captured by stream)
        The second tasks moves any new records that aren't already found in the 'FULL' table.

 a.  Details:  TASK task_create_new_employee_data
              TASK:  task_load_new_employee_records

 b.  Testing:  See Stream Script for details

8.  Other ideas - Combine with Marketplace data

9.  Other ideas - Create final materialized view - can do this in dbt - with Marketplace data

10.  Other ideas - Add in visualizations and data analysis - possibly using Streamlit?  Or Tableau?  Both?

