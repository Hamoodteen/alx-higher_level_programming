#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - f
 * @head: head
 * Return: 0 or 1
*/
int is_palindrome(listint_t **head)
{
	if (*head == NULL)
		return (1);
	if ((*head)->next == NULL)
		return (1);
	if ((*head)->n != (*head)->next->n)
		return (0);
	return (is_palindrome(&((*head)->next)));
}
