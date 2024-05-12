""" trigger/52000118_qd/main.xml """
import trigger_api


# 넬프의 집 : 60100015
class ready(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60100015], questStates=[2]):
            return fadeout(self.ctx)
        if self.quest_user_detected(boxIds=[2001], questIds=[60100015], questStates=[3]):
            return fadeout_a(self.ctx)


class fadeout(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101], animationEffect=True) # 수상한 가면: 11003167
        self.set_portal(portalId=1, visible=False, enable=False, minimapVisible=False)
        self.visible_my_pc(isVisible=False) # 유저 투명 처리
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)
        self.set_scene_skip(state=fadeout_a, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return fadein(self.ctx)


class fadein(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return suspiciousmask(self.ctx)


class suspiciousmask(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4001,4002,4003], returnView=False)
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003167, msg='$52000118_QD__MAIN__0$', duration=3000, align='center')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return dooropen(self.ctx)


class dooropen(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[5001], visible=True)
        self.create_monster(spawnIds=[102], animationEffect=True) # 조디: 11003186

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return jordyspawn(self.ctx)


class jordyspawn(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4004], returnView=False)
        self.add_cinematic_talk(npcId=11003186, msg='$52000118_QD__MAIN__1$', duration=3000, illustId='Jordy_normal', align='Left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return jordyin(self.ctx)


class jordyin(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.add_cinematic_talk(npcId=11003167, msg='$52000118_QD__MAIN__2$', duration=3000)
        self.add_cinematic_talk(npcId=11003186, msg='$52000118_QD__MAIN__3$', duration=3000, illustId='Jordy_normal', align='Left')
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_3001') # 조디 올라감

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return jordyhello(self.ctx)


class jordyhello(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4007], returnView=False)
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003186, msg='$52000118_QD__MAIN__4$', duration=1000, illustId='Jordy_normal', align='Left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return huk(self.ctx)


class huk(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Sit_Down_A', duration=1000)
        self.add_cinematic_talk(npcId=11003167, msg='$52000118_QD__MAIN__5$', duration=1000, align='Left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return suspiciousmaskmove(self.ctx)


class suspiciousmaskmove(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_3002') # 수상한 가면 뒤 돌아봄

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return talk_01(self.ctx)


class talk_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Attack_Idle_A', duration=10000)
        self.add_cinematic_talk(npcId=11003167, msg='$52000118_QD__MAIN__6$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return talk_02(self.ctx)


class talk_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003186, msg='$52000118_QD__MAIN__7$', duration=3000, illustId='Jordy_normal', align='Left')
        self.add_cinematic_talk(npcId=11003186, msg='$52000118_QD__MAIN__8$', duration=3000, illustId='Jordy_normal', align='Left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return talk_03(self.ctx)


class talk_03(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003186, msg='$52000118_QD__MAIN__9$', duration=3000, illustId='Jordy_normal', align='Left')
        self.add_cinematic_talk(npcId=11003167, msg='$52000118_QD__MAIN__10$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return talk_04(self.ctx)


class talk_04(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003186, msg='$52000118_QD__MAIN__11$', duration=3000, illustId='Jordy_normal', align='Left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return killyou(self.ctx)


class killyou(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Attack_01_B')
        self.add_cinematic_talk(npcId=11003167, msg='$52000118_QD__MAIN__12$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return talk_05(self.ctx)


class talk_05(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003186, msg='$52000118_QD__MAIN__13$', duration=3000, illustId='Jordy_normal', align='Left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return talk_06(self.ctx)


class talk_06(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_sound(triggerId=7001, enable=True)
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003167, msg='$52000118_QD__MAIN__14$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return camera_01(self.ctx)


class camera_01(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4005], returnView=False)
        self.set_onetime_effect(id=1, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return camera_02(self.ctx)


class camera_02(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4006], returnView=False)
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/Sound/Eff_System_Dark_Intro_Chord_01.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=500):
            return talk_07(self.ctx)


class talk_07(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003167, msg='$52000118_QD__MAIN__15$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return talk_08(self.ctx)


class talk_08(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.select_camera_path(pathIds=[4007], returnView=False)
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003186, msg='$52000118_QD__MAIN__16$', duration=3000, illustId='Jordy_normal', align='Left')
        self.add_cinematic_talk(npcId=11003167, msg='$52000118_QD__MAIN__17$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return talk_09(self.ctx)


class talk_09(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003167, msg='$52000118_QD__MAIN__18$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return talk_10(self.ctx)


class talk_10(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003186, msg='$52000118_QD__MAIN__19$', duration=3000, illustId='Jordy_normal', align='Left')
        self.add_cinematic_talk(npcId=11003186, msg='$52000118_QD__MAIN__20$', duration=3000, illustId='Jordy_normal', align='Left')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return talk_11(self.ctx)


class talk_11(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003167, msg='$52000118_QD__MAIN__21$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return talk_12(self.ctx)


class talk_12(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_npc_emotion_sequence(spawnId=102, sequenceName='Talk_A')
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_3005') # 수상한 가면 내려감
        self.move_npc(spawnId=102, patrolName='MS2PatrolData_3003') # 조디 비켜줌
        self.add_balloon_talk(spawnId=102, msg='$52000118_QD__MAIN__22$', duration=4000)
        self.add_cinematic_talk(npcId=11003167, msg='$52000118_QD__MAIN__23$', duration=3000)
        # Missing State: State
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return fadeout_a(self.ctx)


class fadeout_a(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=1, visible=True, enable=True, minimapVisible=True)
        self.visible_my_pc(isVisible=True) # 유저 투명 처리 해제
        self.destroy_monster(spawnIds=[101])
        self.destroy_monster(spawnIds=[102])
        self.create_monster(spawnIds=[104], animationEffect=True) # 조디
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return fadein_a(self.ctx)


class fadein_a(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.reset_camera(interpolationTime=0)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_event_ui(type=1, arg2='$52000118_QD__MAIN__24$', arg3='3000', arg4='0')
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)


initial_state = ready
