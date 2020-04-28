#include "lists.h"

/**
 * insert_node - inserts a number in a sorted list
 * @head: a pointer to the given list
 * @number: a given number to be inserted
 *
 * Return: (Pointer) to the processed list
 * ------- (NULL) otherwise on fail
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cursor;
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	cursor = *head;
	if (*head == NULL)
	{
		new_node = add_nodeint_end(head, number);
		return (new_node);
	}
	if (number < cursor->n)
	{
		new_node->next = cursor;
		new_node->n = number;
		*head = new_node;
		return (new_node);
	}
	while (cursor->next)
	{
		if (number < cursor->next->n)
		{
			new_node->next = cursor->next;
			cursor->next = new_node;
			new_node->n = number;
			return (new_node);
		}
		cursor = cursor->next;
	}
	new_node = add_nodeint_end(head, number);
	return (new_node);
}
