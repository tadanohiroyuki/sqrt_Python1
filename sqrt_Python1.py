#[sqrt_Python1.py]
#Copyright (c) [year] [tadanohiroyuki]
#This software is released under the MIT License.
#http://opensource.org/licenses/mit-license.php

while True:
    x = input("正の数値を入力してください")
    
    if x == "end":
        break
    
    try:
        x = float(x)
    except ValueError:
        
        print(x,"は数値に変換できません")
        continue
    
    except:
        print("予期していないエラーです")
        
        exit()
    if(x <= 0):
        
        print(x,"は正の数値ではありません")
        continue 
    
    rnew = x

    diff = abs(rnew - x/rnew)
    
    
    while(diff > 1.0E-6):
        r1 = rnew
        r2 = x/r1
        
        rnew = (r1 + r2)/2
        
        print(r1,rnew,r2)
        
        diff = r1 - r2