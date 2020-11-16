from django.http import HttpResponse

from sqlserver.models import Test,Ami

def testdb(request):
    test1 = Test(name="aa")
    test1.save()
    return HttpResponse("添加数据{}".format("ss"))