allowed = "exdohslrwipnt"
words = ["xrwlstne","rs","ioetdll","lwi","r","pieonois","r","xtp","stia","gicfuvmnr","hdntpxse","sodxws","v","hstirooon","d"]

y = set(allowed)
count = 0
for i in words:
    if set(i).issubset(y):
        count += 1

print(count)
