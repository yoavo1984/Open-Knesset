#encoding: UTF-8
from django.conf.urls.defaults import *
from django.utils.translation import ugettext
from knesset.hashnav import ListView, DetailView
from models import *
from views import *

meetings_list = MeetingsListView(queryset=CommitteeMeeting.objects.all(), paginate_by=20)

committeesurlpatterns = patterns ('',
    url(r'^committee/$', CommitteeListView.as_view(), name='committee-list'),
    url(r'^committee/(?P<pk>\d+)/$', CommitteeDetailView.as_view(), name='committee-detail'),
    url(r'^committee/(?P<committee_id>\d+)/all_meetings/$', meetings_list, name='committee-all-meetings'),
    url(r'^committee/(?P<committee_id>\d+)/date/(?P<date>[\d\-]+)/$', meeting_list_by_date, name='committee-meetings-by-date'),
    url(r'^committee/(?P<committee_id>\d+)/date/$', meeting_list_by_date, name='committee-meetings-by-date'),
    url(r'^committee/meeting/(?P<pk>\d+)/$', MeetingDetailView.as_view(), name='committee-meeting'),
    url(r'^committee/meeting/tag/(?P<tag>.*)/$', meeting_tag,
        name='committeemeeting-tag'),
)
