""" trigger/52010061_qd/main.xml """
from common import *
import state


#  룬블레이더 떡밥 
# 
# 11003843 - 렌듀비앙(101)
# 11003844 - 유페리아(102)
# 11003845 - 이슈라(104)
# 11003846 - 레잔(103)
# 
class 입장(state.State):
    def on_tick(self) -> state.State:
        if quest_user_detected(boxIds=[6001], questIds=[91000076], questStates=[3]):
            return 칼리브해안전경()
        if not quest_user_detected(boxIds=[6001], questIds=[91000076], questStates=[3]):
            return 맵이동()


class 칼리브해안전경(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        visible_my_pc(isVisible=False) # 유저안보이게

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 칼리브해안전경_02()


class 칼리브해안전경_02(state.State):
    def on_enter(self):
        set_scene_skip(state=종료_02, arg2='exit')
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[4001,4002], returnView=False) # 전경비추는카메라

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 칼리브해안전경_03()


class 칼리브해안전경_03(state.State):
    def on_enter(self):
        show_caption(type='VerticalCaption', title='$52010061_QD__main__0$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=2800, scale=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1800):
            return 교역선비추기()


class 교역선비추기(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 스폰조절()


class 스폰조절(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False, arg3=0) # 렌듀비앙
        create_monster(spawnIds=[102], arg2=False, arg3=0) # 유페리아
        create_monster(spawnIds=[103], arg2=False, arg3=0) # 레잔

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 교역선비추기_02()


class 교역선비추기_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[4003,4005], returnView=False) # 교역선비추는카메라

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 레잔대사_01()


class 레잔대사_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4008], returnView=False)
        set_npc_emotion_loop(spawnId=103, sequenceName='Talk_A', duration=4000)
        add_cinematic_talk(npcId=11003846, msg='$52010061_QD__main__1$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 레잔대사_02()


class 레잔대사_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003], returnView=False)
        add_cinematic_talk(npcId=11003846, msg='$52010061_QD__main__2$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 유페리아대사_01()


class 유페리아대사_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4009], returnView=False)
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=6000)
        add_cinematic_talk(npcId=11003844, illustId='Yuperia_normal', msg='$52010061_QD__main__3$', duration=4800, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 랜듀비앙대사_01()


class 랜듀비앙대사_01(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=5000)
        select_camera_path(pathIds=[4005], returnView=False)
        add_cinematic_talk(npcId=11001567, illustId='Renduebian_normal', msg='$52010061_QD__main__4$', duration=4800, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 랜듀비앙대사_02()


class 랜듀비앙대사_02(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4000)
        select_camera_path(pathIds=[4005], returnView=False)
        add_cinematic_talk(npcId=11001567, illustId='Renduebian_normal', msg='$52010061_QD__main__5$', duration=3800, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 유페리아대사_02()


class 유페리아대사_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4009], returnView=False)
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_A', duration=4000)
        add_cinematic_talk(npcId=11003844, illustId='Yuperia_normal', msg='$52010061_QD__main__6$', duration=3800, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 랜듀비앙대사_03()


class 랜듀비앙대사_03(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=101, sequenceName='Talk_A', duration=4000)
        select_camera_path(pathIds=[4010], returnView=False)
        add_cinematic_talk(npcId=11001567, illustId='Renduebian_normal', msg='$52010061_QD__main__7$', duration=3800, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 이슈라등장()


class 이슈라등장(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 이슈라등장_02()


class 이슈라등장_02(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11001975, msg='$52010061_QD__main__8$', duration=4000)
        create_monster(spawnIds=[104], arg2=False, arg3=0) # 이슈라

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 이슈라등장_03()


class 이슈라등장_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4006,4007], returnView=False)
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 이슈라대사()


class 이슈라대사(state.State):
    def on_enter(self):
        set_npc_emotion_loop(spawnId=104, sequenceName='Talk_A', duration=4000)
        add_cinematic_talk(npcId=11003845, illustId='Ishura_normal', msg='$52010061_QD__main__9$', duration=3000, align='left')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 이슈라모션()


class 이슈라모션(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=104, sequenceName='RuneBlader_Bore_A') # 이 후 새로운 모션으로 수정

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 종료_02()


class 종료_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=300, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return UI초기화()


class UI초기화(state.State):
    def on_enter(self):
        visible_my_pc(isVisible=True)
        destroy_monster(spawnIds=[101])
        destroy_monster(spawnIds=[102])
        destroy_monster(spawnIds=[103])
        destroy_monster(spawnIds=[104])
        reset_camera(interpolationTime=2)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 맵이동()


class 맵이동(state.State):
    def on_enter(self):
        move_user(mapId=2000422) # 스카이 포트리스 함교로 텔레포트

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return ()


class (state.State):
    pass


