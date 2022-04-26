#리스트 생성
word_list = []

#데이터 입력 받아, q가 아니라면 리스트에 추가
while True:
    word = input('Enter anything: ')
    if word == 'q':
        break
    else:
        word_list.append(word)

#리스트 출력
print()
print(word_list)

