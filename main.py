from kivymd.app import MDApp
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from kivymd.theming import ThemeManager
from kivymd.toast import toast
from kivy.properties import StringProperty
import requests
from kivymd.uix.menu import MDDropdownMenu
# Import def from exchange.py
from exchange import req_exchange_val
# Import strings from strings.py file
from strings import *


# Check internet connection and rise errors
def check_net():
    timeout = 1
    try:
        requests.head("http://www.google.com/", timeout=timeout)
        return True
    except requests.ConnectionError:

        # Rise error
        toast("Conn ection to internet dosent work")
        return False

def def_menu_list():
    menu_list2 = [{
        "viewclass": "OneLineListItem",
        "text": opt1,
        "on_release": lambda x=0: market_list(x)
    },
        {
            "viewclass": "OneLineListItem",
            "text": opt2,
            "on_release": lambda x=1: market_list(x)
        },
        {
            "viewclass": "OneLineListItem",
            "text": opt3,
            "on_release": lambda x=2: market_list(x)
        },
        {
            "viewclass": "OneLineListItem",
            "text": opt4,
            "on_release": lambda x=3: market_list(x)
        },
        {
            "viewclass": "OneLineListItem",
            "text": opt5,
            "on_release": lambda x=4: market_list(x)
        },
        {
            "viewclass": "OneLineListItem",
            "text": opt6,
            "on_release": lambda x=5: market_list(x)
        }]
    return menu_list2

class CalcApp(MDApp):
    usd = StringProperty(v_usd)
    btc = StringProperty(v_btc)
    eth = StringProperty(v_eth)
    dog = StringProperty(v_dog)
    trx = StringProperty(v_trx)
    src = StringProperty(v_src)
    cnt = StringProperty(v_cnt)
    info = StringProperty(v_info)
    dialog = None

    # Info / Dialog window
    def info_button(self):
        if not self.dialog:
            self.dialog = MDDialog(text="Siema",
                                   buttons=[
                                       MDRectangleFlatButton(text="OK", on_release=self.close_dialog)])
        self.dialog.open()

    # Close info/ dialog window
    def close_dialog(self, obj):
        self.dialog.dismiss(force=True)

    def build(self):
        # self.theme_cls.theme_style = "Light"
        return Builder.load_file('calcapp.kv')


def market_list(set_market=0):
    market_options = [opt1, opt2, opt3, opt4, opt5, opt6]
    print(market_options[set_market])


class MobileView(MDScreen):
    def source_button(self):
        self.menu_list = def_menu_list()
        self.menu = MDDropdownMenu(
            caller=self.ids.source_button,
            items=self.menu_list,
            width_mult=3

        )
        self.menu.open()

    # Count button on mobile device
    def count_button(self):

        # Check internet connection
        if check_net():

            # Check len of text input
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
    def source_button(self):
        self.menu_list = def_menu_list()

        self.menu = MDDropdownMenu(
            caller=self.ids.source_button,
            items=self.menu_list,
            width_mult=4

        )
        self.menu.open()

    def test1(self):
        print("test 1")

    def test2(self):
        print("test 2")

    # Count button on tablet-like device
    def count_button(self):

        # Check internet connection
        if check_net():

            # Check len of text input
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
    def source_button(self):
        self.menu_list = def_menu_list()
        self.menu = MDDropdownMenu(
            caller=self.ids.source_button,
            items=self.menu_list,
            width_mult=5

        )
        self.menu.open()

    def test1(self):
        print("test 1")

    def test2(self):
        print("test 2")

    # Count button on tablet-like device
    def count_button(self):

        # Check internet connection
        if check_net():

            # Check len of text input
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


class ResponsiveView(MDResponsiveLayout, MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.mobile_view = MobileView()
        self.tablet_view = TabletView()
        self.desktop_view = DesktopView()


if __name__ == '__main__':
    CalcApp().run()
