from kivymd.app import MDApp
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.theming import ThemeManager
from exchange import req_exchange_val
from kivymd.toast import toast
from kivy.properties import StringProperty
import requests


def check_net():
    # Check internet connection and rise errors
    timeout = 1
    try:
        requests.head("http://www.google.com/", timeout=timeout)
        return True
    except requests.ConnectionError:
        toast("Conn ection to internet dosent work")
        return False


class CalcApp(MDApp):
    def build(self):
        # self.theme_cls.theme_style = "Light"
        return Builder.load_file('calcapp.kv')



class MobileView(MDScreen):
    usd = StringProperty('USD')
    def count_button(self):
        if check_net():
            if len(self.ids.text_mobile.text) > 10:
                toast("Enter a smaller number")
            elif self.ids.text_mobile.text == '' or self.ids.text_mobile.text == '0':
                toast("Number must be greater then 0")
            else:
                a = req_exchange_val('binance-us', self.ids.text_mobile.text)
                self.ids.btc_text.text = str(a[0])
                self.ids.trx_text.text = str(a[1])
                self.ids.eth_text.text = str(a[2])
                self.ids.dog_text.text = str(a[3])



class TabletView(MDScreen):
    def count_button(self):
        if check_net():
            if len(self.ids.text_tablet.text) > 10:
                toast("Enter a smaller number")
            elif self.ids.text_tablet.text == '' or self.ids.text_tablet.text == '0':
                toast("Number must be greater then 0")
            else:
                a = req_exchange_val('binance-us', self.ids.text_tablet.text)
                self.ids.btc_text_tablet.text = str(a[0])
                self.ids.trx_text_tablet.text = str(a[1])
                self.ids.eth_text_tablet.text = str(a[2])
                self.ids.dog_text_tablet.text = str(a[3])


class DesktopView(MDScreen):
    pass


class ResponsiveView(MDResponsiveLayout, MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = MobileView()
        self.tablet_view = TabletView()
        self.desktop_view = DesktopView()


if __name__ == '__main__':
    CalcApp().run()

