/*
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
*/

#include <stdio.h>

int main() {
    // 이곳에 코드를 작성해주세요!
    int num = 0;
    scanf("%d",&num);
    int num_1 = num / 100;
    int num_2 = (num % 100) / 10;
    int num_3 = num % 10;

    printf("%d%d%d",num_3,num_2,num_1);

    return 0;
}