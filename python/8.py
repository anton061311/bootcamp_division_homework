"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

    # 이곳에 코드를 작성해주세요!
def main():

    while True:
        n = int(input())
        if n > 0:
            sum_of_integers = 0  
            for i in range(1, n + 1):
                sum_of_integers += i  
            print(sum_of_integers)  
        else:
            print("X")
            break

if __name__ == '__main__':
    main()