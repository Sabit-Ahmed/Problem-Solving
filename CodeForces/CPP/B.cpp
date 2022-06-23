#include<bits/stdc++.h>
using namespace std;

int main()
{
    char* a=NULL;
    int n,count=0;
    cin>>n;
    a=new char[n];
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
        //if(a[i]=='x'&&a[i+1]=='x')
          //  count++;

    }

    for(int i=0;i<n;i++)
    {
        if(a[i]=='x'&&a[i+1]=='x'&&a[i+2]=='x')
            count++;

    }
    /*if((count)>2)
    {
        for(int j=0;j<n-1;j++)
        {
            a[j]=a[j+1];
        }
    }*/
    cout<<endl<<count<<endl;

    /*for(int i=0;i<n-1;i++)
    {
        cout<<a[i]<<endl;
    }*/

    delete [] a;
    a=NULL;
    return 0;
}
