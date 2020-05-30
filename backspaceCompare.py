class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        sc=S.count('#')
        tc=T.count('#')
        for i in range(max(sc,tc)):
            if S.find('#') >0 and T.find('#') >0:
                S=S[:S.find('#')-1]+S[S.find('#')+1:]
                T=T[:T.find('#')-1]+T[T.find('#')+1:]

            elif S.find('#') >0 :
                S=S[:S.find('#')-1]+S[S.find('#')+1:]
                if T.find('#') ==0:
                    T=T[T.find('#')+1:]    

            elif T.find('#') >0:

                T=T[:T.find('#')-1]+T[T.find('#')+1:]
                if S.find('#') ==0:
                    S=S[S.find('#')+1:] 
            else:
                #print('else')
                if S.find('#') ==0 and T.find('#')==0:
                    S=S[S.find('#')+1:]
                    T=T[T.find('#')+1:] 
                elif S.find('#') ==0:
                    S=S[S.find('#')+1:]
                else:
                    T=T[T.find('#')+1:] 
        if S == T:
            return True
        else:
            return False