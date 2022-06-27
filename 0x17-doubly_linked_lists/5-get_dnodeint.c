#include "lists.h"

/**
 * get_dnodeint_at_index - Find the nth node of a dlistint_t linked list.
 * @head: Head of list.
 * @index: Index to search.
 * Return: The address of the nth node.
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	for (; index; index--)
	{
		if (!head)
			return (NULL);
		head = head->next;
	}
	return (head);
}
