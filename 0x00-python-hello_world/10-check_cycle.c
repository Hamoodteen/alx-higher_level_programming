#include "lists.h"

/**
 * print_listint - f
 * @h: int
 * Return: 0
*/
size_t print_listint(const listint_t *h)
{
	size_t i;

	for (i = 0; h != NULL; i++)
	{
		printf("%d\n", h->n);
		h = h->next;
	}
	return (i);
}

/**
 * add_nodeint - f
 * @head: list
 * @n: int
 * Return: 0
*/
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *nn;
	int copy;

	if (head == NULL)
		return (NULL);
	memcpy(&copy, &n, sizeof(int));
	nn = malloc(sizeof(listint_t));
	if (nn == NULL)
	{
		free(nn);
		return (NULL);
	}
	nn->n = copy;
	nn->next = *head;
	*head = nn;
	return (nn);
}

/**
 * free_listint - f
 * @head: list
*/
void free_listint(listint_t *head)
{
	if (head == NULL)
		return;
	free_listint(head->next);
	free(head);
}

/**
 * check_cycle - f
 * @list: list
 * Return: 0 or 1
*/
int check_cycle(listint_t *list)
{
	return (0);
}
