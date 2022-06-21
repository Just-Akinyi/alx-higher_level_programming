#include "lists.h"

/**
 * add_dnodeint_end - Add a new node at the end of a dlistint_t list.
 * @head: Pointer to head to the list.
 * @n: New data.
 * Return: The address of the new element, or NULL if it failed.
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new = NULL;
	dlistint_t *end = *head;

	/*Create a new node*/
	new = malloc(sizeof(dlistint_t));
	if (!new)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (!end)
	{
		new->prev = NULL;
		*head = new;
		return (new);
	}

	/*Identify end*/
	for (; end->next;)
		end = end->next;
	new->prev = end;
	end->next = new;

	return (new);
}
