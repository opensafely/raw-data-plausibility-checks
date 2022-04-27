# enter table name
table = "CodedEvent"

start_date = "2019-01-01"
end_date = "2022-03-01"

codelist_path = "codelists/user-bangzheng-creatinine.csv"


# enter filters for schema
# these are useful to (a) make the data size manageable (e.g. one month or year of data)
# and (b) look at a subset of interest e.g. patients with COVID
schema_filter = {
    "": "where CAST(ConsultationDate AS DATE) <= '2022-03-01'",
}

# columns to describe
columns_to_describe = {
    "columns": [
        "Diagnosis",
        "FormName",
        "Region",
        "Der_LoadDate",
        "AgeAtReceivedDate",
        "Count",
    ],
    "threshold": 50,
    "where": "CAST(Received AS DATE) <= '2022-01-24'",
    "include_counts": False,
}
