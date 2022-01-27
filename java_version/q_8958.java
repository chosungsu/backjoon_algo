package java_version;

import java.util.Scanner;

//ox문제
//o가 연속되면 수 증가시킴
public class q_8958 {
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        //전체 ox에 대해 배열을 생성
		int x = in.nextInt();
        String arr[] = new String[x];
		for (int i = 0; i < arr.length; i++) {
            //한 줄씩 배열에 담기
            arr[i] = in.next();
		}
        for (int i = 0; i < arr.length; i++) {
            int cnt = 0;
            int sum = 0;

            for (int j = 0; j < arr[i].length(); j++) {
                if (arr[i].charAt(j) == 'O') {
                    cnt++;
                } else {
                    cnt = 0;
                }
                sum += cnt;
            }
            System.out.println(sum);
        }
	}
}
