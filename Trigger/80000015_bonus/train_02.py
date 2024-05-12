""" trigger/80000015_bonus/train_02.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3201,3202,3203,3204,3205,3206,3207,3208,3209], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3200,3210], visible=True, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3704,3705,3706], visible=False, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[123]):
            return 아이템체크(self.ctx)


class 아이템체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='itemSpawn', value=1):
            return 생성(self.ctx)
        if self.wait_tick(waitTick=200):
            self.create_item(spawnIds=[9026,9027,9028,9029,9030,9031], arg5=15)
            self.set_user_value(key='itemSpawn', value=1)
            return 생성(self.ctx)


class 생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[1201], animationEffect=False)
        self.set_mesh(triggerIds=[3200], visible=False, arg3=500, delay=0, scale=0)
        self.add_buff(boxIds=[1201], skillId=60170051, level=1, isPlayer=True, isSkillSet=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 삼(self.ctx)


class 삼(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3706], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 이(self.ctx)


class 이(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3706], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3705], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 일(self.ctx)


class 일(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3705], visible=False, arg3=0, delay=0, scale=0)
        self.set_mesh(triggerIds=[3704], visible=True, arg3=0, delay=0, scale=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 출발(self.ctx)


class 출발(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[3704], visible=False, arg3=0, delay=0, scale=0)
        self.move_npc(spawnId=1201, patrolName='MS2PatrolData1201A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.npc_detected(boxId=124, spawnIds=[1201]):
            return 소멸(self.ctx)


class 소멸(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            self.destroy_monster(spawnIds=[1201])
            return 딜레이(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=10000):
            return 대기(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 대기
