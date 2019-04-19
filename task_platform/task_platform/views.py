from django.http import HttpResponse
import json
from django.http import JsonResponse

def test_function(request):
    # return HttpResponse('hello world')
    return HttpResponse("{var}".format(var=request.body.decode('utf-8')))



# def test_function(request):
#     var1 = request.GET["var1"]
#     var2 = request.GET["var2"]
#     return HttpResponse("{var1} {var2}".format(var1=var1, var2=var2))

#练习：请用这种方法，在服务器端完成一个加法接口，即在接收到var1和var2后，
# 服务器将其转化为数值，相加后返回。
# def test_function(request):
#     var1 = request.GET['var1']
#     var2 = request.GET['var2']
#     summ = int(var1)+int(var2)
#     return HttpResponse((summ))

#尝试在POST的body中写入两个数，并完成两个数的加法后返回


def __get_response_json_dict(data, err_code=0, message='Success'):
    ret = {
        'err_code': err_code,
        'message': message,
        'data': data
    }
    return ret


def get_sum(request):
    received_data = json.loads(request.body.decode('utf-8'))
    var1 = received_data['var1']
    var2 = received_data['var2']
    sum = var1 + var2
    response_data = {'sum': sum}
    return JsonResponse(
        __get_response_json_dict(data=response_data)
    )


def test_session(request):
    print(request.session.get("privacy"))
    request.session["privacy"] = "This message should not be stored in cookirs"
    return HttpResponse()


#针对cookie 的操作有
#request.COOKIES这个dict直接访问请求中携带的cookies
#response.set_cookie(<key>,<value>)来设置cookies
#response.delete_cookie(<key>)删除cookies
def test_cookies(request):
    print(request.COOKIES)
    response = HttpResponse()
    response.set_cookie("this_is_a_key", "this is value")
    return response

def test_delete_cookie(request):
    response = HttpResponse()
    response.delete_cookie("this_is_key", "this is value")
    return response














