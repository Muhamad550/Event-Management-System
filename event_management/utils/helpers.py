from datetime import datetime
from event_management.utils.helpers import format_date, send_notification

# مثال لاستخدام الدوال
formatted_date = format_date(event.date)
send_notification("New event created!")

def format_date(event_date):
    """تقوم بتنسيق التاريخ إلى صيغة أكثر قابلية للقراءة."""
    return event_date.strftime('%Y-%m-%d %H:%M:%S')

def send_notification(message):
    """تقوم بإرسال إشعار (يمكن تطويرها لترسل إيميل أو رسالة)."""
    print(f"Notification: {message}")
