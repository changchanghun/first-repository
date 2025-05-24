from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

# Chrome 드라이버 초기화
driver = webdriver.Chrome()

base_url = "https://www.lguplus.com/benefit-membership"

all_data = []
driver.get(base_url)
time.sleep(3)

li_list = driver.find_elements(By.CSS_SELECTOR, ".c-tab-slidemenu li")
click_li = li_list[1]
click_a = click_li.find_element(By.TAG_NAME, "a")
click_a.click() 
time.sleep(3)

sec_list = driver.find_elements(By.CSS_SELECTOR, '.c-tabcontent-box ul[role="tablist"] li')[1:]

membership_box = {}
temp = {}
for idx, vlu in enumerate(sec_list):
    vlu.click()
    time.sleep(1)
    
    try:
        next_check = driver.find_element(By.CSS_SELECTOR, ".pagination .active")
        
        if next_check:
            ## 근데 애초에 next_li 클릭도 제대로 안되는데 어떠케함 ? 
            next_li = next_check.find_element(By.XPATH, "(following-sibling::li)[1]")
            next_li_total = next_check.find_elements(By.XPATH, "following-sibling::li")
            # 1.전체 li를 가져옴

            # li를 전체 가져와서 마지막에서 두번째 li가 disabled가 나올때까지 반복한다.
            target_list = driver.find_elements(By.CSS_SELECTOR, '.c-tabmenu-slide-wrap .affiliate-list li') # 데이터 추출

        membership_box[idx] = {}
        temp[idx] = {}

        # 2. 마지막에서 두번째 li가 disabled가 아니면 반복문을 실행하고 next_li 클릭 다시 반복 
        # 3. 마지막에서 두번째 li가 disabled이면 데이터모으고 반복문 끝냄
        for target in target_list:
            target_text = target.find_element(By.CSS_SELECTOR, '.tit').text     # 혜택 이름
            target_won = target.find_element(By.CSS_SELECTOR, '.won').text      # 혜택 내용

            membership_box[idx][target_text] = target_won

        if "disabled" not in next_li.get_attribute("class"):
            temp[idx] = next_li_total
            # 한번에 3페이지까지 넘어가서 문제가됌
            next_li.click()
            # 한번에 3페이지까지 넘어가서 문제가됌
            time.sleep(3)

            target_list = driver.find_elements(By.CSS_SELECTOR, '.c-tabmenu-slide-wrap .affiliate-list li') 
            
            for target in target_list:
                target_text = target.find_element(By.CSS_SELECTOR, '.tit').text     # 혜택 이름
                target_won = target.find_element(By.CSS_SELECTOR, '.won').text      # 혜택 내용
                membership_box[idx][target_text] = target_won
            
            actions = ActionChains(driver)
            actions.move_to_element(vlu).click().perform()
        else:
            print("'.active' 요소가 없습니다. 그냥 넘어갑니다.")
    except Exception as e:
        print(f"오류 발생: {e}")
    
print(membership_box)
# 현재 카테고리 순회하는것까지 만들었고 순회하면서 데이터 끌어 모아야함 


#         total_pages = int(driver.find_element(By.CSS_SELECTOR, ".pagination .last-page").text)


#     try:
#         pagination = driver.find_elements(By.CSS_SELECTOR, ".middlearea .li")
#         total_pages = int(pagination[-1].text) 
#     except Exception as e:
#         print(f"페이지네이션 추출 실패 : {e}")

#     # 3, 4. 각 페이지를 순회하며 데이터 크롤링
#     for page in range(1, total_pages + 1):
#         try:
#             driver.get(f"{base_url}{page}")
#             time.sleep(3)

#             items = driver.find_elements(By.CSS_SELECTOR, ".item")
#             for item in items:
#                 data = item.text
#                 all_data.append(data)
#         except Exception as e:
#             print(f"{page}페이지 크롤링 중 에러 발생: {e}")
#             continue
# except Exception as e:
#     print(f"크롤링 전체 프로세스 중 에러 발생")

# finally:
#     try:
#         with open("output.text", "w", encoding="utf-8") as file:
#             for data in all_data:
#                 file.write(data + "\n")
#     except Exception as e:
#         print(f"파일 저장 중 에러 발생:{e}")
    
driver.quit()
