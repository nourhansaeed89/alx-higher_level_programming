#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * lelist: pointer to list to check
 * Return: 1 if cyclical, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *loop = list, *fast = list;

	while (fast && fast->next)
	{

		loop = loop->next;
		fast = fast->next->next;
		if (slow == fast)
		return (1);
	}
	return (0);
}
