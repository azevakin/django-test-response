from __future__ import unicode_literals

from django.utils import six
from django.test import TestCase
from django.core.urlresolvers import reverse


class ResponseTestCase(TestCase):

    def _url(self, viewname):
        if viewname:
            if isinstance(viewname, (list, tuple)):
                return reverse(viewname[0], args=viewname[1:])
            elif isinstance(viewname, dict):
                view_name = copy.deepcopy(viewname)
                return reverse(view_name.pop('viewname'), kwargs=view_name)
            elif isinstance(viewname, six.string_types) and viewname[0] != '/':
                return reverse(viewname)
        return viewname

    def get(self, viewname, data=None, **extra):
        return self.client.get(self._url(viewname), data, **extra)

    def post(self, viewname, data=None, **extra):
        return self.client.post(self._url(viewname), data, **extra)

    def head(self, viewname, data=None, **extra):
        return self.client.head(self._url(viewname), data, **extra)

    def trace(self, viewname, **extra):
        return self.client.trace(self._url(viewname), **extra)

    def options(self, viewname, data='', **extra):
        return self.client.options(self._url(viewname), data, **extra)

    def put(self, viewname, data='', **extra):
        return self.client.put(self._url(viewname), data, **extra)

    def patch(self, viewname, data='', **extra):
        return self.client.patch(self._url(viewname), data, **extra)

    def delete(self, viewname, data='', **extra):
        return self.client.delete(self._url(viewname), data, **extra)

    def assertStatus(self, response, status_code, msg_prefix=''):
        # If the response supports deferred rendering and hasn't been rendered
        # yet, then ensure that it does get rendered before proceeding further.
        if (hasattr(response, 'render') and callable(response.render)
                and not response.is_rendered):
            response.render()

        if msg_prefix:
            msg_prefix += ": "

        self.assertEqual(response.status_code, status_code,
            msg_prefix + "Couldn't retrieve content: Response code was %d"
            " (expected %d)" % (response.status_code, status_code))

    def assertOK(self, response, msg_prefix=''):
        self.assertStatus(response, 200, msg_prefix)

    def assertCreated(self, response, msg_prefix=''):
        self.assertStatus(response, 201, msg_prefix)

    def assertAccepted(self, response, msg_prefix=''):
        self.assertStatus(response, 202, msg_prefix)

    def assertNoContent(self, response, msg_prefix=''):
        self.assertStatus(response, 204, msg_prefix)

    def assertPermanentRedirect(self, response, msg_prefix=''):
        self.assertStatus(response, 301, msg_prefix)

    def assertRedirect(self, response, msg_prefix=''):
        self.assertStatus(response, 302, msg_prefix)

    def assertBadRequest(self, response, msg_prefix=''):
        self.assertStatus(response, 400, msg_prefix)

    def assertUnauthorized(self, response, msg_prefix=''):
        self.assertStatus(response, 401, msg_prefix)

    def assertPaymentRequired(self, response, msg_prefix=''):
        self.assertStatus(response, 402, msg_prefix)

    def assertForbidden(self, response, msg_prefix=''):
        self.assertStatus(response, 403, msg_prefix)

    def assertNotFound(self, response, msg_prefix=''):
        self.assertStatus(response, 404, msg_prefix)

    def assertNotAllowed(self, response, msg_prefix=''):
        self.assertStatus(response, 405, msg_prefix)

    def assertResponseGone(self, response, msg_prefix=''):
        self.assertStatus(response, 410, msg_prefix)

    def assertServerError(self, response, msg_prefix=''):
        self.assertStatus(response, 500, msg_prefix)
