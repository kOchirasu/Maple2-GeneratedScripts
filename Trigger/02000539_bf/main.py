""" trigger/02000539_bf/main.xml """
import trigger_api


# 플레이어 감지
class idle(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=2, visible=False, enable=False, minimapVisible=False)
        self.set_ladder(triggerIds=[601], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[602], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[603], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[604], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[605], visible=False, animationEffect=False)
        self.set_ladder(triggerIds=[606], visible=False, animationEffect=False)
        self.set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=102, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=103, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=104, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=105, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_onetime_effect(id=106, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_mesh(triggerIds=[904,905,906,907,908,909], visible=True)
        self.set_mesh(triggerIds=[910,911,912,913,921,914,915,922,916,917,918,919,920,923,924,925,926,927], visible=False)
        self.set_mesh(triggerIds=[928,929,930,931,932,933,934,935,936,937], visible=False)
        self.enable_spawn_point_pc(spawnId=0, isEnable=True)
        self.enable_spawn_point_pc(spawnId=1, isEnable=False)
        self.enable_spawn_point_pc(spawnId=2, isEnable=False)
        self.set_skill(triggerIds=[2000], enable=False)
        self.set_effect(triggerIds=[3000], visible=False)
        self.set_effect(triggerIds=[3001], visible=False)
        self.set_effect(triggerIds=[3002], visible=False)
        self.set_effect(triggerIds=[3003], visible=False)
        self.set_effect(triggerIds=[3004], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[701], jobCode=0):
            return ready(self.ctx)


class ready(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[101,102], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[101,102]):
            return 잠시쉬기(self.ctx)


class 잠시쉬기(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[709], jobCode=0):
            return 사다리생성하기(self.ctx)


class 사다리생성하기(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_ladder(triggerIds=[601], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[602], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[603], visible=True, animationEffect=True)
        self.create_monster(spawnIds=[203], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[706], jobCode=0):
            return 잠시쉬기2(self.ctx)


class 잠시쉬기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000539_BF__MAIN__0$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 잠시쉬기3(self.ctx)


class 잠시쉬기3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[904,905,906,907,908,909], visible=False)
        self.set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[710], jobCode=0):
            return 몬스터생성(self.ctx)


class 몬스터생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.destroy_monster(spawnIds=[203])
        self.create_monster(spawnIds=[103,1031,1032,1033,1034], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[103,1031,1032,1033,1034]):
            return 다음몬스터생성조건체크(self.ctx)


class 다음몬스터생성조건체크(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000539_BF__MAIN__1$')
        self.create_monster(spawnIds=[107,1071,1072], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 다음몬스터생성(self.ctx)


class 다음몬스터생성(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[105,1051,1052], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[107,1071,1072,105,1051,1052]):
            return NPC생성1(self.ctx)


class NPC생성1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000539_BF__MAIN__2$')
        self.set_effect(triggerIds=[3000], visible=True)
        self.create_monster(spawnIds=[201], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[707], jobCode=0):
            return NPC생성2(self.ctx)


class NPC생성2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000539_BF__MAIN__3$')
        self.move_npc(spawnId=201, patrolName='MS2PatrolData_500')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3500):
            return 다리만들기1(self.ctx)


class 다리만들기1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_mesh(triggerIds=[910,911], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=1000):
            return 다리만들기2(self.ctx)


class 다리만들기2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000539_BF__MAIN__4$')
        self.set_mesh(triggerIds=[912,913,921], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return 다리만들기3(self.ctx)


class 다리만들기3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[914,915,922], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return 다리만들기4(self.ctx)


class 다리만들기4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[916,917,918], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return 다리만들기5(self.ctx)


class 다리만들기5(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[919,920,926,922,927], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=800):
            return 다리만들기6(self.ctx)


class 다리만들기6(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_mesh(triggerIds=[923,924,925], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[708], jobCode=0):
            return 다음몬스터생성1(self.ctx)


class 다음몬스터생성1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[202], animationEffect=False)
        self.create_monster(spawnIds=[111,1111,1112,112,1121], animationEffect=True)
        self.side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=3000, script='$02000539_BF__MAIN__5$')
        self.enable_spawn_point_pc(spawnId=0, isEnable=False)
        self.enable_spawn_point_pc(spawnId=1, isEnable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[111,1111,1112,112,1121]):
            return 다음몬스터생성조건체크2(self.ctx)


class 다음몬스터생성조건체크2(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000539_BF__MAIN__6$')
        self.create_monster(spawnIds=[113,1131,1132,1133,1134], animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[705], jobCode=0):
            return 다음몬스터생성조건체크3(self.ctx)


class 다음몬스터생성조건체크3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[3001], visible=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[113,1131,1132,1133,1134]):
            return 두번째다리만들기1(self.ctx)


class 두번째다리만들기1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[204], animationEffect=False)
        self.side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=3000, script='$02000539_BF__MAIN__7$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[704], jobCode=0):
            return 두번째다리만들기2(self.ctx)


class 두번째다리만들기2(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 두번째사다리생성하기1(self.ctx)


class 두번째사다리생성하기1(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000539_BF__MAIN__8$')
        self.set_onetime_effect(id=103, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_mesh(triggerIds=[928,929,930,931,932,933,934,935,936,937], visible=True)
        self.set_ladder(triggerIds=[604], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[605], visible=True, animationEffect=True)
        self.set_ladder(triggerIds=[606], visible=True, animationEffect=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 다음몬스터생성3(self.ctx)


class 다음몬스터생성3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.create_monster(spawnIds=[104,1041], animationEffect=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[104,1041]):
            return 보스문으로이동(self.ctx)


class 보스문으로이동(trigger_api.Trigger):
    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[711], jobCode=0):
            return 벽부시기3단계(self.ctx)


class 벽부시기3단계(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_onetime_effect(id=105, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        self.set_mesh(triggerIds=[938,939,940,941,942,943], visible=False)

    def on_tick(self) -> trigger_api.Trigger:
        if self.user_detected(boxIds=[702], jobCode=0):
            return 보스등장(self.ctx)


class 보스등장(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=3000, script='$02000539_BF__MAIN__9$')
        self.enable_spawn_point_pc(spawnId=1, isEnable=False)
        self.enable_spawn_point_pc(spawnId=2, isEnable=True)
        self.create_monster(spawnIds=[119], animationEffect=True)
        self.set_onetime_effect(id=106, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=3000):
            return 보스등장3(self.ctx)


class 보스등장3(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_effect(triggerIds=[3002], visible=True)
        self.set_effect(triggerIds=[3003], visible=True)
        self.set_effect(triggerIds=[3004], visible=True)
        self.set_skill(triggerIds=[2000], enable=True)

    def on_tick(self) -> trigger_api.Trigger:
        if self.monster_dead(boxIds=[119]):
            return 잠시쉬기4(self.ctx)


class 잠시쉬기4(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000539_BF__MAIN__10$')

    def on_tick(self) -> trigger_api.Trigger:
        if self.wait_tick(waitTick=2000):
            return 포탈활성화(self.ctx)


class 포탈활성화(trigger_api.Trigger):
    def on_enter(self) -> 'trigger_api.Trigger':
        self.set_portal(portalId=2, visible=True, enable=True, minimapVisible=True)


initial_state = idle
