#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
//#define debug(x) std::cout << "[debug]" << #x << ":" << x << "\n"
#define debug(x) 0
ostream& operator<<(ostream& o, pair<int,int> p){
    o << "(" << p.first << ", " << p.second << ")";
    return o;
}

ostream& operator<<(ostream& o, vector<pair<int,int>> v){
    o << "<";
    bool firstPrint = true;
    for(auto p: v){
        if (firstPrint){
            firstPrint = false;
        } else {
            o << ", ";
        }
        o << p;
    }
    o << ">";
    return o;
}

int solve(vector<pair<int,int>>& lines){
    sort(lines.begin(), lines.end(), [](pair<int,int> a, pair<int,int> b){
        if(a.first == b.first){
            return a.second > b.second;
        } return a.first < b.first;
    });
    int result = 0;
    int checked_till = -1000000001;
    for(pair<int,int>& p : lines){
        if(p.second <= checked_till){
            debug(checked_till);
            debug(p);
            continue;
        } else {
            int begin = max(p.first, checked_till);
            result += (p.second - begin);
            checked_till = p.second;
            debug(checked_till);
            debug(result);
            debug(p);
        }
    }

    return result;
}

int main(){
    int N;
    vector<pair<int,int>> lines;
    pair<int,int> temp;

    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    cin >> N;
    for(int i = 0;i < N;i++){
        cin >> temp.first >> temp.second;
        lines.push_back(temp);
    }
    cout << solve(lines);
    return 0;
}