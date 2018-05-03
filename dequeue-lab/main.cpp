#include <iostream>
#include <queue>
#include <set>
#include "deq.h"

set<int> ans1,ans2;
//令受限端均为后端

//输入受限
void DFS1(queue<int> answer,int ans_cnt,DEQ<int> deq,int step){
    if(ans_cnt==4){
        int temp=0;
        while(!answer.empty()){
            temp=temp*10+answer.front();
            answer.pop();
        }
        ans1.insert(temp);
        return;
    }
    queue<int> ans_temp;
    int ans_cnt_temp;
    DEQ<int> deq_temp;

    //前端进入deq
    if(step<4) {
        ans_temp = answer;
        ans_cnt_temp = ans_cnt;
        deq_temp = deq;
        deq_temp.PushFront(step+1);
        DFS1(ans_temp,ans_cnt_temp,deq_temp,step+1);
    }


    if(deq.EleCnt()>0){
        //前端弹出deq
        ans_temp = answer;
        ans_cnt_temp = ans_cnt;
        deq_temp = deq;
        ans_temp.push(deq_temp.GetFront());
        ans_cnt_temp++;
        deq_temp.PopFront();
        DFS1(ans_temp,ans_cnt_temp,deq_temp,step);
        //后端弹出deq
        ans_temp = answer;
        ans_cnt_temp = ans_cnt;
        deq_temp = deq;
        ans_temp.push(deq_temp.GetBack());
        ans_cnt_temp++;
        deq_temp.PopBack();
        DFS1(ans_temp,ans_cnt_temp,deq_temp,step);
    }
    return;
}

//输出受限
void DFS2(queue<int> answer,int ans_cnt,DEQ<int> deq,int step){
    if(ans_cnt==4){
        int temp=0;
        while(!answer.empty()){
            temp=temp*10+answer.front();
            answer.pop();
        }
        ans2.insert(temp);
        return;
    }
    queue<int> ans_temp;
    int ans_cnt_temp;
    DEQ<int> deq_temp;


    if(step<4) {
        //前端进入deq
        ans_temp = answer;
        ans_cnt_temp = ans_cnt;
        deq_temp = deq;
        deq_temp.PushFront(step+1);
        DFS2(ans_temp,ans_cnt_temp,deq_temp,step+1);

        //后端进入deq
        ans_temp = answer;
        ans_cnt_temp = ans_cnt;
        deq_temp = deq;
        deq_temp.PushBack(step+1);
        DFS2(ans_temp,ans_cnt_temp,deq_temp,step+1);
    }


    if(deq.EleCnt()>0){
        //前端弹出deq
        ans_temp = answer;
        ans_cnt_temp = ans_cnt;
        deq_temp = deq;
        ans_temp.push(deq_temp.GetFront());
        ans_cnt_temp++;
        deq_temp.PopFront();
        DFS2(ans_temp,ans_cnt_temp,deq_temp,step);
    }
    return;
}

int main() {
    DEQ<int> deq;
    queue<int> answer;
    DFS1(answer,0,deq,0);
    DFS2(answer,0,deq,0);
    int flag=1;
    cout<<"When input is restricted:"<<endl;
    for(set<int>::iterator it1=ans1.begin();it1!=ans1.end();it1++){
        cout<<*it1;
        if(flag%5==0) cout<<endl;
        else cout<<" ";
        flag++;
    }
    cout<<endl<<endl;
    flag=1;
    cout<<"When output is restricted:"<<endl;
    for(set<int>::iterator it2=ans2.begin();it2!=ans2.end();it2++){
        cout<<*it2;
        if(flag%5==0) cout<<endl;
        else cout<<" ";
        flag++;
    }
    cout<<endl<<endl;
    cout<<"Answer for 3(1):"<<endl;
    for(set<int>::iterator it1=ans1.begin();it1!=ans1.end();it1++){
        if(ans2.count(*it1)==0) cout<<*it1<<endl;
    }
    cout<<"Answer for 3(2):"<<endl;
    for(set<int>::iterator it2=ans2.begin();it2!=ans2.end();it2++){
        if(ans1.count(*it2)==0) cout<<*it2<<endl;
    }
    return 0;
}