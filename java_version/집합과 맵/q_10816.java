import java.io.*;
import java.util.*;

public class q_10816 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in));
        // 1. 상근이의 카드갯수 읽기
        int n = Integer.parseInt(br.readLine());
        int cards[] = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        // 2. 카드 숫자 하나씩 리스트에 넣기
        for (int i = 0; i < n; ++i) {
            cards[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(cards);
        // 3. 서치할 카드갯수 읽기
        int m = Integer.parseInt(br.readLine());
        int num;
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        // 4. 숫자 비교
        for (int i = 0; i < m; ++i) {
            num = Integer.parseInt(st.nextToken());
            sb.append(
                (upper(cards, key) - lower(cards, key))
                + " "
            );
        }
        br.close();
        System.out.println(sb.toString());
    }
    private static int lower(int[] cards, int key) {
		int left = 0; 
		int right = cards.length - 1; 
 
		while (left < right) {
 
			int mid = (left + right) / 2; // 중간위치를 구한다.
 
            // 찾고자 하는 값이 중간값보다 작을 때
            // 우측 밴드를 중간값으로 변경
			if (key <= cards[mid]) {
				right = mid - 1;
			}
            // 좌측 밴드를 중간값 + 1로 변경
			else {
				left = mid + 1;
			}
 
		}
 
		return left;
	}
 
	private static int upper(int[] cards, int key) {
		int left = 0; 
		int right = cards.length - 1; 
 
		while (left < right) {
 
			int mid = (left + right) / 2; // 중간위치를 구한다.
 
			// 찾고자 하는 값이 중간값보다 작을 때
            // 우측 밴드를 중간값으로 변경
			if (key < cards[mid]) {
				right = mid - 1;
			}
			// 좌측 밴드를 중간값 + 1로 변경
			else {
				left = mid + 1;
			}
 
		}
 
		return left;
	}
}
