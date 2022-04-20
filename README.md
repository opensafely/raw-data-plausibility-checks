# Raw data plausibility checking


## About the OpenSAFELY framework

The OpenSAFELY framework is a secure analytics platform for
electronic health records research in the NHS.

Instead of requesting access for slices of patient data and
transporting them elsewhere for analysis, the framework supports
developing analytics against dummy data, and then running against the
real data *within the same infrastructure that the data is stored*.
Read more at [OpenSAFELY.org](https://opensafely.org). 

To enable this, some exploration of raw data is required in order to 
implement new data as easy-to-use and well-documented functions for
end users. 

This repo contains (will contain) a template for performing plausibility
checking of datasets.

## How to use the template

1. 
2.  Make changes to the `config.py` in the analysis folder.
3.  
4.  This code can then be [run locally](https://docs.opensafely.org/en/latest/actions-pipelines/#running-your-code-locally) using the command `opensafely run run_all`
5.  This generates a notebook (ipynb) file
6.  Someone with L2/3 access can then clone the repository and run the notebook as per [these instructions](https://bennettinstitute-team-manual.pages.dev/tech-team/playbooks/opensafely-tpp-notebooks/).


## How to use the numeric values template

1.  Add desired codelist(s) to `codelists/codelists.txt`
2.  Download codelist(s) using `opensafely codelists update`
3.  Specify one codelist and other required information in `analysis/config_numeric_value_checks.py`.
4.  Generate the notebook (ipynb) file [locally](https://docs.opensafely.org/en/latest/actions-pipelines/#running-your-code-locally) using the command `opensafely run create_notebook_numeric`. Alternatively, run the `analysis/create_notebook_numeric_value_checks.py` file itself directly.
5.  Repeat steps 3-4 for each codelist.
5.  Commit the new & modified files to the repo.
6.  Someone with L2/3 access can then clone the repository and run the notebook as per [these instructions](https://bennettinstitute-team-manual.pages.dev/tech-team/playbooks/opensafely-tpp-notebooks/).
7.  Notebooks can be saved to html and made available for release.
