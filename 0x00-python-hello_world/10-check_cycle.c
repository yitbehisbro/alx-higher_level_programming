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
	listint_t *pprev;
	listint_t *nprev;

	pprev = list;
	nprev = list;
	while (pprev != NULL && pprev->next != NULL && list != NULL)
	{
		list = list->next;
		pprev = pprev->next->next;

		if (list == pprev)
		{
			list = nprev;
			nprev =  pprev;
			while (1)
			{
				pprev = nprev;
				while (pprev->next != list && pprev->next != nprev)
				{
					pprev = pprev->next;
				}
				if (pprev->next == list)
					break;

				list = list->next;
			}
			return (1);
		}
	}
	return (0);
}
