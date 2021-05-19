#include<iostream>

using namespace std ;

class node
{
    public :
    int data ;
    node  *left , *right;
};

class BST 
{
    public : 
        node *root;
        BST(){
            root = NULL;
        }

        node *recur_insert(node *r, int key){
            node *new_node = new node;
            new_node->data = key;
            new_node->left = NULL;
            new_node->right = NULL;

            if (r== NULL){
                r = new_node;
                return (new_node);
            }

            else if(key < r->data){
                r->left = recur_insert(r->left,key);

            }

            else {
                r->right = recur_insert(r->right,key);
            }
        }

        node *iter_insert(node *r, int key){
            node *new_node = new node;
            new_node->data = key;
            new_node->left = NULL;
            new_node->right = NULL;

            node *temp = r ;
            node *parent = NULL;

            while (temp != NULL ){
                parent = temp;
                if(key < temp->data)
                    temp= temp->left;
                else 
                    temp= temp->right;

            }

            if (parent == NULL )
                parent = new_node;
            else if (key < parent->data)
                parent->left = new_node;
            else 
                parent->right = new_node;

            return parent;
        }

        node *search(node *r,int key){
            node *temp = r;
            while (temp !=  NULL){
                if (key == temp->data)
                    return temp;
                else if (key < temp->data)
                    temp = temp->left;
                else 
                    temp = temp->right;
            }

            return NULL;
        }
};

int main(){
    BST bst;
    bst.root = bst.recur_insert(bst.root,50);
    bst.recur_insert(bst.root,30);
    bst.recur_insert(bst.root,10);
    bst.recur_insert(bst.root,40);
    bst.recur_insert(bst.root,20);
    bst.recur_insert(bst.root,80);

    bst.iter_insert(bst.root,44);
    bst.iter_insert(bst.root,77);

    bst.inorder(bst.root);

    cout << "\n MINIMUM IN BSTree IS " << bst.bstmin(bst.root) << endl ;
    node *found;
    found = bst.search(bst.root,100);

    if(found != NULL)
        cout << "Found Element " << endl;
    else 
        cout << "Element not found in BST " << endl ;

    cout << "Number of nodes in the longest path of BST : ";
    cout << bst.longest_path_count(bst.root) << endl;

    bst.mirror(bst.root);
    cout << "After mirroring , tree is " << endl ;
    bst.inorder(bst.root);

    bst.mirror(bst.root);

    cout << "Before deleting 75 " << endl;
    bst.inorder(bst.root);

    bst.delete_node(bst.root , 75 );

    cout << "Before deleting 75 " << endl;
    bst.inorder(bst.root);

    bst.delete_node(bst.root,75);
    cout << "After deleting 75 " << endl;

    bst.inorder(bst.root);
    return 0;

}