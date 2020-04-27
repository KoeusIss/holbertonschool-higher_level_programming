#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: a pointer to the list
 *
 * Return: (1) if there is a cycle
 * ------- (0) otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *fast;
	listint_t *slow;

	if (list == NULL)
		return (0);
	slow = list;
	fast = list->next;
	while (slow && fast && fast->next)
	{
		if (slow == fast)
			return (1);
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
