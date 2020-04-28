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
	listint_t *tmp;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	if (*head == NULL)
	{
		new_node->n = number;
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}
	cursor = *head;
	while (cursor->next)
	{
		if (number < cursor->next->n)
		{
			tmp = cursor->next;
			cursor->next = new_node;
			new_node->next = tmp;
			new_node->n = number;
			return (new_node);
		}
		cursor = cursor->next;
	}
	return (NULL);
}
