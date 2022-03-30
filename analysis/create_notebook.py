import nbformat as nbf
#from config import demographics


nb = nbf.v4.new_notebook()


imports = """
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from IPython.display import HTML
from IPython.display import Markdown as md
from IPython.core.display import HTML as Center
from config import dbconn, dataset, columns_to_describe
from IPython.display import Image, display
from utilities import *
%matplotlib inline

import pyodbc
import os
from datetime import date, datetime

#from utilities import *
from sense_checking import *

pd.set_option('display.max_colwidth', 250)

# get the server credentials
dbconn = os.environ.get('FULL_DATABASE_URL', None).strip('"')

"""

header = """
display(
md("# Data Plausibility Check for {dataset}"),
md(f"Note: all row/patient counts are rounded to the nearest 10 and counts <=5 removed"),
)
"""

methods = """
display(
md("### Methods"),
md(f"The {dataset} dataset has been linked to patients in OpenSAFELY-TPP, covering 40% of England's population."),
md(f"All analytical code and output is available for inspection at the [OpenSAFELY GitHub repository](https://github.com/opensafely)")
)
"""

notebook_run_date = """\
display(
md(f"This notebook was run on {date.today().strftime('%Y-%m-%d')}"\
    "and reflects the dataset at this date, "\
    "but has been filtered to reflect the original data submission (`'Received' <= 2022-01-24`)."
    )
)"""

get_data = """
image_paths['total'] = '../output/joined/plot_total.png'
"""
#image_paths = {d: f'../output/joined/plot_{d}.png' for d in demographics}

schema = """
display(md("### Schema"))
get_schema(dbconn, table=dataset, where=schema_filter)
"""

column_descriptions = """
display(md("### Column Summaries"))

counts_of_distinct_values(dbconn, table=dataset, 
    columns=columns_to_describe["columns"], 
    threshold=columns_to_describe["threshold"], 
    where=columns_to_describe["where"],
    include_counts=columns_to_describe["include_counts"]
    )
"""

nb['cells'] = [
    nbf.v4.new_code_cell(imports),
    nbf.v4.new_code_cell(header),
    nbf.v4.new_code_cell(methods),
    nbf.v4.new_code_cell(get_data),
    nbf.v4.new_code_cell(notebook_run_date),
    nbf.v4.new_code_cell(schema),
    nbf.v4.new_code_cell(column_descriptions),
    ]

counter = """\
i=0
"""

# nb['cells'].append(nbf.v4.new_code_cell(counter))

# for d in range(len(demographics)):
#     cell_counts = """\
#     display(
#     md(f"## Breakdown by {demographics[i]}")
#     )
   
#     """
#     nb['cells'].append(nbf.v4.new_code_cell(cell_counts))
    
#     cell_plot = """\
#     display(Image(filename=image_paths[demographics[i]]))
#     i+=1
#     """
#     nb['cells'].append(nbf.v4.new_code_cell(cell_plot))


nbf.write(nb, 'analysis/Test_Notebook.ipynb')
