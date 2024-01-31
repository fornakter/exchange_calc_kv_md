import clipboard
from kivymd.app import MDApp
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
# from kivymd.theming import ThemeManager
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
    try:
        requests.head("http://www.google.com/")
        return True
    except requests.ConnectionError:
        # Rise error
        toast("Connection to internet doesn't work")
        return False


def market_list(set_market):
    market_options = [opt1, opt2, opt3, opt4, opt5, opt6]
    a = market_options[set_market]
    return a


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

    def copy_email_button(self, obj):
        clipboard.copy("fornakter@gmail.com")
        toast("Copied")

    # Info / Dialog window
    def info_button(self):
        if not self.dialog:
            self.dialog = MDDialog(title="CryptoCalc",
                                   text="Questions and feedback: fornakter@gmail.com\n"
                                        "Version: 2.1\n"
                                        "Created by: Adam Fatyga",
                                   buttons=[
                                        MDRectangleFlatButton(text="OK", on_release=self.close_dialog),
                                        MDRectangleFlatButton(text="Copy email", on_release=self.copy_email_button),
                                        ])
        self.dialog.open()

        # Close info/ dialog window
    def close_dialog(self, obj):
        self.dialog.dismiss(force=True)

    def build(self):
        # self.theme_cls.theme_style = "Light"
        return Builder.load_file('calcapp.kv')


class MobileView(MDScreen):
    market = opt1

    def source_button(self):
        self.menu_list = [{
            "viewclass": "OneLineListItem",
            "text": opt1,
            "on_release": lambda x=0: self.market_list(x),
        },
            {
                "viewclass": "OneLineListItem",
                "text": opt2,
                "on_release": lambda x=1: self.market_list(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": opt3,
                "on_release": lambda x=2: self.market_list(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": opt4,
                "on_release": lambda x=3: self.market_list(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": opt5,
                "on_release": lambda x=4: self.market_list(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": opt6,
                "on_release": lambda x=5: self.market_list(x)
            }]
        self.menu = MDDropdownMenu(
            caller=self.ids.source_button,
            items=self.menu_list,
            width_mult=3
        )
        self.menu.open()

    # Select market
    def market_list(self, set_market):
        market_options = [opt1, opt2, opt3, opt4, opt5, opt6]
        self.market = market_options[set_market]
        self.menu.dismiss()
        return self.market

    # Count button on mobile device
    def count_button(self):

        # Check internet connection
        if check_net():

            # Check len of text input
            if len(self.ids.text_mobile.text) > 10:
                toast("Enter a smaller number")
            elif self.ids.text_mobile.text == '' or self.ids.text_mobile.text <= '0':
                toast("Number must be greater then 0")
            else:
                a = req_exchange_val(self.ids.text_mobile.text)
                self.ids.btc_text.text = str(a[0])
                self.ids.trx_text.text = str(a[1])
                self.ids.eth_text.text = str(a[2])
                self.ids.dog_text.text = str(a[3])


class TabletView(MDScreen):
    market = opt1

    def source_button(self):
        self.menu_list = [{
            "viewclass": "OneLineListItem",
            "text": opt1,
            "on_release": lambda x=0: self.market_list(x)
        },
            {
                "viewclass": "OneLineListItem",
                "text": opt2,
                "on_release": lambda x=1: self.market_list(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": opt3,
                "on_release": lambda x=2: self.market_list(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": opt4,
                "on_release": lambda x=3: self.market_list(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": opt5,
                "on_release": lambda x=4: self.market_list(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": opt6,
                "on_release": lambda x=5: self.market_list(x)
            }]
        self.menu = MDDropdownMenu(
            caller=self.ids.source_button,
            items=self.menu_list,
            width_mult=3
        )
        self.menu.open()

    # Select market
    def market_list(self, set_market):
        market_options = [opt1, opt2, opt3, opt4, opt5, opt6]
        self.market = market_options[set_market]
        self.menu.dismiss()
        return self.market

    # Count button on tablet-like device
    def count_button(self):

        # Check internet connection
        if check_net():

            # Check len of text input
            if len(self.ids.text_tablet.text) > 10:
                toast("Enter a smaller number")
            elif self.ids.text_tablet.text == '' or self.ids.text_tablet.text <= '0':
                toast("Number must be greater then 0")
            else:
                a = req_exchange_val(self.ids.text_tablet.text)
                self.ids.btc_text_tablet.text = str(a[0])
                self.ids.trx_text_tablet.text = str(a[1])
                self.ids.eth_text_tablet.text = str(a[2])
                self.ids.dog_text_tablet.text = str(a[3])


class DesktopView(MDScreen):
    market = opt1

    def source_button(self):
        self.menu_list = [{
            "viewclass": "OneLineListItem",
            "text": opt1,
            "on_release": lambda x=0: self.market_list(x)
        },
            {
                "viewclass": "OneLineListItem",
                "text": opt2,
                "on_release": lambda x=1: self.market_list(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": opt3,
                "on_release": lambda x=2: self.market_list(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": opt4,
                "on_release": lambda x=3: self.market_list(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": opt5,
                "on_release": lambda x=4: self.market_list(x)
            },
            {
                "viewclass": "OneLineListItem",
                "text": opt6,
                "on_release": lambda x=5: self.market_list(x)
            }]
        self.menu = MDDropdownMenu(
            caller=self.ids.source_button,
            items=self.menu_list,
            width_mult=3
        )
        self.menu.open()

    # Select market
    def market_list(self, set_market):
        market_options = [opt1, opt2, opt3, opt4, opt5, opt6]
        self.market = market_options[set_market]
        self.menu.dismiss()
        return self.market

    # Count button on desktop device
    def count_button(self):

        # Check internet connection
        if check_net():

            # Check len of text input
            if len(self.ids.text_tablet.text) > 10:
                toast("Enter a smaller number")
            elif self.ids.text_tablet.text == '' or self.ids.text_tablet.text <= '0':
                toast("Number must be greater then 0")
            else:
                a = req_exchange_val(self.ids.text_tablet.text)
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
