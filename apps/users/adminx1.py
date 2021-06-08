import xadmin

from apps.users.models import UserProfile

class UserAdmin(object):

    list_display = ['nick_name','birthday', 'gender', 'address', 'mobile']
    search_fields = ['nick_name','birthday', 'gender', 'address', 'mobile']
    list_filter = ['nick_name','birthday', 'gender', 'address', 'mobile']


xadmin.site.register(UserProfile, UserAdmin)
