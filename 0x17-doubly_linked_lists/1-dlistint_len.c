#include "lists.h"

/**
 * dlistint_len - Count the number of elements in a linked dlistint_t list.
 * @h: Head of a dlistint_t list.
 * Return: Number of elements in a linked dlistint_t list.
 */
size_t dlistint_len(const dlistint_t *h)
{
	size_t n_nodes = 0;

	for (; h; h = h->next)
		n_nodes++;

	return (n_nodes);
}
