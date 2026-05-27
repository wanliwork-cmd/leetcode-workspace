package com.wan;

import java.lang.reflect.Array;
import java.util.Arrays;

/**
 * @author WanLi
 * @date 2026/1/20 16:00
 * @description: 移动零
 */
public class topic_283 {



    /*  283.移动零
        给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
        请注意 ，必须在不复制数组的情况下原地对数组进行操作。

        示例 1:
        输入: nums = [0,1,0,3,12]
        输出: [1,3,12,0,0]

        示例 2:
        输入: nums = [0]
        输出: [0]

        提示:
        1 <= nums.length <= 104
        -231 <= nums[i] <= 231 - 1

        进阶：你能尽量减少完成的操作次数吗？
    *
    *
    * */

    public static int[] moveZeroes(int[] nums) {
        //判断数组的大小是否小于2
        if(nums.length < 2){
            return nums;
        }
        int i = 0,j=0;
        for(;i<nums.length;i++){
            //判断非零元素然后赋值给j索引
            if(nums[i] != 0){
                nums[j] = nums[i];
                j++;
            }
        }
        while(j < nums.length){
            nums[j] = 0;
            j++;
        }
        return nums;
    }

    //优化
    public static int[] moveZeroes1(int[] nums) {
        if (nums.length < 2){
            return nums;
        }
        int i = 0,j=0;
        for(;i < nums.length;i++){
            if(nums[i] != 0){
                if(i != j){
                    nums[j] = nums[i];
                    nums[i] = 0;
                }
                j++;
            }
        }
        return nums;
    }


    public static void main(String[] args) {
        int[] nums = {0,1,0,3,12};
        int[] nums1 = {0};
        int[] nums2 = {1,0,3,4,0,0,7,8,9,10};
        System.out.println(Arrays.toString(moveZeroes(nums)));
        System.out.println(Arrays.toString(moveZeroes(nums1)));
        System.out.println(Arrays.toString(moveZeroes(nums2)));
    }
}
