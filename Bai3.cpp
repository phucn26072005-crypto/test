//#include<stdio.h>
//#include<conio.h>
//int main(){
//	int n, i, chon;
//	double S = 0;
//	printf("Nhap n:");
//	scanf_s("%d", &n);
//	printf("\n==MENU==\n");
//	printf("1. S=2+4+...+2n\n");
//	printf("2. S=1*2+2*3+...+n(n+1)\n");
//	printf("3. S=1/(1*2)+...+1/(n(n+1))\n");
//	printf("Chon cong thuc(1-3):");
//	scanf_s("%d", &chon);
//	if (chon == 1){
//		for (i = 1; i <= n; i++);
//		S += 2 * i;
//		printf("Ket qua: %0lf\n", S);
//	}
//	else if (chon == 2){
//		for (i = 1; i <= n; i++);
//		S += i * (i+1) ;
//		printf("Ket qua: %0lf\n", S);
//	}
//	else if (chon == 3){
//		for (i = 1; i <= n; i++);
//		S += 1.0 / (i*(i + 1));
//		printf("Ket qua: %0lf\n", S);
//	}
//	else{
//		printf("Lua chon khong hop le\n");
//	}
//	_getch();
//	return 0;
//}