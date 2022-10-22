""" trigger/52010029_qd/main.xml """
from common import *
import state


#  치유의 숲 : 52010026  
#  들어오자마자 앉아있는 상태 연출 
class idle(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=False)
        set_effect(triggerIds=[5004], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[2001]):
            return black()


class black(state.State):
    def on_enter(self):
        set_onetime_effect(id=1, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return ready()


class ready(state.State):
    def on_enter(self):
        set_scene_skip(state=Skip_1, arg2='nextState')
        show_caption(type='VerticalCaption', title='$52010029_QD__MAIN__0$', desc='$52010029_QD__MAIN__1$', align='centerRight', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__2$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__3$', duration=3000)
        select_camera_path(pathIds=[4018,4003,4002,4019], returnView=False)
        move_user(mapId=52010029, portalId=6006)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 시작_원경을보여주자_02()


class 시작_원경을보여주자_02(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4016], returnView=False)
        create_monster(spawnIds=[406], arg2=True)
        create_monster(spawnIds=[407], arg2=True)
        create_monster(spawnIds=[405], arg2=True)
        create_monster(spawnIds=[408], arg2=True)
        create_monster(spawnIds=[409], arg2=True)
        create_monster(spawnIds=[410], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=100):
            return 시작_원경을보았으니이제시작하자()


class 시작_원경을보았으니이제시작하자(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user_path(patrolName='MS2PatrolData_3006')
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__4$', duration=2000)
        add_balloon_talk(spawnId=0, msg='$52010029_QD__MAIN__5$', duration=2000, delayTick=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 차전투시작_몬스터스폰1()


class 차전투시작_몬스터스폰1(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4015], returnView=False)
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__6$', duration=3000)
        add_balloon_talk(spawnId=406, msg='$52010029_QD__MAIN__7$', duration=2000, delayTick=0)
        add_balloon_talk(spawnId=407, msg='$52010029_QD__MAIN__8$', duration=2000, delayTick=0)
        set_npc_emotion_sequence(spawnId=405, sequenceName='Attack_01_A')
        set_npc_emotion_sequence(spawnId=408, sequenceName='Attack_01_B')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 차전투시작_몬스터스폰_02_1()


class 차전투시작_몬스터스폰_02_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4016], returnView=False)
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=10000)
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__9$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__10$', duration=3000)
        destroy_monster(spawnIds=[405])
        destroy_monster(spawnIds=[406])
        destroy_monster(spawnIds=[407])
        destroy_monster(spawnIds=[408])
        destroy_monster(spawnIds=[409])
        destroy_monster(spawnIds=[410])
        create_monster(spawnIds=[501], arg2=True)
        create_monster(spawnIds=[401], arg2=True)
        create_monster(spawnIds=[402], arg2=True)
        create_monster(spawnIds=[403], arg2=True)
        create_monster(spawnIds=[404], arg2=True)
        create_monster(spawnIds=[703], arg2=True)
        set_npc_emotion_loop(spawnId=501, sequenceName='Stun_A', duration=16000000)
        set_npc_emotion_loop(spawnId=703, sequenceName='Stun_A', duration=16000000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 차전투시작_몬스터스폰_black1()


class 차전투시작_몬스터스폰_black1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_effect(triggerIds=[5001], visible=True)
        set_effect(triggerIds=[5002], visible=True)
        select_camera_path(pathIds=[4008], returnView=False)
        show_caption(type='VerticalCaption', title='$52010029_QD__MAIN__11$', desc='$52010029_QD__MAIN__12$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)
        add_cinematic_talk(npcId=11003392, msg='$52010029_QD__MAIN__13$', duration=3000)
        set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_effect(triggerIds=[5001], visible=True)
        set_ambient_light(primary=[128,128,128])
        add_balloon_talk(spawnId=401, msg='$52010029_QD__MAIN__14$', duration=3000, delayTick=0)
        add_balloon_talk(spawnId=402, msg='$52010029_QD__MAIN__15$', duration=3500, delayTick=0)
        add_cinematic_talk(npcId=11003392, msg='$52010029_QD__MAIN__16$', duration=3500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 시작_괴롭힘당하는바야르_02()


class 시작_괴롭힘당하는바야르_02(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4005], returnView=False)
        add_cinematic_talk(npcId=11003391, msg='$52010029_QD__MAIN__17$', duration=3000)
        set_npc_emotion_loop(spawnId=703, sequenceName='Stun_A', duration=16000000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 시작_괴롭힘당하는바야르_02_01()


class 시작_괴롭힘당하는바야르_02_01(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003397, msg='$52010029_QD__MAIN__18$', duration=4000)
        add_cinematic_talk(npcId=11003391, msg='$52010029_QD__MAIN__19$', duration=4000)
        create_monster(spawnIds=[701], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 시작_괴롭힘당하는바야르_03()


class 시작_괴롭힘당하는바야르_03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4007], returnView=False)
        move_npc(spawnId=701, patrolName='MS2PatrolData_3001')
        add_cinematic_talk(npcId=11003431, msg='$52010029_QD__MAIN__20$', duration=3000)
        show_caption(type='VerticalCaption', title='$52010029_QD__MAIN__21$', desc='$52010029_QD__MAIN__22$', align='centerLeft', offsetRateX=0, offsetRateY=0, duration=3000, scale=2)
        add_cinematic_talk(npcId=11003431, msg='$52010029_QD__MAIN__23$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 시작_괴롭힘당하는바야르_03_01()


class 시작_괴롭힘당하는바야르_03_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_npc_emotion_sequence(spawnId=701, sequenceName='Attack_01_D')
        add_cinematic_talk(npcId=11003431, msg='$52010029_QD__MAIN__24$', duration=4000)
        add_cinematic_talk(npcId=11003431, msg='$52010029_QD__MAIN__25$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 시작_괴롭힘당하는바야르_04()


class 시작_괴롭힘당하는바야르_04(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4005], returnView=False)
        set_npc_emotion_loop(spawnId=703, sequenceName='Down_Idle_A', duration=16000000)
        add_cinematic_talk(npcId=11003391, msg='$52010029_QD__MAIN__26$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 시작_괴롭힘당하는바야르_05()


class 시작_괴롭힘당하는바야르_05(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4016], returnView=False)
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__27$', duration=3000)
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=3500)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 차전투시작_01_1()


class 차전투시작_01_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=1)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 차전투시작_02_1()


class 차전투시작_02_1(state.State):
    def on_enter(self):
        set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_local_camera(cameraId=4014, enable=True)
        create_monster(spawnIds=[605], arg2=True) # 악당Mob_1
        create_monster(spawnIds=[606], arg2=True) # 악당Mob_2
        create_monster(spawnIds=[607], arg2=True) # 악당Mob_3
        create_monster(spawnIds=[608], arg2=True) # 악당Mob_4
        create_monster(spawnIds=[613], arg2=True) # 악당Mob_5
        create_monster(spawnIds=[614], arg2=True) # 악당Mob_6
        destroy_monster(spawnIds=[701])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 차전투시작_02_1_1()


class 차전투시작_02_1_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 차전투시작_03_1()


class Skip_1(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        set_effect(triggerIds=[5001], visible=True)
        set_effect(triggerIds=[5002], visible=True)
        set_local_camera(cameraId=4014, enable=True)
        destroy_monster(spawnIds=[405])
        destroy_monster(spawnIds=[406])
        destroy_monster(spawnIds=[407])
        destroy_monster(spawnIds=[408])
        destroy_monster(spawnIds=[409])
        destroy_monster(spawnIds=[410])
        destroy_monster(spawnIds=[605], arg2=True) # 악당Mob_1
        destroy_monster(spawnIds=[606], arg2=True) # 악당Mob_2
        destroy_monster(spawnIds=[607], arg2=True) # 악당Mob_3
        destroy_monster(spawnIds=[608], arg2=True) # 악당Mob_4
        destroy_monster(spawnIds=[613], arg2=True) # 악당Mob_5
        destroy_monster(spawnIds=[614], arg2=True) # 악당Mob_6
        create_monster(spawnIds=[501], arg2=True)
        create_monster(spawnIds=[401], arg2=True)
        create_monster(spawnIds=[402], arg2=True)
        create_monster(spawnIds=[403], arg2=True)
        create_monster(spawnIds=[404], arg2=True)
        create_monster(spawnIds=[703], arg2=True)
        create_monster(spawnIds=[605], arg2=True) # 악당Mob_1
        create_monster(spawnIds=[606], arg2=True) # 악당Mob_2
        create_monster(spawnIds=[607], arg2=True) # 악당Mob_3
        create_monster(spawnIds=[608], arg2=True) # 악당Mob_4
        create_monster(spawnIds=[613], arg2=True) # 악당Mob_5
        create_monster(spawnIds=[614], arg2=True) # 악당Mob_6
        destroy_monster(spawnIds=[701])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 차전투시작_03_1()


class 차전투시작_03_1(state.State):
    def on_enter(self):
        add_balloon_talk(spawnId=605, msg='$52010029_QD__MAIN__28$', duration=2000, delayTick=1000)
        add_balloon_talk(spawnId=606, msg='$52010029_QD__MAIN__29$', duration=2000, delayTick=1500)
        set_npc_emotion_loop(spawnId=501, sequenceName='Stun_A', duration=16000000)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_event_ui(type=1, arg2='$52010029_QD__MAIN__30$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[605,606,607,608,613,614]):
            return 차전투시작_01_2()


class 차전투시작_01_2(state.State):
    def on_enter(self):
        set_onetime_effect(id=3, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        create_monster(spawnIds=[702], arg2=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        destroy_monster(spawnIds=[701])
        destroy_monster(spawnIds=[605])
        destroy_monster(spawnIds=[606])
        destroy_monster(spawnIds=[607])
        destroy_monster(spawnIds=[608])
        destroy_monster(spawnIds=[613])
        destroy_monster(spawnIds=[614])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 차전투시작_02_2()


class 차전투시작_02_2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52010029, portalId=6002)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 차전투시작_02_01_2()


class 차전투시작_02_01_2(state.State):
    def on_enter(self):
        set_local_camera(cameraId=4014, enable=False)
        select_camera_path(pathIds=[4001], returnView=False)
        set_onetime_effect(id=3, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_scene_skip(state=Skip_2, arg2='nextState')
        move_user_path(patrolName='MS2PatrolData_3002')
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__31$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 차전투시작_02_01_01_2()


class 차전투시작_02_01_01_2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4004], returnView=False)
        set_npc_emotion_loop(spawnId=703, sequenceName='Stun_A', duration=16000000)
        add_cinematic_talk(npcId=11003431, msg='$52010029_QD__MAIN__32$', duration=3000)
        add_cinematic_talk(npcId=11003431, msg='$52010029_QD__MAIN__33$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 차전투시작_02_02_2()


class 차전투시작_02_02_2(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003431, msg='$52010029_QD__MAIN__34$', duration=3000)
        set_npc_emotion_sequence(spawnId=702, sequenceName='Attack_01_D')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 차전투시작_02_03_2()


class 차전투시작_02_03_2(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003431, msg='$52010029_QD__MAIN__35$', duration=3000)
        set_npc_emotion_sequence(spawnId=501, sequenceName='Attack_01_J')
        move_user(mapId=52010029, portalId=6001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 차전투시작_02_04_2()


class 차전투시작_02_04_2(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003431, msg='$52010029_QD__MAIN__36$', duration=3000)
        set_npc_emotion_sequence(spawnId=501, sequenceName='Attack_01_E')
        set_npc_emotion_sequence(spawnId=702, sequenceName='Attack_01_E')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 차전투시작_03_2()


class 차전투시작_03_2(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4013], returnView=False)
        create_monster(spawnIds=[601], arg2=True)
        create_monster(spawnIds=[602], arg2=True)
        create_monster(spawnIds=[603], arg2=True)
        create_monster(spawnIds=[604], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 차전투시작_03_1_2()


class 차전투시작_03_1_2(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 차전투시작_04_2()


class Skip_2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        move_user(mapId=52010029, portalId=6001)
        destroy_monster(spawnIds=[601])
        destroy_monster(spawnIds=[602])
        destroy_monster(spawnIds=[603])
        destroy_monster(spawnIds=[604])
        create_monster(spawnIds=[601], arg2=True)
        create_monster(spawnIds=[602], arg2=True)
        create_monster(spawnIds=[603], arg2=True)
        create_monster(spawnIds=[604], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 차전투시작_04_2()


class 차전투시작_04_2(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        reset_camera(interpolationTime=1)
        set_event_ui(type=1, arg2='$52010029_QD__MAIN__37$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[601,602,603,604]):
            return 차전투종료2()


class 차전투종료2(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52010029, portalId=6001)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 차전투종료직후2()


class 차전투종료직후2(state.State):
    def on_enter(self):
        set_onetime_effect(id=4, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        destroy_monster(spawnIds=[601])
        destroy_monster(spawnIds=[602])
        destroy_monster(spawnIds=[603])
        destroy_monster(spawnIds=[604])
        set_scene_skip(state=Skip_3, arg2='nextState')
        select_camera_path(pathIds=[4004], returnView=False)
        set_npc_emotion_loop(spawnId=501, sequenceName='Stun_A', duration=16000000)
        add_cinematic_talk(npcId=11003431, msg='$52010029_QD__MAIN__38$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 차전투종료_01_2()


class 차전투종료_01_2(state.State):
    def on_enter(self):
        add_cinematic_talk(npcId=11003431, msg='$52010029_QD__MAIN__39$', duration=3000)
        set_npc_emotion_sequence(spawnId=702, sequenceName='Attack_01_C')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 차전투시작_01_3()


class 차전투시작_01_3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[609], arg2=True)
        create_monster(spawnIds=[610], arg2=True)
        create_monster(spawnIds=[611], arg2=True)
        create_monster(spawnIds=[612], arg2=True)
        create_monster(spawnIds=[616], arg2=True)
        create_monster(spawnIds=[617], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 차전투시작_01_1_3()


class 차전투시작_01_1_3(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 차전투시작_02_3()


class Skip_3(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        destroy_monster(spawnIds=[609])
        destroy_monster(spawnIds=[610])
        destroy_monster(spawnIds=[611])
        destroy_monster(spawnIds=[612])
        destroy_monster(spawnIds=[616])
        destroy_monster(spawnIds=[617])
        create_monster(spawnIds=[609], arg2=True)
        create_monster(spawnIds=[610], arg2=True)
        create_monster(spawnIds=[611], arg2=True)
        create_monster(spawnIds=[612], arg2=True)
        create_monster(spawnIds=[616], arg2=True)
        create_monster(spawnIds=[617], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 차전투시작_02_3()


class 차전투시작_02_3(state.State):
    def on_enter(self):
        reset_camera(interpolationTime=1)
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_event_ui(type=1, arg2='$52010029_QD__MAIN__40$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[609,610,611,612,616,617]):
            return 차전투시작_02_직후3()


class 차전투시작_02_직후3(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        move_user(mapId=52010029, portalId=6003)
        set_scene_skip(state=Skip_4, arg2='nextState')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 차전투시작_01_4()


class 차전투시작_01_4(state.State):
    def on_enter(self):
        set_onetime_effect(id=5, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        select_camera_path(pathIds=[4011], returnView=False)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        destroy_monster(spawnIds=[609])
        destroy_monster(spawnIds=[610])
        destroy_monster(spawnIds=[611])
        destroy_monster(spawnIds=[612])
        destroy_monster(spawnIds=[616])
        destroy_monster(spawnIds=[617])
        move_user_path(patrolName='MS2PatrolData_3004')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 차전투시작_02_01_4()


class 차전투시작_02_01_4(state.State):
    def on_enter(self):
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=5000)
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__41$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 차전투시작_02_4()


class 차전투시작_02_4(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4004], returnView=False)
        add_cinematic_talk(npcId=11003431, msg='$52010029_QD__MAIN__42$', duration=4000)
        set_npc_emotion_sequence(spawnId=501, sequenceName='Attack_01_J')
        add_cinematic_talk(npcId=11003431, msg='$52010029_QD__MAIN__43$', duration=3000)
        add_cinematic_talk(npcId=11003392, msg='$52010029_QD__MAIN__44$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__45$', duration=2000)
        add_cinematic_talk(npcId=11003392, msg='$52010029_QD__MAIN__46$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__47$', duration=3000)
        set_onetime_effect(id=102, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_npc_emotion_sequence(spawnId=702, sequenceName='Attack_01_G')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=18000):
            return 차전투시작_03_4()


class 차전투시작_03_4(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4004], returnView=False)
        add_cinematic_talk(npcId=11003431, msg='$52010029_QD__MAIN__48$', duration=4000)
        add_cinematic_talk(npcId=11003431, msg='$52010029_QD__MAIN__49$', duration=4000)
        add_cinematic_talk(npcId=11003431, msg='$52010029_QD__MAIN__50$', duration=4000)
        set_npc_emotion_loop(spawnId=501, sequenceName='Stun_A', duration=16000000)
        destroy_monster(spawnIds=[401])
        destroy_monster(spawnIds=[402])
        destroy_monster(spawnIds=[403])
        destroy_monster(spawnIds=[404])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=8000):
            return 차전투시작_04_4()


class 차전투시작_04_4(state.State):
    def on_enter(self):
        set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        add_cinematic_talk(npcId=11003431, msg='$52010029_QD__MAIN__51$', duration=4000)
        set_effect(triggerIds=[5002], visible=False)
        set_effect(triggerIds=[5003], visible=True)
        set_effect(triggerIds=[5004], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=4000):
            return 차전투시작_05_4()


class 차전투시작_05_4(state.State):
    def on_enter(self):
        set_effect(triggerIds=[5001], visible=False)
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__52$', duration=2000)
        set_effect(triggerIds=[5003], visible=True)
        destroy_monster(spawnIds=[501])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 차전투시작_06_4()


class 차전투시작_06_4(state.State):
    def on_enter(self):
        set_npc_emotion_sequence(spawnId=501, sequenceName='Attack_02_E')
        set_onetime_effect(id=6, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_npc_emotion_loop(spawnId=703, sequenceName='Down_Idle_A', duration=16000000)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        destroy_monster(spawnIds=[702])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 차전투시작_07_4()


class 차전투시작_07_4(state.State):
    def on_enter(self):
        set_onetime_effect(id=6, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4007], returnView=False)
        move_user(mapId=52010029, portalId=6005)
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=6000)
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__53$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__54$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 차전투시작_08_4()


class 차전투시작_08_4(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4005], returnView=False)
        add_cinematic_talk(npcId=11003391, msg='$52010029_QD__MAIN__55$', duration=3000)
        add_cinematic_talk(npcId=11003391, msg='$52010029_QD__MAIN__56$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6500):
            return 차전투시작_09_4()


class 차전투시작_09_4(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4007], returnView=False)
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=3500)
        set_npc_emotion_loop(spawnId=703, sequenceName='Attack_Idle_A', duration=16000000)
        add_balloon_talk(npcID=0, msg='$52010029_QD__MAIN__57$', duration=3000)
        add_cinematic_talk(npcId=11003391, msg='$52010029_QD__MAIN__58$', duration=4000)
        add_balloon_talk(spawnId=0, msg='$52010029_QD__MAIN__59$', duration=2000, delayTick=4000)
        add_cinematic_talk(npcId=11003391, msg='$52010029_QD__MAIN__60$', duration=4000)
        add_balloon_talk(spawnId=0, msg='$52010029_QD__MAIN__61$', duration=3000, delayTick=7000)
        add_cinematic_talk(npcId=11003391, msg='$52010029_QD__MAIN__62$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__63$', duration=3000)
        move_user_path(patrolName='MS2PatrolData_3003')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=14000):
            return 차전투시작_09_01_4()


class 차전투시작_09_01_4(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4005], returnView=False)
        add_cinematic_talk(npcId=11003391, msg='$52010029_QD__MAIN__64$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__65$', duration=3000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=7000):
            return 에바고르전투_01()


class 에바고르전투_01(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        select_camera_path(pathIds=[4005], returnView=False)
        add_cinematic_talk(npcId=11003391, msg='$52010029_QD__MAIN__66$', duration=4000)
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__67$', duration=2000)
        add_cinematic_talk(npcId=11003391, msg='$52010029_QD__MAIN__68$', duration=3000)
        set_npc_emotion_sequence(spawnId=703, sequenceName='Attack_02_A')
        face_emotion(spawnId=703, emotionName='Trigger_Fury')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=10000):
            return 에바고르전투_01_1()


class 에바고르전투_01_1(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 에바고르전투_02()


class Skip_4(state.State):
    def on_enter(self):
        set_cinematic_ui(type=4)
        move_user(mapId=52010029, portalId=6005)
        set_effect(triggerIds=[5001], visible=False)
        set_effect(triggerIds=[5002], visible=False)
        select_camera_path(pathIds=[4005], returnView=False)
        destroy_monster(spawnIds=[401])
        destroy_monster(spawnIds=[402])
        destroy_monster(spawnIds=[403])
        destroy_monster(spawnIds=[404])
        destroy_monster(spawnIds=[501])
        destroy_monster(spawnIds=[702])
        set_onetime_effect(id=7, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 에바고르전투_02()


class 에바고르전투_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=7, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        reset_camera(interpolationTime=0)
        destroy_monster(spawnIds=[703])
        create_monster(spawnIds=[699], arg2=True)
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 에바고르전투_03()


class 에바고르전투_03(state.State):
    def on_enter(self):
        set_onetime_effect(id=7, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=500):
            return 에바고르전투_04()


class 에바고르전투_04(state.State):
    def on_enter(self):
        set_cinematic_ui(type=0)
        set_cinematic_ui(type=2)
        set_event_ui(type=1, arg2='$52010029_QD__MAIN__69$', arg3='3000', arg4='0')

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[699]):
            return 훈계_01()


class 훈계_01(state.State):
    def on_enter(self):
        set_achievement(triggerId=2001, type='trigger', achieve='evagor')
        set_onetime_effect(id=8, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        destroy_monster(spawnIds=[699])
        set_scene_skip(state=Warp, arg2='exit')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3600):
            return 훈계_02_01()


class 훈계_02_01(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4012], returnView=False)
        create_monster(spawnIds=[704], arg2=True)
        move_user(mapId=52010029, portalId=6004)
        set_npc_emotion_loop(spawnId=704, sequenceName='Down_Idle_A', duration=16000000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 훈계_02_02()


class 훈계_02_02(state.State):
    def on_enter(self):
        set_onetime_effect(id=8, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=9000)
        add_cinematic_talk(npcId=11003391, msg='$52010029_QD__MAIN__70$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__71$', duration=3000)
        add_cinematic_talk(npcId=11003391, msg='$52010029_QD__MAIN__72$', duration=4000)
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__73$', duration=3000)
        add_cinematic_talk(npcId=11003391, msg='$52010029_QD__MAIN__74$', duration=2000)
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__75$', duration=4000)
        add_cinematic_talk(npcId=11003391, msg='$52010029_QD__MAIN__76$', duration=3000)
        add_cinematic_talk(npcId=11003391, msg='$52010029_QD__MAIN__77$', duration=4000)
        add_cinematic_talk(npcId=11003391, msg='$52010029_QD__MAIN__78$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=30000):
            return 훈계_03()


class 훈계_03(state.State):
    def on_enter(self):
        set_cinematic_ui(type=1)
        set_cinematic_ui(type=3)
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__79$', duration=3000)
        add_cinematic_talk(npcId=11003391, msg='$52010029_QD__MAIN__80$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__81$', duration=5000)
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__82$', duration=3000)
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__83$', duration=3000)
        add_cinematic_talk(npcId=11003391, msg='$52010029_QD__MAIN__84$', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=21000):
            return 훈계_04()


class 훈계_04(state.State):
    def on_enter(self):
        move_user_path(patrolName='MS2PatrolData_3005')
        add_cinematic_talk(npcId=0, msg='$52010029_QD__MAIN__85$', duration=4000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=5000):
            return 훈계_05()


class 훈계_05(state.State):
    def on_enter(self):
        select_camera_path(pathIds=[4017], returnView=False)
        add_cinematic_talk(npcId=11003391, msg='$52010029_QD__MAIN__86$', duration=2000)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=6000):
            return 훈계_06()


class 훈계_06(state.State):
    def on_enter(self):
        set_scene_skip()

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return Warp()


class Warp(state.State):
    def on_enter(self):
        move_user(mapId=2000051, portalId=21)


