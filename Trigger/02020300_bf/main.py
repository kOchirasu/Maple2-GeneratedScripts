""" trigger/02020300_bf/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990002, key='Spawn', value=0)
        set_user_value(triggerId=99990003, key='RandomBomb', value=0)
        set_user_value(triggerId=99990004, key='Laser', value=0)
        set_user_value(triggerId=99990005, key='elevator', value=0)
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_interact_object(triggerIds=[10002185], state=0) # 엘리베이터 발판
        enable_spawn_point_pc(spawnId=100, isEnable=True) # <시작 위치 세팅>
        enable_spawn_point_pc(spawnId=101, isEnable=False)
        enable_spawn_point_pc(spawnId=102, isEnable=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[901]):
            return 시작()


class 시작(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[902]):
            set_event_ui(type=1, arg2='$02020300_BF__MAIN__0$', arg3='5000')
            create_monster(spawnIds=[101,102,103], arg2=False)
            return 추가대사_01()


class 추가대사_01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            set_user_value(triggerId=99990004, key='Laser', value=1)
            side_npc_talk(type='talk', npcId=29500101, illust='ArcheonBlack_Normal', script='$02020300_BF__MAIN__1$', duration=5000)
            return 추가대사_02()


class 추가대사_02(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102,103]):
            side_npc_talk(type='talk', npcId=29000170, illust='ArcaneBlader_normal', script='$02020300_BF__MAIN__2$', duration=5000)
            return 추가대사_03()


class 추가대사_03(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            side_npc_talk(type='talk', npcId=11003536, illust='Neirin_normal', script='$02020300_BF__MAIN__3$', duration=5000)
            return 엘리베이터_체크()


class 엘리베이터_체크(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            side_npc_talk(type='talk', npcId=29000170, illust='ArcaneBlader_normal', script='$02020300_BF__MAIN__4$', duration=5000)
            return 엘리베이터_스위치()


class 엘리베이터_스위치(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10002185], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10002185], arg2=0):
            return 엘리베이터_활성화()


class 엘리베이터_활성화(state.State):
    def on_enter(self):
        set_breakable(triggerIds=[5001], enabled=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[903]):
            return 아르케온_탑승_가이드()


class 아르케온_탑승_가이드(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02020300_BF__MAIN__5$', arg3='5000')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[711]):
            set_user_value(triggerId=99990005, key='elevator', value=1)
            enable_spawn_point_pc(spawnId=100, isEnable=False)
            enable_spawn_point_pc(spawnId=101, isEnable=True)
            enable_spawn_point_pc(spawnId=102, isEnable=False)
            return 레이저_패턴_시작()


class 레이저_패턴_시작(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[904]):
            return 갈림길_전투()


class 갈림길_전투(state.State):
    def on_enter(self):
        create_monster(spawnIds=[201,202,203,204], arg2=False)
        set_actor(triggerId=9001, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_end')
        set_mesh(triggerIds=[1001], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[905]):
            return 짜투리_전투()


class 짜투리_전투(state.State):
    def on_enter(self):
        create_monster(spawnIds=[301,302,303,304], arg2=False)
        set_mesh(triggerIds=[2001,2002,2003,2004], visible=True)
        set_mesh(triggerIds=[30000,30010,30020,30030], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[911]):
            return 웨이브_시작()


class 웨이브_시작(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=29000170, illust='ArcaneBlader_unfair', script='$02020300_BF__MAIN__6$', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            set_mesh(triggerIds=[2001,2002,2003,2004], visible=False)
            set_mesh(triggerIds=[30000,30010,30020,30030], visible=False)
            return 추가대사_04()


class 추가대사_04(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=29500101, illust='ArcheonBlack_Normal', script='$02020300_BF__MAIN__7$', duration=5000)
        set_user_value(triggerId=99990002, key='Spawn', value=1)

    def on_tick(self) -> state.State:
        if user_value(key='SpawnRoomEnd', value=1):
            set_actor(triggerId=9001, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_start')
            return 길열림()


class 길열림(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[1001], visible=False)
        set_mesh(triggerIds=[2001,2002,2003,2004], visible=True)
        set_mesh(triggerIds=[30000,30010,30020,30030], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[921]):
            return 지뢰방_시작()


class 지뢰방_시작(state.State):
    def on_enter(self):
        enable_spawn_point_pc(spawnId=100, isEnable=False) # <시작 위치 세팅>
        enable_spawn_point_pc(spawnId=101, isEnable=False)
        enable_spawn_point_pc(spawnId=102, isEnable=True)
        set_actor(triggerId=9002, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_end')
        set_actor(triggerId=9003, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_end')
        set_actor(triggerId=9004, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_end')
        set_mesh(triggerIds=[5001], visible=False)
        set_mesh(triggerIds=[3001,3002,3003], visible=True)
        set_user_value(triggerId=99990003, key='RandomBomb', value=1)
        side_npc_talk(type='talk', npcId=29500101, illust='ArcheonBlack_Normal', script='$02020300_BF__MAIN__8$', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 추가대사_05()


class 추가대사_05(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=29000170, illust='ArcaneBlader_normal', script='$02020300_BF__MAIN__9$', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 추가대사_06()


class 추가대사_06(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003536, illust='Neirin_normal', script='$02020300_BF__MAIN__10$', duration=5000)

    def on_tick(self) -> state.State:
        if user_value(key='RandomBombEnd', value=1):
            set_user_value(triggerId=99990004, key='Laser', value=0)
            return 보스전()


class 보스전(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=29000170, illust='ArcaneBlader_normal', script='$02020300_BF__MAIN__11$', duration=5000)
        set_actor(triggerId=9002, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_start')
        set_mesh(triggerIds=[3001], visible=False)
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990005, key='elevator', value=0)


