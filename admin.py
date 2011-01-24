from django.contrib import admin
from funkymail.models import Domain, Mailbox, Alias

class DomainAdmin(admin.ModelAdmin):
	pass

class MailboxAdmin(admin.ModelAdmin):
	pass

class AliasAdmin(admin.ModelAdmin):
	pass

admin.site.register(Domain, DomainAdmin)
admin.site.register(Mailbox, MailboxAdmin)
admin.site.register(Alias, AliasAdmin)

