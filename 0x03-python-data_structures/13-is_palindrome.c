#include "lists.h"
/**
* is_palindrome - is palindrome or not
* @head: pointer to head of list
* Return: 1 if true, 0 if false
*/
int is_palindrome(listint_t **head)
{
	listint_t *forward, *backward;
	int length = 0, mid = 0, iter, iter2;

	forward = *head;
	backward = *head;

	if (forward->next == NULL || *head == NULL)
		return (1);
	while (forward)
	{
		length++;
		forward = forward->next;
	}
	mid = length / 2;
	if (length % 2 != 0)
		mid += 1;
	for (iter = 0; iter <= mid; iter++)
	{
		forward = *head;
		for (iter2 = 1; iter2 < length - iter; iter2++)
			forward = forward->next;
		if (foraward->n != backward->n)
			return (0);
		backward = backward->next;
	}
	return (1);
}
