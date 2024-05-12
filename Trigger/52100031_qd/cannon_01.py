""" trigger/52100031_qd/cannon_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[691], visible=False)
        self.set_mesh(triggerIds=[3901], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='cannon01', value=1):
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[2901], animationEffect=True)
        self.add_buff(boxIds=[2901], skillId=40444001, level=1, isPlayer=True, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2901]):
            self.set_effect(triggerIds=[691], visible=True)
            self.set_mesh(triggerIds=[3901], visible=False, arg3=0, delay=0, scale=5)
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
