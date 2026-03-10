from json import dumps

tables = { 
    1: ['Jiho', False], 
    2: [], 
    3: [], 
    4: [], 
    5: [], 
    6: [], 
    7: [], 
} 

def assign_table(table_number, name, vip_status = False):
    tables[table_number].append(name)
    tables[table_number].append(vip_status)

assign_table(6, 'Yoni', False)
assign_table(4, 'Карл')

print(tables)