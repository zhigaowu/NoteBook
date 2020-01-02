// Linus tell us how to use pointer to pointer
void freeListNode(Node** pHead, Node* pCond)
{
	Node** pCurr = pHead;
	while (*pCurr)
	{
		Node* entry = *pCurr;
		if (pCond->data == entry->data)
		{
			*pCurr = entry->pNext;
			free(entry);
		}
		else 
		{
			pCurr = &(entry->pNext);
		}
	}
}
