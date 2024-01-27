#include <stdio.h>

/**
 * main - factorize many number as posible
 * Return: 0
 */

int main(void)
{
	long long int no = ;
	long int f1 = 2;
	long int f2;


	while (no % f1)
	{
		if (f1 <= no)
		{
			f1++;
		}
		else
		{
			return (-1);
		}
	}


	f2 = no / f1;
	printf("%lld = %ld * %ld\n", no, f2, f1);
	return (0);
}
