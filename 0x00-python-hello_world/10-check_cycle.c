#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to the linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *h = malloc(sizeof(listint_t));

	if (list == NULL)
		return ('\0');
	if (h == NULL)
		return ('\0');

	h = list->next;
	while (h != NULL && h != list)
		h = h->next;
	return (h == list);
}
