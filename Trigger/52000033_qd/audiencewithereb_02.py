""" trigger/52000033_qd/audiencewithereb_02.xml """
from common import *
import state


class idle(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[60100010], questStates=[1]):
            return ready()


class ready(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52000033, portalId=10)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return pcmove()


class pcmove(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1) # 보험용
        set_cinematic_ui(type=3) # 보험용
        move_user_path(patrolName='MS2PatrolData_1004')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return ErebTalk_01()


class ErebTalk_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[700], returnView=False) # 에레브 얼굴로 클로즈업
        add_cinematic_talk(npcId=11001663, msg='$52000033_QD__AUDIENCEWITHEREB_02__0$', duration=5000)
        set_scene_skip(state=end, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return ErebTalk_02()


class ErebTalk_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[901], returnView=False) # 에레브 얼굴로 클로즈업
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11001663, msg='$52000033_QD__AUDIENCEWITHEREB_02__1$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Erebintroduce()


class Erebintroduce(state.State):
    def on_enter(self):
        show_caption(scale=2.3, type='NameCaption', title='$52000033_QD__AUDIENCEWITHEREB_02__18$', desc='$52000033_QD__AUDIENCEWITHEREB_02__19$', align='centerLeft', offsetRateX=-0.15, duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return ErebTalk_03()


class ErebTalk_03(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11001663, msg='$52000033_QD__AUDIENCEWITHEREB_02__2$', duration=3000)
        add_cinematic_talk(npcId=11001663, msg='$52000033_QD__AUDIENCEWITHEREB_02__3$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return Kaltalk_01()


class Kaltalk_01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11001665, msg='$52000033_QD__AUDIENCEWITHEREB_02__4$', duration=3000, illustId='Karl_normal', align='Left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return Kaltalk_02()


class Kaltalk_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[902], returnView=False) # 칼 얼굴로 클로즈업
        set_npc_emotion_sequence(spawnId=301, sequenceName='Talk_A')
        add_cinematic_talk(npcId=11001665, msg='$52000033_QD__AUDIENCEWITHEREB_02__5$', duration=3000)
        add_cinematic_talk(npcId=11001665, msg='$52000033_QD__AUDIENCEWITHEREB_02__6$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return kaltroduce()


class kaltroduce(state.State):
    def on_enter(self):
        show_caption(scale=2.3, type='NameCaption', title='$52000033_QD__AUDIENCEWITHEREB_02__20$', desc='$52000033_QD__AUDIENCEWITHEREB_02__21$', align='centerLeft', offsetRateX=-0.15, duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return talk_01()


class talk_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[601], returnView=False) # 뒷 뷰
        add_cinematic_talk(npcId=11001663, illustId='Ereb_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__7$', duration=1000, delayTick=0, align='left') # 에레브
        add_cinematic_talk(npcId=11001665, illustId='Karl_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__8$', duration=3000, delayTick=0, align='right') # 칼

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return talk_02()


class talk_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11001666, illustId='Fray_serious', msg='$52000033_QD__AUDIENCEWITHEREB_02__9$', duration=3000, delayTick=3, align='center')
        add_cinematic_talk(npcId=11001663, illustId='Ereb_closeEye', msg='$52000033_QD__AUDIENCEWITHEREB_02__10$', duration=1000, delayTick=0, align='left') # 에레브
        add_cinematic_talk(npcId=11001665, illustId='Karl_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__11$', duration=1000, delayTick=0, align='right') # 칼

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6649):
            return talk_03()


class talk_03(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11001666, illustId='Fray_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__12$', duration=3000, align='Right')
        add_cinematic_talk(npcId=11001666, illustId='Fray_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__13$', duration=3000, align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return talk_04()


class talk_04(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11001666, illustId='Fray_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__14$', duration=3000, align='Right')
        add_cinematic_talk(npcId=11001666, illustId='Fray_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__15$', duration=3000, align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return talk_05()


class talk_05(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11001663, illustId='Ereb_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__16$', duration=3000, delayTick=0, align='left') # 에레브
        add_cinematic_talk(npcId=11001665, illustId='Karl_normal', msg='$52000033_QD__AUDIENCEWITHEREB_02__17$', duration=3000, delayTick=3, align='right') # 칼
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return end()


class end(state.State):
    def on_enter(self):
        set_achievement(triggerId=9001, type='trigger', achieve='AudienceWithEreb')
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)

    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[9001], questIds=[60100010], questStates=[1]):
            return end()


