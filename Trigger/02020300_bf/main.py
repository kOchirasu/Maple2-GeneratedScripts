""" trigger/02020300_bf/main.xml """
import common


class 대기(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990002, key='Spawn', value=0)
        self.set_user_value(triggerId=99990003, key='RandomBomb', value=0)
        self.set_user_value(triggerId=99990004, key='Laser', value=0)
        self.set_user_value(triggerId=99990005, key='elevator', value=0)
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.set_interact_object(triggerIds=[10002185], state=0) # 엘리베이터 발판
        self.enable_spawn_point_pc(spawnId=100, isEnable=True) # <시작 위치 세팅>
        self.enable_spawn_point_pc(spawnId=101, isEnable=False)
        self.enable_spawn_point_pc(spawnId=102, isEnable=False)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[901]):
            return 시작(self.ctx)


class 시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[902]):
            self.set_event_ui(type=1, arg2='$02020300_BF__MAIN__0$', arg3='5000')
            self.create_monster(spawnIds=[101,102,103], animationEffect=False)
            return 추가대사_01(self.ctx)


class 추가대사_01(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            self.set_user_value(triggerId=99990004, key='Laser', value=1)
            self.side_npc_talk(type='talk', npcId=29500101, illust='ArcheonBlack_Normal', script='$02020300_BF__MAIN__1$', duration=5000)
            return 추가대사_02(self.ctx)


class 추가대사_02(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.monster_dead(boxIds=[101,102,103]):
            self.side_npc_talk(type='talk', npcId=29000170, illust='ArcaneBlader_normal', script='$02020300_BF__MAIN__2$', duration=5000)
            return 추가대사_03(self.ctx)


class 추가대사_03(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            self.side_npc_talk(type='talk', npcId=11003536, illust='Neirin_normal', script='$02020300_BF__MAIN__3$', duration=5000)
            return 엘리베이터_체크(self.ctx)


class 엘리베이터_체크(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            self.side_npc_talk(type='talk', npcId=29000170, illust='ArcaneBlader_normal', script='$02020300_BF__MAIN__4$', duration=5000)
            return 엘리베이터_스위치(self.ctx)


class 엘리베이터_스위치(common.Trigger):
    def on_enter(self):
        self.set_interact_object(triggerIds=[10002185], state=1)

    def on_tick(self) -> common.Trigger:
        if self.object_interacted(interactIds=[10002185], stateValue=0):
            return 엘리베이터_활성화(self.ctx)


class 엘리베이터_활성화(common.Trigger):
    def on_enter(self):
        self.set_breakable(triggerIds=[5001], enable=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[903]):
            return 아르케온_탑승_가이드(self.ctx)


class 아르케온_탑승_가이드(common.Trigger):
    def on_enter(self):
        self.set_event_ui(type=1, arg2='$02020300_BF__MAIN__5$', arg3='5000')

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[711]):
            self.set_user_value(triggerId=99990005, key='elevator', value=1)
            self.enable_spawn_point_pc(spawnId=100, isEnable=False)
            self.enable_spawn_point_pc(spawnId=101, isEnable=True)
            self.enable_spawn_point_pc(spawnId=102, isEnable=False)
            return 레이저_패턴_시작(self.ctx)


class 레이저_패턴_시작(common.Trigger):
    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[904]):
            return 갈림길_전투(self.ctx)


class 갈림길_전투(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[201,202,203,204], animationEffect=False)
        self.set_actor(triggerId=9001, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_end')
        self.set_mesh(triggerIds=[1001], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[905]):
            return 짜투리_전투(self.ctx)


class 짜투리_전투(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[301,302,303,304], animationEffect=False)
        self.set_mesh(triggerIds=[2001,2002,2003,2004], visible=True)
        self.set_mesh(triggerIds=[30000,30010,30020,30030], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[911]):
            return 웨이브_시작(self.ctx)


class 웨이브_시작(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=29000170, illust='ArcaneBlader_unfair', script='$02020300_BF__MAIN__6$', duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            self.set_mesh(triggerIds=[2001,2002,2003,2004], visible=False)
            self.set_mesh(triggerIds=[30000,30010,30020,30030], visible=False)
            return 추가대사_04(self.ctx)


class 추가대사_04(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=29500101, illust='ArcheonBlack_Normal', script='$02020300_BF__MAIN__7$', duration=5000)
        self.set_user_value(triggerId=99990002, key='Spawn', value=1)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='SpawnRoomEnd', value=1):
            self.set_actor(triggerId=9001, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_start')
            return 길열림(self.ctx)


class 길열림(common.Trigger):
    def on_enter(self):
        self.set_mesh(triggerIds=[1001], visible=False)
        self.set_mesh(triggerIds=[2001,2002,2003,2004], visible=True)
        self.set_mesh(triggerIds=[30000,30010,30020,30030], visible=True)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[921]):
            return 지뢰방_시작(self.ctx)


class 지뢰방_시작(common.Trigger):
    def on_enter(self):
        self.enable_spawn_point_pc(spawnId=100, isEnable=False) # <시작 위치 세팅>
        self.enable_spawn_point_pc(spawnId=101, isEnable=False)
        self.enable_spawn_point_pc(spawnId=102, isEnable=True)
        self.set_actor(triggerId=9002, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_end')
        self.set_actor(triggerId=9003, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_end')
        self.set_actor(triggerId=9004, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_end')
        self.set_mesh(triggerIds=[5001], visible=False)
        self.set_mesh(triggerIds=[3001,3002,3003], visible=True)
        self.set_user_value(triggerId=99990003, key='RandomBomb', value=1)
        self.side_npc_talk(type='talk', npcId=29500101, illust='ArcheonBlack_Normal', script='$02020300_BF__MAIN__8$', duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 추가대사_05(self.ctx)


class 추가대사_05(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=29000170, illust='ArcaneBlader_normal', script='$02020300_BF__MAIN__9$', duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return 추가대사_06(self.ctx)


class 추가대사_06(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=11003536, illust='Neirin_normal', script='$02020300_BF__MAIN__10$', duration=5000)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='RandomBombEnd', value=1):
            self.set_user_value(triggerId=99990004, key='Laser', value=0)
            return 보스전(self.ctx)


class 보스전(common.Trigger):
    def on_enter(self):
        self.side_npc_talk(type='talk', npcId=29000170, illust='ArcaneBlader_normal', script='$02020300_BF__MAIN__11$', duration=5000)
        self.set_actor(triggerId=9002, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_start')
        self.set_mesh(triggerIds=[3001], visible=False)
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)

    def on_tick(self) -> common.Trigger:
        if self.true():
            return 종료(self.ctx)


class 종료(common.Trigger):
    def on_enter(self):
        self.set_user_value(triggerId=99990005, key='elevator', value=0)


initial_state = 대기
