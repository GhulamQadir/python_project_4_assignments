def main(dataList,value,a):
    a=14 # a primitive data types values stay in function if we don't return it
    for i in range(3):
        dataList.append(value)


if __name__ == '__main__':
    a:int=12
    dataList:list[str]= []
    dataStructure = main(dataList,"My book",a)
    print(a)
    print(f"Updated List: {dataList}")
    