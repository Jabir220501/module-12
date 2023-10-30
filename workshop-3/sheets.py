import gspread
# Set up credentials
gc = gspread.serviece_account(filename="credentials")
sh = gc.open_by_key("")
worksheet = sh.sheet1

res = worksheet.get_all_records()

# Create a new record
def create_record(data):
    worksheet.insert_row(data, 2)  

# Read all records
def read_records():
    return worksheet.get_all_records()

# Update a record
def update_record(row, data):
    worksheet.update("A" + str(row), data) 

# Delete a record
def delete_record(row):
    worksheet.delete_row(row)

# Example Usage
data_to_create = ["John Doe", 30, "New York"]
create_record(data_to_create)
print(read_records())
update_record(2, ["Jane Smith", 25, "Los Angeles"])
print(read_records())
delete_record(3)
print(read_records())
