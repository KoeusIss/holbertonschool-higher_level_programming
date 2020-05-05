#include "lists.h"
/**
 * list_len - returns the length of a linked list
 * @head: a pointer to a linked list
 *
 * Return: (Success) the length of the list as integer
 * ------- (Fail) return a negative number
 */
size_t list_len(listint_t *head)
{
	size_t length = 0;

	while (head)
	{
		length++;
		head = head->next;
	}
	return (length);
}
/**
 * is_palindrome - checks if a linked list in palindrome
 * @head: a pointer the linked list
 *
 * Return: (Success) 1 if is palindrome
 * ------- (Fail) return 0 if not palindrome
 */
int is_palindrome(listint_t **head)
{
	int *array;
	size_t length, i = 0;
	listint_t *cursor;

	if (*head == NULL)
		return (1);
	length = list_len(*head);
	array = malloc(length * sizeof(int));
	if (array == NULL)
		return (0);
	while (cursor)
	{
		array[i++] = cursor->n;
		cursor = cursor->next;
	}
	for (i = 0; i < length / 2; i++)
	{
		if (array[i] != array[length - 1 - i])
			return (0);
	}
	free(array);
	return (1);
}
