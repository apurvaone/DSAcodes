#include<iostream>
using namespace std;

class Node
{

    public:


    int data;
    Node* next;

    Node(int data)
    {
      this->data= data;
      next= NULL;

    }


};


void printList(Node * head)
{

    while ( head!= NULL)
    {
        cout<< head->data<<" ";
        head = head->next;
    }
}

int main()
{
    Node* head= NULL;
    head=  new Node(5);

    Node * first= new Node(1);
    Node * second= new Node(2);
    Node * third= new Node(3);

    head->next= first;
    first->next = second;
    second->next= third;
 
  
    printList(head);
   




}