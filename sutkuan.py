fromthis,tothis = [int(e) for e in input('สูตรคูณแม่ a -> b : ').split()]
def sutkuan(fromthis,tothis):
    for i in range(fromthis,tothis+1):
        for k in range(1,13):
            print(f'{i} x {k} = {i*k}')
        print('-'*20)

sutkuan(fromthis,tothis)