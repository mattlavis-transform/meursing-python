import json
import sys
import classes.globals as g
from classes.database import Database
from classes.meursing_additional_code import MeursingAdditionalCode, DatabaseRow

sql = """
select mac.additional_code,
mtcc.row_column_code, mht.description as heading_description, mtcc.subheading_sequence_number 
from meursing_additional_codes mac, meursing_table_cell_components mtcc,
meursing_heading_texts mht
where mac.meursing_additional_code_sid = mtcc.meursing_additional_code_sid
and mtcc.row_column_code = mht.row_column_code
and mtcc.heading_number = mht.meursing_heading_number
and mtcc.heading_number = 10
order by mht.row_column_code, mtcc.subheading_sequence_number, mac.additional_code
"""

d = Database()
codes = []
rows = d.run_query(sql)
for row in rows:
    code = DatabaseRow(row[0], row[1], row[2], row[3])
    codes.append(code)

meursing_codes = {}
for code in codes:
    key = "key_" + code.additional_code
    if key in meursing_codes:
        meursing_code = meursing_codes[key]
        if code.row_column_code == 0: # This is a row
            meursing_code["milk_fat"] = code.milk_fat
            meursing_code["milk_protein"] = code.milk_protein
        else: # This is a column
            meursing_code["starch"] = code.starch
            meursing_code["sucrose"] = code.sucrose
    else:
        meursing_code = dict() # MeursingAdditionalCode()
        if code.row_column_code == 0: # This is a row
            meursing_code["milk_fat"] = code.milk_fat
            meursing_code["milk_protein"] = code.milk_protein
        else: # This is a column
            meursing_code["starch"] = code.starch
            meursing_code["glucose"] = code.glucose
        
        meursing_codes[key] = meursing_code


with open('data/meursing_codes.json', 'w') as outfile:
    json.dump(meursing_codes, outfile, indent=4)
    
print("Done")