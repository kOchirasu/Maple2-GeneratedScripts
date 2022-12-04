""" trigger/52000117_qd/main.xml """
import trigger_api


# 트라이아 청사 : 60100015
class ready(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[101], animationEffect=True) # 조디

    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[2001], questIds=[60100015], questStates=[1]):
            return fadeout(self.ctx)


class fadeout(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return fadein(self.ctx)

    def on_exit(self):
        self.move_user(mapId=52000117, portalId=6001)


class fadein(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return jordyidle(self.ctx)


class jordyidle(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11003166, msg='$52000117_QD__MAIN__0$', duration=3000, illustId='Jordy_normal', align='Left')
        self.add_cinematic_talk(npcId=11003166, msg='$52000117_QD__MAIN__1$', duration=3000)
        self.set_scene_skip(state=end, action='exit')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return pcmove(self.ctx)


class pcmove(trigger_api.Trigger):
    def on_enter(self):
        self.move_user_path(patrolName='MS2PatrolData_3002')
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Bore_A')
        self.add_cinematic_talk(npcId=11003166, msg='$52000117_QD__MAIN__2$', duration=3000)
        self.add_cinematic_talk(npcId=11003166, msg='$52000117_QD__MAIN__3$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return wow(self.ctx)


class wow(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Emotion_Angry_A'])
        self.add_cinematic_talk(npcId=0, msg='$52000117_QD__MAIN__15$', duration=2000)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Sit_Down_A', duration=3000)
        self.set_npc_emotion_loop(spawnId=101, sequenceName='Sit_Down_A', duration=3000)
        self.add_balloon_talk(spawnId=101, msg='$52000117_QD__MAIN__5$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_01(self.ctx)


class scene_01(trigger_api.Trigger):
    def on_enter(self):
        self.add_balloon_talk(spawnId=101, msg='$52000117_QD__MAIN__6$', duration=3000)
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_3001')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return scene_02(self.ctx)


class scene_02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera_path(pathIds=[4001], returnView=False) # 대화 모습
        self.add_cinematic_talk(npcId=11003166, msg='$52000117_QD__MAIN__7$', duration=3000)
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.set_pc_emotion_loop(sequenceName='Emotion_Dance_S', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return pctalk(self.ctx)


class pctalk(trigger_api.Trigger):
    def on_enter(self):
        self.set_pc_emotion_sequence(sequenceNames=['Talk_A','Talk_B'])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return scene_03(self.ctx)


class scene_03(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003166, msg='$52000117_QD__MAIN__8$', duration=3000)
        self.add_cinematic_talk(npcId=11003166, msg='$52000117_QD__MAIN__9$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return scene_04(self.ctx)


class scene_04(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003166, msg='$52000117_QD__MAIN__10$', duration=3000)
        self.add_cinematic_talk(npcId=11003166, msg='$52000117_QD__MAIN__11$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return scene_05(self.ctx)


class scene_05(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=101, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003166, msg='$52000117_QD__MAIN__12$', duration=3000)
        self.add_cinematic_talk(npcId=11003166, msg='$52000117_QD__MAIN__13$', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return scene_06(self.ctx)


class scene_06(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=101, patrolName='MS2PatrolData_3003')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_fadeout(self.ctx)


class scene_fadeout(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_cinematic_ui(type=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return jordydel(self.ctx)


class jordydel(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return scene_fadein(self.ctx)


class scene_fadein(trigger_api.Trigger):
    def on_enter(self):
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.set_scene_skip()

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return end(self.ctx)


class end(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[101])
        self.reset_camera(interpolationTime=0.5)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_achievement(triggerId=2001, type='trigger', achieve='jordyhello')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return endmessage(self.ctx)


class endmessage(trigger_api.Trigger):
    def on_enter(self):
        self.play_system_sound_in_box(sound='System_ShowGuideSummary_01')
        self.set_event_ui(type=1, arg2='$52000117_QD__MAIN__14$', arg3='3000', arg4='0')
        self.move_user(mapId=52000118, portalId=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return endmessage(self.ctx)


initial_state = ready
