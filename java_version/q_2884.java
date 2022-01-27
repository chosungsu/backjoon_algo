package java_version;

import java.util.Scanner;

//시간을 45분 일찍 설정하는 로직
public class q_2884 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();

        //분 단위가 45분보다 큰 수일 경우 시간 단위를 건들지 않음
        if (y >= 45) {
            System.out.println(x + " " + (y - 45));
        } else {
            //시간 단위가 자정을 가리킬 때
            if (x == 0) {
                System.out.println(23 + " " + (60 - (45 - y)));
            } else {
                System.out.println((x - 1) + " " + (60 - (45 - y)));
            }
            
        }
	}
}
