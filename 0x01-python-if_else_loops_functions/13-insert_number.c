#include "lists.h"
/**
* insert_node - inserts a node into a sorted list
* @head: beginning of the sorted list
* @number: number to be added to the list
* Return: new node
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *scout = *head;

	if (*head == NULL || scout->n > number)
	{
		new = malloc(sizeof(listint_t));

		if (!new)
			return (NULL);

		new->n = number;
		new->next = *head;
		*head = new;
		return (new);
	}
	while (scout)
	{
		if (!scout->next || scout->next->n > number)
		{
			new = malloc(sizeof(listint_t));
			if (!new)
				return (NULL);
			new->n = number;
			new->next = scout->next;
			scout->next = new;
			return (new);
		}
		scout = scout->next;
	}
	return (NULL);
}
