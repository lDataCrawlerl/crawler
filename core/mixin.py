# coding: utf-8
import random
from common.const.user_agent import windows_browsers, linux_browsers, mac_browsers


class UserAgentMixin(object):

    @classmethod
    def get_user_agent(cls):
        rand = random.randint(1, 3)
        if rand == 1:
            browsers = windows_browsers
        elif rand == 2:
            browsers = linux_browsers
        elif rand == 3:
            browsers = mac_browsers
        return random.choice(browsers)


class ProxyMixin(object):

    def get_proxys(self):
        pass


if __name__ == '__main__':
    class Test(UserAgentMixin):

        def get_user_agent(self):
            return super(Test, self).get_user_agent()

    t = Test()
    print t.get_user_agent()
