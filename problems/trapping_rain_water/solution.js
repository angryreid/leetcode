/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    let sum=0,l=0,r=height.length-1;
    let maxl=0,maxr=0;
    while(l<r){
        maxl = Math.max(height[l],maxl);
        maxr = Math.max(height[r],maxr);
        
        if(maxl === Math.min(maxl,maxr)){
            sum += maxl - height[l];
            l++;
        }
        else{
            sum += maxr - height[r];
            r--;
        }
    }
    return sum;
};