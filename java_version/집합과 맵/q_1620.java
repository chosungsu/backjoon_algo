import java.io.*;
import java.util.HashMap;
import java.util.StringTokenizer;

public class q_1620 {
    public static void main(String args[]) throws IOException {
		BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
        // n, m 읽기
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		HashMap<String, Integer> nameMap = new HashMap<>();
		String[] nameArr = new String[n + 1];
		StringBuilder sb = new StringBuilder();
		
		// 이름을 n개를 HashMap에 입력한다.
		for(int i = 1; i < n + 1; i++) {
			String name = br.readLine();
			nameMap.put(name, i);
			nameArr[i] = name;
		}
		
		while(m --> 0) {
			String findStr = br.readLine();
			if(isStringNumber(findStr)) { 
                // 숫자(인덱스)를 입력받은 경우
				int index = Integer.parseInt(findStr);
				sb.append(nameArr[index]);
			}
			else {	
                // 문자를 입력받은 경우
				sb.append(nameMap.get(findStr));
			}
			sb.append("\n");
		}
		
		System.out.println(sb.toString());
	}
	
	// 이 문자열이 숫자인지 아닌지 판단하는 함수
	public static boolean isStringNumber(String s) {
	   try {
	       Double.parseDouble(s);
	       return true;
	   }
	   catch (NumberFormatException e) {
	       return false;
	   }
	}
}
