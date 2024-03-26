"""
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
"""

def main():
    age = int(input()) 
    if age > 61:
        print("DISCOUNT")
    elif age == 61:
        print("DISCOUNT\nBOARD")
    else:
        print("BOARD")
    # 2번의 경우 웹을 통한vs코드로 접속하여 깃허브 커밋, 스테이징, 푸쉬가 되는지 확인하기 위함이다.
if __name__ == '__main__':
    main()
