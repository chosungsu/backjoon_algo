package java_version.함수;

import java.util.*;
//한수 구하기
//각 자리가 등차수열을 이룬다면 한수이다.
public class q_1065 {
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        System.out.print(arith(in.nextInt()));
	}
    public static int arith(int num) {
        int cnt = 0;
        //100보다 작은 수는 무조건 한수이다.
        if (num < 100) {
            return num;
        }
        else {
            cnt = 99;
            if (num == 1000) {
                num = 999;
            }
            for (int i = 100; i <= num; i++) {
                int hund = i / 100;
                int ten = (i/10)%10;
                int one = i % 10;
                if ((hund - ten) == (ten - one)) {
                    cnt++;
                }
            }
        }
        return cnt;
    }
}