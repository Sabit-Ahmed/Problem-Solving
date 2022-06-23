#include<iostream>
#include<string>
using namespace std;
int main()
{
    int n,count1=0,count2=0;char s[100000];
    cin>>n;
    for(int i=0;i<n;i++)
        {
            cin>>s[i];
            if(s[i]=='A')
                count1++;
            else if(s[i]=='D')
                count2++;
        }
        if(count1>count2)
            cout<<"Anton";
        else if(count1<count2)
            cout<<"Danik";
        else
            cout<<"Friendship";
    return 0;
}
