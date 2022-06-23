#include<bits/stdc++.h>
using namespace std;

int main()
{
    int n,count=0,p[100],q[100];
    cin>>n;

    for(int i=0;i<n;i++)
    {
        cin>>p[i]>>q[i];
        if(q[i]-p[i]>=2)
        {
            count++;
        }
    }
    cout<<endl<<count<<endl;
}
