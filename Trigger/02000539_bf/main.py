""" trigger/02000539_bf/main.xml """
from common import *
import state


#  플레이어 감지 
class idle(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_ladder(triggerIds=[601], visible=False, animationEffect=False)
        set_ladder(triggerIds=[602], visible=False, animationEffect=False)
        set_ladder(triggerIds=[603], visible=False, animationEffect=False)
        set_ladder(triggerIds=[604], visible=False, animationEffect=False)
        set_ladder(triggerIds=[605], visible=False, animationEffect=False)
        set_ladder(triggerIds=[606], visible=False, animationEffect=False)
        set_onetime_effect(id=101, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=102, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=103, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=104, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=105, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_onetime_effect(id=106, enable=False, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_mesh(triggerIds=[904,905,906,907,908,909], visible=True)
        set_mesh(triggerIds=[910,911,912,913,921,914,915,922,916,917,918,919,920,923,924,925,926,927], visible=False)
        set_mesh(triggerIds=[928,929,930,931,932,933,934,935,936,937], visible=False)
        enable_spawn_point_pc(spawnId=0, isEnable=True)
        enable_spawn_point_pc(spawnId=1, isEnable=False)
        enable_spawn_point_pc(spawnId=2, isEnable=False)
        set_skill(triggerIds=[2000], isEnable=False)
        set_effect(triggerIds=[3000], visible=False)
        set_effect(triggerIds=[3001], visible=False)
        set_effect(triggerIds=[3002], visible=False)
        set_effect(triggerIds=[3003], visible=False)
        set_effect(triggerIds=[3004], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[701], jobCode=0):
            return ready()


class ready(state.State):
    def on_enter(self):
        create_monster(spawnIds=[101,102], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[101,102]):
            return 잠시쉬기()


class 잠시쉬기(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[709], jobCode=0):
            return 사다리생성하기()


class 사다리생성하기(state.State):
    def on_enter(self):
        set_ladder(triggerIds=[601], visible=True, animationEffect=True)
        set_ladder(triggerIds=[602], visible=True, animationEffect=True)
        set_ladder(triggerIds=[603], visible=True, animationEffect=True)
        create_monster(spawnIds=[203], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[706], jobCode=0):
            return 잠시쉬기2()


class 잠시쉬기2(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000539_BF__MAIN__0$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 잠시쉬기3()


class 잠시쉬기3(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[904,905,906,907,908,909], visible=False)
        set_onetime_effect(id=101, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[710], jobCode=0):
            return 몬스터생성()


class 몬스터생성(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[203])
        create_monster(spawnIds=[103,1031,1032,1033,1034], arg2=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[103,1031,1032,1033,1034]):
            return 다음몬스터생성조건체크()


class 다음몬스터생성조건체크(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000539_BF__MAIN__1$')
        create_monster(spawnIds=[107,1071,1072], arg2=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 다음몬스터생성()


class 다음몬스터생성(state.State):
    def on_enter(self):
        create_monster(spawnIds=[105,1051,1052], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[107,1071,1072,105,1051,1052]):
            return NPC생성1()


class NPC생성1(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000539_BF__MAIN__2$')
        set_effect(triggerIds=[3000], visible=True)
        create_monster(spawnIds=[201], arg2=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[707], jobCode=0):
            return NPC생성2()


class NPC생성2(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000539_BF__MAIN__3$')
        move_npc(spawnId=201, patrolName='MS2PatrolData_500')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3500):
            return 다리만들기1()


class 다리만들기1(state.State):
    def on_enter(self):
        set_onetime_effect(id=102, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_mesh(triggerIds=[910,911], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1000):
            return 다리만들기2()


class 다리만들기2(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000539_BF__MAIN__4$')
        set_mesh(triggerIds=[912,913,921], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 다리만들기3()


class 다리만들기3(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[914,915,922], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 다리만들기4()


class 다리만들기4(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[916,917,918], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 다리만들기5()


class 다리만들기5(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[919,920,926,922,927], visible=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=800):
            return 다리만들기6()


class 다리만들기6(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[923,924,925], visible=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[708], jobCode=0):
            return 다음몬스터생성1()


class 다음몬스터생성1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[202], arg2=False)
        create_monster(spawnIds=[111,1111,1112,112,1121], arg2=True)
        side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=3000, script='$02000539_BF__MAIN__5$')
        enable_spawn_point_pc(spawnId=0, isEnable=False)
        enable_spawn_point_pc(spawnId=1, isEnable=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[111,1111,1112,112,1121]):
            return 다음몬스터생성조건체크2()


class 다음몬스터생성조건체크2(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000539_BF__MAIN__6$')
        create_monster(spawnIds=[113,1131,1132,1133,1134], arg2=True)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[705], jobCode=0):
            return 다음몬스터생성조건체크3()


class 다음몬스터생성조건체크3(state.State):
    def on_enter(self):
        set_effect(triggerIds=[3001], visible=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[113,1131,1132,1133,1134]):
            return 두번째다리만들기1()


class 두번째다리만들기1(state.State):
    def on_enter(self):
        create_monster(spawnIds=[204], arg2=False)
        side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=3000, script='$02000539_BF__MAIN__7$')

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[704], jobCode=0):
            return 두번째다리만들기2()


class 두번째다리만들기2(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 두번째사다리생성하기1()


class 두번째사다리생성하기1(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=4000, script='$02000539_BF__MAIN__8$')
        set_onetime_effect(id=103, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_mesh(triggerIds=[928,929,930,931,932,933,934,935,936,937], visible=True)
        set_ladder(triggerIds=[604], visible=True, animationEffect=True)
        set_ladder(triggerIds=[605], visible=True, animationEffect=True)
        set_ladder(triggerIds=[606], visible=True, animationEffect=True)

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 다음몬스터생성3()


class 다음몬스터생성3(state.State):
    def on_enter(self):
        create_monster(spawnIds=[104,1041], arg2=False)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[104,1041]):
            return 보스문으로이동()


class 보스문으로이동(state.State):
    def on_tick(self) -> state.State:
        if user_detected(boxIds=[711], jobCode=0):
            return 벽부시기3단계()


class 벽부시기3단계(state.State):
    def on_enter(self):
        set_onetime_effect(id=105, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')
        set_mesh(triggerIds=[938,939,940,941,942,943], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[702], jobCode=0):
            return 보스등장()


class 보스등장(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004644, illust='SlaveMan3_normal', duration=3000, script='$02000539_BF__MAIN__9$')
        enable_spawn_point_pc(spawnId=1, isEnable=False)
        enable_spawn_point_pc(spawnId=2, isEnable=True)
        create_monster(spawnIds=[119], arg2=True)
        set_onetime_effect(id=106, enable=True, path='BG/Common/Eff_Com_Vibrate_Short.xml')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=3000):
            return 보스등장3()


class 보스등장3(state.State):
    def on_enter(self):
        set_effect(triggerIds=[3002], visible=True)
        set_effect(triggerIds=[3003], visible=True)
        set_effect(triggerIds=[3004], visible=True)
        set_skill(triggerIds=[2000], isEnable=True)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[119]):
            return 잠시쉬기4()


class 잠시쉬기4(state.State):
    def on_enter(self):
        side_npc_talk(npcId=11004643, illust='SlaveWoman3_normal', duration=3000, script='$02000539_BF__MAIN__10$')

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return 포탈활성화()


class 포탈활성화(state.State):
    def on_enter(self):
        set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)


