#include<stdio.h>
int main()
{
    printf("\n..........Knapsack problems using Greedy Algorithm...........\n");
    int n,i,j;
    printf("Enter the number of items : ");
    scanf("%d",&n);   
    int weight[50],profit[50],ratio[50],capacity,temp;
    printf("\nEnter Weight and Profit\n");
    for (i=0;i<n;i++)
        scanf("%d%d", &weight[i], &profit[i]);
    printf("\nEnter the capacity of knapsack : ");
    scanf("%d",&capacity);
    for(i=0;i<n;i++)
        ratio[i]=profit[i]/weight[i];
    float totalvalue=0;    
    for (i = 0; i < n; i++)
        for (j = i + 1; j < n; j++)
            if (ratio[i] < ratio[j])
            {
                temp = ratio[j];
                ratio[j] = ratio[i];
                ratio[i] = temp;
                temp = weight[j];
                weight[j] = weight[i];
                weight[i] = temp;
                temp = profit[j];
                profit[j] = profit[i];
                profit[i] = temp;
            }
    for (i = 0; i < n; i++) 
    {
        if (weight[i] > capacity)
            break;
        else 
        {
            totalvalue = totalvalue + profit[i];
            capacity = capacity - weight[i];
        }
     } 
    if (i < n)
        totalvalue = totalvalue + (ratio[i]*capacity);
    printf("\nThe maximum value is : %f\n",totalvalue); 
    return 0;    
}
