package java_version;

import java.util.Scanner;
import java.util.StringTokenizer;

//단어의 개수
//단어의 개수 중복포함 세어야 한다.
public class q_1152 {
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        String a = in.nextLine();
        //공백 기준으로 토큰 저장
        StringTokenizer st = new StringTokenizer(a, " ");
        System.out.println(st.countTokens());
	}
}
