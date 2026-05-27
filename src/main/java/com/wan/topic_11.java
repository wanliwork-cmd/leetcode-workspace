package com.wan;

/**
 * @author WanLi
 * @date 2026/1/19 14:08
 * @description: 盛最多水的容器
 */
public class topic_11 {

    /*  题目11： 盛最多水的容器
    *   给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
        找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
        返回容器可以储存的最大水量。
        说明：你不能倾斜容器。
    * */
    //暴力破解法
    public static int maxArea(int[] height) {
        int max = 0;
        for(int i = 0; i < height.length-1;i++){
            for (int j = i+1;j < height.length;j++){
                int area = (j - i) * Math.min(height[i],height[j]);
                max = Math.max(area, max);
            }
        }
        return max;
    }

    /*
    *   使用双指针(双指针夹逼思想)
    * 核心思想：
        用两个指针分别指向数组的最左端和最右端
        每次计算当前两个指针形成的容器面积
        移动较短的那条线对应的指针
        重复直到两个指针相遇
    * */
    public static int maxArea1(int[] height){
        int max = 0;
        int i = 0;
        int j = height.length-1;
        while(i < j){
            max = Math.max(Math.min(height[i], height[j]) * (j - i),max);
            if(height[i] < height[j]){
                i++;
            }else{
                j--;
            }
        }
        return max;
    }


    public static void main(String[] args) {
        int[] height = {1,8,6,2,5,4,8,3,7};
        int[] height1 = {1,8,6,2,5,4,8,3,7,100,10,20};
        System.out.println(maxArea(height));
        System.out.println(maxArea(height1));
        System.out.println(maxArea1(height));
        System.out.println(maxArea1(height1));
    }



}
