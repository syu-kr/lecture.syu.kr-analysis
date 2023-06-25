#
#     ____                  __________
#    / __ \_   _____  _____/ __/ / __ \_      __
#   / / / / | / / _ \/ ___/ /_/ / / / / | /| / /
#  / /_/ /| |/ /  __/ /  / __/ / /_/ /| |/ |/ /
#  \____/ |___/\___/_/  /_/ /_/\____/ |__/|__/
# 
#  The copyright indication and this authorization indication shall be
#  recorded in all copies or in important parts of the Software.
# 
#  @author 0verfl0w767
#  @link https://github.com/0verfl0w767
#  @license MIT LICENSE
#
import os
import json

from utils.Logger import Logger

LOGGER = Logger()

LOGGER.logo()

RED_TEXT = "\033[1;91m"
GREEN_TEXT = "\033[1;92m"
YELLOW_TEXT = "\033[1;93m"
PURPLE_TEXT = "\033[45m"
RESET_TEXT = "\033[0m"

name = ""
data_path = ""

with open("config.json", "r", encoding = "utf-8") as f:
  JSON_DATA = json.load(f)
  name = JSON_DATA["professor-name"]
  data_path = JSON_DATA["data-path"]

REAL_PATH = data_path
YEARS = os.path.abspath(REAL_PATH)

for YEAR in os.listdir(YEARS):
  SEMESTERS = os.path.abspath(YEARS + "\\" + YEAR)
  
  for SEMESTER in os.listdir(SEMESTERS):
    COLLEGES = os.path.abspath(YEARS + "\\" + YEAR + "\\" + SEMESTER)
    datas = []
    
    for COLLEGE in os.listdir(COLLEGES):
      if COLLEGE == "전체대학" or COLLEGE == "학부(과).json":
        continue
      
      UNDERGRADUATES = os.path.abspath(YEARS + "\\" + YEAR + "\\" + SEMESTER + "\\" + COLLEGE)
      
      for UNDERGRADUATE in os.listdir(UNDERGRADUATES):
        DATA_PATH = os.path.abspath(YEARS + "\\" + YEAR + "\\" + SEMESTER + "\\" + COLLEGE + "\\" + UNDERGRADUATE)
        
        with open(DATA_PATH, "r", encoding = "utf-8") as f:
          FILE_DATAS = json.load(f)
          
          if not FILE_DATAS["api"]:
            continue
          
          for DATA in FILE_DATAS["api"]:
            # if "컴퓨터"  in DATA["학부(과)"]:
            #   datas.append(DATA["교수명"])
            if DATA["교수명"] == name:
              datas.append(DATA["과목명"])
    
    if not datas:
      LOGGER.info(YEAR + " " + SEMESTER + " " + RED_TEXT + "분석된 정보가 없습니다." + RESET_TEXT)
    else:
      LOGGER.info(YEAR + " " + SEMESTER + " " + YELLOW_TEXT + ", ".join(list(set(datas))) + RESET_TEXT)
    