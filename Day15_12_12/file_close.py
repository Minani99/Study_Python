def test():
    print("1")
    try:
        print("2")
        return
    except:
        print("exc")
    finally:
        print("final")
    print("함수 내부 마지막줄")

test()