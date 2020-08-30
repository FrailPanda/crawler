import custom_module
import simplejson as json
import uuid
import xlrd

def check_null_value(item):
    if item == '':
        return None
    else:
        return item

def init():
    wb = xlrd.open_workbook('../xlsx/2020-2.xlsx')
    sh = wb.sheet_by_index(0)

    data_list = []

    for row_num in range(1, sh.nrows):
        row_value = sh.row_values(row_num)

        dic = {}

        # id
        dic['id'] = str(uuid.uuid4())

        # code
        dic['code'] = row_value[7] + '-' + row_value[8]

        # instructor
        dic['instructor'] = row_value[10]

        # department
        dic['department'] = row_value[1]

        # major
        dic['major'] = row_value[2]

        # classification
        dic['classification'] = row_value[5]

        # year
        dic['year'] = row_value[3]

        # credits
        dic['credits'] = float(row_value[11])

        # time_str
        dic['time_str'] = check_null_value(row_value[18])

        print(dic['time_str'])
        # times
        dic['times'] = custom_module.time_dict(dic['time_str'])

        # location
        dic['location'] = custom_module.convert_location(dic['time_str'])

        data_list.append(dic)


    # crawler 부분 추가
    wb = xlrd.open_workbook('../xlsx/output.csv')
    sh = wb.sheet_by_index(0)

    data_list = []

    for row_num in range(1, sh.nrows):
        row_value = sh.row_values(row_num)

        dic = {}


    j = json.dumps(data_list, ensure_ascii=False, indent=4)


    with open('../json/result.json', 'w', encoding='UTF-8-sig') as f:
        f.write(j)

if __name__ == "__main__":
    init()