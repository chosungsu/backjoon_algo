package java_version.문자열;

import java.util.Scanner;

//두 수를 뒤집고 그 수 중 큰 수를 찾기
public class q_2908 {
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        int a = in.nextInt();
        int b = in.nextInt();
        a = Integer.parseInt(new StringBuilder().append(a).reverse().toString());
        b = Integer.parseInt(new StringBuilder().append(b).reverse().toString());
        System.out.print(a > b ? a : b);
        
	}
}
