class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        a_ix = len(a)-1
        b_ix = len(b)-1
        add = 0
        while a_ix >= 0 and b_ix >= 0:
            if a[a_ix] == "1":
                if b[b_ix] == "1":
                    if add == 1:
                        result = "1"+result
                    else:
                        result = "0"+result
                        add = 1
                else:
                    if add == 1:
                        result = "0"+result
                    else:
                        result = "1"+result
            else:
                if b[b_ix] == "1":
                    if add == 1:
                        result = "0"+result
                    else:
                        result = "1"+result
                else:
                    if add == 1:
                        result = "1"+result
                        add = 0
                    else:
                        result = "0"+result
            a_ix -= 1
            b_ix -= 1
        else:
            if a_ix < 0:
                while b_ix >= 0:
                    if b[b_ix] == "1":
                        if add == 1:
                            result = "0"+result
                        else:
                            result = "1"+result
                    else:
                        if add == 1:
                            result = "1"+result
                            add = 0
                        else:
                            result = "0"+result
                    b_ix -= 1
            else:
                while a_ix >= 0:
                    if a[a_ix] == "1":
                        if add == 1:
                            result = "0"+result
                        else:
                            result = "1"+result
                    else:
                        if add == 1:
                            result = "1"+result
                            add = 0
                        else:
                            result = "0"+result
                    a_ix -= 1
        if add == 1:
            return "1"+result
        else:         
            return result  
        