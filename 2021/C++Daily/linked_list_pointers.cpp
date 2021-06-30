#include <cstdio>
#include <iostream>

struct Node{
    //holds a pointer to the next node, name and age variables 
    Node* next_node_ptr{};
    char name[64]{};
    short age{};
    //function to insert a node after the node you initialized
    void insert_this_node_after_current_node(Node* new_node_ptr){
        
        new_node_ptr->next_node_ptr = next_node_ptr;
        
        next_node_ptr = new_node_ptr;
        
    }

};

int main(){
    Node person1, person2, person3;
    person1.name[0] = 'M';
    person1.name[1] = 'a';
    person1.name[2] = 't';
    person1.name[3] = 'h';
    person1.name[4] = 'i';
    person1.name[5] = 'e';
    person1.name[6] = 'u';
    person1.age = 17;
    person1.insert_this_node_after_current_node(&person2);
    person1.name[0] = 'M';
    person1.name[1] = 'a';
    person1.name[2] = 't';
    person1.name[3] = 'h';
    person1.name[4] = 'i';
    person1.name[5] = 'e';
    person1.name[6] = 'x';
    person1.age = 14;
    person2.insert_this_node_after_current_node(&person3);
    person1.name[0] = 'M';
    person1.name[1] = 'a';
    person1.name[2] = 't';
    person1.name[3] = 'w';
    person1.name[4] = 'i';
    person1.name[5] = 'e';
    person1.name[6] = 'u';
    person1.age = 300;

    for (Node *cursor = &person1; cursor; cursor = cursor->next_node_ptr){
        printf("person %c%c%c%c%c%c%c age:%d\n", 
        cursor->name[0],
        cursor->name[1],
        cursor->name[2],
        cursor->name[3],
        cursor->name[4],
        cursor->name[5],
        cursor->name[6],
        cursor->age);
    }
}