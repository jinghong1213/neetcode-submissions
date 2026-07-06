class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # l 是最慢速度（1根），r 是最快速度（香蕉堆里最多的那一堆的数量）
        l, r = 1, max(piles)

        # res 用来记录目前最安全、又能吃完的最小速度，先拿最快的速度顶替
        res = r

        # 开始用二分查找来测试速度 k
        while l <= r:
            # 选一个中间的速度 k 拿来测试
            k = (l + r) // 2

            # 计算用这个速度 k 吃完所有香蕉，总共需要多少小时（totalTime）
            totalTime = 0
            for p in piles:
                # float(p) / k 是算需要多少小时，math.ceil() 是向上取整
                # 比如 7 根香蕉，速度是 3：7/3 = 2.33，向上取整就是 3 小时
                totalTime += math.ceil(float(p) / k)

            # --- 判断测试结果 ---
            if totalTime <= h:
                # 【情况 A】总时间没有超时（<= h），说明这个速度 k 是可行的！
                res = k  # 先把这个不错的速度记在小本本 res 里面

                # 但 Koko 想挑战更慢、更优雅的吃法，所以我们去左半区找更小的速度
                r = k - 1
            else:
                # 【情况 B】总时间超时了（> h），说明这个速度 k 太慢了，吃不完！
                # 没办法，下一轮只能把速度加快，去右半区找更大的速度
                l = k + 1

        # 退出循环后，res 记下来的就是刚好能吃完的“最慢黄金速度”
        return res

        #时间复杂度直接从原本慢吞吞的 O(max(P) x N) 优化成极其高效的 O(Nlog(max(P)))