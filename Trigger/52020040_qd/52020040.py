""" trigger/52020040_qd/52020040.xml """
from common import *
import state


class wait_01(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2001]):
            return wait_02()


class wait_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_effect(triggerIds=[6000], visible=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return wait_03()


class wait_03(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101], arg2=False)
        create_monster(spawnIds=[102], arg2=False)
        create_monster(spawnIds=[103], arg2=False)
        create_monster(spawnIds=[104], arg2=False)
        create_monster(spawnIds=[105], arg2=False)
        set_cinematic_ui(type=1)
        move_user(mapId=52020040, portalId=1)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 크리티아스로()


class 크리티아스로(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_CameraMasking_FastFadeIn.xml')
        select_camera_path(pathIds=[4001,4002], returnView=False)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 크리티아스로_02()


class 크리티아스로_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4003,4004,4005], returnView=False)
        set_cinematic_ui(type=3)
        set_npc_emotion_loop(spawnId=102, sequenceName='Talk_B', duration=1E+11)
        add_cinematic_talk(npcId=11004434, illustId='Bliche_normal', align='left', msg='$52020040_QD__52020040__0$', duration=3000)
        add_cinematic_talk(npcId=11004437, illustId='Neirin_smile', align='right', msg='$52020040_QD__52020040__1$', duration=3000)
        add_cinematic_talk(npcId=11004434, illustId='Bliche_normal', align='left', msg='$52020040_QD__52020040__2$', duration=3000)
        set_scene_skip(state=Skip_1, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 크리티아스로_02_01()


class 크리티아스로_02_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4006], returnView=False)
        show_caption(type='HorizonCaption', title='$52020040_QD__52020040__3$', align='bottomLeft', offsetRateX=0, offsetRateY=0, duration=5000, scale=2.5)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 크리티아스로_03()


class 크리티아스로_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4007], returnView=False)
        add_cinematic_talk(npcId=11004436, illustId='Schatten_smile', align='left', msg='$52020040_QD__52020040__4$', duration=3000)
        add_cinematic_talk(npcId=11004438, illustId='Mason_closeEye', align='right', msg='$52020040_QD__52020040__5$', duration=3000)
        add_cinematic_talk(npcId=11004435, illustId='Conder_smile', align='left', msg='$52020040_QD__52020040__6$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=9000):
            return 크리티아스로_04()


class 크리티아스로_04(state.State):
    def on_enter(self):
        set_ambient_light(primary=[232,92,53])
        set_directional_light(diffuseColor=[41,21,18], specularColor=[130,130,130])
        add_cinematic_talk(npcId=11004435, illustId='Conder_normal', align='left', msg='$52020040_QD__52020040__7$', duration=2500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 경보()


class 경보(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=True)
        set_actor(triggerId=201, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=202, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=203, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=204, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=205, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=206, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=207, visible=True, initialSequence='sf_quest_light_A01_On')
        set_actor(triggerId=208, visible=True, initialSequence='sf_quest_light_A01_On')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 경보_01()


class 경보_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4008], returnView=False)
        add_cinematic_talk(npcId=11004437, illustId='Neirin_surprise', align='left', msg='$52020040_QD__52020040__8$', duration=2500)
        add_cinematic_talk(npcId=11004437, illustId='Neirin_surprise', align='left', msg='$52020040_QD__52020040__9$', duration=2800)
        add_cinematic_talk(npcId=11004434, illustId='Bliche_normal', align='right', msg='$52020040_QD__52020040__10$', duration=2800)
        add_cinematic_talk(npcId=11004437, illustId='Neirin_surprise', align='left', msg='$52020040_QD__52020040__11$', duration=2800)
        add_cinematic_talk(npcId=11004434, illustId='Bliche_normal', align='right', msg='$52020040_QD__52020040__12$', duration=2400)
        add_cinematic_talk(npcId=11004437, illustId='Neirin_surprise', align='left', msg='$52020040_QD__52020040__13$', duration=2800)
        add_cinematic_talk(npcId=11004434, illustId='Bliche_mad', align='right', msg='$52020040_QD__52020040__14$', duration=2800)
        add_cinematic_talk(npcId=11004437, illustId='Neirin_surprise', align='left', msg='$52020040_QD__52020040__15$', duration=2400)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=21300):
            return 경보_02()


class 경보_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4009,4010], returnView=False)
        set_effect(triggerIds=[6000], visible=False)
        add_cinematic_talk(npcId=11004440, msg='$52020040_QD__52020040__16$', duration=3000)
        add_cinematic_talk(npcId=11004440, msg='$52020040_QD__52020040__17$', duration=5000)
        add_cinematic_talk(npcId=11004440, msg='$52020040_QD__52020040__18$', duration=2600)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10200):
            return 경보끝_01()


class 경보끝_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_ambient_light(primary=[131,160,209])
        set_directional_light(diffuseColor=[134,160,143], specularColor=[130,130,130])
        set_actor(triggerId=201, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=202, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=203, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=204, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=205, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=206, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=207, visible=True, initialSequence='sf_quest_light_A01_Off')
        set_actor(triggerId=208, visible=True, initialSequence='sf_quest_light_A01_Off')
        add_cinematic_talk(npcId=11004435, illustId='Conder_normal', align='right', msg='$52020040_QD__52020040__19$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 경보끝_02_01()


class 경보끝_02_01(state.State):
    def on_enter(self):
        set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 경보끝_02_02()


class 경보끝_02_02(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 경보끝_02()


class 경보끝_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4012], returnView=False)
        add_cinematic_talk(npcId=11004437, illustId='Neirin_surprise', align='left', msg='$52020040_QD__52020040__20$', duration=2800)
        add_cinematic_talk(npcId=11004437, illustId='Neirin_surprise', align='left', msg='$52020040_QD__52020040__21$', duration=2800)
        add_cinematic_talk(npcId=11004437, illustId='Neirin_surprise', align='left', msg='$52020040_QD__52020040__22$', duration=3000)
        add_cinematic_talk(npcId=11004434, illustId='Bliche_normal', align='right', msg='$52020040_QD__52020040__23$', duration=3000)
        add_cinematic_talk(npcId=11004434, illustId='Bliche_normal', align='right', msg='$52020040_QD__52020040__24$', duration=3000)
        add_cinematic_talk(npcId=11004437, illustId='Neirin_surprise', align='left', msg='$52020040_QD__52020040__25$', duration=3000)
        add_cinematic_talk(npcId=11004435, illustId='Conder_normal', align='right', msg='$52020040_QD__52020040__26$', duration=3000)
        add_cinematic_talk(npcId=11004436, illustId='Schatten_surprise', align='left', msg='$52020040_QD__52020040__27$', duration=3000)
        add_cinematic_talk(npcId=11004435, illustId='Conder_normal', align='right', msg='$52020040_QD__52020040__28$', duration=2500)
        add_cinematic_talk(npcId=11004438, illustId='Mason_normal', align='left', msg='$52020040_QD__52020040__29$', duration=3000)
        add_cinematic_talk(npcId=11004434, illustId='Bliche_normal', align='right', msg='$52020040_QD__52020040__30$', duration=2500)
        add_cinematic_talk(npcId=11004434, illustId='Bliche_normal', align='right', msg='$52020040_QD__52020040__31$', duration=3000)
        add_cinematic_talk(npcId=11004438, illustId='Mason_normal', align='left', msg='$52020040_QD__52020040__32$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52020040_QD__52020040__33$', duration=2500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=37800):
            return 경보끝_03()


class 경보끝_03(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4011,4013], returnView=False)
        # <action name="SetPcEmotionLoop" arg1="Talk_A" arg2="9999999999999" />
        add_cinematic_talk(npcId=11004438, illustId='Mason_normal', msg='$52020040_QD__52020040__34$', align='left', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52020040_QD__52020040__35$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52020040_QD__52020040__36$', duration=3000)
        add_cinematic_talk(npcId=11004436, illustId='Schatten_surprise', align='left', msg='$52020040_QD__52020040__37$', duration=3500)
        add_cinematic_talk(npcId=11004437, illustId='Neirin_normal', align='right', msg='$52020040_QD__52020040__38$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52020040_QD__52020040__39$', duration=3000)
        add_cinematic_talk(npcId=11004434, illustId='Bliche_closeEye', align='left', msg='$52020040_QD__52020040__40$', duration=2800)
        add_cinematic_talk(npcId=11004437, illustId='Neirin_normal', align='right', msg='$52020040_QD__52020040__41$', duration=3000)
        add_cinematic_talk(npcId=11004434, illustId='Bliche_closeEye', align='left', msg='$52020040_QD__52020040__42$', duration=3000)
        add_cinematic_talk(npcId=11004434, illustId='Bliche_normal', align='left', msg='$52020040_QD__52020040__43$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52020040_QD__52020040__44$', duration=3000)
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=33200):
            return 이동()


class Skip_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 이동_02()


class 이동(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 이동_02()


class 이동_02(state.State):
    def on_enter(self):
        move_user(mapId=2020029, portalId=2)


