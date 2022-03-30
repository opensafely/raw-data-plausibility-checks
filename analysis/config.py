
# enter table name
table = "therapeutics"

# enter filters for schema
# these are useful to (a) make the data size manageable (e.g. one month or year of data)
# and (b) look at a subset of interest e.g. patients with COVID
schema_filter = {"": "where CAST(Received AS DATE) <= '2022-01-24'",
         "_non_hospitalised": "where CAST(Received AS DATE) <= '2022-01-24' AND COVID_indication='non_hospitalised'"}

# columns to describe
columns_to_describe = {
    "columns": ["Diagnosis", "FormName", "Region", "Der_LoadDate", "AgeAtReceivedDate", "Count"],
    "threshold": 50,
    "where":"CAST(Received AS DATE) <= '2022-01-24'", 
    "include_counts":False,
    }
    
