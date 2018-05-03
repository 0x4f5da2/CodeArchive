#ifndef WEEK7_DISCUSSION_DEQUEUE_H
#define WEEK7_DISCUSSION_DEQUEUE_H
#define MAXSIZE 1000
using namespace std;


template <typename T>
class DEQ{
protected:
    T que[MAXSIZE];
    int back,front;
    int cnt;
public:
    DEQ(){
        back=front=0;
        cnt=0;
    }
    bool PushFront(const T ToPush){
        if(cnt>=MAXSIZE-1)  return false;
        front=((front-1)+MAXSIZE)%MAXSIZE;
        que[front]=ToPush;
        cnt++;
        return true;
    }
    bool PushBack(const T ToPush){
        if(cnt>=MAXSIZE-1)  return false;
        que[back]=ToPush;
        back=((back+1)+MAXSIZE)%MAXSIZE;
        cnt++;
        return true;
    }
    bool PopFront(){
        if(cnt==0){
            return false;
        }
        front=((front+1)+MAXSIZE)%MAXSIZE;
        cnt--;
        return true;
    }
    bool PopBack(){
        if(cnt==0){
            return false;
        }
        back=((back-1)+MAXSIZE)%MAXSIZE;
        cnt--;
        return true;
    }
    int EleCnt(){
        return cnt;
    }
    T GetFront(){
        return que[front];
    }
    T  GetBack(){
        return que[((back-1)+MAXSIZE)%MAXSIZE];
    }
};
#endif //WEEK7_DISCUSSION_DEQUEUE_H