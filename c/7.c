/*
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
*/

#include <stdio.h>

int main() {
    // 이곳에 코드를 작성해주세요!
    int year, month;
    scanf("%d %d", &year, &month);

    if(month == 4 || month == 6 || month == 9 || month == 11){
        printf("%d\n", 30);
    }
    else if(month == 1 || month == 3 || month == 5 || month == 7 || month == 8 || month == 10 || month == 12){
        printf("%d\n", 31);
    }
    else {
        if((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)){
            printf("%d\n", 29);
        }
        else{
            printf("%d\n", 28);
        }
    }
    return 0;
}