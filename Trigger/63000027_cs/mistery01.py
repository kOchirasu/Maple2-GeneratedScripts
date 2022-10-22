""" trigger/63000027_cs/mistery01.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        set_effect(triggerIds=[5200], visible=False) # VibrateLong
        set_effect(triggerIds=[5300], visible=False) # Sound_SpaceDestroy
        set_effect(triggerIds=[5400], visible=False) # Voice_Vision_00001725
        set_effect(triggerIds=[5401], visible=False) # Voice_Vision_00001741
        set_effect(triggerIds=[5402], visible=False) # Voice_Vision_00001872
        set_effect(triggerIds=[5500], visible=False) # Sound_VisionBuff
        set_mesh(triggerIds=[3100], visible=False, arg3=0, arg4=0, arg5=0) # barrier
        set_mesh(triggerIds=[3101], visible=False, arg3=0, arg4=0, arg5=0) # barrier
        set_mesh(triggerIds=[3102], visible=False, arg3=0, arg4=0, arg5=0) # barrier
        set_mesh(triggerIds=[3103], visible=False, arg3=0, arg4=0, arg5=0) # barrier
        set_user_value(key='CollapseEnd', value=0)
        set_user_value(key='ZoomIn', value=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9000]):
            return Enter01()


#  최초 입장 
class Enter01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9000], questIds=[90000451], questStates=[1]):
            return QuestOnGoing01()
        if quest_user_detected(boxIds=[9000], questIds=[90000450], questStates=[3]):
            return QuestOnGoing11()
        if quest_user_detected(boxIds=[9000], questIds=[90000450], questStates=[2]):
            return Delay01()
        if wait_tick(waitTick=3000):
            return Quit()


#  별, 수정, 그리고 퀘스트 수락한 상태 
class QuestOnGoing01(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return TimeToLeave01()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


#  기묘한 조짐 퀘스트 완료 상태 
class QuestOnGoing11(state.State):
    def on_enter(self):
        create_monster(spawnIds=[102], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return SecondQuestStart01()

    def on_exit(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


class Delay01(state.State):
    def on_enter(self):
        select_camera(triggerId=500, enable=True)
        set_scene_skip(state=VisionApp02, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return LookAround01()


class LookAround01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return LookAround02()


class LookAround02(state.State):
    def on_enter(self):
        select_camera(triggerId=501, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return LookAround03()


class LookAround03(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_1000')
        set_conversation(type=1, spawnId=0, script='$63000027_CS__MISTERY01__0$', arg4=3, arg5=0)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return LookAround04()


class LookAround04(state.State):
    def on_enter(self):
        select_camera(triggerId=502, enable=True)
        set_pc_emotion_sequence(sequenceNames=['Bore_C'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return VisionApp01()


class VisionApp01(state.State):
    def on_enter(self):
        select_camera(triggerId=600, enable=True)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return VisionApp02()


class VisionApp02(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)
        move_npc(spawnId=101, patrolName='MS2PatrolData_101')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return VisionTalk01()


class VisionTalk01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5400], visible=True) # Voice_Vision_00001725
        set_conversation(type=2, spawnId=11001560, script='$63000027_CS__MISTERY01__1$', arg4=5) # Voice 00001725
        set_skip(state=VisionTalk04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return VisionTalk02()


class VisionTalk02(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()

    def on_tick(self) -> state.State:
        if true():
            return VisionTalk03()


class VisionTalk03(state.State):
    def on_enter(self):
        set_conversation(type=2, spawnId=11001560, script='$63000027_CS__MISTERY01__2$', arg4=5)
        set_skip(state=VisionTalk04)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return VisionTalk04()


class VisionTalk04(state.State):
    def on_enter(self):
        remove_cinematic_talk()
        set_skip()
        destroy_monster(spawnIds=[101])
        create_monster(spawnIds=[102], arg2=False)
        select_camera(triggerId=601, enable=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return VisionTalk05()


class VisionTalk05(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return FirstQuestEnd01()


class FirstQuestEnd01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10034010, textId=10034010) # 가이드 : 비전을 향해 이동하기

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[9100]):
            return FirstQuestEnd02()

    def on_exit(self):
        hide_guide_summary(entityId=10034010)


class FirstQuestEnd02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10034020, textId=10034020) # 가이드 : [[icon:questcomplete]] 비전과 대화하기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000450], questStates=[3]):
            return SecondQuestStart01()

    def on_exit(self):
        hide_guide_summary(entityId=10034020)


class SecondQuestStart01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        show_guide_summary(entityId=10034030, textId=10034030) # 가이드 : [[icon:questaccept]] 비전과 대화하기

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9900], questIds=[90000451], questStates=[1]):
            return TimeToLeave01()

    def on_exit(self):
        hide_guide_summary(entityId=10034030)


class TimeToLeave01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)
        select_camera(triggerId=700, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=250):
            return TimeToLeave02()


class TimeToLeave02(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[102])
        create_monster(spawnIds=[103], arg2=False)
        move_user(mapId=63000027, portalId=10, boxId=9900)
        set_scene_skip(state=VisionSayGoodbye04, arg2='exit')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=250):
            return TimeToLeave03()


class TimeToLeave03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera(triggerId=701, enable=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PCGetEffect01()


class PCGetEffect01(state.State):
    def on_enter(self):
        add_buff(boxIds=[9900], skillId=70000097, level=1) # 신비로운 힘
        set_effect(triggerIds=[5500], visible=True) # Sound_VisionBuff

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return VisionSayGoodbye01()


class VisionSayGoodbye01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5402], visible=True) # Voice_Vision_00001872
        set_conversation(type=1, spawnId=103, script='$63000027_CS__MISTERY01__3$', arg4=4, arg5=0) # Voice 00001872

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return VisionSayGoodbye02()


class VisionSayGoodbye02(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5401], visible=True) # Voice_Vision_00001741
        set_conversation(type=1, spawnId=103, script='$63000027_CS__MISTERY01__4$', arg4=4, arg5=0) # Voice 00001741
        set_conversation(type=1, spawnId=103, script='$63000027_CS__MISTERY01__5$', arg4=3, arg5=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return VisionSayGoodbye03()


class VisionSayGoodbye03(state.State):
    def on_enter(self):
        move_npc(spawnId=103, patrolName='MS2PatrolData_102')
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return VisionSayGoodbye04()


class VisionSayGoodbye04(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[103])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Collapse01()


class Collapse01(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5200], visible=True) # VibrateLong
        select_camera(triggerId=710, enable=True)
        set_mesh(triggerIds=[3100], visible=True, arg3=0, arg4=0, arg5=0) # barrier
        set_mesh(triggerIds=[3101], visible=True, arg3=0, arg4=0, arg5=0) # barrier
        set_mesh(triggerIds=[3102], visible=True, arg3=0, arg4=0, arg5=0) # barrier
        set_mesh(triggerIds=[3103], visible=True, arg3=0, arg4=0, arg5=0) # barrier
        set_user_value(triggerId=2, key='CollapseStart', value=1)
        set_effect(triggerIds=[5300], visible=True) # Sound_SpaceDestroy

    def on_tick(self) -> state.State:
        if user_value(key='ZoomIn', value=1):
            return Collapse02()


class Collapse02(state.State):
    def on_enter(self):
        select_camera(triggerId=711, enable=True)

    def on_tick(self) -> state.State:
        if user_value(key='CollapseEnd', value=1):
            return PCFainted01()


class PCFainted01(state.State):
    def on_enter(self):
        set_pc_emotion_sequence(sequenceNames=['Down2_A','Down_Idle_A'])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2667):
            return PCTeleport01()


class PCTeleport01(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=10000)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_cinematic_ui(type=4)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return PCTeleport02()


class PCTeleport02(state.State):
    def on_enter(self):
        move_user(mapId=63000028, portalId=1, boxId=9900)
        select_camera(triggerId=711, enable=False)

    def on_tick(self) -> state.State:
        if not user_detected(boxIds=[9900]):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)


