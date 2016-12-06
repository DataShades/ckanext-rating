import pylons.config as config
from ckan.plugins import toolkit
import ckan.logic as logic
c = toolkit.c


def rating_create_auth():
    return {
        'check_access_user': check_access_user,
    }


@logic.auth_allow_anonymous_access
def check_access_user(context, data_dict):
    print 'Hello from def check_access_user():'
    print 'context = {}'.format(context)
    if c.user:#context[user]
        return {'success': True}
    else:
        allow_rating = config.get('rating.enabled_for_unauthenticated_users')
        if allow_rating == 'false' or '':
            return {'success': False}
        if allow_rating == 'true':
            return {'success': True}
    return {'success': False}
