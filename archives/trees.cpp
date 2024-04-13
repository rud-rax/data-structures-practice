#include <iostream>

using namespace std;
class tree
{
    struct tnode
    {
        int data;
        tnode *left;
        tnode *right;
    };
    tnode*root,*nn;
public:

    void create();
    void display();
    void inorder(tnode*tn);
    tree()
    {
        root=NULL;
    }
};
void tree::create()
{
    nn=new tnode;
    cout<<"Enter data :"<<endl;
    cin>>nn->data;
    nn->left=nn->right=NULL;
    if (root==NULL)
    {
        root=nn;
    }
    else
    {
        tnode*temp,*parent;
        temp=root;
        while(temp!=NULL)
        {
            parent=temp;
            if(nn->data<temp->data)
            {
                temp=temp->left;
            }
            else
                temp=temp->right;
        }
        if(nn->data<parent->data)
        {
            parent->left=nn;
        }
        else
            parent->right=nn;
    }
}

void tree::inorder(tnode*tn)
{
    if(tn!=NULL)
    {
        inorder(tn->left);
        cout<<tn->data;
        inorder(tn->right);
    }
}
void tree::display()
{
    tnode*temp;
    temp=root;
    cout<<"data : "<<endl;
    inorder(temp);
}

int main()
{
    tree dl;
    int choice;
    do
    {
        cout<<endl<<"Enter 1. to create"<<endl;
        cout<<"Enter 2. to display "<<endl;
        cout<<"Enetr 3. to stop"<<endl;
        cin>>choice;
        switch(choice)
        {
            case 1 :dl.create();
            break;
            case 2 :dl.display();
            break;
           default:cout<<"You have entered wrong choice"<<endl;
           break;
        }
    }while(choice>=1 && choice<=2);
    return 0;
}

