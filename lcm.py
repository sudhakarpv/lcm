# lcm
def main():
    pass
    inp=list(map(int,input().split()))
    k=max(inp)
    j=min(inp)
    while(k%j!=0):
        k+=k
    print(k)
if __name__ == '__main__':
    main()
