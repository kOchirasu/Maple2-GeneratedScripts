""" trigger/80000015_bonus/train_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[3100,3101,3102,3103,3104,3105,3106,3107,3108,3109,3110,3111,3112,3113], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3100], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3701,3702,3703], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[121]):
            return 아이템체크(self.ctx)


class 아이템체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='itemSpawn', value=1):
            return 생성(self.ctx)
        if self.wait_tick(waitTick=200):
            self.create_item(spawnIds=[9020,9021,9022,9023,9024,9025], arg5=15)
            self.set_user_value(key='itemSpawn', value=1)
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1200], animationEffect=False)
        self.set_mesh(triggerIds=[3100], visible=False, arg3=500, delay=0, scale=0)
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

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=122, spawnIds=[1200]):
            return 소멸(self.ctx)


class 소멸(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.destroy_monster(spawnIds=[1200])
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
