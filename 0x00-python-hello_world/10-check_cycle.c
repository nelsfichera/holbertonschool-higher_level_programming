#include "lists.h"
/**
* check_cycle - checks if a linked list is a loop
* @head: head of a linked list
* Return: 0 if false, 1 if true
*/
int check_cycle(listint_t *list)
{
	turtle = head;
	hare = head;

	while (turtle && hare && hare->next)
	{
		turtle = turtle->next;
		hare = hare->next->next;
		if(turtle == hare)
			return (1);
	}
	return (0);
}
