from django.contrib import admin
#from .models import Post
from .models import Session, GroupMember, TeamScore, SessionScore


#admin.site.register(Post)
admin.site.register(Session)
admin.site.register(GroupMember)
admin.site.register(TeamScore)
admin.site.register(SessionScore)
