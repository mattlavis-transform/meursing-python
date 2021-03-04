import sys
import classes.globals as g


class MeursingAdditionalCode:
    def __init__(self):
        self.additional_code = None
        self.milk_fat = None
        self.milk_protein = None
        self.starch = None
        self.sucrose = None


class DatabaseRow:
    def __init__(self, additional_code, row_column_code, description, subheading_sequence_number):
        self.additional_code = additional_code
        self.row_column_code = int(row_column_code)
        self.description = description
        self.subheading_sequence_number = str(subheading_sequence_number)
        
        self.milk_fat = None
        self.milk_protein = None
        self.starch = None
        self.sucrose = None
        
        if self.row_column_code == 0:
            self.lookup_row()
        else:
            self.lookup_column()
            
    def lookup_row(self):
        self.milk_fat = g.rows_json[self.subheading_sequence_number]["milk_fat"]
        self.milk_protein = g.rows_json[self.subheading_sequence_number]["milk_protein"]

    def lookup_column(self):
        self.starch = g.columns_json[self.subheading_sequence_number]["starch"]
        self.sucrose = g.columns_json[self.subheading_sequence_number]["sucrose"]
