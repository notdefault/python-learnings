#!/usr/bin/python

from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
	def build(self):
		return Button(text="Hello")


TestApp().run();
#print "Hello, this is Python";