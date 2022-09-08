class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        varity={'2':["a","b","c"],'3':["d","e","f"],'4':["g","h","i"],'5':["j","k","l"],'6':["m","n","o"],'7':["p","q","r","s"],'8':["t","u","v"],'9':["w","x","y","z"]}
        final=[]
        for i in digits:
            final.append(varity[i])
        if len(final)<1:
            return final
        if len(final)<2:
            return final[0]
        else:
            while(True):
                if(len(final)==1):
                    return final[0]
                else:
                    a=final[0]
                    b=final[1]
                    final=final[2:]
                    sub=[]
                    for each1 in a:
                        for each2 in b:
                            sub.append(each1+each2)
                    lemma=[]
                    lemma.append(sub)
                    lemma.extend(final)
                    final=lemma
