def get_result(x,y):
    if y==0:
        return 1
    elif y==2:
        return x*x
    elif y<2:
        return x
    elif y % 2 != 0:
        return get_result(x * x, (y-1)/2)*x
    elif y % 2 ==0:
        return get_result(x * x,y/2)
    else:
        return 0

def main():
    try:
        result=0
        x=2
        y=6
        if isinstance(y,int):
            result = get_result(x, y)
            print(result)
        else:
            print("please input int for y")
    except BaseException as e:
        print(e)

if __name__ == "__main__":
    main()