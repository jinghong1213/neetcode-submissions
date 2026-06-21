class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # if students[j] == sandwiches[i], cancel it, else queue behind
        # return the leftover students which unable to eat = len(students)
        # edge cases: the order of the sandwiches does matter
        # eg: student[1, 1, 1, 1]
        #     sandwiches[0, 1, 1, 1]
        # In this case, no one is getting sandwiches

        # 一开始，还没吃午餐的学生人数 = 总人数
        res = len(students)

        # 创造一个点名小本本，统计每种口味的学生各有多少人
        #cnt = {}
        #for s in students:
        #    if s not in cnt:
        #        cnt[s] = 0
        #    cnt[s] += 1  # 对应口味的人数加 1

        cnt = Counter(students)

        # 盯着那一叠三明治，从最上面的开始发
        for s in sandwiches:
            # 如果点名本上显示：现在还有学生想要这一款三明治
            if cnt[s] > 0:
                res -= 1  # 成功喂饱一个，剩下没吃的人数减 1
                cnt[s] -= 1  # 点名本上，该口味的需求量减 1
            else:
                # 【核心死局】最上面的三明治没人要了，后面的三明治拿不出，队伍直接卡死！
                # 直接返回现在还饿着肚子的学生人数
                return res

        # 如果所有三明治都完美发完了，res 会刚好变成 0
        return res

        
