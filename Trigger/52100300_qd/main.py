""" trigger/52100300_qd/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990002, key='Spawn', value=0)
        set_user_value(triggerId=99990003, key='RandomBomb', value=0)
        set_user_value(triggerId=99990004, key='Laser', value=0)
        set_portal(portalId=1, visible=False, enabled=False, minimapVisible=False)
        set_portal(portalId=3, visible=False, enabled=False, minimapVisible=False)
        set_interact_object(triggerIds=[10002185], state=0) # 엘리베이터 발판
        enable_spawn_point_pc(spawnId=100, isEnable=True) # <시작 위치 세팅>
        enable_spawn_point_pc(spawnId=101, isEnable=False)
        enable_spawn_point_pc(spawnId=102, isEnable=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[901]):
            return 연출시작()


# 연출시작
class 연출시작(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_cinematic_ui(type=1)
        move_user(mapId=52100300, portalId=5001)
        create_monster(spawnIds=[351])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출시작_2()


class 연출시작_2(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[4004,4005], returnView=False)
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2900):
            return 연출시작_2_02()


class 연출시작_2_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4006,4007], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 연출시작_2_03()


class 연출시작_2_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출시작_3()


class 연출시작_3(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[4001,4002], returnView=False)
        show_caption(type='VerticalCaption', title='$52100300_QD__MAIN__12$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 연출시작_4()


class 연출시작_4(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003], returnView=False)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=0, msg='$52100300_QD__MAIN__13$', duration=3500)
        add_cinematic_talk(npcId=11004682, illustId='11004022', align='right', msg='$52100300_QD__MAIN__14$', duration=3500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 연출시작_5()


class 연출시작_5(state.State):
    def on_enter(self):
        move_npc(spawnId=351, patrolName='MS2PatrolData_3001')
        add_cinematic_talk(npcId=11004682, illustId='11004022', align='right', msg='$52100300_QD__MAIN__15$', duration=3500)
        add_cinematic_talk(npcId=0, msg='$52100300_QD__MAIN__16$', duration=3500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 연출시작_6()


class 연출시작_6(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        destroy_monster(spawnIds=[351], arg2=False)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출시작_7()


class Skip_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        destroy_monster(spawnIds=[351])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 연출시작_7()


class 연출시작_7(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=0)
        set_portal(portalId=3, visible=True, enabled=True, minimapVisible=True)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[902]):
            set_event_ui(type=1, arg2='$52100300_QD__MAIN__0$', arg3='5000')
            create_monster(spawnIds=[101,102,103], arg2=False)
            return 추가대사_01()


class 추가대사_01(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            set_user_value(triggerId=99990004, key='Laser', value=1)
            side_npc_talk(type='talk', npcId=29500101, illust='ArcheonBlack_Normal', script='$52100300_QD__MAIN__1$', duration=5000)
            return 추가대사_02()


class 추가대사_02(state.State):
    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102,103]):
            side_npc_talk(type='talk', npcId=29000170, illust='ArcaneBlader_normal', script='$52100300_QD__MAIN__2$', duration=5000)
            return 추가대사_03()


class 추가대사_03(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            side_npc_talk(type='talk', npcId=11003536, illust='Neirin_normal', script='$52100300_QD__MAIN__3$', duration=5000)
            return 엘리베이터_체크()


class 엘리베이터_체크(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            side_npc_talk(type='talk', npcId=29000170, illust='ArcaneBlader_normal', script='$52100300_QD__MAIN__4$', duration=5000)
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
        set_event_ui(type=1, arg2='$52100300_QD__MAIN__5$', arg3='5000')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[711]):
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
        enable_spawn_point_pc(spawnId=100, isEnable=False) # <시작 위치 세팅>
        enable_spawn_point_pc(spawnId=101, isEnable=True)
        enable_spawn_point_pc(spawnId=102, isEnable=False)

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
        side_npc_talk(type='talk', npcId=29000170, illust='ArcaneBlader_unfair', script='$52100300_QD__MAIN__6$', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 추가대사_04()


class 추가대사_04(state.State):
    def on_enter(self):
        set_user_value(triggerId=99990002, key='Spawn', value=1)
        set_mesh(triggerIds=[2001,2002,2003,2004], visible=False)
        set_mesh(triggerIds=[30000,30010,30020,30030], visible=False)
        side_npc_talk(type='talk', npcId=29500101, illust='ArcheonBlack_Normal', script='$52100300_QD__MAIN__7$', duration=5000)

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
        side_npc_talk(type='talk', npcId=29500101, illust='ArcheonBlack_Normal', script='$52100300_QD__MAIN__8$', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 추가대사_05()


class 추가대사_05(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=29000170, illust='ArcaneBlader_normal', script='$52100300_QD__MAIN__9$', duration=5000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 추가대사_06()


class 추가대사_06(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=11003536, illust='Neirin_normal', script='$52100300_QD__MAIN__10$', duration=5000)

    def on_tick(self) -> state.State:
        if user_value(key='RandomBombEnd', value=1):
            set_user_value(triggerId=99990004, key='Laser', value=0)
            return 보스전()


class 보스전(state.State):
    def on_enter(self):
        side_npc_talk(type='talk', npcId=29000170, illust='ArcaneBlader_normal', script='$52100300_QD__MAIN__11$', duration=5000)
        set_actor(triggerId=9002, visible=True, initialSequence='sf_fi_funct_darkdoor_A01_start')
        set_mesh(triggerIds=[3001], visible=False)
        set_portal(portalId=1, visible=True, enabled=True, minimapVisible=True)

    def on_tick(self) -> state.State:
        if true():
            return 종료()


class 종료(state.State):
    pass


