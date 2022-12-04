""" trigger/52100300_qd/bombcontrol.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990001, key='RandomBombEnd', value=0)
        self.start_combine_spawn(groupId=[522], isStart=False)
        self.start_combine_spawn(groupId=[523], isStart=False)
        self.start_combine_spawn(groupId=[524], isStart=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_value(key='RandomBomb', value=1):
            return 포탑생성_1(self.ctx)


class 포탑생성_1(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[152], animationEffect=True) # 몬스터 등장
        self.start_combine_spawn(groupId=[524], isStart=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[152]):
            return 포탑생성_2(self.ctx)


class 포탑생성_2(trigger_api.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[522], isStart=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=15000):
            return 포탑생성_3(self.ctx)


class 포탑생성_3(trigger_api.Trigger):
    def on_enter(self):
        self.start_combine_spawn(groupId=[523], isStart=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[151,152,153,154,155,156,157,158,159]):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990001, key='RandomBombEnd', value=1)
        self.start_combine_spawn(groupId=[522], isStart=False)
        self.start_combine_spawn(groupId=[523], isStart=False)
        self.start_combine_spawn(groupId=[524], isStart=False)


initial_state = 대기
