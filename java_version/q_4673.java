package java_version;

public class q_4673 {
    public static void main(String args[]){
        boolean[] check = new boolean[10001];
        for (int i = 1; i < 10001; i++) {
            int n = d(i);
            if (n < 10001) {
                check[n] = true;
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i < 10001; i++) {
            //false값만 추출
            if (!check[i]) {
                sb.append(i).append("\n");
            }
        }
        System.out.println(sb);
	}
    public static int d(int num) {
        int sum = num;
        while (num != 0) {
            //나머지 더하는 로직
            sum += (num % 10);
            //새로운 숫자를 생성해주는 로직
            num = num / 10;
        }
        return sum;
    }
}
