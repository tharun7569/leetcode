#include <string>
class Solution {
public:
    string convertToTitle(int n) {
        string r="";
        while(n>0)r=char('A'+(--n)%26)+r,n/=26;
        return r;
    }
};
