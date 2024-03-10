#라이브러리
from openai import OpenAI

#API키 입력
client = OpenAI(
    api_key="mykey"
)

#대화가 끊기지 않도록 while True 사용
while True : 
    maTalkContent = input("사용자(나)\t:\t")

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"{maTalkContent}"}
        ]
        )
    #gpt 어시스턴트 문구
    ChatGpt_turbo = completion.choices[0].message.content #gpt어시스턴트 문구
    print(f"ChatGpt(3.5-turbo)\t:\t{ChatGpt_turbo}")

    #무한반복 종료 및 break문
    if maTalkContent in ["다음에 봐", "그만", "여기까지", "종료"]: #해당 리스트안의 단어가 나오면 종료
        break