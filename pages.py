import pageObjects.basePage as basePage
import pageObjects.homePage as homePage
import pageObjects.loginPage as loginPage
import pageObjects.appView as appView


class Pages:
    login_page = None  # type: loginPage.LoginPage
    base_page = None  # type: basePage.BasePage
    home_page = None  # type: homePage.HomePage
    app_page = None   # type: appView.AppView

    def __init__(self, context):
        self.login_page = loginPage.LoginPage(context)
        self.base_page = basePage.BasePage(context)
        self.home_page = homePage.HomePage(context)
        self.app_page = appView.AppView(context)


class PagesType:
    pages: Pages