""" trigger/02000461_bf/cannon_03.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[693], visible=False)
        self.set_effect(triggerIds=[793], visible=False)
        self.set_mesh(triggerIds=[3903], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='cannon03', value=1):
            return 생성(self.ctx)


class 생성(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[2903], animationEffect=True)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2903]):
            self.set_effect(triggerIds=[693], visible=True)
            self.set_mesh(triggerIds=[3903], visible=False, arg3=0, delay=0, scale=5)
            return 보스전_대기(self.ctx)


class 보스전_대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_value(key='Bosscannon03', value=1):
            return 보스전용_생성(self.ctx)


class 보스전용_생성(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[693], visible=False)
        self.set_effect(triggerIds=[793], visible=True)
        self.set_mesh(triggerIds=[3903], visible=True, arg3=0, delay=0, scale=0)
        self.create_monster(spawnIds=[2903], animationEffect=True)
        self.add_buff(boxIds=[2099], skillId=70002081, level=1, isPlayer=True, isSkillSet=False)

    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[2903]):
            self.set_effect(triggerIds=[693], visible=True)
            self.set_effect(triggerIds=[793], visible=False)
            self.set_mesh(triggerIds=[3903], visible=False, arg3=0, delay=0, scale=5)
            self.add_buff(boxIds=[2099], skillId=70002082, level=1, isPlayer=True, isSkillSet=False)
            self.add_buff(boxIds=[2903], skillId=40444001, level=1, isPlayer=True, isSkillSet=False)
            return 보스전용_재생성대기(self.ctx)
        if self.user_value(key='DungeonClear', value=1):
            return 종료(self.ctx)


class 보스전용_재생성대기(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=90000):
            return 보스전용_생성(self.ctx)
        if self.user_value(key='DungeonClear', value=1):
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[693], visible=False)
        self.set_effect(triggerIds=[793], visible=False)
        self.set_mesh(triggerIds=[3903], visible=True, arg3=0, delay=0, scale=0)
        self.destroy_monster(spawnIds=[2903])


initial_state = 대기
