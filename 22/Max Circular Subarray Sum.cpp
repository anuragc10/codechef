// { Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
class Solution{
    public:
    // arr: input array
    // num: size of array
    //Function to find maximum circular subarray sum.
    int kadane(int arr[],int n){
        int maxsum=INT_MIN;
        int curr=0;
        for(int i=0;i<n;i++){
            curr+=arr[i];
            if(curr<0)
            {
                curr=0;
            }
            maxsum=max(maxsum,curr);
        }
        return maxsum;
    }
    int circularSubarraySum(int arr[], int num){
        // your code here
        int wrapsum;
        int nonwrapsum;
        
        nonwrapsum=kadane(arr,num);
        
        int totalsum=0;
        int t=0;
        for(int i=0;i<num;i++)
        {
            if(arr[i]>=0)
            {
                t=1;
                break;
            }
        }
        for(int i=0;i<num;i++)
        {
            totalsum+=arr[i];
            arr[i]=-arr[i];
        }
        if(t==0)
        {
        for(int i=0;i<num;i++)
        {
            arr[i]=-arr[i];
        }
        sort(arr,arr+num);
        return arr[num-1];
        }
        else{
        wrapsum=totalsum+kadane(arr,num);
        return max(wrapsum,nonwrapsum);
        }
    }
};

// { Driver Code Starts.

int main()
 {
	int T;
	
	//testcases
	cin>> T;
	
	while (T--)
	{
	    int num;
	    
	    //size of array
	    cin>>num;
	    int arr[num];
	    
	    //inserting elements
	    for(int i = 0; i<num; i++)
	        cin>>arr[i];
	        
	    Solution ob;
	    //calling function
	    cout << ob.circularSubarraySum(arr, num) << endl;
	    
	}
	
	return 0;
}  // } Driver Code Ends
