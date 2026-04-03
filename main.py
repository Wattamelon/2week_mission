


def main():
    print("2주차 과제 퀴즈풀이")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    
    try: 
        tmp = int(input())
        if tmp == 1:
            print("퀴즈 풀기")
        elif tmp == 2:
            print("퀴즈 추가")
        elif tmp == 3:
            print("퀴즈 목록")
        elif tmp == 4:
            print("점수 확인")
        elif tmp == 5: 
            print("종료")
        else:
            print("1~5사이의 숫자를 입력 해주세요.")

    except:
        print("1~5사이의 숫자를 입력 해주세요.")
        



if __name__ == '__main__':
    main()