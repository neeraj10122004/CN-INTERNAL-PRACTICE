#include<bits/stdc++.h>
using namespace std;

int main(){
    string divisor;
    string dataword;
    cout << "enter divisor : " << endl;
    cin >> divisor ;
    cout << "enter dataword : " << endl;
    cin >> dataword ;

    vector<int> div;
    deque<int> data;
    vector<int> original_data;
    for(int i=0;i<divisor.size();i++){
        string s(1,divisor[i]);
        div.emplace_back(stoi(s));
        
    }
    for(int i=0;i<dataword.size();i++){
        string s(1,dataword[i]);
        data.emplace_back(stoi(s));
        original_data.emplace_back(stoi(s));
    }
    for(int i=0;i<div.size()-1;i++){
        data.emplace_back(0);
    }
    cout << "divisor" <<endl;
    cout << "\n";
    for(int i=0;i<div.size();i++){
        cout << div[i] <<" ";
    }
    cout << "\n";
    cout << "dataword" <<endl;
    cout << "\n";
    for(int i=0;i<data.size();i++){
        cout << data[i] <<" ";
    }
    cout << "\n";

    while(data.size()>div.size()-1){
        if(data[0]==1){
        for(int j=0;j<div.size();j++){
            data[j]=data[j]+div[j];
            data[j]%=2;
        }
        }
        data.pop_front();
    }
    cout << endl;
    cout << "redundancy" <<endl;
    for(int i=0;i<data.size();i++){
        cout << data[i] << " ";
        original_data.emplace_back(data[i]);
    }
    cout << endl;
    cout << "transmitting frame" <<endl;
    for(int i=0;i<original_data.size();i++){
        cout << original_data[i] << " ";
    }
    cout << endl;
    string inp;
    cout << "enter the reciver input "<<endl;
    cin >> inp ;
    deque<int> rec;
    vector<int> recived;
    for(int i=0;i<inp.size();i++){
        string s(1,inp[i]);
        rec.emplace_back(stoi(s));
        recived.emplace_back(stoi(s));
    }
    cout << endl;

    while(rec.size()>div.size()-1){
        if(rec[0]==1){
        for(int j=0;j<div.size();j++){
            rec[j]=rec[j]+div[j];
            rec[j]%=2;
        }
        }
        rec.pop_front();
    }
    cout << endl;
    int error_bit=0;
    cout << "reminder" << endl;
    for(int i=0;i<rec.size();i++){
        cout << rec[i] << " ";
        error_bit+=((int)pow(2,i))*rec[i];
    }
    cout << endl;

    
    if(error_bit==0){
        cout << "no error" <<endl;
    }
    else{
        cout << "\n" <<"error at reciver side"<< "\n";
    for (int i=0;i<recived.size();i++) {
        cout<<recived[i]<<" ";
    }
    cout << endl;
    }
    return 0;
}