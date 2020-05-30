class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        st=''
        for i,c in enumerate(strs):
            #i index c value
            st=''.join(sorted(c))
            #print(st)
            if (st not in d.keys()):
                d[st]=[strs[i]]
               # print('if',i)
            else:
                d[st].append(strs[i])
                #print('el',i)
        return list(d.values())
        