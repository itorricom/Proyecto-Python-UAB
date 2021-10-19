#include <iostream>
using namespace std;

int main() {
  int num;
  cin>>num;
  string pareja[num];
  for(int i=0; i<num; i++){
    int t , l;
    cin>>t>>l;
    if(l%t==0){
      pareja[i]='R';
    }else{
      pareja[i]='I';
    }
  }
  for(int j=0; j<num; j++){
    cout<<pareja[j]<<endl;
  }
  return 0;
}
