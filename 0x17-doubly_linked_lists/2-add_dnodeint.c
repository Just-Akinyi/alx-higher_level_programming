#include "lists.h"

/**
 * add_dnodeint - Add a new node at the beginning of a dlistint_t list.
 * @head: Pointer to head of the list.
 * @n: New data.
 * Return:  The address of the new element, or NULL if it failed.
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *new = NULL;

	/*Create new node*/
	new = malloc(sizeof(dlistint_t));
	if (!new)
		return (NULL);

	new->n = n;
	new->prev = NULL;
	new->next = *head;

	if (*head)
		(*head)->prev = new;

	*head = new;

	return (new);
}
