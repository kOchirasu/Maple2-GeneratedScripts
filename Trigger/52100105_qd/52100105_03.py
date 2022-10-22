""" trigger/52100105_qd/52100105_03.xml """
from common import *
import state


class Ready(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=False)
        set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[1000]):
            return 퀘스트체크()


class 퀘스트체크(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[1000], questIds=[50101030], questStates=[3]):
            return 시작암전1()
        if quest_user_detected(boxIds=[1000], questIds=[50101030], questStates=[2]):
            return 연출끝()
        if quest_user_detected(boxIds=[1000], questIds=[50101030], questStates=[1]):
            return 연출끝()


class 시작암전1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=False)
        set_effect(triggerIds=[601], visible=False)
        visible_my_pc(isVisible=False)
        set_onetime_effect(id=200, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 컷신1_1()


class 컷신1_1(state.State):
    def on_enter(self):
        set_effect(triggerIds=[601], visible=True)
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='Kritias_EpicCutScene07_01.swf', movieId=0)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='0'):
            return None # Missing State: 컷신1_2
        if wait_tick(waitTick=3000):
            return 몹소환1()


class 몹소환1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[500], arg2=False) # 클라디아
        create_monster(spawnIds=[1], arg2=False) # 의자
        create_monster(spawnIds=[400], arg2=False)
        create_monster(spawnIds=[401], arg2=False)
        create_monster(spawnIds=[402], arg2=False)
        create_monster(spawnIds=[403], arg2=False)
        create_monster(spawnIds=[404], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 인게임준비0()


class 인게임준비0(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_onetime_effect(id=200, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 투르카대사1()


class 투르카대사1(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[500], arg2=False)
        set_scene_skip(state=컷신3_1, arg2='nextState')
        select_camera_path(pathIds=[700,701], returnView=False)
        add_cinematic_talk(npcId=11004430, illustId='Turka_normal', msg='$52100105_QD__52100105_03__0$', duration=6000, align='Right')
        add_cinematic_talk(npcId=11004430, illustId='Turka_normal', msg='$52100105_QD__52100105_03__1$', duration=6000, align='Right')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 클라디아생성1()


class 클라디아생성1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[500], arg2=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 클라디아이동1()


class 클라디아이동1(state.State):
    def on_enter(self):
        move_npc(spawnId=500, patrolName='PatrolData_500_1')
        select_camera_path(pathIds=[703,704], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 클라디아대사1()


class 클라디아대사1(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=500, sequenceName='Talk_A', duration=8666)
        add_cinematic_talk(npcId=11004392, illustId='cladia_normal', msg='$52100105_QD__52100105_03__2$', duration=5000, align='left')
        add_cinematic_talk(npcId=11004392, illustId='cladia_angry', msg='$52100105_QD__52100105_03__3$', duration=5000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 투르카공격지시1()


class 투르카공격지시1(state.State):
    def on_enter(self):
        select_camera(triggerId=705, enable=True)
        add_cinematic_talk(npcId=11004430, illustId='Turka_normal', msg='$52100105_QD__52100105_03__4$', duration=3000, align='Right')
        set_npc_emotion_loop(spawnId=400, sequenceName='Bore_A', duration=1333)
        set_npc_emotion_loop(spawnId=500, sequenceName='Attack_Idle_A', duration=5333)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 암전1()


class 암전1(state.State):
    def on_enter(self):
        set_skip()
        move_npc(spawnId=401, patrolName='PatrolData_401_1')
        move_npc(spawnId=402, patrolName='PatrolData_402_1')
        move_npc(spawnId=403, patrolName='PatrolData_403_1')
        move_npc(spawnId=404, patrolName='PatrolData_404_1')
        set_onetime_effect(id=100, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 컷신3_1()


class 컷신3_1(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[401], arg2=False)
        destroy_monster(spawnIds=[402], arg2=False)
        destroy_monster(spawnIds=[403], arg2=False)
        destroy_monster(spawnIds=[404], arg2=False)
        destroy_monster(spawnIds=[500], arg2=False)
        create_widget(type='SceneMovie')
        widget_action(type='SceneMovie', func='Clear')
        play_scene_movie(fileName='Kritias_EpicCutScene07_02.swf', movieId=1)

    def on_tick(self) -> state.State:
        if widget_condition(type='SceneMovie', name='IsStop', condition='1'):
            return 클라디아생성2()
        if wait_tick(waitTick=12000):
            return 클라디아생성2()


class 클라디아생성2(state.State):
    def on_enter(self):
        create_monster(spawnIds=[500], arg2=False)
        move_npc(spawnId=500, patrolName='PatrolData_500_1')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 투르카도망1()


class 투르카도망1(state.State):
    def on_enter(self):
        set_scene_skip(state=연출끝, arg2='nextState')
        set_cinematic_ui(type=4)
        set_onetime_effect(id=100, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_npc_emotion_loop(spawnId=500, sequenceName='Attack_Idle_A', duration=5333)
        set_npc_emotion_loop(spawnId=400, sequenceName='Damg_A', duration=5333)
        select_camera(triggerId=706, enable=True)
        add_cinematic_talk(npcId=11004430, illustId='Turka_Broken_Hood', msg='$52100105_QD__52100105_03__5$', duration=4000, align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 투르카도망2()


class 투르카도망2(state.State):
    def on_enter(self):
        set_effect(triggerIds=[600], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 투르카도망3()


class 투르카도망3(state.State):
    def on_enter(self):
        move_npc(spawnId=400, patrolName='PatrolData_400_1')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 투르카도망4()


class 투르카도망4(state.State):
    def on_enter(self):
        select_camera(triggerId=707, enable=True)
        destroy_monster(spawnIds=[500], arg2=False)
        add_cinematic_talk(npcId=11004430, illustId='Turka_Broken_Hood', msg='$52100105_QD__52100105_03__6$', duration=5000, align='center')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 투르카도망5()


class 투르카도망5(state.State):
    def on_enter(self):
        set_onetime_effect(id=101, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출끝()


class 연출끝(state.State):
    def on_enter(self):
        set_skip()
        destroy_monster(spawnIds=[-1], arg2=False)
        set_effect(triggerIds=[600], visible=False)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=0)
        visible_my_pc(isVisible=True)
        set_onetime_effect(id=101, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        move_user(mapId=52100110, portalId=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return None # Missing State: 


