#include<iostream>
using namespace std;

struct Node
{

    int data;
    struct Node* prev;
    struct Node* next;
};
typedef struct Node Node;




void printList( Node* head)
{


    Node* ptr= head;
    while (ptr!= NULL)
    {
        cout<<ptr->data<<" ";
        ptr=ptr->next;
    }
    
}


void push(Node* *headr,int data)
{
   Node * newnode= (Node*)malloc(sizeof(Node));
   newnode->data= data;
  

   newnode->next= *headr;
      newnode->prev= NULL;

   if(*headr!= NULL)
   (*headr)->prev= newnode;

   *headr= newnode;
   

}

void deleteS(Node* *headr)
{

    if(*headr==NULL)
    return;
   Node* ptr= *headr;
   *headr= (*headr)->next;
   (*headr)->prev= NULL;
   delete ptr; 

}




void append(Node* *headr,int data)
{  
     Node* newnode= (Node*) malloc(sizeof(Node));
     newnode->data= data;

     if(*headr==NULL)
     {
         newnode->next= NULL;
         newnode->prev=NULL;
         *headr= newnode;
         return;

     }

     Node* lastNode= *headr;
     while (lastNode->next!= NULL)
     {
        lastNode= lastNode->next;
     }

     newnode->prev= lastNode;
     lastNode->next= newnode;
     newnode->next=  NULL;

     



}

void insertAfter(Node* prevNode, int data)
{ if(prevNode==NULL)
return;




Node* newnode= (Node*) malloc(sizeof(Node));
newnode->data=data;

newnode->next= prevNode->next;
if(prevNode->next!=NULL)
prevNode->next->prev= newnode;
prevNode->next= newnode;
newnode->prev= prevNode;




}

void deleteE( Node* *headr)
{
    if(*headr==NULL)
    return;

    Node* ptr= *headr;
    while (ptr->next!= NULL)
    {
        ptr=ptr->next;
    }

    ptr->prev->next= NULL;
    delete ptr;
    

}

int main()
{

    Node* head= NULL;
    append(&head,9);
    push(&head,1);
    push(&head,2);
    push(&head,3);
    push(&head,4);
    insertAfter(head->next->next->next->next,7);
    deleteS(&head);
    deleteE(&head);
   

    printList(head);

}