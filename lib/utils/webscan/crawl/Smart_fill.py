#-*- encoding:utf-8 -*-
#基于知识库自动填表

form_name_kb = {
    'admin' : ['username', 'user', 'userid', 'nickname', 'name'],
    '123456' : ['password', 'pass', 'pwd'],
    'test@test.com' : ['email', 'mail', 'usermail'],
    '13990112341' : ['mobile'],
    'Miscan' : ['conntent', 'text', 'query', 'search', 'data', 'comment'],
    'Miscan.test.test.com' : ['domain'],
    'http://Miscan.test.test.com' : ['link', 'url', 'website']
}

def smart_fill(variable_name):
    variable_name = variable_name.lower()
    flag = False
    for filled_value, variable_name_list in form_name_kb.items():
        for variable_name_db in variable_name_list:
            if(variable_name_db == variable_name):
                flag = True
                return filled_value
    if(not flag):
        msg = '[smart_fill] Falied to find a value for parameter with name "' + variable_name + '".'
        #log.debug(msg)
        return 'UNKNOWN'