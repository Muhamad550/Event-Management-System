def validate_event_date(event_date):
    """تقوم بالتحقق من أن تاريخ الفعالية في المستقبل."""
    from datetime import datetime
    if event_date < datetime.now():
        raise ValueError("Event date must be in the future.")
    return True