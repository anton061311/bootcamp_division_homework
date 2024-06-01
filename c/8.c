/*
    main 함수 안의 내용만 수정해주세요.
    수정할 경우, 자동 채점 프로그램이 제대로 동작하지 않을 가능성이 있습니다.
*/

#include <stdio.h>

int res1(int n){
    return n * (n+1) / 2;
}

int res2(int n){
    int mul = 1;
    for(int i = 1; i <= n; i++){
        mul *= i;
    }
    return mul;
}

int main() {
    // 이곳에 코드를 작성해주세요!
    int n;
    scanf("%d", &n);
    int sum = res1(n);
    int mul = res2(n);

    printf("%d\n%d\n", sum, mul);

    return 0;
}