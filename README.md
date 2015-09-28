django-test-response
===

Better TestCase for test response.

Replace your code:

    class FooTestCase(TestCase):
        def test_status_code(self):
            url = reverse('view-path', args=(10,))
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)

with this:

    class FooTestCase(ResponseTestCase):
        def test_status_code(self):
            response = self.get(('view-path', args=(10,)))
            self.assertOK(response)
