#include<bits/stdc++.h>
using namespace std;

int main()
{
    int f=0;
    string st;
    cin>>st;



    for(int i=1; i<=st.length(); i++)
    {
        if(st[i]<=90&&st[i+1]>=97)
        {
            for(int j=i-1 ; j>0; j--)
            {
                st[j]=st[j]-32;

            }
            //s[0]=s[0]+32;
            cout<<st<<endl;
            f++;
            break;

        }
        else if(st[i]>=65&&st[i]<=90)
        {
            //s[0]=s[0]-32;
            st[i]=st[i]+32;
        }
        else if(st[0]>=97&&st[0]<=122)
        {
            st[0]=st[0]-32;
            break;
        }

    }


    if(f!=1)
    {
        cout<<st<<endl;
    }

    return 0;
}
