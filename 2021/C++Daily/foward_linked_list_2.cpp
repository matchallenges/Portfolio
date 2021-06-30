#include <iostream>

using namespace std;

struct Node {
    public:
        int data{};
        Node* next{};
};

int main(){

    Node* head = nullptr;
    Node* second = nullptr;
    Node* third = nullptr;

    head = new Node();
    second = new Node();
    third = new Node();

    head->data = 0;
    head->next = second;
    second->data = 1;
    second->next = third;
    third->data = 2;
    third->next = nullptr;
    
    cout << head->data << "->" << second->data << "->" << third->data << endl;
    
}