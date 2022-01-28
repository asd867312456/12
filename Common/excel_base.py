from xlrd import open_workbook
class Doexcel():

    def excel_data_list(self, filename, sheetname):
        data_list = []
        wb = open_workbook(filename)  # 打开excel
        sh = wb.sheet_by_name(sheetname)  # 定位工作表
        header = sh.row_values(0)   # 获取标题行的数据
        for i in range(1, sh.nrows):   # 跳过标题行，从第二行开始获取数据
            col_datas = dict(zip(sh.row_values(0), sh.row_values(i)))   # 将标题和每一行的数据，组装成字典
            data_list.append(col_datas)   # 将字典添加到列表中 ，列表嵌套字典，相当于每个字典的元素都是一个列表（也就是一行数据）
        return data_list

    def get_test_data(self, data_list, case_id):
        '''
        :param data_list: 工作表的所有行数据
        :param case_id: 用例id，用来判断执行哪几条case。如果id=all ，那就执行所有用例；否则，执行列表参数中指定的用例
        :return:  返回最终要执行的测试用例
        '''
        if case_id == 'all':    
            final_data = data_list
        else:
            final_data = []
            for item in data_list:
                if item['id'] in case_id:
                    final_data.append(item)
        return final_data
if __name__ == "__main__":
    data_list=Doexcel().excel_data_list('E:/12/Config/oms_request.xls',"Sheet1")
    # print(data_list)
    final_data=Doexcel().get_test_data(data_list, "test_001,test_002")
    print(final_data)
    print(final_data[0]['url'])
    print(final_data[1]['url'])
