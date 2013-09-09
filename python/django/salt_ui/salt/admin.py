from django.contrib import admin
from salt_ui.salt import models

class usernameAdmin(admin.ModelAdmin):
    pass

class passwordAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.User,usernameAdmin)
#admin.site.register(models.User,passwordAdmin)
