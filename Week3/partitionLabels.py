class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        end, indx, res = float('-inf'), -1, []
        for x in range(len(S)):
            if x > end: 
                end = max(end, S.rfind(S[x]))
                indx += 1 # Next res indx
                res.append(end+1)
            else: 
                end = max(end, S.rfind(S[x]))
                res[indx] = end+1 # Replace curr result
        
        final = [j - i for i, j in zip(res[: -1], res[1: ])]
        final.insert(0, res[0])
        return final