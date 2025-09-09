def date_time() -> str:
    """Get the current date and time."""
    from datetime import datetime
    return "Current date and time: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")