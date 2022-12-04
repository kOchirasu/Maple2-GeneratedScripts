""" trigger/02000461_bf/cannon_05.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[695], visible=False)
        self.set_effect(triggerIds=[795], visible=False)
        self.set_mesh(triggerIds=[3905], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='cannon05', value=1):
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2905], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2905]):
            self.set_effect(triggerIds=[695], visible=True)
            self.set_mesh(triggerIds=[3905], visible=False, arg3=0, delay=0, scale=5)
            return 보스전_대기(self.ctx)


class 보스전_대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='Bosscannon05', value=1):
            return 보스전용_생성(self.ctx)


class 보스전용_생성(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[695], visible=False)
        self.set_effect(triggerIds=[795], visible=True)
        self.set_mesh(triggerIds=[3905], visible=True, arg3=0, delay=0, scale=0)
        self.create_monster(spawnIds=[2905], animationEffect=True)
        self.add_buff(boxIds=[2099], skillId=70002101, level=1, isPlayer=True, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2905]):
            self.set_effect(triggerIds=[695], visible=True)
            self.set_effect(triggerIds=[795], visible=False)
            self.set_mesh(triggerIds=[3905], visible=False, arg3=0, delay=0, scale=5)
            self.add_buff(boxIds=[2099], skillId=70002102, level=1, isPlayer=True, isSkillSet=False)
            self.add_buff(boxIds=[2905], skillId=40444001, level=1, isPlayer=True, isSkillSet=False)
            return 보스전용_재생성대기(self.ctx)
        if self.user_value(key='DungeonClear', value=1):
            return 종료(self.ctx)


class 보스전용_재생성대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=90000):
            return 보스전용_생성(self.ctx)
        if self.user_value(key='DungeonClear', value=1):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[695], visible=False)
        self.set_effect(triggerIds=[795], visible=False)
        self.set_mesh(triggerIds=[3905], visible=True, arg3=0, delay=0, scale=0)
        self.destroy_monster(spawnIds=[2905])


initial_state = 대기
