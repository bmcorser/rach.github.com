Motivation
---------- 

Why test ? 

You already testing via:
 opening the browser 
 running the app 

But testing is repetive/manual

Goal, Be lazy! 

Test help you to relax about:

deployment
refactoring
new developer 
regression


When you’re writing new code, you can use tests to validate your code works as expected.
When you’re refactoring or modifying old code, you can use tests to ensure your changes haven’t affected your application’s behavior unexpectedly.


Terminology
-----------
Unit tests (isolated shouldnt have side effect)
Integration test (test side effect) 
Functional/Browser test 
Acceptance test (ensure the spec/delivery, more communly BDD)
Regression Test (test to prove a bug)
Performance test (queries)
Load tests 


Unit test 
---------

Should deal only with one piece of code 
Tied to the code
Fast (important to validate implementation)
Testing small portion of code 
No interaction with other components

unit testability
----------------
avoid side effect
separate components
delegate the business logic from view to model/manager

Integration test
----------------
Test more than one piece of code 
And how components interact together
Setup/Teardown are important for cleaning the mess
django: inherit from TestCase
Bit slower

Important
~~~~~~~~~

100% unittest won't guarantee that the software works.
because you need to test how components interact

Loads of time ? what is the win
-------------------------------
make life easier
make a loose coopled code 
will save you time and stress 
create more generic code 



Advice
------ 
Split your integration and unittests, you cannot wait x minutes during the
dev process. Otherwise you will end checking email and hackernews for 20min 

Desciptive name !!! when it fail you know what is about.. save time

Django 
------ 

How to unittest view ?
----------------------
Mock request / client 
access db
render template ... 

-> delegate logic to model 
-> split view in method which abstract the logic with simple signature
  a bit yuk

-> Class based view FTW
    allow to split logic in method and test individualy 

Unitest depending step

test step 1
test step 2 without going throught step 1 again but by starting with the
expected result

If you don't bypass you won't have any good result on step2 if step1 fail

class BurgerFactory

   def make meat()

   def make_burger()

Working with models
-------------------

As possible avoid to hit the database

Populating test DB

fixture works only with static data (if it fit your need)
-> try to avoid them to avoid to write test which work only this fixture
more the maintenanting task

If u can, use factory to generate models which suit you need.

Form
---- 

test validate 
test failing validation

ModelForm
--------- 

similare but that test aswell full clean: clean_fields / clean / validate_unique

Get started
-----------
descriptive test names
short test touching minimal amount of code
even trivial test as starting point
make sure their work

Reward
------ 
-> easy way to bootstrap your application (Conf management)
-> no need of server/browser during development
-> people will trust your work 
-> More relax when you code ! (cover your back)
-> Piece of Mind and Deplay Friday


Quote from Charles Darwin .. seen at djangocon 

"it is no the strongest of the species that survives, nor the more intelligent but the one most responsive to change"

Having test allow you to change code faster, and being responsive.

------------
Test as Doc ?

Keeping doc uptodate is hard.
When you build lib/ reusable components ... you can see this test as 

Code without test is broken as designed  -- jacob Kaplan-Moss 

There is noway that you can prove that it works


TDD
DDD : Document driven dev
TDD test driven doc

Stucture
--------
Class MyTest(unittest.TestCase):

def setUp(self): #before each test
def tearDowm(self): #after each test

@classmethod
def setUpClass(cls): #once before tests in an individual class
@classmethod
def tearDownClass(cls): #once before tests in an individual class

Assertion
---------
assertEqual(a, b, msg=None) 
assertNotEqual(a, b, msg=None) 
assertTrue(x, msg=None) 
assertFalse(x, msg=None)
assertIs(a, b, msg=None) 
assertIsNot(a, b, msg=None) 
assertIsNone(x, msg=None)  
assertIsNotNone(x, msg=None) 
assertIn(a, b, msg=None)
assertNotIn(a, b, msg=None)  
assertIsInstance(a, b, msg=None) 
assertNotIsInstance(a, b, msg=None)

Extra Assert:
assertAlmostEqual(first, second, places=7, msg=None, delta=None)
assertNotAlmostEqual(first, second, places=7, msg=None, delta=None)
assertGreater(first, second, msg=None)
assertGreaterEqual(first, second, msg=None)
assertLess(first, second, msg=None)
assertLessEqual(first, second, msg=None)
assertRegexpMatches(text, regexp, msg=None)
assertNotRegexpMatches(text, regexp, msg=None)
assertItemsEqual(actual, expected, msg=None)


method 
skip 
fail


Nose 
exclude
ipdb


Django
------

Test case hierachie

https://docs.djangoproject.com/en/dev/_images/django_unittest_classes_hierarchy.png


TestCase

class TestCase

This class provides some additional capabilities that can be useful for testing Web sites.

Converting a normal unittest.TestCase to a Django TestCase is easy: Just change the base class of your test from 'unittest.TestCase' to 'django.test.TestCase'. All of the standard Python unit test functionality will continue to be available, but it will be augmented with some useful additions, including:

    Automatic loading of fixtures.
    Wraps each test in a transaction.
    Creates a TestClient instance.
    Django-specific assertions for testing for things like redirection and form errors.

Changed in Django 1.5: The order in which tests are run has changed. See Order in which tests are executed.

TestCase inherits from TransactionTestCase.
TransactionTestCase

class TransactionTestCase

Django TestCase classes make use of database transaction facilities, if available, to speed up the process of resetting the database to a known state at the beginning of each test. A consequence of this, however, is that the effects of transaction commit and rollback cannot be tested by a Django TestCase class. If your test requires testing of such transactional behavior, you should use a Django TransactionTestCase.

TransactionTestCase and TestCase are identical except for the manner in which the database is reset to a known state and the ability for test code to test the effects of commit and rollback:

    A TransactionTestCase resets the database after the test runs by truncating all tables. A TransactionTestCase may call commit and rollback and observe the effects of these calls on the database.

    A TestCase, on the other hand, does not truncate tables after a test. Instead, it encloses the test code in a database transaction that is rolled back at the end of the test. It also prevents the code under test from issuing any commit or rollback operations on the database, to ensure that the rollback at the end of the test restores the database to its initial state.

    When running on a database that does not support rollback (e.g. MySQL with the MyISAM storage engine), TestCase falls back to initializing the database by truncating tables and reloading initial data.

Note
Changed in Django 1.5: Please see the release notes

Prior to 1.5, TransactionTestCase flushed the database tables before each test. In Django 1.5, this is instead done after the test has been run.

When the flush took place before the test, it was guaranteed that primary key values started at one in TransactionTestCase tests.

Tests should not depend on this behaviour, but for legacy tests that do, the reset_sequences attribute can be used until the test has been properly updated.
Changed in Django 1.5: The order in which tests are run has changed. See Order in which tests are executed.

TransactionTestCase inherits from SimpleTestCase.

TransactionTestCase.reset_sequences
    New in Django 1.5: Please see the release notes

    Setting reset_sequences = True on a TransactionTestCase will make sure sequences are always reset before the test run:

    class TestsThatDependsOnPrimaryKeySequences(TransactionTestCase):
        reset_sequences = True

        def test_animal_pk(self):
            lion = Animal.objects.create(name="lion", sound="roar")
            # lion.pk is guaranteed to always be 1
            self.assertEqual(lion.pk, 1)

    Unless you are explicitly testing primary keys sequence numbers, it is recommended that you do not hard code primary key values in tests.

    Using reset_sequences = True will slow down the test, since the primary key reset is an relatively expensive database operation.

SimpleTestCase

class SimpleTestCase

New in Django 1.4: Please see the release notes

A very thin subclass of unittest.TestCase, it extends it with some basic functionality like:

    Saving and restoring the Python warning machinery state.
    Checking that a callable raises a certain exception.
    Testing form field rendering.
    Testing server HTML responses for the presence/lack of a given fragment.
    The ability to run tests with modified settings

If you need any of the other more complex and heavyweight Django-specific features like:

    Using the client Client.
    Testing or using the ORM.
    Database fixtures.
    Custom test-time URL maps.
    Test skipping based on database backend features.
    The remaining specialized assert* methods.

then you should use TransactionTestCase or TestCase instead.

SimpleTestCase inherits from django.utils.unittest.TestCase.


tip:
Running tests outside the test runner¶
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()

Regardless of the value of the DEBUG setting in your configuration file, all Django tests run with DEBUG=False. This is to ensure that the observed output of your code matches what will be seen in a production setting.

Caches are not cleared after each test, and running "manage.py test fooapp" can insert data from the tests into the cache of a live system if you run your tests in production because, unlike databases, a separate "test cache" is not used. This behavior may change in the future.


Fixture loading

TestCase.fixtures

A test case for a database-backed Web site isn't much use if there isn't any data in the database. To make it easy to put test data into the database, Django's custom TestCase class provides a way of loading fixtures.

A fixture is a collection of data that Django knows how to import into a database. For example, if your site has user accounts, you might set up a fixture of fake user accounts in order to populate your database during tests.

The most straightforward way of creating a fixture is to use the manage.py dumpdata command. This assumes you already have some data in your database. See the dumpdata documentation for more details.


fixtures = ['mammals.json', 'birds']

URLconf configuration

TestCase.urls

If your application provides views, you may want to include tests that use the test client to exercise those views. However, an end user is free to deploy the views in your application at any URL of their choosing. This means that your tests can't rely upon the fact that your views will be available at a particular URL.

In order to provide a reliable URL space for your test, django.test.TestCase provides the ability to customize the URLconf configuration for the duration of the execution of a test suite. If your TestCase instance defines an urls attribute, the TestCase will use the value of that attribute as the ROOT_URLCONF for the duration of that test.

For example:

from django.test import TestCase

class TestMyViews(TestCase):
    urls = 'myapp.test_urls'

    def testIndexPageView(self):
        # Here you'd test your view using ``Client``.
        call_some_test_code()

This test case will use the contents of myapp.test_urls as the URLconf for the duration of the test case.

from django.test.utils import override_settings

@override_settings(LOGIN_URL='/other/login/')

The test runner accomplishes this by transparently replacing the normal email backend with a testing backend. (Don't worry -- this has no effect on any other email senders outside of Django, such as your machine's mail server, if you're running one.)

django.core.mail.outbox

During test running, each outgoing email is saved in django.core.mail.outbox. This is a simple list of all EmailMessage instances that have been sent. The outbox attribute is a special attribute that is created only when the locmem email backend is used. It doesn't normally exist as part of the django.core.mail module and you can't import it directly. The code below shows how to access this attribute correctly.




Testing tools
-------------

Client
------
The test client is a Python class that acts as a dummy Web browser, allowing you to test your views and interact with your Django-powered application programmatically.

Some of the things you can do with the test client are:

    Simulate GET and POST requests on a URL and observe the response -- everything from low-level HTTP (result headers and status codes) to page content.
        Test that the correct view is executed for a given URL.
            Test that a given request is rendered by a given Django template, with a template context that contains certain values.

if you need in Browser testing then you will need to implement  LiveServerTestCase 

To resolve URLs, the test client uses whatever URLconf is pointed-to by your ROOT_URLCONF setting.

By default, the test client will disable any CSRF checks performed by your site

method:
------ 
get(path, data={}, follow=False, \**extra)
post(path, data={}, content_type=MULTIPART_CONTENT, follow=False, \**extra)

..head, options, put, delete 

RequestFactory
--------------
The RequestFactory shares the same API as the test client. However, instead of behaving like a browser, the RequestFactory provides a way to generate a request instance that can be used as the first argument to any view. This means you can test a view function the same way as you would test any other function -- as a black box, with exactly known inputs, testing for specific outputs.





result response objects



    client

        The test client that was used to make the request that resulted in the response.

    content

        The body of the response, as a string. This is the final page content as rendered by the view, or any error message.

    context

        The template Context instance that was used to render the template that produced the response content.

        If the rendered page used multiple templates, then context will be a list of Context objects, in the order in which they were rendered.

        Regardless of the number of templates used during rendering, you can retrieve context values using the [] operator. For example, the context variable name could be retrieved using:

        >>> response = client.get('/foo/')
        >>> response.context['name']
        'Arthur'

    request

        The request data that stimulated the response.

    status_code

        The HTTP status of the response, as an integer. See RFC 2616 for a full list of HTTP status codes.

    templates

        A list of Template instances used to render the final content, in the order they were rendered. For each template in the list, use template.name to get the template's file name, if the template was loaded from a file. (The name is a string such as 'admin/index.html'.)

login
logout

Assert 
SimpleTestCase.assertRaisesMessage(expected_exception, expected_message, callable_obj=None, *args, **kwargs) 

SimpleTestCase.assertFieldOutput(self, fieldclass, valid, invalid, field_args=None, field_kwargs=None, empty_value=u'')
     New in Django 1.4: Please see the release notes

         Asserts that a form field behaves correctly with various inputs.

TestCase.assertContains(response, text, count=None, status_code=200, msg_prefix='', html=False)

TestCase.assertNotContains(response, text, status_code=200, msg_prefix='', html=False)

Asserts that a Response instance produced the given status_code and that text appears in the content of the response. If count is provided, text must occur exactly count times in the response.


TestCase.assertFormError(response, form, field, errors, msg_prefix='')
Asserts that a field on a form raises the provided list of errors when rendered on the form

TestCase.assertRedirects(response, expected_url, status_code=302, target_status_code=200, msg_prefix='')


Persistent state
----------------
The test client is stateful. If a response returns a cookie, then that cookie will be stored in the test client and sent with all subsequent get() and post() requests.

Expiration policies for these cookies are not followed. If you want a cookie to expire, either delete it manually or create a new Client instance (which will effectively delete all cookies).

references
http://docs.python.org/library/unittest.html
https://docs.djangoproject.com/en/dev/topics/testing/

