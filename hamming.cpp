#include<bits/stdc++.h>
using namespace std;

vector<int> gen(int n,int cl){
    vector<int> ret;
    bool temp=false;
    for(int i=0;i<=cl;i++){
        if(n!=1){
        if(i%n==0 && i!=0){
            temp=!temp;
        }
        if(temp){
            ret.emplace_back(i);
        }
        }
        else{
            if(temp){
            ret.emplace_back(i);
            }
            temp=!temp;
        }
    }
    return ret;
}
int main(){
    //considering even paratiy
    string s;
    int m,r,cl;
    cout << "enter the string \n";
    cin >> s;
    cout << "string : "<< s<<"\n" <<"string length (l) : "<< s.size()<<"\n";
    m=s.size();
    for(int i=1;i<=m;i++){
        if((int)pow(2,i)>=(i+m+1)){
            r=i;
            break;
        }
    }
    cl=m+r;
    cout << "redundancy (r): " << r << "\n";
    cout << "code length (cl): " << cl << "\n";
    vector<int> code(cl,0);
    vector<pair<int,int>> red;
    for(int i=0;i<cl;i++){
        int y = (int)pow(2,i)-1;
        if(y>=cl){
            break;
        }
        else{
            red.emplace_back((int)y+1,0);
            code[y]=-1;
        }
    }
    reverse(code.begin(),code.end());
    int j=0;
    for(int i=0;i<cl;i++){
        if(code[i]!=-1){
            string st(1,s[j]);
            j++;
            code[i]=stoi(st);
        }
    }

    for(int i=0;i<code.size();i++){
        cout << code[i] << " ";
    }
    cout << "\n";
    reverse(code.begin(),code.end());

    for(int j=0;j<red.size();j++){
        cout << red[j].first << endl;
        vector<int> aa= gen(red[j].first,cl);
        code[red[j].first-1]=-1;
        for(int i=0;i<aa.size();i++){
            if(code[aa[i]-1]!=-1){
            code[red[j].first-1]+=code[aa[i]-1];
            }
        }
        code[red[j].first-1]+=1;
        code[red[j].first-1]%=2;
    }

    reverse(code.begin(),code.end());
    cout << "sender side encoded code :" <<endl;
    cout << "\n";
    for(int i=0;i<code.size();i++){
        cout << code[i] << " ";
    }
    cout << "\n";

    cout << "enter recived code : "<<endl;
    string rec;
    cin >> rec;
    vector<int> recived;
    for(int i=0;i<rec.size();i++){
        string rr(1,rec[i]);
        recived.emplace_back(stoi(rr));
    }
    cout << "reciver side recived code :" <<endl;
    cout << "\n";
    for(int i=0;i<recived.size();i++){
        cout << recived[i] << " ";
    }
    cout << "\n";

    int error_node=0;
    vector<pair<int,int>> paratiy;
    for(int i=0;i<recived.size();i++){
        int y = (int)pow(2,i)-1;
        if(y>=recived.size()){
            break;
        }
        else{
            paratiy.emplace_back((int)y+1,0);
        }
    }
    reverse(recived.begin(),recived.end());
    vector<int> p;
    for(int j=0;j<paratiy.size();j++){
        cout << paratiy[j].first<< paratiy[j].second<<endl;
        vector<int> aa= gen(paratiy[j].first,recived.size());
        for(int i=0;i<aa.size();i++){
            paratiy[j].second+=recived[aa[i]-1];
        }
        paratiy[j].second%=2;
        p.emplace_back(paratiy[j].second);
        error_node+=((int)pow(2,j))*paratiy[j].second;
    }
    reverse(p.begin(),p.end());
    if(error_node==0){
        cout << "no error " <<endl;
    }
    else{
        cout << endl;
        for(int i=0;i<p.size();i++){
            cout << p[i] << " ";
        }
        cout << endl;
        cout << "error node " << error_node <<endl; 
    }
    if(recived[error_node-1]==0){
        recived[error_node-1]=1;
    }
    else{
        recived[error_node-1]=0;
    }
    reverse(recived.begin(),recived.end());
    cout << "\n";
    for(int i=0;i<recived.size();i++){
        cout << recived[i] << " ";
    }
    cout << "\n";
    return 0;
}