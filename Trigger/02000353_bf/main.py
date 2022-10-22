""" trigger/02000353_bf/main.xml """
from common import *
import state

from dungeon_common.checkusercount import *

class idle(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)
        set_effect(triggerIds=[5004], visible=False)
        set_effect(triggerIds=[6001], visible=False)
        set_effect(triggerIds=[6002], visible=False)
        set_effect(triggerIds=[6003], visible=False)
        set_effect(triggerIds=[6004], visible=False)
        set_effect(triggerIds=[6101], visible=False)
        set_effect(triggerIds=[6301], visible=False)
        set_effect(triggerIds=[6302], visible=False)

    def on_tick(self) -> state.State:
        if count_users(boxId=701, boxId=1):
            return CheckUserCount()


class DungeonStart(state.DungeonStart):
    def on_enter(self):
        set_mesh(triggerIds=[2001,2002,2003,2004], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Start()

state.DungeonStart = DungeonStart


class Start(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 시작_03()


class 시작_03(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5004], visible=True)
        set_timer(timerId='2', seconds=2, display=False)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 시작_04()


class 시작_04(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[901,902,903], visible=False, arg4=0, arg5=10) # 벽 해제
        set_skill(triggerIds=[2020], isEnable=True) # 벽 날리는 스킬

    def on_tick(self) -> state.State:
        if count_users(boxId=702, boxId=1):
            return 시작_05()


class 시작_05(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=101, textId=40010) # 적을 모두 처치하시오
        set_effect(triggerIds=[6001], visible=True)
        set_effect(triggerIds=[6002], visible=True)
        set_effect(triggerIds=[6003], visible=True)
        set_effect(triggerIds=[6004], visible=True)
        set_effect(triggerIds=[6101], visible=True)
        set_actor(triggerId=3001, visible=False, initialSequence='Dmg_A')
        set_actor(triggerId=3002, visible=False, initialSequence='Dmg_A')
        set_actor(triggerId=3003, visible=False, initialSequence='Dmg_A')
        set_actor(triggerId=3004, visible=False, initialSequence='Dmg_A')
        set_actor(triggerId=3101, visible=False, initialSequence='Dmg_A')
        create_monster(spawnIds=[11,12,13,14,15], arg2=False) # 기본 배치 될 몬스터 등장
        create_monster(spawnIds=[101,102,103,104,105,106,108,109,110,111,112,113,114,115,116,117,118], arg2=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[11,12,13,14,15]):
            return 관문_01_개방전()

    def on_exit(self):
        hide_guide_summary(entityId=101)


class 관문_01_개방전(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000353_BF__MAIN__2$', arg3='2000')
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 관문_01_개방()


class 관문_01_개방(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_skip(state=관문_02_스킵)
        select_camera(triggerId=8001, enable=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 관문_01_개방_이벤트_00()


class 관문_01_개방_이벤트_00(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=True)
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 관문_01_개방_이벤트_01()


class 관문_01_개방_이벤트_01(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2001], isEnable=True) # 벽 날리는 스킬
        set_skill(triggerIds=[2002], isEnable=True) # 벽 날리는 스킬
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 관문_01_개방_이벤트_02()


class 관문_01_개방_이벤트_02(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2003], isEnable=True) # 벽 날리는 스킬
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 관문_01_개방_이벤트_03()


class 관문_01_개방_이벤트_03(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2004], isEnable=True) # 벽 날리는 스킬
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 관문_02_시작()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_cinematic_ui(type=7)


class 관문_02_스킵(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2001], isEnable=True)
        set_skill(triggerIds=[2002], isEnable=True)
        set_skill(triggerIds=[2003], isEnable=True)
        set_skill(triggerIds=[2004], isEnable=True)
        set_skip()
        reset_camera(interpolationTime=0)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            remove_buff(boxId=199, skillId=70000107)
            return 관문_02_시작()


class 관문_02_시작(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        select_camera(triggerId=8001, enable=False)
        show_guide_summary(entityId=103, textId=40011) # 다음 지역으로 이동하세요

    def on_tick(self) -> state.State:
        if count_users(boxId=703, boxId=1):
            return 관문_02_시작_02()

    def on_exit(self):
        hide_guide_summary(entityId=103)


class 관문_02_시작_02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6005], visible=True)
        set_effect(triggerIds=[6006], visible=True)
        set_effect(triggerIds=[6007], visible=True)
        set_effect(triggerIds=[6008], visible=True)
        set_actor(triggerId=3005, visible=False, initialSequence='Dmg_A')
        set_actor(triggerId=3006, visible=False, initialSequence='Dmg_A')
        set_actor(triggerId=3007, visible=False, initialSequence='Dmg_A')
        set_actor(triggerId=3008, visible=False, initialSequence='Dmg_A')
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=101, textId=40010) # 적을 모두 처치하시오
        create_monster(spawnIds=[21,22,23,24,25,26,27], arg2=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[21,22,23,24,25,26,27]):
            return 관문_02_개방전()

    def on_exit(self):
        hide_guide_summary(entityId=101)


class 관문_02_개방전(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000353_BF__MAIN__3$', arg3='2000')
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 관문_02_개방()


class 관문_02_개방(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5002], visible=True)
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 관문_02_개방_이벤트_01()


class 관문_02_개방_이벤트_01(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2006], isEnable=True) # 벽 날리는 스킬
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 관문_02_개방_이벤트_02()


class 관문_02_개방_이벤트_02(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2007], isEnable=True) # 벽 날리는 스킬
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 관문_02_개방_이벤트_03()


class 관문_02_개방_이벤트_03(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2008], isEnable=True) # 벽 날리는 스킬
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 관문_03_시작_01()


class 관문_03_시작_01(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=103, textId=40011) # 다음 지역으로 이동하세요

    def on_tick(self) -> state.State:
        if count_users(boxId=704, boxId=1):
            return 관문_03_시작_02()

    def on_exit(self):
        hide_guide_summary(entityId=103)


class 관문_03_시작_02(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=101, textId=40010) # 적을 모두 처치하시오
        set_effect(triggerIds=[6301], visible=True)
        set_effect(triggerIds=[6302], visible=True)
        set_actor(triggerId=3301, visible=False, initialSequence='Dmg_A')
        set_actor(triggerId=3302, visible=False, initialSequence='Dmg_A')
        create_monster(spawnIds=[31,32,33], arg2=False) # 기본 배치 될 몬스터 등장

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[31,32,33]):
            return 관문_03_개방전()

    def on_exit(self):
        hide_guide_summary(entityId=101)


class 관문_03_개방전(state.State):
    def on_enter(self):
        set_event_ui(type=1, arg2='$02000353_BF__MAIN__4$', arg3='2000')
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 관문_03_개방()


class 관문_03_개방(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5003], visible=True)
        set_timer(timerId='2', seconds=2)

    def on_tick(self) -> state.State:
        if time_expired(timerId='2'):
            return 관문_03_개방_이벤트_01()


class 관문_03_개방_이벤트_01(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2009], isEnable=True) # 벽 날리는 스킬
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 관문_03_개방_이벤트_02()


class 관문_03_개방_이벤트_02(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2010], isEnable=True) # 벽 날리는 스킬
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 관문_03_개방_이벤트_03()


class 관문_03_개방_이벤트_03(state.State):
    def on_enter(self):
        set_skill(triggerIds=[2011], isEnable=True) # 벽 날리는 스킬
        set_timer(timerId='1', seconds=1)

    def on_tick(self) -> state.State:
        if time_expired(timerId='1'):
            return 지역클리어()


class 지역클리어(state.State):
    def on_enter(self):
        play_system_sound_in_box(sound='System_Space_PopUp_01')
        show_guide_summary(entityId=103, textId=40009) # 포탈로 이동하세요
        set_mesh(triggerIds=[6006], visible=False, arg4=0, arg5=10) # 벽 해제
        set_mesh(triggerIds=[6007], visible=True, arg4=0, arg5=10) # 화살표 표시
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


