#include <iostream>

using namespace std ;

struct node {
    int data ;
    node *left , *right ;
    bool lthread , rthread ;

};

class BST {
    public :
    node *root;

    BST(){
        root = NULL ;
    }

    node *insert(int key){
        node *ptr = root ;
        node *par = NULL;
        while(ptr != NULL){
            if (key == ptr -> data){
                cout << "Duplicate Key\n";
                return root;
            }

            par = ptr ;
            if (key < ptr->data){
                if (!ptr->lthread){
                    ptr = ptr->left ;
                }
                else {
                    break ;
                }
            else {

                if (!ptr->rthread){
                    ptr = ptr->right;
                }
                else {
                    break;
                }
            }
            }

            node *new_node = new node ;
            new_node->data = key ;
            new_node->left = NULL ;
            new_node->right = NULL;
            new_node->lthread = NULL;
            new_node->rthread = NULL;

            if (par == NULL){
                
            }

        }
    }
}



