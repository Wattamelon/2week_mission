1. 깃허브 원격레포지토리 연결 과정 

img1

(base) melon@munseongon-ui-MacBookAir 코디세이 % cd 2week_mission 
(base) melon@munseongon-ui-MacBookAir 2week_mission % git init
/Users/melon/Desktop/코디세이/2week_mission/.git/ 안의 빈 깃 저장소를 다시 초기화했습니다
(base) melon@munseongon-ui-MacBookAir 2week_mission % git commit -m "first commit"
현재 브랜치 main

최초 커밋

추적하지 않는 파일:
  (커밋할 사항에 포함하려면 "git add <파일>..."을 사용하십시오)
        .gitignore
        README.md
        docs/
        test.py

커밋할 사항을 추가하지 않았지만 추적하지 않는 파일이 있습니다 (추적하려면 "git
add"를 사용하십시오)
(base) melon@munseongon-ui-MacBookAir 2week_mission % git add .
(base) melon@munseongon-ui-MacBookAir 2week_mission % git commit -m "first commit"
[main (최상위-커밋) fb00abc] first commit
 4 files changed, 13 insertions(+)
 create mode 100644 .gitignore
 create mode 100644 README.md
 create mode 100644 docs/git.md
 create mode 100644 test.py
(base) melon@munseongon-ui-MacBookAir 2week_mission % git branch -M main
(base) melon@munseongon-ui-MacBookAir 2week_mission % git remote add origin https://github.com/Wattamelon/2week_mission.git
(base) melon@munseongon-ui-MacBookAir 2week_mission % git push -u origin main
오브젝트 나열하는 중: 6, 완료.
오브젝트 개수 세는 중: 100% (6/6), 완료.
Delta compression using up to 8 threads
오브젝트 압축하는 중: 100% (3/3), 완료.
오브젝트 쓰는 중: 100% (6/6), 484 bytes | 484.00 KiB/s, 완료.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/Wattamelon/2week_mission.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
(base) melon@munseongon-ui-MacBookAir 2week_mission % 

img2


2. 메뉴화면 브랜치 생성 및 원격저장소 push

(base) melon@munseongon-ui-MacBookAir 2week_mission % git branch feature-menu
(base) melon@munseongon-ui-MacBookAir 2week_mission % git branch
  feature-menu
* main
(base) melon@munseongon-ui-MacBookAir 2week_mission % git checkout feature-menu
'feature-menu' 브랜치로 전환합니다
(base) melon@munseongon-ui-MacBookAir 2week_mission % git push origin feature-menu
Total 0 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote: 
remote: Create a pull request for 'feature-menu' on GitHub by visiting:
remote:      https://github.com/Wattamelon/2week_mission/pull/new/feature-menu
remote: 
To https://github.com/Wattamelon/2week_mission.git
 * [new branch]      feature-menu -> feature-menu
(base) melon@munseongon-ui-MacBookAir 2week_mission % 

3. menu 기능 구현 후 main 브랜치 merge
(base) melon@munseongon-ui-MacBookAir src % git add .
(base) melon@munseongon-ui-MacBookAir src % git commit -m "feat: 메뉴 선택 및 예외처리" 
[feature-menu b69912f] feat: 메뉴 선택 및 예외처리
 1 file changed, 45 insertions(+)
 create mode 100644 src/main.py
(base) melon@munseongon-ui-MacBookAir src % git push origin feature-menu
오브젝트 나열하는 중: 14, 완료.
오브젝트 개수 세는 중: 100% (14/14), 완료.
Delta compression using up to 8 threads
오브젝트 압축하는 중: 100% (9/9), 완료.
오브젝트 쓰는 중: 100% (10/10), 511.05 KiB | 19.66 MiB/s, 완료.
Total 10 (delta 3), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (3/3), completed with 1 local object.
To https://github.com/Wattamelon/2week_mission.git
   02fd73a..b69912f  feature-menu -> feature-menu
(base) melon@munseongon-ui-MacBookAir src % git checkout main
'main' 브랜치로 전환합니다
브랜치가 'origin/main'에 맞게 업데이트된 상태입니다.
(base) melon@munseongon-ui-MacBookAir src % git merge feature-menu
업데이트 중 02fd73a..b69912f
Fast-forward
 "2\354\243\274\354\260\250 \354\236\205\355\225\231 \354\227\260\354\210\230.pdf" | Bin 0 -> 788212 bytes
 docs/git.md                                                                       |  18 ++++++++++++++++++
 main.py                                                                           |  27 ++++++++++++++++++++++++++-
 src/main.py                                                                       |  45 +++++++++++++++++++++++++++++++++++++++++++++
 4 files changed, 89 insertions(+), 1 deletion(-)
 create mode 100644 "2\354\243\274\354\260\250 \354\236\205\355\225\231 \354\227\260\354\210\230.pdf"
 create mode 100644 src/main.py
(base) melon@munseongon-ui-MacBookAir src % git branch

  feature-menu
* main
(base) melon@munseongon-ui-MacBookAir src % git log --oneline --graph
* b69912f (HEAD -> main, origin/feature-menu, feature-menu) feat: 메뉴 선택 및 예외처리
* 6c02a17 feat:메뉴화면 출력 추가
* 02fd73a (origin/main) update
* fb00abc first commit

4. menu.py 입력 공백 제거 기능 추가
(base) melon@munseongon-ui-MacBookAir 2week_mission % git branch
  feature-menu
* main
(base) melon@munseongon-ui-MacBookAir 2week_mission % git checkout -b fix-input-strip
새로 만든 'fix-input-strip' 브랜치로 전환합니다
(base) melon@munseongon-ui-MacBookAir 2week_mission % git branch
  feature-menu
* fix-input-strip
  main
(base) melon@munseongon-ui-MacBookAir 2week_mission % python main.py                 
=============================
2주차 과제 퀴즈풀이
안내 : 코디세이 2주차 과제용 퀴즈입니다. 숫자를 선택해주세요.
=============================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
원하는 메뉴 번호를 입력하세요.
  1  
=============================
퀴즈 풀기
=============================
=============================
2주차 과제 퀴즈풀이
안내 : 코디세이 2주차 과제용 퀴즈입니다. 숫자를 선택해주세요.
=============================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료
원하는 메뉴 번호를 입력하세요.
5
=============================
프로그램을 종료합니다.
(base) melon@munseongon-ui-MacBookAir 2week_mission % git add .
(base) melon@munseongon-ui-MacBookAir 2week_mission % git commit -m "fix : 메뉴 입력 공백 처리" 
[fix-input-strip 899d833] fix : 메뉴 입력 공백 처리
 6 files changed, 46 insertions(+), 31 deletions(-)
 create mode 100644 src/__init__.py
 create mode 100644 src/__pycache__/__init__.cpython-312.pyc
 create mode 100644 src/__pycache__/menu.cpython-312.pyc
 rename src/{main.py => menu.py} (94%)
(base) melon@munseongon-ui-MacBookAir 2week_mission % git checkout main
'main' 브랜치로 전환합니다
브랜치가 'origin/main'에 맞게 업데이트된 상태입니다.
(base) melon@munseongon-ui-MacBookAir 2week_mission % git merge fix-input-strip
업데이트 중 b69912f..899d833
Fast-forward
 docs/git.md                              |  43 ++++++++++++++++++++++++++++++++++++++++++-
 main.py                                  |  28 ++--------------------------
 src/__init__.py                          |   0
 src/__pycache__/__init__.cpython-312.pyc | Bin 0 -> 175 bytes
 src/__pycache__/menu.cpython-312.pyc     | Bin 0 -> 1987 bytes
 src/{main.py => menu.py}                 |   6 ++----
 6 files changed, 46 insertions(+), 31 deletions(-)
 create mode 100644 src/__init__.py
 create mode 100644 src/__pycache__/__init__.cpython-312.pyc
 create mode 100644 src/__pycache__/menu.cpython-312.pyc
 rename src/{main.py => menu.py} (94%)
(base) melon@munseongon-ui-MacBookAir 2week_mission % git push origin main
오브젝트 나열하는 중: 15, 완료.
오브젝트 개수 세는 중: 100% (15/15), 완료.
Delta compression using up to 8 threads
오브젝트 압축하는 중: 100% (10/10), 완료.
오브젝트 쓰는 중: 100% (10/10), 3.12 KiB | 3.12 MiB/s, 완료.
Total 10 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/Wattamelon/2week_mission.git
   b69912f..899d833  main -> main
(base) melon@munseongon-ui-MacBookAir 2week_mission % 