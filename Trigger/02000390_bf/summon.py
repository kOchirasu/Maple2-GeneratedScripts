""" trigger/02000390_bf/summon.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=203903, key='Summon', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Summon', value=1):
            return Summon(self.ctx)


class Summon(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[501,502,503], animationEffect=True)
        self.set_user_value(triggerId=203903, key='Summon', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Summon', value=1):
            return Summon_02(self.ctx)


class Summon_02(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=102, script='$02000390_BF__SUMMON__0$', arg4=2, arg5=0)
        self.set_conversation(type=1, spawnId=101, script='$02000390_BF__SUMMON__1$', arg4=2, arg5=2)
        self.create_monster(spawnIds=[504,505,506], animationEffect=True)
        self.set_user_value(triggerId=203903, key='Summon', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Summon', value=1):
            return Summon_03(self.ctx)


class Summon_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=203903, key='Summon', value=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Summon', value=1):
            return Summon(self.ctx)


initial_state = idle
