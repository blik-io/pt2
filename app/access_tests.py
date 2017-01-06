from .models import User, DataPoint, Device, Location

def device_test(user):
    return True
    location_id = Device.objects.get(id=device_id).location_id
    allowed_users = Location.objects.get(id=location_id).allowed_users
    return user in allowed_users

def location_test(user):
    allowed_users = Location.objects.get(slug=slug).allowed_users
    return user in allowed_users

def user_test(user):
    pass
