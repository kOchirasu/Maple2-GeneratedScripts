""" trigger/80000014_bonus/train.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3123,3124,3125,3126,3127,3128,3129], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3121], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3122], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3701,3702,3703], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[120]):
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1200], animationEffect=False)
        self.set_mesh(triggerIds=[3122], visible=False, arg3=500, delay=0, scale=0)
        self.add_buff(boxIds=[1200], skillId=60170051, level=1, isPlayer=True, isSkillSet=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 삼(self.ctx)


class 삼(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3703], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 이(self.ctx)


class 이(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3703], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3702], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 일(self.ctx)


class 일(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3702], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3701], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 출발(self.ctx)


class 출발(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3701], visible=False, arg3=0, delay=0, scale=0)
        self.move_npc(spawnId=1200, patrolName='MS2PatrolData1200A')
        self.create_item(spawnIds=[9020,9021,9022,9023,9024,9025], arg5=10)

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=121, spawnIds=[1200]):
            return 소멸(self.ctx)


class 소멸(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.destroy_monster(spawnIds=[1200])
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
