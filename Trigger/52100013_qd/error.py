""" trigger/52100013_qd/error.xml """
import trigger_api


# 플레이어 감지
# 슈팅전 체크 에디셔널 이펙트를 계속 걸어줌
class ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.is_dungeon_room():
            return idle(self.ctx)
        if not self.is_dungeon_room():
            return quest_idle(self.ctx)


class idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Error', value=1):
            return end(self.ctx)
        if self.user_detected(boxIds=[702]):
            return error(self.ctx)


class error(trigger_api.Trigger):
    def on_enter(self):
        self.move_random_user(mapId=52100013, portalId=2, triggerId=702, count=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return idle(self.ctx)


class quest_idle(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Error', value=1):
            return end(self.ctx)
        if self.user_detected(boxIds=[702]):
            return quest_error(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[50100090], questStates=[1]):
            return end(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[50100080], questStates=[2]):
            return end(self.ctx)


class quest_error(trigger_api.Trigger):
    def on_enter(self):
        self.move_random_user(mapId=52100013, portalId=2, triggerId=702, count=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return quest_idle(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[50100090], questStates=[1]):
            return end(self.ctx)
        if self.quest_user_detected(boxIds=[701], questIds=[50100080], questStates=[2]):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1001,1002], visible=False)


initial_state = ready
