phone_book = ["12","123","1235","567","88", "8888"]
# 전화번호부의 번호들을 서로 비교한다
def solution(phone_book):
    phone_book.sort()
    print(phone_book)
    for i in range(len(phone_book)-1):
        j = i+1
        if(phone_book[i] == phone_book[j][:len(phone_book[i])]):
            return False
    return True

solution(phone_book)