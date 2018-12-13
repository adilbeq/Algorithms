public class Test{
	public static void main(String[] args) {
		int n = 5;
		int[] array = new int[n];
		array[0] = 73;
		array[1] = 31;
		array[2] = 96;
		array[3] = 24;
		array[4] = 46;
		
		int counter = 0;
		int now = 1;
		while(n != 0){
			int iter = 1;
			int max = -99;
			for (int i=0; i<n; i++){
				if(iter * array[i] > max){
					max = array[i] * iter;
					counter = counter + max;
					now = i;
				}
				iter++;
			}
			array[now] = 1;
			n--;
		}

		System.out.println(counter);

	}
}