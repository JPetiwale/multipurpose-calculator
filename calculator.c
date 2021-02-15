#include <stdio.h>
int main(){

//variable declaraqtion
    char operator;
    int num1, num2;
    int result;

//operator entered
    printf("Please enter operator(+,-,*,/): \n");
    scanf("%c",&operator);

//operator shown
    printf("You have selected %c \n", operator);

//num1 and num2 aentered
    printf("Please enter num1: \n");
    scanf("%d",&num1);
    printf("Please enter num2: \n");
    scanf("%d",&num2);

//num1 and num2 shown
    printf("num1 is %d and num2 is %d \n",num1,num1);

//calculator
     result=0;
    switch(operator)    
    {
        case '+':
            result=num1+num2;
            break;
             
        case '-':
            result=num1-num2;
            break;
         
        case '*':
            result=num1*num2;
            break;

        case '/':
            result=(float)num1/(float)num2;
            break;
             
        default:
            printf("Invalid operation.\n");
    }

//final print 
    printf("Result: %d %c %d = %d ",num1,operator,num2,result);
    //end
    return 0;
}