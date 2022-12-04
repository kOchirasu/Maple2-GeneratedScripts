""" trigger/02000252_bf/elite_01.xml """
import trigger_api


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8901], visible=False) # 가이드 화살표
        self.set_effect(triggerIds=[604], visible=False) # 벨라 음성
        self.set_mesh(triggerIds=[2119,2120,2121,2122,2123,2124], visible=True)
        self.set_mesh(triggerIds=[2146,2147,2148,2149,2150,2151,2152,2153,2154,2155,2156,2157,2158,2159,2160,2161,2162,2163,2164,2165,2166], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=903, boxId=1):
            return 딜레이(self.ctx)


class 대기2(trigger_api.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[2119,2120,2121,2122,2123,2124], visible=True)
        self.set_mesh(triggerIds=[2146,2147,2148,2149,2150,2151,2152,2153,2154,2155,2156,2157,2158,2159,2160,2161,2162,2163,2164,2165,2166], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.count_users(boxId=903, boxId=1):
            return 딜레이2(self.ctx)


class 딜레이(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라(self.ctx)


class 딜레이2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라2(self.ctx)


class 벨라(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.create_monster(spawnIds=[1002], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라대사(self.ctx)


class 벨라2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.create_monster(spawnIds=[1002], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라대사2(self.ctx)


class 벨라대사(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=3)
        self.set_conversation(type=1, spawnId=1002, script='$02000252_BF__ELITE_01__0$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라스킬(self.ctx)


class 벨라대사2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=3)
        self.set_conversation(type=1, spawnId=1002, script='$02000252_BF__ELITE_01__1$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라스킬2(self.ctx)


class 벨라스킬(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 이동(self.ctx)


class 벨라스킬2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=2)
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_2')

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 이동2(self.ctx)


class 이동(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        # <action name="무작위유저를이동시킨다" arg1="02000252" arg2="9999" arg3="903" arg4="1" />
        self.create_monster(spawnIds=[201], animationEffect=False)
        self.create_monster(spawnIds=[1093], animationEffect=False)
        self.create_monster(spawnIds=[1094], animationEffect=False)
        self.create_monster(spawnIds=[1095], animationEffect=False)
        self.create_monster(spawnIds=[1096], animationEffect=False)
        self.create_monster(spawnIds=[1097], animationEffect=False)
        self.create_monster(spawnIds=[1098], animationEffect=False)
        self.create_monster(spawnIds=[1099], animationEffect=False)
        self.create_monster(spawnIds=[1100], animationEffect=False)
        self.create_monster(spawnIds=[1101], animationEffect=False)
        self.set_mesh(triggerIds=[2146,2147,2148,2149,2150,2151,2152,2153,2154,2155,2156,2157,2158,2159,2160,2161,2162,2163,2164,2165,2166], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라삭제(self.ctx)


class 이동2(trigger_api.Trigger):
    def on_enter(self):
        self.set_timer(timerId='1', seconds=1)
        # <action name="무작위유저를이동시킨다" arg1="02000252" arg2="9999" arg3="903" arg4="1" />
        self.set_mesh(triggerIds=[2146,2147,2148,2149,2150,2151,2152,2153,2154,2155,2156,2157,2158,2159,2160,2161,2162,2163,2164,2165,2166], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.time_expired(timerId='1'):
            return 벨라삭제(self.ctx)


class 벨라삭제(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[201]):
            return 개봉(self.ctx)


class 개봉(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[8901], visible=True) # 가이드 화살표
        self.set_mesh(triggerIds=[2146,2147,2148,2149,2150,2151,2152,2153,2154,2155,2156,2157,2158,2159,2160,2161,2162,2163,2164,2165,2166], visible=False)
        self.set_mesh(triggerIds=[2119,2120,2121,2122,2123,2124], visible=False)


initial_state = 대기
