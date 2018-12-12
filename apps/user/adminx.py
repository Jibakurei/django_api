import xadmin
from xadmin import views
from .models import VerifyCode

class BaseSetting(object):
    enble_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = "后台"
    site_footer = "shop"
    
class VerifyCodeAdmin(object):
    list_display = ['code','mobile',"add_time"]
    pass

xadmin.site.register(VerifyCode,VerifyCodeAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)