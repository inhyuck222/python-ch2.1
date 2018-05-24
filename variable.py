import keyword

# 변수 이름은 문자, 숫자, _로 구성된다.

friend = 1
a = 10
my_name = '임인혁'
myName = '임인혁'
_yourName = '루피'
member1 = '상디'

# 에러: 다른 구성의 변수 이름은 사용할 수 없다.
# friend$ = 1
# a! = 20
# 1abc = 23

# 에러: 예약어는 변수 이름으로 사용할 수 없다.
# def = 10
print(keyword.kwlist)
print("keyword length ", len(keyword.kwlist))
