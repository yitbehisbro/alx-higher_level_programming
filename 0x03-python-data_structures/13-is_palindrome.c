#include "lists.h"

/**
 * half_reverse - reverses the half list
 *
 * @head: pointer to the list
 * Return: no return
 */
void half_reverse(listint_t **head)
{
	listint_t *prev, *current, *next;

	prev = NULL;
	current = *head;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}

/**
 * int_compare - compares each element of the list
 * @first: pointer to first half
 * @second: pointer to second half
 *
 * Return: 1 if are equals, 0 if not
 */
int int_compare(listint_t *first, listint_t *second)
{
	listint_t *temp1, *temp2;

	temp1 = first;
	temp2 = second;

	while (temp1 != NULL && temp2 != NULL)
	{
		if (temp1->n == temp2->n)
		{
			temp1 = temp1->next;
			temp2 = temp2->next;
		}
		else
		{
			return (0);
		}
	}

	if (temp1 == NULL && temp2 == NULL)
	{
		return (1);
	}

	return (0);
}

/**
 * is_palindrome - checks if the list is palindrome
 * @head: pointer to the struct or list
 *
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	int flag;
	listint_t *slw, *fst, *prev_slw, *scan_half, *mid;

	slw = fst = prev_slw = *head;
	mid = NULL;
	flag = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (fst != NULL && fst->next != NULL)
		{
			fst = fst->next->next;
			prev_slw = slw;
			slw = slw->next;
		}

		if (fst != NULL)
		{
			mid = slw;
			slw = slw->next;
		}

		scan_half = slw;
		prev_slw->next = NULL;
		half_reverse(&scan_half);
		flag = int_compare(*head, scan_half);

		if (mid != NULL)
		{
			prev_slw->next = mid;
			mid->next = scan_half;
		}
		else
		{
			prev_slw->next = scan_half;
		}
	}
	return (flag);
}
