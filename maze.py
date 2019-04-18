grid =          [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 , 1],
                 [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 , 1],
                 [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1 , 1],
                 [1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0 , 1],
                 [1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0 , 1],
                 [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0 , 1],
                 [1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1 , 1],
                 [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0 , 1],
                 [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0 , 1],
                 [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0 , 1],
                 [1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 3 , 1],
                 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 , 1]]
moves=['0']
stack=[]
rightWay=[]
position=['','']

def draw():
    j=0
    for i in range(0, 12, 1):
            print(str(grid[i][j])+'|'+str(grid[i][j+1])+'|'+str(grid[i][j+2])+'|'+str(grid[i][j+3])+'|'+str(grid[i][j+4])+'|'+str(grid[i][j+5])+'|'+str(grid[i][j+6])+'|'+str(grid[i][j+7])+'|'+str(grid[i][j+8])+'|'+str(grid[i][j+9])+'|'+str(grid[i][j+10])+'|'+str(grid[i][j+11])+'|')
def isWin(x,y):
    if grid[x][y]==3 :
        return True
    else:
        return False
def isRightEmpty(x,y):
    if grid[x][y+1]==0 or grid[x][y+1]==3:
        return True
    else:
        return False
def isLeftEmpty(x,y):
    if grid[x][y-1]==0 or grid[x][y-1]==3:
        return True
    else:
        return False

def isTopEmpty(x,y):
    if grid[x-1][y]==0 or grid[x-1][y]==3:
        return True
    else:
        return False

def isDownEmpty(x,y):
    if grid[x+1][y]==0 or grid[x+1][y]==3:
        return True
    else:
        return False
        
def operation (x,y):
# رسم جدول
    draw()
# اضافه کردن مختصات کنونی به انتهای استک
    stack.append([x , y])
    print('moved to ['+str(x)+']['+str(y)+']')
#برسی بردن
    if isWin(x,y):
        print (' you win the game with :'+moves[0]+'moves')
        print ('the lenghs of right way :'+str(len(rightWay)))
        print ('the right Way is :')
        print (rightWay)
        
        

    else:
        moves[0] =str(int( moves[0])+1)
        grid[x][y]= 'x'
        if isRightEmpty(x,y):
            rightWay.append('Right')
            print ('right is empty')
            operation(x,y+1)
        elif isDownEmpty(x,y):
            rightWay.append('Down')
            print('Down is empty')
            operation(x+1,y)
        elif isLeftEmpty(x,y):
            rightWay.append('Left')
            print('Left is empty')
            operation(x,y-1)
        elif isTopEmpty(x,y):
            rightWay.append('Top')
            print('Top  is empty')
            operation(x-1,y)

        else:
            print('Way Is Wrong')
            stack.pop()
            rightWay.pop()
            position=stack.pop()    
            print(position)
            operation(position[0],position[1])
            
def start(x,y):
    operation(x,y)


var1, var2 = [int(x) for x in input("Enter begennig place ").split()]   
start(var1,var2)

