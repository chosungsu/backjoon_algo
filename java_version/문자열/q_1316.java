package java_version.문자열;

import java.util.Scanner;

public class q_1316 {
    public static void main(String[] args){
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int cnt = 0; // 그룹 단어 개수
		
		for (int i = 0; i < N; i++) {
			String S = sc.next();
			boolean check[] = new boolean[26]; 
            //그룹 단어일 경우 불린값
			boolean tmp = true;
			
			for (int j = 0; j < S.length(); j++) {
				int index = S.charAt(j)-'a';
				if(check[index]) { 
                    // 이전에 사용한적이 있는 문자라면
					if(S.charAt(j) != S.charAt(j-1)) { 
                        // 이전 문자와 연속되지 않는다면
						tmp = false;
						break;
					}
				}else { 
                    // 이전에 사용한적이 없는 문자라면
					check[index] = true;
				}
			}
			if(tmp) cnt++;
		}
		
		System.out.println(cnt);
	}
}
