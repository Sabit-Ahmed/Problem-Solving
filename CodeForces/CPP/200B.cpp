#include<bits/stdc++.h>
using namespace std;

int main()
{
    double n,s,p[100];
    s=0;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>p[i];
        s=s+p[i];
    }
    cout<<s/n<<endl;
}
