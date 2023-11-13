import leetcode
leetcode_session = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMjQzNDY5IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYWxsYXV0aC5hY2NvdW50LmF1dGhfYmFja2VuZHMuQXV0aGVudGljYXRpb25CYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYmMzMmQyMTM3MTc5ZjkzYmQ3NzYzNDU2OTQ5MTcwMGJkMDIzNDdiMiIsImlkIjoyNDM0NjksImVtYWlsIjoibmluYWQubXVuZGFsaWtAZ21haWwuY29tIiwidXNlcm5hbWUiOiJuaW5hZCIsInVzZXJfc2x1ZyI6Im5pbmFkIiwiYXZhdGFyIjoiaHR0cHM6Ly9zMy11cy13ZXN0LTEuYW1hem9uYXdzLmNvbS9zMy1sYy11cGxvYWQvYXNzZXRzL2RlZmF1bHRfYXZhdGFyLmpwZyIsInJlZnJlc2hlZF9hdCI6MTY5NzY2NzI0OCwiaXAiOiIxMzYuNjIuMjUyLjciLCJpZGVudGl0eSI6IjM1ZGFkNzBhYmM2MDFlMjI5ZTExNWQyMDBjYjlhMGJhIiwic2Vzc2lvbl9pZCI6Mzg4MTc3MjAsIl9zZXNzaW9uX2V4cGlyeSI6MTIwOTYwMH0.0JzCPUhtCM3CTX41EgU2hOZ-UdssUWwNauw5Zxb2tbY"
csrf_token = "sRKWy2x2nC68INvzH9Kxtrhq4cbbOJ7uxc2m4mTCE9mVZFJiFO3ADsWq8FPQqbHt"
configuration = leetcode.Configuration()
configuration.api_key["x-csrftoken"] = csrf_token
configuration.api_key["csrftoken"] = csrf_token
configuration.api_key["LEETCODE_SESSION"] = leetcode_session
configuration.api_key["Referer"] = "https://leetcode.com"
configuration.debug = False

api_instance =leetcode.DefaultApi(leetcode.ApiClient(configuration))
graphql_request = leetcode.GraphqlQuery(
query="""
     {
       user {
            username
            isCurrentUserPremium
         }
     }
     """,
variables=leetcode.GraphqlQueryVariables(),
)
# print(api_instance.graphql_post(body=graphql_request))


api_response=api_instance.api_problems_topic_get(topic="algorithms")
solved_questions=[]
for questions in api_response.stat_status_pairs:
    print(questions)
    # if questions.status=="ac":
    #    solved_questions.append(questions.stat)
    #    solved_questions.append('-------')
# print(solved_questions)
# print("Total number of solved questions ",len(solved_questions))
