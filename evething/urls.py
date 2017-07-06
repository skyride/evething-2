from django.conf import settings
from django.conf.urls import patterns, include, url


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    # Admin
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    # Authentication things
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="auth_login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="auth_logout"),
    url(r'^accounts/register/$', 'thing.views.account_register')
)

urlpatterns += patterns(
    'thing.views',
    url(r'^$', 'home', name='home'),

    (r'^account/$', 'account'),
    (r'^account/change_password/$', 'account_change_password'),
    (r'^account/settings/$', 'account_settings'),
    (r'^account/skillplan/add/$', 'account_skillplan_add'),
    (r'^account/skillplan/delete/$', 'account_skillplan_delete'),
    (r'^account/skillplan/edit/$', 'account_skillplan_edit'),

    (r'^account/esi/update/$', 'account_esi_forceupdate'),
    (r'^account/esi/delete/$', 'account_esi_delete'),

    (r'^account/sso/authorize/$', 'account_sso_authorize'),
    (r'^account/sso/callback/$', 'account_sso_callback'),

    (r'^assets/$', 'assets_summary'),
    (r'^assets/filter/$', 'assets_filter'),

    (r'^clones/$', 'clones_home'),

    url(r'^blueprints/$', 'blueprints', name='blueprints'),
    (r'^blueprints/add/$', 'blueprints_add'),
    (r'^blueprints/del/$', 'blueprints_del'),
    (r'^blueprints/edit/$', 'blueprints_edit'),
    (r'^blueprints/export/$', 'blueprints_export'),
    (r'^blueprints/import/$', 'blueprints_import'),

    (r'^bpcalc/$', 'bpcalc'),

    (r'^character/(?P<character_name>[\w\'\- ]+)/$', 'character_sheet'),
    (r'^character/(?P<character_name>[\w\'\- ]+)/settings/', 'character_settings'),
    (r'^character/(?P<character_name>[\w\'\- ]+)/mastery/', 'character_mastery'),
    (r'^character/(?P<character_name>[\w\'\- ]+)/skillplan/(?P<skillplan_id>\d+)$', 'character_skillplan'),
    (r'^character_anon/(?P<anon_key>[a-z0-9]+)/$', 'character_anonymous',),
    (r'^character_anon/(?P<anon_key>[a-z0-9]+)/mastery/', 'character_anonymous_mastery'),
    (r'^character_anon/(?P<anon_key>[a-z0-9]+)/skillplan/(?P<skillplan_id>\d+)$', 'character_anonymous_skillplan'),

    (r'^contracts/$', 'contracts'),
    (r'^contracts/(?P<contract_id>[a-z0-9]+)/$', 'contracts_view'),

    (r'^events/$', 'events'),

    (r'^industry/$', 'industry'),

    (r'^mail/$', 'mail'),
    (r'^mail/json/body/(?P<message_id>\d+)/$', 'mail_json_body'),
    (r'^mail/json/headers/$', 'mail_json_headers'),
    (r'^mail/mark_read/$', 'mail_mark_read'),
    (r'^mail/character/search/(?P<query>[\w\- ]+)/$', 'character_search'),

    (r'^orders/$', 'orders'),

    (r'^trade/$', 'trade'),
    (r'^trade/(?P<year>\d{4})-(?P<month>\d{2})/$', 'trade_timeframe'),
    (r'^trade/(?P<period>all)/$', 'trade_timeframe'),
    (r'^trade/(?P<slug>[-\w]+)/$', 'trade_timeframe'),

    (r'^transactions/$', 'transactions'),

    (r'^wallet_journal/$', 'wallet_journal'),
    (r'^wallet_journal/aggregate/$', 'wallet_journal_aggregate'),

    (r'^pi/$', 'pi'),
)

if getattr(settings, 'ENABLE_GSFAPI', None):
    urlpatterns += patterns('', (r'^gsfapi/', include('gsfapi.urls')))
