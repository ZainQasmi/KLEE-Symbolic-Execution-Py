
#include <klee/klee.h>

int calculator(int x,int y,char op){
	if(op=='+'){
		return (x+y);
	}
	else if(op=='-'){
		return (x-y);
	}
	else if(op=='/'){
		if(y!=0){
			return (x/y);
		}
		return 0;
	}
	else if(op=='*'){
		return (x*y);
	}
	else{
		return 0;
	}
}

int main(){
	int one_num,two_num,check;
	char operation;
	klee_make_symbolic(&one_num, sizeof(one_num), "first_num");
	klee_make_symbolic(&two_num, sizeof(two_num), "second_num");
	klee_make_symbolic(&operation, sizeof(operation), "mathematical_operation");
  	return calculator(one_num,two_num,operation);
}