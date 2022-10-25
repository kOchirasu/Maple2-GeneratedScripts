""" trigger/99999913/05_rarebox.xml """
import common


class Setting(common.Trigger):
    def on_enter(self):
        self.set_user_value(key='RareBoxOnCount', value=0)
        self.set_user_value(key='RareBoxOff', value=0)
        self.set_interact_object(triggerIds=[11000038], state=2) # Rare Box

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='RareBoxOnCount', value=1):
            return Delay(self.ctx)


class Delay(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[11000038], state=2) # Rare Box

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=180000):
            return BoxOn(self.ctx)


class BoxOn(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='머쉬룸 타워 근처에 황금 상자가 나타났습니다!\n황금 상자를 차지해보세요!', arg3='5000', arg4='0')
        self.set_interact_object(triggerIds=[11000038], state=1) # Rare Box

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='RareBoxOff', value=1):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[11000038], state=2) # Rare Box

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return Setting(self.ctx)


initial_state = Setting
