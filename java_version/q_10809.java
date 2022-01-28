package java_version;

import java.util.Scanner;

//알파벳 찾기
//포함되면 인덱스 출력, 아니면 -1 출력
public class q_10809 {
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        //배열 생성 - 알바벳 크기만큼
        int[] arr = new int[26];
        for (int i = 0; i < arr.length; i++) {
            //배열값을 -1로 고정
            arr[i] = -1;
        }
        String S = in.nextLine();
        for (int j = 0; j < S.length(); j++) {
            char ch = S.charAt(j);
            if (arr[ch - 'a'] == -1) {
                arr[ch - 'a'] = j;
            }
        }
        for (int val : arr) {
            System.out.print(val + " ");
        }
        
	}
}
