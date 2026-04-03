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

