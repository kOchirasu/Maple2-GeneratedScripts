""" trigger/63000027_cs/mistery01.xml """
import common


class Wait(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=False) # 가이드 서머리 사운드 이펙트
        self.set_effect(triggerIds=[5200], visible=False) # VibrateLong
        self.set_effect(triggerIds=[5300], visible=False) # Sound_SpaceDestroy
        self.set_effect(triggerIds=[5400], visible=False) # Voice_Vision_00001725
        self.set_effect(triggerIds=[5401], visible=False) # Voice_Vision_00001741
        self.set_effect(triggerIds=[5402], visible=False) # Voice_Vision_00001872
        self.set_effect(triggerIds=[5500], visible=False) # Sound_VisionBuff
        self.set_mesh(triggerIds=[3100], visible=False, arg3=0, delay=0, scale=0) # barrier
        self.set_mesh(triggerIds=[3101], visible=False, arg3=0, delay=0, scale=0) # barrier
        self.set_mesh(triggerIds=[3102], visible=False, arg3=0, delay=0, scale=0) # barrier
        self.set_mesh(triggerIds=[3103], visible=False, arg3=0, delay=0, scale=0) # barrier
        self.set_user_value(key='CollapseEnd', value=0)
        self.set_user_value(key='ZoomIn', value=0)

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9000]):
            return Enter01(self.ctx)


# 최초 입장
class Enter01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9000], questIds=[90000451], questStates=[1]):
            return QuestOnGoing01(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[90000450], questStates=[3]):
            return QuestOnGoing11(self.ctx)
        if self.quest_user_detected(boxIds=[9000], questIds=[90000450], questStates=[2]):
            return Delay01(self.ctx)
        if self.wait_tick(waitTick=3000):
            return Quit(self.ctx)


# 별, 수정, 그리고 퀘스트 수락한 상태
class QuestOnGoing01(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[102], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return TimeToLeave01(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


# 기묘한 조짐 퀘스트 완료 상태
class QuestOnGoing11(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[102], animationEffect=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return SecondQuestStart01(self.ctx)

    def on_exit(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


class Delay01(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=500, enable=True)
        self.set_scene_skip(state=VisionApp02, action='nextState')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return LookAround01(self.ctx)


class LookAround01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return LookAround02(self.ctx)


class LookAround02(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=501, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return LookAround03(self.ctx)


class LookAround03(common.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_1000')
        self.set_conversation(type=1, spawnId=0, script='$63000027_CS__MISTERY01__0$', arg4=3, arg5=0)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return LookAround04(self.ctx)


class LookAround04(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=502, enable=True)
        self.set_pc_emotion_sequence(sequenceNames=['Bore_C'])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=3000):
            return VisionApp01(self.ctx)


class VisionApp01(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=600, enable=True)
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1500):
            return VisionApp02(self.ctx)


class VisionApp02(common.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=False)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_101')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return VisionTalk01(self.ctx)


class VisionTalk01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5400], visible=True) # Voice_Vision_00001725
        self.set_conversation(type=2, spawnId=11001560, script='$63000027_CS__MISTERY01__1$', arg4=5) # Voice 00001725
        self.set_skip(state=VisionTalk04)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return VisionTalk02(self.ctx)


class VisionTalk02(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()

    def on_tick(self) -> common.Trigger:
        if self.true():
            return VisionTalk03(self.ctx)


class VisionTalk03(common.Trigger):
    def on_enter(self):
        self.set_conversation(type=2, spawnId=11001560, script='$63000027_CS__MISTERY01__2$', arg4=5)
        self.set_skip(state=VisionTalk04)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=5000):
            return VisionTalk04(self.ctx)


class VisionTalk04(common.Trigger):
    def on_enter(self):
        self.remove_cinematic_talk()
        self.set_skip()
        self.destroy_monster(spawnIds=[101])
        self.create_monster(spawnIds=[102], animationEffect=False)
        self.select_camera(triggerId=601, enable=False)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return VisionTalk05(self.ctx)


class VisionTalk05(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=500):
            return FirstQuestEnd01(self.ctx)


class FirstQuestEnd01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=10034010, textId=10034010) # 가이드 : 비전을 향해 이동하기

    def on_tick(self) -> common.Trigger:
        if self.user_detected(boxIds=[9100]):
            return FirstQuestEnd02(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10034010)


class FirstQuestEnd02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=10034020, textId=10034020) # 가이드 : [[icon:questcomplete]] 비전과 대화하기

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000450], questStates=[3]):
            return SecondQuestStart01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10034020)


class SecondQuestStart01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5000], visible=True) # 가이드 서머리 사운드 이펙트
        self.show_guide_summary(entityId=10034030, textId=10034030) # 가이드 : [[icon:questaccept]] 비전과 대화하기

    def on_tick(self) -> common.Trigger:
        if self.quest_user_detected(boxIds=[9900], questIds=[90000451], questStates=[1]):
            return TimeToLeave01(self.ctx)

    def on_exit(self):
        self.hide_guide_summary(entityId=10034030)


class TimeToLeave01(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.select_camera(triggerId=700, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=250):
            return TimeToLeave02(self.ctx)


class TimeToLeave02(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[102])
        self.create_monster(spawnIds=[103], animationEffect=False)
        self.move_user(mapId=63000027, portalId=10, boxId=9900)
        self.set_scene_skip(state=VisionSayGoodbye04, action='exit')

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=250):
            return TimeToLeave03(self.ctx)


class TimeToLeave03(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=701, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return PCGetEffect01(self.ctx)


class PCGetEffect01(common.Trigger):
    def on_enter(self):
        self.add_buff(boxIds=[9900], skillId=70000097, level=1) # 신비로운 힘
        self.set_effect(triggerIds=[5500], visible=True) # Sound_VisionBuff

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return VisionSayGoodbye01(self.ctx)


class VisionSayGoodbye01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5402], visible=True) # Voice_Vision_00001872
        self.set_conversation(type=1, spawnId=103, script='$63000027_CS__MISTERY01__3$', arg4=4, arg5=0) # Voice 00001872

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=4000):
            return VisionSayGoodbye02(self.ctx)


class VisionSayGoodbye02(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5401], visible=True) # Voice_Vision_00001741
        self.set_conversation(type=1, spawnId=103, script='$63000027_CS__MISTERY01__4$', arg4=4, arg5=0) # Voice 00001741
        self.set_conversation(type=1, spawnId=103, script='$63000027_CS__MISTERY01__5$', arg4=3, arg5=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=6000):
            return VisionSayGoodbye03(self.ctx)


class VisionSayGoodbye03(common.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=103, patrolName='MS2PatrolData_102')
        self.set_scene_skip()

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return VisionSayGoodbye04(self.ctx)


class VisionSayGoodbye04(common.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[103])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=1000):
            return Collapse01(self.ctx)


class Collapse01(common.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[5200], visible=True) # VibrateLong
        self.select_camera(triggerId=710, enable=True)
        self.set_mesh(triggerIds=[3100], visible=True, arg3=0, delay=0, scale=0) # barrier
        self.set_mesh(triggerIds=[3101], visible=True, arg3=0, delay=0, scale=0) # barrier
        self.set_mesh(triggerIds=[3102], visible=True, arg3=0, delay=0, scale=0) # barrier
        self.set_mesh(triggerIds=[3103], visible=True, arg3=0, delay=0, scale=0) # barrier
        self.set_user_value(triggerId=2, key='CollapseStart', value=1)
        self.set_effect(triggerIds=[5300], visible=True) # Sound_SpaceDestroy

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='ZoomIn', value=1):
            return Collapse02(self.ctx)


class Collapse02(common.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=711, enable=True)

    def on_tick(self) -> common.Trigger:
        if self.user_value(key='CollapseEnd', value=1):
            return PCFainted01(self.ctx)


class PCFainted01(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Down2_A','Down_Idle_A'])

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2667):
            return PCTeleport01(self.ctx)


class PCTeleport01(common.Trigger):
    def on_enter(self):
        self.set_pc_emotion_loop(sequenceName='Down_Idle_A', duration=10000)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> common.Trigger:
        if self.wait_tick(waitTick=2000):
            return PCTeleport02(self.ctx)


class PCTeleport02(common.Trigger):
    def on_enter(self):
        self.move_user(mapId=63000028, portalId=1, boxId=9900)
        self.select_camera(triggerId=711, enable=False)

    def on_tick(self) -> common.Trigger:
        if not self.user_detected(boxIds=[9900]):
            return Quit(self.ctx)


class Quit(common.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = Wait
