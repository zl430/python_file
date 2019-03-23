# -*- coding: utf-8 -*-
import os
import re
def gci(filepath):
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath, fi)
        if os.path.isdir(fi_d):
            gci(fi_d)
        else:
            file_name = os.path.join(filepath, fi_d)
            file = open(file_name, 'rb')
            while True:
                f = str(file.readline(), encoding="utf-8")
            # abc = re.findall('-\S+'+'[\u4e00-\u9fa5]..\S*', str(f))
            # aaa = "".join(abc).replace("\r", "")
                find_count = 0
                # if re.findall(r'(.*[\u4E00-\u9FA5]+)|([\u4E00-\u9FA5]+.*)', str(f)):
                # if re.findall(r'sendResponse\(new ResponseResult\(1\, ("[\u4E00-\u9FA5]+").*|static.*([\u4E00-\u9FA5]+).*', str(f)):
                if re.findall(r'print\(|error\(', str(f)):
                    continue
                else:
                    if re.findall(r'(.*"[\u4E00-\u9FA5]+")|("[\u4E00-\u9FA5]+.*")', str(f)):
                       # outfile.write(f)
                       print(file_name)
                       # write = open('E:/test_file.txt', 'a', encoding="utf-8")
                       write = open('E:/kson_file.txt', 'a', encoding="utf-8")
                       write.writelines(file_name)
                       print(f)
                       write.writelines(f)
                       write.close()
                       find_count += 1
                    if not f:
                        break
            # over = re.findall('\S*'+'[\u4e00-\u9fa5]*', str(f))
            # # print(over)
            # if over != []:
            #     print(file_name)
            #     print("".join(over))
# gci('E:/SVN/file/cathunter-client/src')
# gci('C:/Users/zuolei/Desktop/表文件/src')
gci('C:/Users/zuolei/Desktop/表文件/src/aaa')
#----------------------------------------------------------------------------
# def gci(filepath):
#     files = os.listdir(filepath)
#     for fi in files:
#         fi_d = os.path.join(filepath, fi)
#         if os.path.isdir(fi_d):
#             gci(fi_d)
#         else:
#             file_name = os.path.join(filepath, fi_d)
#             file = open(file_name, 'rb')
#             while True:
#                 f = str(file.readline(), encoding="utf-8")
#                 find_count = 0
#             #     # if re.findall(r'(.*[\u4E00-\u9FA5]+)|([\u4E00-\u9FA5]+.*)', str(f)):
#                 if re.findall(r'^-\S*', str(f)):
#                     continue
#                 else:
#                     if re.search(r'["\u4E00-\u9FA5"]', str(f)):
#                         print(f)
#                         write = open('E:/lua_file.txt', 'a', encoding="utf-8")
#                         write.writelines(file_name)
#                         write.writelines(f)
#                         write.close()
#                         find_count += 1
#                     if not f:
#                         break
#                     # over = re.findall('\S*'+'[\u4e00-\u9fa5]*', str(f))
#             # print(over)
#             # if over != []:
#             #     print(file_name)
#             #     print("".join(over))
# gci('E:/SVN/file/cathunter-client/src/activity')
# # gci('C:/Users/zuolei/Desktop/表文件/src')