from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

from .models import Like


def add_like(obj, user):
    obj_type = ContentType.objects.get_for_model(obj)
    like, created = Like.objects.get_or_create(content_type=obj_type, object_id=obj.id, user=user)
    return like
    

def remove_like(obj, user):
    obj_type = ContentType.objects.get_for_model(obj)
    Like.objects.filter(content_type=obj_type, object_id=obj.id, user=user).delete()
