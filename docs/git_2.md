1. 리팩토링 전 main 브랜치 업데이트

(base) melon@munseongon-ui-MacBookAir 2week_mission % git add .
(base) melon@munseongon-ui-MacBookAir 2week_mission % git commit -m "refactoring 전 업데이트"  
[main 43e85e7] refactoring 전 업데이트
 2 files changed, 93 insertions(+)
 create mode 100644 docs/git_2.md
(base) melon@munseongon-ui-MacBookAir 2week_mission % git push origin main
오브젝트 나열하는 중: 8, 완료.
오브젝트 개수 세는 중: 100% (8/8), 완료.
Delta compression using up to 8 threads
오브젝트 압축하는 중: 100% (4/4), 완료.
오브젝트 쓰는 중: 100% (5/5), 1.12 KiB | 1.12 MiB/s, 완료.
Total 5 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/Wattamelon/2week_mission.git
   0b7845c..43e85e7  main -> main

2. quiz_class 브랜치 생성 

(base) melon@munseongon-ui-MacBookAir 2week_mission % git branch quiz_class
(base) melon@munseongon-ui-MacBookAir 2week_mission % git branch
  feature-menu
  fix-input-strip
* main
  quiz_class
  show_quizzes
(base) melon@munseongon-ui-MacBookAir 2week_mission % git checkout quiz_class
'quiz_class' 브랜치로 전환합니다
(base) melon@munseongon-ui-MacBookAir 2week_mission % git branch
  feature-menu
  fix-input-strip
  main
* quiz_class
  show_quizzes
(base) melon@munseongon-ui-MacBookAir 2week_mission % 



3. quiz_class 구현 후 main 브랜치 병합.

(base) melon@munseongon-ui-MacBookAir 2week_mission % git add .
(base) melon@munseongon-ui-MacBookAir 2week_mission % git commit -m "Feat : 퀴즈 클래스 구현" 
[quiz_class c977829] Feat : 퀴즈 클래스 구현
 1 file changed, 24 insertions(+)
 create mode 100644 src/quiz.py
(base) melon@munseongon-ui-MacBookAir 2week_mission % git checkout main
'main' 브랜치로 전환합니다
브랜치가 'origin/main'에 맞게 업데이트된 상태입니다.
(base) melon@munseongon-ui-MacBookAir 2week_mission % git merge quiz_class
업데이트 중 43e85e7..c977829
Fast-forward
 src/quiz.py | 24 ++++++++++++++++++++++++
 1 file changed, 24 insertions(+)
 create mode 100644 src/quiz.py
(base) melon@munseongon-ui-MacBookAir 2week_mission % git push origin main
오브젝트 나열하는 중: 6, 완료.
오브젝트 개수 세는 중: 100% (6/6), 완료.
Delta compression using up to 8 threads
오브젝트 압축하는 중: 100% (4/4), 완료.
오브젝트 쓰는 중: 100% (4/4), 682 bytes | 682.00 KiB/s, 완료.
Total 4 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/Wattamelon/2week_mission.git
   43e85e7..c977829  main -> main
(base) melon@munseongon-ui-MacBookAir 2week_mission %     




4. quiz_data 클래스 생성

(base) melon@munseongon-ui-MacBookAir 2week_mission % git checkout -b quiz_data
새로 만든 'quiz_data' 브랜치로 전환합니다
(base) melon@munseongon-ui-MacBookAir 2week_mission % git branch
  feature-menu
  fix-input-strip
  main
  quiz_class
* quiz_data
  show_quizzes


5. quiz_data 병합

(base) melon@munseongon-ui-MacBookAir 2week_mission % git branch
  feature-menu
  fix-input-strip
  main
  quiz_class
* quiz_data
  show_quizzes
(base) melon@munseongon-ui-MacBookAir 2week_mission % git add .
(base) melon@munseongon-ui-MacBookAir 2week_mission % git commit -m "Feat : 기본 퀴즈데이터 생성" 
[quiz_data f356f05] Feat : 기본 퀴즈데이터 생성
 2 files changed, 91 insertions(+)
 create mode 100644 src/quiz_data.py
(base) melon@munseongon-ui-MacBookAir 2week_mission % git checkout main
'main' 브랜치로 전환합니다
브랜치가 'origin/main'에 맞게 업데이트된 상태입니다.
(base) melon@munseongon-ui-MacBookAir 2week_mission % git merge quiz_data
업데이트 중 c977829..f356f05
Fast-forward
 docs/git_2.md    | 81 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 src/quiz_data.py | 10 ++++++++++
 2 files changed, 91 insertions(+)
 create mode 100644 src/quiz_data.py
(base) melon@munseongon-ui-MacBookAir 2week_mission % git push origin main
오브젝트 나열하는 중: 10, 완료.
오브젝트 개수 세는 중: 100% (10/10), 완료.
Delta compression using up to 8 threads
오브젝트 압축하는 중: 100% (6/6), 완료.
오브젝트 쓰는 중: 100% (6/6), 1.94 KiB | 1.94 MiB/s, 완료.
Total 6 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/Wattamelon/2week_mission.git
   c977829..f356f05  main -> main
(base) melon@munseongon-ui-MacBookAir 2week_mission % 


6. QuizGame 클래스 구현 (까먹고 브랜치 안만들고 main 브랜치에서 진행)

(base) melon@munseongon-ui-MacBookAir 2week_mission % git add .
(base) melon@munseongon-ui-MacBookAir 2week_mission % git commit -m "Feat : play quiz 메소드 추가"
[main 021ac59] Feat : play quiz 메소드 추가
 1 file changed, 43 insertions(+), 1 deletion(-)
(base) melon@munseongon-ui-MacBookAir 2week_mission % git branch
  feature-menu
  fix-input-strip
* main
  quiz_class
  quiz_data
  show_quizzes
(base) melon@munseongon-ui-MacBookAir 2week_mission % git push origin main
오브젝트 나열하는 중: 7, 완료.
오브젝트 개수 세는 중: 100% (7/7), 완료.
Delta compression using up to 8 threads
오브젝트 압축하는 중: 100% (4/4), 완료.
오브젝트 쓰는 중: 100% (4/4), 1.18 KiB | 1.18 MiB/s, 완료.
Total 4 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/Wattamelon/2week_mission.git
   376e451..021ac59  main -> main
(base) melon@munseongon-ui-MacBookAir 2week_mission % 



7. save_data 메소드 구현 완료

(base) melon@munseongon-ui-MacBookAir 2week_mission % git add .  
(base) melon@munseongon-ui-MacBookAir 2week_mission % git commit -m "save_data 메소드 구현 완료" 
[main 4f79a3a] save_data 메소드 구현 완료
 2 files changed, 51 insertions(+), 1 deletion(-)
(base) melon@munseongon-ui-MacBookAir 2week_mission % git push origin main
오브젝트 나열하는 중: 11, 완료.
오브젝트 개수 세는 중: 100% (11/11), 완료.
Delta compression using up to 8 threads
오브젝트 압축하는 중: 100% (6/6), 완료.
오브젝트 쓰는 중: 100% (6/6), 1.10 KiB | 1.10 MiB/s, 완료.
Total 6 (delta 4), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (4/4), completed with 4 local objects.
To https://github.com/Wattamelon/2week_mission.git
   021ac59..4f79a3a  main -> main
(base) melon@munseongon-ui-MacBookAir 2week_mission % 