//Shreepooja Yelugoti
//SECOD462
#include <iostream>
using namespace std;
int hash_table[20];


int hash_fun(int key)
{
        int value;
        value=key%20;
        return value;

}

void insert_ele(int key)
{
    int index,index_new,i=1;
    index=hash_fun(key);
    index_new=index;
    if(hash_table[index]==-1)
    {
        hash_table[index]=key;
    }
    else
    {
        while(hash_table[index_new]!=-1 && i<20)
        {
            index_new=(index+(i*i))%20;
            if(hash_table[index_new]==-1)
            {
                hash_table[index_new]=key;
                break;
            }
            i=i+1;
        }
        if(i>=20)
        {
            cout<<"Cannot place the element "<<key<<endl;
        }
    }
}
void display()
{
    int i;
    for(i=0;i<20;i++)
    {
        if(hash_table[i]!=-1)
        {
        cout<<"Key:"<<hash_table[i]<<endl;
        }
        else
        {
            cout<<"Key:NIL"<<endl;
        }
    }
}
int main()
{
    for(int i=0;i<20;i++)
    {
        hash_table[i]=-1;
    }
    char choice;
    int run=0,info;
    while(run!=1)
    {
        cout<<"Enter 1. to insert "<<endl;
        cout<<"Enter 2. to display "<<endl;
        cout<<"Enetr 3. to stop"<<endl;
        cin>>choice;
        switch(choice)
        {
            case '1':cout<<"Enter the key"<<endl;
                     cin>>info;
                     insert_ele(info);
                     break;
            case '2': display();
                      break;
            case '3':run=1;
                      break;
        }
    }

    return 0;

}
