from django.test import SimpleTestCase, TestCase,Client
from cloths.views import firstpage,registration,edit,delete,update,home
from django.urls import resolve, reverse
from customer.models import Customer
from django.contrib.auth.models import User
# Create your tests here.

class TestUrls(SimpleTestCase):
    def test_case_firstpage(self):
        url=reverse('firstpage')
        self.assertEquals(resolve(url).func,firstpage)

    def test_case_home(self):
        url=reverse('home')
        self.assertEquals(resolve(url).func,home)

    def test_case_create_url(self):
        url=reverse('create')
        self.assertEquals(resolve(url).func,registration)

    def test_case_edit_url(self):
        url=reverse('edit',args=[1])
        self.assertEquals(resolve(url).func,edit)

    def test_case_delete_url(self):
        url=reverse('delete',args=[1])
        self.assertEquals(resolve(url).func,delete)

    def test_case_update_url(self):
        url=reverse('update',args=[1])
        self.assertEquals(resolve(url).func,update)

class TestViews(TestCase):
    def test_case_homepage_views(self):
        user=User.objects.create(username="testcase")
        user.set_password('123456')
        user.save()
 
        client=Client()
 
        logged_in=client.login(username='testcase',password="123456")
 
        url=reverse('adminn')
 
        response=client.get(url)
     
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,"adminn/admin2.html")

    def test_case_registration_views(self):
            user=User.objects.create(username="testcase")
            user.set_password('123456')
            user.save()
 
            client=Client()
 
            logged_in=client.login(username='testcase',password="123456")
 
            url=reverse('create')
 
            response=client.post(url,{
            'username':'test name',
            'email' : 'test email',
            'psw':'test pass',
            
        })
     
            self.assertEquals(response.status_code,302)
            self.assertRedirects(response,"/store/cloth_pannel")

    
    def test_case_delete_views(self):
        user=User.objects.create(username="testcase")
        user.set_password('123456')
        user.save()
 
        client=Client()
 
        logged_in=client.login(username='testcase',password="123456")
 
        newlyCreated=User.objects.create(
            username='test name',
            email='test email',
            password='test pass',
        
        )
        print("here is customer id")
        print(newlyCreated.id)
        url=reverse('delete',args=[newlyCreated.id])
 
    
        response=client.delete(url)
        print(response)
        self.assertEquals(response.status_code,302)
        self.assertRedirects(response,"/user_pannel")