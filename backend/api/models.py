from django.db import models

# Create your models here.
class Person(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=10)

class TypeRecord(models.Model):
    frequent = models.IntegerField()
    faild_count = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

class ProgramLanguage(models.Model):
    language_name = models.CharField(max_length=20)

class Word(models.Model):
    alphabet = models.CharField(max_length=20)
    program_language = models.ForeignKey(ProgramLanguage, on_delete=models.CASCADE)

class FaildWord(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    record = models.ForeignKey(TypRecord, on_delete=models.CASCADE)


# # 名前がayukiのユーザーを取得
# user = User.filter(name='ayuki').first()
# print(user.name) # ayuki



# user = select * from User where name='ayuki' limit 1;
# user_name = user[1]
# print(user_name)

'''
Python

user_name : スネークケース : 変数、関数
UserName : アッパーキャメルケース : クラス名
userName : ロウアーキャメルケース : 使わない
'''
