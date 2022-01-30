package java_version.사칙연산입출력;

import java.util.Scanner;

//곱셈 식 구하기
public class q_2588 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        //두번째 줄 숫자 읽기
        String code = sc.next();

        System.out.println(x * (code.charAt(2) - '0'));
        System.out.println(x * (code.charAt(1) - '0'));
        System.out.println(x * (code.charAt(0) - '0'));
        System.out.println(x * Integer.parseInt(code));
	}
}
