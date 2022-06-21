#include "lists.h"

/**
 * print_dlistint - Print all the elements of a dlistint_t list.
 * @h: Head of dlistint_t list.
 * Return: Number of nodes in the list.
 */
size_t print_dlistint(const dlistint_t *h)
{
	size_t n_nodes = 0;

	for (; h; h = h->next)
	{
		printf("%d\n", h->n);
		n_nodes++;
	}
	return (n_nodes);
}
