/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
    var result = [];
    var counter = {};

    for (var idx = 0; idx < nums1.length; ++idx){
        var num = nums1[idx];
        if(!counter.hasOwnProperty(num)){
            counter[num] = 0;
        }
        counter[num] ++;
    }

    for (idx = 0; idx < nums2.length; ++idx){
        var num = nums2[idx];
        if(counter.hasOwnProperty(num) && counter[num] > 0){
            result.push(num);
            counter[num] --;
        }
    }

    return result;
};