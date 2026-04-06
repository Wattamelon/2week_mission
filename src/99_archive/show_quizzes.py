import json
from pathlib import Path


def show():
    with path.open("r",encoding='utf-8') as f:
        json_data = json.load(f)
    json_data = json_data["quizzes"]

    if len(json_data) == 0:
        print("등록된 문제가 존재하지 않습니다.")

    else: 
        print(f"총 {len(json_data)}문제")
        print("-------------------------")

        for i in json_data :
            print(f" {i['id']}번 문제")
            print(f" 문제 : {i['question']}")
            print("-------------------------")


if __name__ == "__main__":
    path = Path("../state.json")
    show()
else:
    path = Path("state.json")

