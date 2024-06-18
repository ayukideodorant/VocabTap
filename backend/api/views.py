from django.http.response import JsonResponse
from rest_framework import status

from . import models
from django.views.decorators.csrf import csrf_exempt
import random
import json
# Create your views here.

@csrf_exempt
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

@csrf_exempt
def create_user(req):
    # リクエストからデータを取得
    data = json.loads(req.body)
    user_name = data.get("name")
    user_password = data.get("password")
    # ユーザーをDBに登録
    user_obj = models.User(name=user_name, password=user_password)
    user_obj.save()
    return JsonResponse({"name": user_name, "password": user_password})

@csrf_exempt
def login_user(req):
    # 入力されたユーザ名とパスワードを取得
    data = json.loads(req.body)
    user_name = data.get("name")
    user_password = data.get("password")
    # 入力されたユーザ名でデータベースからユーザ名と一致するパスワードを取得
    user_obj = models.User.objects.filter(name=user_name).first()
    if not user_obj:
        return JsonResponse({"status": "user is not found."}, status=status.HTTP_404_NOT_FOUND)
    # 入力されたパスワードとデータベースのパスワードが一致するか否か
    if user_obj.password == user_password:
    # 一致する場合、ログインOK
        return JsonResponse({"status": "OK"}, status=status.HTTP_202_ACCEPTED)
    # 一致しない場合、ログインNG
    return JsonResponse({"status": "NG"}, status=status.HTTP_401_UNAUTHORIZED)

@csrf_exempt
def create_word(req):
    # リクエストからデータを取得
    data = json.loads(req.body)
    new_alphabet = data.get("alphabet")
    new_program_language_id = data.get("program_language_id")
    # ユーザーをDBに登録
    new_word_obj = models.Word(alphabet=new_alphabet, program_language_id=new_program_language_id)
    new_word_obj.save()
    return JsonResponse({"alphabet": new_alphabet, "program_language_id": new_program_language_id})


def import_words(csv_path):
    # csv_pathを参照してcsvファイルを開く
    with open(csv_path) as csv_file:
        word_list = csv_file.readlines() # ['a,2', 'able,2', 'afternoon,2' ... ]
    # １行ずつ読み取る
    for word_line in word_list:
        word, lang_num = word_line.split(',')
        print("word: ", word, ", ", "lang_num: ", lang_num)
        # DBにデータを登録
        new_word_obj = models.Word(alphabet=word, program_language_id=int(lang_num))
        new_word_obj.save()


from backend.settings import BASE_DIR
def do(req):
    csv_file_path = str(BASE_DIR) + "/word/chu1.csv"
    import_words(csv_file_path)
    return JsonResponse({"message": "imported words"})


@csrf_exempt
def get_word(req):
    id_num = random.randint(5, 452)
    word_obj = models.Word.objects.filter(id=id_num).first()
    word = word_obj.alphabet
    return JsonResponse({"message": word})