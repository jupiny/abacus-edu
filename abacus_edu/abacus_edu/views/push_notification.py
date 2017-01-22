from django.conf import settings
from django.shortcuts import redirect

from pyfcm import FCMNotification


def push_notification(request):
    if request.method == 'POST':
        topic = request.POST.get('topic')
        title = request.POST.get('title')
        message = request.POST.get('message')
        push_service = FCMNotification(api_key=settings.FCM_API_KEY)
        result = push_service.notify_topic_subscribers(
            topic_name=topic,
            message_title=title,
            message_body=message,
        )
        return redirect(request.META.get('HTTP_REFERER'))
