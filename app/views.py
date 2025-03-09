from django.shortcuts import render, redirect, HttpResponse
from app.models import CustomUser
# Create your views here.
from django.shortcuts import get_object_or_404, render

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from datetime import datetime

def get_user_data(request, id):
    user = get_object_or_404(CustomUser, id=id)
    return render(request, 'NFC.html', {'user': user})


def home(request):
    return render(request, 'home.html')
# @csrf_exempt  # Only use this if you're testing without CSRF protection. Remove it in production.
# def recommendation(request):
#         model = "deepseek-r1-distill-llama-70b"
#         api_key = "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"
#         deepseek = ChatGroq(api_key=api_key, model_name=model)
#         parser = StrOutputParser()
#         deepseek_chain = deepseek | parser
#         loader = TextLoader('recommendation/foods_data.txt', encoding='utf-8')
#         data = loader.load()
#         chat_history = []

        
#         data = json.loads(request.body)  # Parse JSON request
#         user_message = data.get("message", "").strip()
        
#         if not user_message:
#             return JsonResponse({"response": "يرجى إدخال رسالة صحيحة"}, status=400)
        
#         chat_history.append(f"مستخدم: {user_message}")
        
#         # Call your deepseek_chain model here (modify as needed)
#         response = deepseek_chain.invoke("\n".join(chat_history))
        
#         chat_history.append(f"نظام: {response}")
        
#         return JsonResponse({"response": response}, status=200, json_dumps_params={'ensure_ascii': False})

# @csrf_exempt
# def comment(request):
    
#     try:
#         body_unicode = request.body.decode("utf-8")
#         if not body_unicode:  # Handle empty request body
#             return JsonResponse({"response": "الطلب فارغ. يرجى إرسال تعليق."}, status=400)

#         data = json.loads(body_unicode)
#         user_message = data.get("message", "").strip()
      
#         if not user_message:
#             return JsonResponse({"response": "يرجى إدخال تعليق صالح."}, status=400)

#         # Load the sentiment analysis model
#         model_name = 'CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment'
#         sentiment_pipeline = pipeline('text-classification', model=model_name)

#         result = sentiment_pipeline(user_message)
#         label = result[0]['label']
#         score = round(result[0]['score'] * 100, 2)

#         return JsonResponse({"response": f"التصنيف: {label} | النسبة: {score}%"}, status=200, json_dumps_params={'ensure_ascii': False})

#     except json.JSONDecodeError:
#         return JsonResponse({"response": "خطأ في تنسيق البيانات. يرجى إرسال JSON صحيح."}, status=400)


def login_view(request):
    if request.method=="POST":
        user = authenticate(username=request.POST['phone'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect(reverse('user_data', kwargs={'id': user.id}))
        else:
            return HttpResponse("Wrong Credintials.")
        
    return render(request, 'login.html')


def report(request, temp, soil):
    current_date = datetime.now().strftime('%Y-%m-%d')
    context = {
        "temperature": temp,  # استبدل بالقيمة الفعلية
        "soil_moisture": soil,  # استبدل بالقيمة الفعلية
        "current_date": datetime.today().strftime('%Y-%m-%d'),
    }
    return render(request, 'report.html', context)
