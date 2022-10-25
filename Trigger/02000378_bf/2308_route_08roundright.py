""" trigger/02000378_bf/2308_route_08roundright.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_agent(triggerIds=[28081], visible=True)
        self.set_agent(triggerIds=[28082], visible=True)
        self.set_agent(triggerIds=[28083], visible=True)
        self.set_agent(triggerIds=[28084], visible=True)
        self.set_mesh(triggerIds=[230800,230801,230802,230803,230804,230805,230806,230807,230808,230809,230810,230811,230812,230813,230814,230815,230816,230817,230818,230819,230820,230821], visible=False, arg3=0, delay=0, scale=0) # Fake
        self.set_mesh(triggerIds=[430800,430801,430802,430803,430804,430805,430806,430807,430808,430809,430810,430811,430812,430813,430814,430815,430816,430817,430818,430819,430820,430821], visible=False, arg3=0, delay=0, scale=0) # Real
        self.set_user_value(key='RouteSelected', value=0)
        self.set_user_value(key='MakeTrue', value=0)
        self.set_user_value(key='MakeFalse', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='RouteSelected', value=1):
            return StartDazzlingRandom01(self.ctx)


# 가짜 길이 깜빡이는 연출
class StartDazzlingRandom01(common.Trigger):
    def on_enter(self):
        self.set_random_mesh(triggerIds=[230800,230801,230802,230803,230804,230805,230806,230807,230808,230809,230810,230811,230812,230813,230814,230815,230816,230817,230818,230819,230820,230821], visible=True, meshCount=7, arg4=100, delay=500) # Fake

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom02(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self):
        self.set_random_mesh(triggerIds=[230800,230801,230802,230803,230804,230805,230806,230807,230808,230809,230810,230811,230812,230813,230814,230815,230816,230817,230818,230819,230820,230821], visible=False, meshCount=22, arg4=0, delay=0) # Fake


class StartDazzlingRandom02(common.Trigger):
    def on_enter(self):
        self.set_random_mesh(triggerIds=[230800,230801,230802,230803,230804,230805,230806,230807,230808,230809,230810,230811,230812,230813,230814,230815,230816,230817,230818,230819,230820,230821], visible=True, meshCount=7, arg4=100, delay=500) # Fake

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return StartDazzlingRandom01(self.ctx)
        if self.user_value(key='MakeTrue', value=1):
            return MakeTrue(self.ctx)
        if self.user_value(key='MakeFalse', value=1):
            return MakeFalse(self.ctx)

    def on_exit(self):
        self.set_random_mesh(triggerIds=[230800,230801,230802,230803,230804,230805,230806,230807,230808,230809,230810,230811,230812,230813,230814,230815,230816,230817,230818,230819,230820,230821], visible=False, meshCount=22, arg4=0, delay=0) # Fake


class MakeTrue(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5008], visible=True) # 08Round_BridgeApp
        self.set_mesh(triggerIds=[230800,230801,230802,230803,230804,230805,230806,230807,230808,230809,230810,230811,230812,230813,230814,230815,230816,230817,230818,230819,230820,230821], visible=False, arg3=0, delay=0, scale=5) # Fake
        self.set_random_mesh(triggerIds=[430800,430801,430802,430803,430804,430805,430806,430807,430808,430809,430810,430811,430812,430813,430814,430815,430816,430817,430818,430819,430820,430821], visible=True, meshCount=22, arg4=0, delay=50) # Real
        self.set_agent(triggerIds=[28081], visible=False)
        self.set_agent(triggerIds=[28082], visible=False)
        self.set_agent(triggerIds=[28083], visible=False)
        self.set_agent(triggerIds=[28084], visible=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class MakeFalse(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[230800,230801,230802,230803,230804,230805,230806,230807,230808,230809,230810,230811,230812,230813,230814,230815,230816,230817,230818,230819,230820,230821], visible=False, arg3=0, delay=0, scale=5) # Fake

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


class Quit(common.Trigger):
    pass


initial_state = Wait
