"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    try:
        number = int(input())
        reversed_number = int(str(number)[::-1])
        print(reversed_number)
    except ValueError:
        print("Please enter a valid integer.")
        #하지만 1번 문제는 커밋과 푸시를 위해 일단 주석 하나를 달고 차이를 확인해보자.

if __name__ == '__main__':
    main()