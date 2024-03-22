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

if __name__ == '__main__':
    main()