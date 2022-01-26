package java_version;

import java.util.Scanner;

//더하기 사이클
//주어진 수의 오른쪽 수와 합의 오른쪽 수를 잇는다.
public class q_1110 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        //주어진 수 구하기
        int x = sc.nextInt();
        //사이클 길이 변수
        int cnt = 0;
        //동일한 수를 카피함
        int copy = x;

        while (true) {
            x = ((x % 10) * 10) + (((x / 10) + (x % 10)) % 10);
            cnt++;
            if (copy == x) {
                break;
            }
        }
        System.out.println(cnt);
        
	}
}
