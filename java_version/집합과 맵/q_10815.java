import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class q_10815 {
    public static void main(String[] args) throws Exception {
        //BufferedReader, BufferedWriter 생성
        BufferedReader br = new BufferedReader(
            new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(
            new OutputStreamWriter(System.out));
        StringTokenizer st;
 
        // 1. 카드의 개수 읽기 첫번째줄
        int N = Integer.parseInt(br.readLine()); 
        // 상근이의 카드 목록을 리스트화하기
        int[] cards = new int[N];
        // 2. 리스트에 담는 로직 두번째줄
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            cards[i] = Integer.parseInt(st.nextToken());
        }
        // 이분탐색할 배열은 정렬되어 있어야 함.
        Arrays.sort(cards); 

        // 3. 구별할 수의 개수 읽기 세번째줄
        int M = Integer.parseInt(br.readLine());
        // 최종 결과를 StringBuilder로 보여주기
        StringBuilder sb = new StringBuilder();
        // 4. StringBuilder에 담는 로직 네번째줄
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            int temp = Integer.parseInt(st.nextToken());
            sb.append(binarySearch(cards, N, temp) + " ");
        }
 
        // 최종 결과 출력하기
        bw.write(sb.toString() + "\n");
        bw.flush();
        bw.close();
        br.close();
    }
 
    // 이진법 탐색 함수 생성
    public static int binarySearch(int[] cards, int N, int search) {
        int first = 0;
        int last = N - 1;
        int mid = 0;
 
        // 마지막 인덱스가 될 때까지 반복
        while (first <= last) {
            mid = (first + last) / 2; // 중간 인덱스
 
            if (cards[mid] == search) { 
                // 중간값과 찾으려는 수가 같은 경우
                return 1;
            }
 
            if (cards[mid] < search) { 
                // 중간값이 찾으려는 수보다 작으면, 
                // 그 이하로는 볼 필요 없음.
                // 따라서 첫번째 인덱스를 중간 + 1로 변경
                first = mid + 1;
            } else { 
                // 중간값이 찾으려는 수보다 크면, 
                // 그 이상으로는 볼 필요 없음.
                // 따라서 마지막 인덱슬르 중간 - 1로 변경
                last = mid - 1;
            }
        }
 
        return 0;
    }
}
