# coding: utf-8
from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription


class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Carlos Ferreira Junior',
            cpf='12345678901',
            email='ferreirajuniorcarlos@gmail.com',
            phone='91-88282471'
        )

    def test_create(self):
        'Subscription must have name,cpf,email,phone'
        self.obj.save()
        self.assertEqual(1, self.obj.pk)
        
    def test_has_created_at(self):
        'Subscription must have automatic created at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Carlos Ferreira Junior', unicode(self.obj))


class SubscriptionUniqueTest(TestCase):
    def setUp(self):
        #Create a first entry to force the collision
        Subscription.objects.create(name="Carlos Ferreira Junior", cpf="12345678902",
                                    email="outro@email.com", phone="912222222")

    def test_cpf_unique(self):
        'CPF must be unique'
        s = Subscription(name="Carlos Ferreira Junior", cpf="12345678902",
                         email="outro@email.com", phone="912222222")
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
         s = Subscription(name="Carlos Ferreira Junior", cpf="12345678902",
                         email="outro@email.com", phone="912222222")
         
         self.assertRaises(IntegrityError, s.save)
        
