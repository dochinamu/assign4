import time
import random

#초 카운트 함수 정의
def count_time(sec):
    for i in range(sec, 0, -1):
        print(i)
        time.sleep(1)

#안내문 출력
menu_list = []
print('5개의 메뉴를 추가해주세요! 5개가 입력되면 오늘의 메뉴를 추천해드려요 \n동일한 메뉴는 안돼요!')
print()

#입력 받고 현재 메뉴 수 출력(이미 있는 메뉴라면 다시 입력 요구+원래 있던 메뉴 빼고 다시 집어넣기)
while len(menu_list) != 5:
    menu = input('메뉴 추가: ')
    if menu not in menu_list:
        menu_list.append(menu)
    else:
        print('이미 있는 메뉴예요! 다른 메뉴를 입력해주세요.')
        del menu_list[menu_list.index(menu)]
        menu_list.append(menu)
    print('현재 메뉴 수 =', len(menu_list))
    print()

#3초 카운트
count_time(3)

#리스트 출력
print()
print(menu_list)
print('과연 오늘의 메뉴는?')
print()

#3초 카운트
count_time(3)

#최종 결정된 메뉴 출력
choice = random.choice(menu_list)
print('오늘의 메뉴는', menu_list.index(choice)+1, '번째 메뉴,', choice,'입니다')