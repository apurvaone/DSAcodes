#include<iostream>
using namespace std;

struct Node
{
int data;

struct Node* prev;
struct Node* next;

};
typedef struct Node Node;


void push( Node* *headr)
{

Node* newnode= (Node*) malloc(sizeof(Node));
newnode->data=data;
newnode->next= *headr;
*headr->



}

int main()
{

Node* head= NULL;


}