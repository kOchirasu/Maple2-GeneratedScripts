""" trigger/52000085_qd/50001538.xml """
import trigger_api


class 퀘스트체크(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.quest_user_detected(boxIds=[199], questIds=[50100280], questStates=[1]):
            return 대기(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50100280], questStates=[2]):
            return 던전종료(self.ctx)
        if self.quest_user_detected(boxIds=[199], questIds=[50100280], questStates=[3]):
            return 던전종료(self.ctx)


class 대기(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[602], visible=False)
        self.set_effect(triggerIds=[603], visible=False)
        self.set_mesh(triggerIds=[3000,3001], visible=True, arg3=0, delay=0, scale=0)
        self.create_monster(spawnIds=[1001,1002,1003], animationEffect=False)
        self.set_portal(portalId=91, visible=False, enable=False, minimapVisible=False)
        self.remove_buff(boxId=199, skillId=70000115)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[199]):
            return 연출시작(self.ctx)


class 연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_local_camera(cameraId=2000, enable=False)
        self.set_npc_emotion_loop(spawnId=1001, sequenceName='Attack_Idle_A', duration=1E+12)
        self.set_pc_emotion_loop(sequenceName='Attack_Idle_A', duration=1E+12)
        self.set_skip(state=연출종료)
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.select_camera(triggerId=300, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 트루카대사01(self.ctx)


class 트루카대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1003, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003071, illustId='11003762', msg='$52000085_QD__50001538__0$', align='left', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 트루카대사02(self.ctx)


class 트루카대사02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=301, enable=True)
        self.add_cinematic_talk(npcId=11003071, illustId='11003762', msg='$52000085_QD__50001538__1$', align='left', duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 에르다대사01(self.ctx)


class 에르다대사01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=302, enable=True)
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_1002A')
        self.add_cinematic_talk(npcId=11003069, illustId='SnowQueen_normal', msg='$52000085_QD__50001538__2$', align='right', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 에르다대사02(self.ctx)


class 에르다대사02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_1003A')
        self.add_cinematic_talk(npcId=11003069, illustId='SnowQueen_normal', msg='$52000085_QD__50001538__3$', align='right', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 트루카대사03(self.ctx)


class 트루카대사03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=303, enable=True)
        self.set_npc_emotion_sequence(spawnId=1003, sequenceName='Talk_A')
        self.add_cinematic_talk(npcId=11003071, illustId='11003762', msg='$52000085_QD__50001538__4$', align='left', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 트루카대사04(self.ctx)


class 트루카대사04(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003071, illustId='11003762', msg='$52000085_QD__50001538__5$', align='left', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 에르다대사03(self.ctx)


class 에르다대사03(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=302, enable=True)
        self.add_cinematic_talk(npcId=11003069, illustId='SnowQueen_normal', msg='$52000085_QD__50001538__6$', align='right', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 트루카대사05(self.ctx)


class 트루카대사05(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003071, illustId='11003762', msg='$52000085_QD__50001538__7$', align='left', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 트루카대사06(self.ctx)


class 트루카대사06(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003071, illustId='11003762', msg='$52000085_QD__50001538__8$', align='left', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 트루카대사07(self.ctx)


class 트루카대사07(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=303, enable=True)
        self.add_cinematic_talk(npcId=11003071, illustId='11003762', msg='$52000085_QD__50001538__9$', align='left', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 에르다대사04(self.ctx)


class 에르다대사04(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003069, illustId='SnowQueen_normal', msg='$52000085_QD__50001538__10$', align='right', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 설눈이이동01(self.ctx)


class 설눈이이동01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=304, enable=True)
        self.move_npc(spawnId=1001, patrolName='MS2PatrolData_1001A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 설눈이대사01(self.ctx)


class 설눈이대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=1001, sequenceName='Attack_Idle_A', duration=1E+12)
        self.add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000085_QD__50001538__11$', align='right', duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 트루카대사08(self.ctx)


class 트루카대사08(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=305, enable=True)
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_1003B')
        self.add_cinematic_talk(npcId=11003071, illustId='11003762', msg='$52000085_QD__50001538__12$', align='left', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 트루카대사09(self.ctx)


class 트루카대사09(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1004], animationEffect=False)
        self.add_cinematic_talk(npcId=11003071, illustId='11003762', msg='$52000085_QD__50001538__13$', align='left', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 홀슈타트등장(self.ctx)


class 홀슈타트등장(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=306, enable=True)
        self.move_npc(spawnId=1004, patrolName='MS2PatrolData_1004A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 홀슈타트대사01(self.ctx)


class 홀슈타트대사01(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=307, enable=True)
        self.add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000085_QD__50001538__14$', align='left', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 트루카대사10(self.ctx)


class 트루카대사10(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=308, enable=True)
        self.add_cinematic_talk(npcId=11003071, illustId='11003762', msg='$52000085_QD__50001538__15$', align='right', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 홀슈타트대사02(self.ctx)


class 홀슈타트대사02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=310, enable=True)
        self.add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000085_QD__50001538__16$', align='left', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 트루카대사11(self.ctx)


class 트루카대사11(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=308, enable=True)
        self.add_cinematic_talk(npcId=11003071, illustId='11003762', msg='$52000085_QD__50001538__17$', align='right', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 트루카대사12(self.ctx)


class 트루카대사12(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=309, enable=True)
        self.add_cinematic_talk(npcId=11003071, illustId='11003762', msg='$52000085_QD__50001538__18$', align='right', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 포털이펙트(self.ctx)


class 포털이펙트(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_sequence(spawnId=1003, sequenceName='Bore_A')
        self.set_effect(triggerIds=[601], visible=True)
        self.add_cinematic_talk(npcId=11004022, illustId='11004022', msg='$52000085_QD__50001538__19$', align='left', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return NPC합체(self.ctx)


class NPC합체(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1003, patrolName='MS2PatrolData_1099')
        self.move_npc(spawnId=1004, patrolName='MS2PatrolData_1099')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=600):
            return NPC소멸(self.ctx)


class NPC소멸(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1003,1004])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 포털삭제(self.ctx)


class 포털삭제(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[601], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 설눈이이동02(self.ctx)


class 설눈이이동02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=311, enable=True)
        self.move_user_path(patrolName='MS2PatrolData_PC')
        self.move_npc(spawnId=1001, patrolName='MS2PatrolData_1001B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 설눈이대사02(self.ctx)


class 설눈이대사02(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000085_QD__50001538__20$', align='right', duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 에르다방향전환(self.ctx)


class 에르다방향전환(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1002, patrolName='MS2PatrolData_1002B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 에르다대사05(self.ctx)


class 에르다대사05(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=312, enable=True)
        self.add_cinematic_talk(npcId=11003069, illustId='SnowQueen_normal', msg='$52000085_QD__50001538__21$', align='left', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 설눈이대사03(self.ctx)


class 설눈이대사03(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000085_QD__50001538__22$', align='right', duration=2000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 에르다대사06(self.ctx)


class 에르다대사06(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=1002, sequenceName='Attack_Idle_A', duration=1E+12)
        self.select_camera(triggerId=313, enable=True)
        self.add_cinematic_talk(npcId=11003069, illustId='SnowQueen_normal', msg='$52000085_QD__50001538__23$', align='left', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 연출종료(self.ctx)


class 연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip()
        self.destroy_monster(spawnIds=[1001,1002,1003,1004])
        self.create_monster(spawnIds=[2001,2002], animationEffect=True)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.reset_camera(interpolationTime=0)
        self.move_user(mapId=52000085, portalId=99)
        self.add_buff(boxIds=[199], skillId=70000115, level=1, isPlayer=False, isSkillSet=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=7500):
            self.create_monster(spawnIds=[2003,2004,2005], animationEffect=False)
            return 에르다사망대기(self.ctx)


class 에르다사망대기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[2002]):
            return 에르다사망딜레이(self.ctx)


class 에르다사망딜레이(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[2003,2004,2005])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 암전(self.ctx)


class 암전(trigger_api.Trigger):
    def on_enter(self):
        self.set_onetime_effect(id=2, enable=True, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')
        self.set_cinematic_ui(type=1)
        self.set_cinematic_ui(type=3)
        self.move_user(mapId=52000085, portalId=98)
        self.destroy_monster(spawnIds=[2001,2002])

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 종료연출시작(self.ctx)


class 종료연출시작(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip(state=종료연출종료)
        self.create_monster(spawnIds=[1005,1006], animationEffect=False)
        self.select_camera(triggerId=314, enable=True)
        self.set_onetime_effect(id=2, enable=False, path='BG/Common/ScreenMask/Eff_fadein_1sec.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 에르다대사07(self.ctx)


class 에르다대사07(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003069, illustId='SnowQueen_normal', msg='$52000085_QD__50001538__24$', align='left', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 설눈이대사04(self.ctx)


class 설눈이대사04(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000085_QD__50001538__25$', align='right', duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 에르다공중부양준비(self.ctx)


class 에르다공중부양준비(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=315, enable=True)
        self.set_npc_emotion_loop(spawnId=1006, sequenceName='Attack_Idle_A', duration=1E+12)
        self.add_cinematic_talk(npcId=11003069, illustId='SnowQueen_normal', msg='$52000085_QD__50001538__26$', align='left', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 에르다공중부양(self.ctx)


class 에르다공중부양(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip()
        self.move_npc(spawnId=1006, patrolName='MS2PatrolData_1006')
        self.add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000085_QD__50001538__27$', align='right', duration=3000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1500):
            return 얼림(self.ctx)


class 얼림(trigger_api.Trigger):
    def on_enter(self):
        self.set_npc_emotion_loop(spawnId=1005, sequenceName='Stun_A', duration=1E+12)
        self.set_pc_emotion_loop(sequenceName='StunFrozen_A', duration=25000)
        self.set_effect(triggerIds=[602], visible=True)
        self.set_effect(triggerIds=[603], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 에르다공중부양중(self.ctx)


class 에르다공중부양중(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=316, enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return PC말풍선대사01(self.ctx)


class PC말풍선대사01(trigger_api.Trigger):
    def on_enter(self):
        self.destroy_monster(spawnIds=[1006])
        self.select_camera(triggerId=317, enable=True)
        self.set_conversation(type=1, spawnId=0, script='$52000085_QD__50001538__28$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 설눈이말풍선대사01(self.ctx)


class 설눈이말풍선대사01(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1007], animationEffect=False)
        self.set_conversation(type=1, spawnId=1005, script='$52000085_QD__50001538__29$', arg4=4)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC말풍선대사02(self.ctx)


class PC말풍선대사02(trigger_api.Trigger):
    def on_enter(self):
        self.select_camera(triggerId=318, enable=True)
        self.set_conversation(type=1, spawnId=0, script='$52000085_QD__50001538__30$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 설만이이동01(self.ctx)


class 설만이이동01(trigger_api.Trigger):
    def on_enter(self):
        self.set_conversation(type=1, spawnId=1007, script='$52000085_QD__50001538__31$', arg4=5)
        self.move_npc(spawnId=1007, patrolName='MS2PatrolData_1007A')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 설눈이인사(self.ctx)


class 설눈이인사(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[603], visible=False)
        self.set_npc_emotion_loop(spawnId=1005, sequenceName='Idle_A', duration=1E+12)
        self.set_conversation(type=1, spawnId=1005, script='$52000085_QD__50001538__32$', arg4=2)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2500):
            return 설만이이동02(self.ctx)


class 설만이이동02(trigger_api.Trigger):
    def on_enter(self):
        self.move_npc(spawnId=1005, patrolName='MS2PatrolData_1005A')
        self.move_npc(spawnId=1007, patrolName='MS2PatrolData_1007B')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return PC말풍선대사03(self.ctx)


class PC말풍선대사03(trigger_api.Trigger):
    def on_enter(self):
        self.set_effect(triggerIds=[602], visible=False)
        self.set_pc_emotion_loop(sequenceName='Idle_A', duration=1000)
        self.move_user_path(patrolName='MS2PatrolData_PC2')
        self.move_npc(spawnId=1007, patrolName='MS2PatrolData_1007C')
        self.set_conversation(type=1, spawnId=0, script='$52000085_QD__50001538__33$', arg4=3)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 설만이대사01(self.ctx)


class 설만이대사01(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip(state=종료연출종료)
        self.select_camera(triggerId=319, enable=True)
        self.add_cinematic_talk(npcId=11003073, illustId='11000404', msg='$52000085_QD__50001538__34$', align='right', duration=6000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=6000):
            return 설눈이대사05(self.ctx)


class 설눈이대사05(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000085_QD__50001538__35$', align='left', duration=5000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=5000):
            return 설만이대사02(self.ctx)


class 설만이대사02(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003073, illustId='11000404', msg='$52000085_QD__50001538__36$', align='right', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 설눈이대사06(self.ctx)


class 설눈이대사06(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000085_QD__50001538__37$', align='left', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 설눈이대사07(self.ctx)


class 설눈이대사07(trigger_api.Trigger):
    def on_enter(self):
        self.add_cinematic_talk(npcId=11003068, illustId='Seolnunyi_normal', msg='$52000085_QD__50001538__38$', align='left', duration=4000)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=4000):
            return 종료연출종료(self.ctx)


class 종료연출종료(trigger_api.Trigger):
    def on_enter(self):
        self.set_skip()
        self.set_npc_emotion_loop(spawnId=1005, sequenceName='Idle_A', duration=1E+12)
        self.set_pc_emotion_loop(sequenceName='Idle_A', duration=1000)
        self.destroy_monster(spawnIds=[1005,1006,1007])
        self.set_achievement(triggerId=199, type='trigger', achieve='snowqueenerda')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 던전종료(self.ctx)


class 던전종료(trigger_api.Trigger):
    def on_enter(self):
        self.create_monster(spawnIds=[1008,1009], animationEffect=False)
        self.set_cinematic_ui(type=0)
        self.set_cinematic_ui(type=2)
        self.set_effect(triggerIds=[601], visible=False)
        self.set_effect(triggerIds=[602], visible=False)
        self.set_effect(triggerIds=[603], visible=False)
        self.set_portal(portalId=91, visible=True, enable=True, minimapVisible=True)
        self.reset_camera(interpolationTime=0)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 종료(self.ctx)


class 종료(trigger_api.Trigger):
    pass


initial_state = 퀘스트체크
