from django.http.response import JsonResponse

from . import models

import random
# Create your views here.
def test(req):
    print("777")
    first_names = ['taro', 'jiro', 'saburo', 'shiro']
    last_names = ['suzuki', 'tanaka', 'yamada', 'kawasaki']
    cities = ['kyoto', 'seikacho', 'uji', 'kameoka']
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    city = random.choice(cities)
    # リクエストの中身を取得
    address = req.GET.get('address', 'Higasi kujo')
    # インスタンスの作成
    person = models.Person(first_name=first_name, last_name=last_name, city=city, address=address)
    person.save()
    return JsonResponse({"message": "created person", "first_name": first_name, "last_name": last_name, "city": city, "address": address})