#include <iostream>
using namespace std;
struct table
{
    int info;
    int key;
};
struct table *hash_table[8];
int hash_fun(int key)//Function to give the hash key
{
        int code;
        code=key%8;
        return code;
}
void insert(int key)
{
        int index;
        struct table *obj=new struct table;
        obj->key = key ;
        index=hash_fun(key);
        while(hash_table[index]!=NULL && hash_table[index]->key!=-1)
        {

            index=(index+1)%8;//using linear probing,incrementing to the next position
        }
        hash_table[index]=obj;
}
void display()
{
    int i;
    for(i=0;i<8;i++)
    {
        if(hash_table[i]!=NULL)
        {
        cout<<"Key:"<<hash_table[i]->key<<endl;
        }
        else
        {
            cout<<"Key:NIL "<<endl;
        }
    }
}
int main()
{
    insert(72);
    insert(15);
    insert(18);
    insert(43);
    insert(36);
    insert(10);
    insert(65);
    display();
}
