from src.show_quizzes import show

def menu():
    while True:
        print("=============================")
        print("2주차 과제 퀴즈풀이")
        print("안내 : 코디세이 2주차 과제용 퀴즈입니다. 숫자를 선택해주세요.")
        print("=============================")
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        try: 
            print("원하는 메뉴 번호를 입력하세요.")
            tmp = int(input().strip())
            print("=============================")
            if tmp == 1:
                print("퀴즈 풀기")
            elif tmp == 2:
                print("퀴즈 추가")
            elif tmp == 3:
                show() # 퀴즈목록
            elif tmp == 4:
                print("점수 확인")
            elif tmp == 5: 
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 1~5 사이의 숫자를 입력해주세요.")
        except KeyboardInterrupt:
            print("입력이 중단되었습니다. 프로그램을 종료합니다.")
            break
        except EOFError:
            print("입력을 받을 수 없습니다. 프로그램을 종료합니다.")
            break
        except:
            print("1~5사이의 숫자를 입력 해주세요.")

        print("=============================")


