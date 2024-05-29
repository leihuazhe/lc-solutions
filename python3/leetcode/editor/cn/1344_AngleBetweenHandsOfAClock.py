#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# source:  https://leetcode-cn.com/problems/angle-between-hands-of-a-clock
# source:  https://leetcode.com/problems/angle-between-hands-of-a-clock

# [1344]-angle-between-hands-of-a-clock

"""
给你两个数 hour 和 minutes 。请你返回在时钟上，由给定时间的时针和分针组成的较小角的角度（60 单位制）。 

 

 示例 1： 

 

 输入：hour = 12, minutes = 30
输出：165
 

 示例 2： 

 

 输入：hour = 3, minutes = 30
输出；75
 

 示例 3： 

 

 输入：hour = 3, minutes = 15
输出：7.5
 

 示例 4： 

 输入：hour = 4, minutes = 50
输出：155
 

 示例 5： 

 输入：hour = 12, minutes = 0
输出：0
 

 

 提示： 

 
 1 <= hour <= 12 
 0 <= minutes <= 59 
 与标准答案误差在 10^-5 以内的结果都被视为正确结果。 
 

 Related Topics 数学 👍 50 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # 6d
        min_deg = 360 / 60
        # 30d
        hour_deg = 360 / 12

        hour = 0 if hour == 12 else hour

        hour_angle = hour_deg * hour + (minutes / 60) * hour_deg
        min_angle = min_deg * minutes

        return min(abs(hour_angle - min_angle), 360 - abs(hour_angle - min_angle))


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    s = Solution()
    print(s.angleClock(hour=12, minutes=30))
    print(s.angleClock(hour=3, minutes=30))
    print(s.angleClock(hour=3, minutes=15))
    print(s.angleClock(hour=4, minutes=50))
    print(s.angleClock(hour=12, minutes=0))
    print(s.angleClock(hour=1, minutes=57))
    print(s.angleClock(hour=3, minutes=30))
