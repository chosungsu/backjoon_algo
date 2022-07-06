package java_version.기본수학2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class q_1358 {
    public static void main(String[] args) throws IOException {
 
		String f = "factor\n";
		String m = "multiple\n";
		String n = "neither\n";
        
		BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st;
 
		while(true) {
			
			st = new StringTokenizer(br.readLine()," ");
			
			int first = Integer.parseInt(st.nextToken());
			int second = Integer.parseInt(st.nextToken());
			
			if(first == 0 && second == 0) break;
			
            //두번째 숫자를 첫번째 숫자로 나눈 나머지가 0인 경우
            //약수이므로 factor 반환
			if(second % first == 0) {
				sb.append(f);
			}
            //첫번째 숫자를 두번째 숫자로 나눈 나머지가 0인 경우
            //배수이므로 multiple 반환
			else if(first % second == 0) {
				sb.append(m);
			}
            //둘 다 아니면 neither 반환
			else {
				sb.append(n);
			}
			
		}
		System.out.println(sb);
	}
}
