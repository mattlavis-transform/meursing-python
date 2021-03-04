# CDS Data Loader

This Python application is used to load the CDS files

## Installation

- Create and activate a virtual environment, e.g.

  `python3 -m venv venv/`
  `source venv/bin/activate`

- Install necessary Python modules 

  - autopep8==1.5.4
  - pycodestyle==2.6.0
  - toml==0.10.2

  via `pip3 install -r requirements.txt`
  
- Create 2 subfolders, one for the XML source (`xml`) and one for the CSV extracts (`csv`)

- No need for a database - all activities take place using ElementTree XML parser and store data locally as CSV for ease of testing.


## Usage

- Run the main.py file

  `python3 main.py`

  pip3 install meursing

- This runs through every XML file in the `xml` subfolder and extracts the core tables to CSV to check the validity of the data loaders.

- To date, it creates the following files (with their subsidiary elements):

  - additional_codes
  - base_regulations
  - certificates
  - footnotes
  - goods_nomenclatures
  - measures
  - quota order numbers
  - quota definitions
  - quota balances
  - quota suspension periods
  - quota blocking periods

- More will be delivered in good time ... next priority
  - quota-related events

- There is no data available for:
  
  - geographical areas and memberships (quite urgent)
  - modification regulations