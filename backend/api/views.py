from django.http.response import JsonResponse
import random
# Create your views here.
def test(req):
    print("777")
    users = ["taro", "yuko", "ayuki", "kin-downey"]
    user_name = random.choice(users)
    return JsonResponse({"message": user_name})