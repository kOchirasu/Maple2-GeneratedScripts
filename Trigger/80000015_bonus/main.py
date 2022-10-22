""" trigger/80000015_bonus/main.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=False)
        set_interact_object(triggerIds=[10001339], state=1)
        set_interact_object(triggerIds=[10001340], state=2)
        set_portal(portalId=2, visible=False, enabled=False, minimapVisible=False)
        set_mesh(triggerIds=[3020,3021,3022,3023], visible=True, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3024], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[30001,30002,30003,30004,30005,30006,30007,30008,30009,30010,30011,30012,30013,30014,30015,30016,30017,30018,30019,30020,30021,30022,30023,30024,30025,30026,30027,30028,30029,30030,30031,30032,30033,30034,30035,30036,30037,30038,30039,30040,30041,30042,30043,30044,30045,30046,30047,30048,30049,30050,30051,30052,30053,30054,30055,30056,30057,30058,30059,30060,30061,30062,30063,30064,30065,30066,30067,30068,30069,30070,30071,30072,30073,30074,30075,30076,30077,30078,30079,30080,30081,30082,30083,30084,30085,30086,30087,30088,30089,30090], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[199]):
            return 문열기()


class 문열기(state.State):
    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001339], arg2=0):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        score_board_create(type='ScoreBoardTopCenter', maxScore=0)
        score_board_set_score(score=0)
        spawn_item_range(rangeIds=[9001,9002,9003,9004,9005,9006,9007,9008,9009,9010,9011,9012,9013,9014,9015,9016,9017,9018,9019], randomPickCount=11)
        set_event_ui(type=1, arg2='$80000015_bonus__main__0$', arg3='3000')

    def on_tick(self) -> state.State:
        if all_of():
            return 보스소환대기()
        """
        <condition name="WaitTick" waitTick="1500">
        """


class 보스소환대기(state.State):
    def on_tick(self) -> state.State:
        if all_of():
            return 보스등장()


class 보스등장(state.State):
    def on_enter(self):
        set_effect(triggerIds=[6000], visible=True)
        set_mesh(triggerIds=[30001,30002,30003,30004,30005,30006,30007,30008,30009,30010,30011,30012,30013,30014,30015,30016,30017,30018,30019,30020,30021,30022,30023,30024,30025,30026,30027,30028,30029,30030,30031,30032,30033,30034,30035,30036,30037,30038,30039,30040,30041,30042,30043,30044,30045,30046,30047,30048,30049,30050,30051,30052,30053,30054,30055,30056,30057,30058,30059,30060,30061,30062,30063,30064,30065,30066,30067,30068,30069,30070,30071,30072,30073,30074,30075,30076,30077,30078,30079,30080,30081,30082,30083,30084,30085,30086,30087,30088,30089,30090], visible=False, arg3=0, arg4=0, arg5=3)
        spawn_npc_range(rangeIds=[2099], isAutoTargeting=False, score=5000)

    def on_tick(self) -> state.State:
        if monster_dead(boxIds=[2099]):
            return 딜레이()


class 딜레이(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[0])

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=1500):
            return 정산()


class 정산(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3020,3021,3022,3023], visible=False, arg3=0, arg4=0, arg5=0)
        set_mesh(triggerIds=[3024], visible=True, arg3=0, arg4=0, arg5=0)

    def on_tick(self) -> state.State:
        if score_board_compare(compareOp='GreaterEqual', score=28000):
            debug_string(value='28000 이상')
            set_achievement(triggerId=199, type='trigger', achieve='HighScoreTreasureMap04')
            return 반응대기()
        if score_board_compare(compareOp='Less', score=28000):
            debug_string(value='28000 미만')
            return 반응대기()
        if wait_tick(waitTick=500):
            return 반응대기()


class 반응대기(state.State):
    def on_enter(self):
        set_interact_object(triggerIds=[10001340], state=1)

    def on_tick(self) -> state.State:
        if object_interacted(interactIds=[10001340], arg2=0):
            dungeon_clear()
            set_achievement(triggerId=199, type='trigger', achieve='TreasureMap04')
            score_board_remove()
            set_portal(portalId=2, visible=True, enabled=True, minimapVisible=True)
            return 종료()


class 종료(state.State):
    pass


