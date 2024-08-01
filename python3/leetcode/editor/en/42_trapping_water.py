from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        ans = 0
        # monotonic stack
        st = []
        for i in range(len(height)):
            h = height[i]
            while st and h >= height[st[-1]]:
                middle = st.pop()
                if not st:
                    break
                left = st[-1]
                dh = min(height[left], h) - height[middle]
                distance = (i - left - 1)
                print('left', left, 'middle', middle, 'right', h, 'distance', distance, 'dh', dh)
                ans += dh * distance
            st.append(i)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
