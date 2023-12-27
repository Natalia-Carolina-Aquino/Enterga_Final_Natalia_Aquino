from django.contrib import admin

from AppBlog.models import Knit, Yarn, Accessories, KnitComment, YarnComment, AccessoriesComment

# Register your models here.
admin.site.register(Knit)
admin.site.register(Yarn)
admin.site.register(Accessories)
admin.site.register(KnitComment)
admin.site.register(YarnComment),
admin.site.register(AccessoriesComment)
