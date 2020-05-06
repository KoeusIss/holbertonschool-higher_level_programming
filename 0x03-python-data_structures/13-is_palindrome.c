#include "lists.h"
/**
 * is_palindrome - checks if a linked list in palindrome
 * @head: a pointer the linked list
 *
 * Return: (Success) 1 if is palindrome
 * ------- (Fail) return 0 if not palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *cursor = NULL, *start = NULL, *end = NULL;
	
	if (*head == NULL)
		return (1);
	start = *head;
	while (start != end)
	{
		cursor = start;
		while (cursor->next && cursor->next != end)
			cursor = cursor->next;
		end = cursor;
		if (start->n != end->n)
			return (0);
		if (start == end)
			break;
		start = start->next;
	}
	return (1);
}
