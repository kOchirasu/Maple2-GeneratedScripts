""" trigger/02000347_bf/fire.xml """
from common import *
import state


class 대기(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050], visible=False, arg3=0, arg4=0)
        set_skill(triggerIds=[7001], isEnable=False)
        set_skill(triggerIds=[7002], isEnable=False)
        set_skill(triggerIds=[7003], isEnable=False)
        set_skill(triggerIds=[7004], isEnable=False)
        set_skill(triggerIds=[7005], isEnable=False)
        set_skill(triggerIds=[7006], isEnable=False)
        set_skill(triggerIds=[7007], isEnable=False)
        set_skill(triggerIds=[7008], isEnable=False)
        set_skill(triggerIds=[7009], isEnable=False)
        set_skill(triggerIds=[7010], isEnable=False)
        set_skill(triggerIds=[7011], isEnable=False)
        set_skill(triggerIds=[7012], isEnable=False)
        set_skill(triggerIds=[7013], isEnable=False)
        set_skill(triggerIds=[7014], isEnable=False)
        set_skill(triggerIds=[7015], isEnable=False)
        set_skill(triggerIds=[7016], isEnable=False)
        set_skill(triggerIds=[7017], isEnable=False)
        set_skill(triggerIds=[7018], isEnable=False)
        set_skill(triggerIds=[7019], isEnable=False)
        set_skill(triggerIds=[7020], isEnable=False)
        set_skill(triggerIds=[7021], isEnable=False)
        set_skill(triggerIds=[7022], isEnable=False)
        set_skill(triggerIds=[7023], isEnable=False)
        set_skill(triggerIds=[7024], isEnable=False)
        set_skill(triggerIds=[7025], isEnable=False)
        set_skill(triggerIds=[7026], isEnable=False)
        set_skill(triggerIds=[7027], isEnable=False)
        set_skill(triggerIds=[7028], isEnable=False)
        set_skill(triggerIds=[7029], isEnable=False)
        set_skill(triggerIds=[7030], isEnable=False)
        set_skill(triggerIds=[7031], isEnable=False)
        set_skill(triggerIds=[7032], isEnable=False)
        set_skill(triggerIds=[7033], isEnable=False)
        set_skill(triggerIds=[7034], isEnable=False)
        set_skill(triggerIds=[7035], isEnable=False)
        set_skill(triggerIds=[7036], isEnable=False)
        set_skill(triggerIds=[7037], isEnable=False)
        set_skill(triggerIds=[7038], isEnable=False)
        set_skill(triggerIds=[7039], isEnable=False)
        set_skill(triggerIds=[7040], isEnable=False)
        set_skill(triggerIds=[7041], isEnable=False)
        set_skill(triggerIds=[7042], isEnable=False)
        set_skill(triggerIds=[7043], isEnable=False)
        set_skill(triggerIds=[7044], isEnable=False)
        set_skill(triggerIds=[7045], isEnable=False)
        set_skill(triggerIds=[7046], isEnable=False)
        set_skill(triggerIds=[7047], isEnable=False)
        set_skill(triggerIds=[7048], isEnable=False)
        set_skill(triggerIds=[7049], isEnable=False)
        set_skill(triggerIds=[7050], isEnable=False)
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)
        set_effect(triggerIds=[604], visible=False)
        set_effect(triggerIds=[605], visible=False)
        set_effect(triggerIds=[606], visible=False)
        set_effect(triggerIds=[607], visible=False)
        set_effect(triggerIds=[608], visible=False)
        set_effect(triggerIds=[609], visible=False)
        set_effect(triggerIds=[610], visible=False)
        set_effect(triggerIds=[611], visible=False)
        set_effect(triggerIds=[612], visible=False)
        set_effect(triggerIds=[613], visible=False)
        set_effect(triggerIds=[614], visible=False)
        set_effect(triggerIds=[615], visible=False)
        set_effect(triggerIds=[616], visible=False)
        set_effect(triggerIds=[617], visible=False)
        set_effect(triggerIds=[618], visible=False)
        set_effect(triggerIds=[619], visible=False)
        set_effect(triggerIds=[620], visible=False)
        set_effect(triggerIds=[621], visible=False)
        set_effect(triggerIds=[622], visible=False)
        set_effect(triggerIds=[623], visible=False)
        set_effect(triggerIds=[624], visible=False)
        set_effect(triggerIds=[625], visible=False)
        set_effect(triggerIds=[626], visible=False)
        set_effect(triggerIds=[627], visible=False)
        set_effect(triggerIds=[628], visible=False)
        set_effect(triggerIds=[629], visible=False)
        set_effect(triggerIds=[630], visible=False)
        set_effect(triggerIds=[631], visible=False)
        set_effect(triggerIds=[632], visible=False)
        set_effect(triggerIds=[633], visible=False)
        set_effect(triggerIds=[634], visible=False)
        set_effect(triggerIds=[635], visible=False)
        set_effect(triggerIds=[636], visible=False)
        set_effect(triggerIds=[637], visible=False)
        set_effect(triggerIds=[638], visible=False)
        set_effect(triggerIds=[639], visible=False)
        set_effect(triggerIds=[640], visible=False)
        set_effect(triggerIds=[641], visible=False)
        set_effect(triggerIds=[642], visible=False)
        set_effect(triggerIds=[643], visible=False)
        set_effect(triggerIds=[644], visible=False)
        set_effect(triggerIds=[645], visible=False)
        set_effect(triggerIds=[646], visible=False)
        set_effect(triggerIds=[647], visible=False)
        set_effect(triggerIds=[648], visible=False)
        set_effect(triggerIds=[649], visible=False)
        set_effect(triggerIds=[650], visible=False)

    def on_tick(self) -> state.State:
        if user_detected(boxIds=[60002]):
            return 시작()


class 시작(state.State):
    def on_enter(self):
        set_mesh(triggerIds=[3001,3002,3003,3004,3005,3006,3007,3008,3009,3010,3011,3012,3013,3014,3015,3016,3017,3018,3019,3020,3021,3022,3023,3024,3025,3026,3027,3028,3029,3030,3031,3032,3033,3034,3035,3036,3037,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050], visible=False, arg3=0, arg4=2)
        set_skill(triggerIds=[7001], isEnable=False)
        set_skill(triggerIds=[7002], isEnable=False)
        set_skill(triggerIds=[7003], isEnable=False)
        set_skill(triggerIds=[7004], isEnable=False)
        set_skill(triggerIds=[7005], isEnable=False)
        set_skill(triggerIds=[7006], isEnable=False)
        set_skill(triggerIds=[7007], isEnable=False)
        set_skill(triggerIds=[7008], isEnable=False)
        set_skill(triggerIds=[7009], isEnable=False)
        set_skill(triggerIds=[7010], isEnable=False)
        set_skill(triggerIds=[7011], isEnable=False)
        set_skill(triggerIds=[7012], isEnable=False)
        set_skill(triggerIds=[7013], isEnable=False)
        set_skill(triggerIds=[7014], isEnable=False)
        set_skill(triggerIds=[7015], isEnable=False)
        set_skill(triggerIds=[7016], isEnable=False)
        set_skill(triggerIds=[7017], isEnable=False)
        set_skill(triggerIds=[7018], isEnable=False)
        set_skill(triggerIds=[7019], isEnable=False)
        set_skill(triggerIds=[7020], isEnable=False)
        set_skill(triggerIds=[7021], isEnable=False)
        set_skill(triggerIds=[7022], isEnable=False)
        set_skill(triggerIds=[7023], isEnable=False)
        set_skill(triggerIds=[7024], isEnable=False)
        set_skill(triggerIds=[7025], isEnable=False)
        set_skill(triggerIds=[7026], isEnable=False)
        set_skill(triggerIds=[7027], isEnable=False)
        set_skill(triggerIds=[7028], isEnable=False)
        set_skill(triggerIds=[7029], isEnable=False)
        set_skill(triggerIds=[7030], isEnable=False)
        set_skill(triggerIds=[7031], isEnable=False)
        set_skill(triggerIds=[7032], isEnable=False)
        set_skill(triggerIds=[7033], isEnable=False)
        set_skill(triggerIds=[7034], isEnable=False)
        set_skill(triggerIds=[7035], isEnable=False)
        set_skill(triggerIds=[7036], isEnable=False)
        set_skill(triggerIds=[7037], isEnable=False)
        set_skill(triggerIds=[7038], isEnable=False)
        set_skill(triggerIds=[7039], isEnable=False)
        set_skill(triggerIds=[7040], isEnable=False)
        set_skill(triggerIds=[7041], isEnable=False)
        set_skill(triggerIds=[7042], isEnable=False)
        set_skill(triggerIds=[7043], isEnable=False)
        set_skill(triggerIds=[7044], isEnable=False)
        set_skill(triggerIds=[7045], isEnable=False)
        set_skill(triggerIds=[7046], isEnable=False)
        set_skill(triggerIds=[7047], isEnable=False)
        set_skill(triggerIds=[7048], isEnable=False)
        set_skill(triggerIds=[7049], isEnable=False)
        set_skill(triggerIds=[7050], isEnable=False)
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)
        set_effect(triggerIds=[604], visible=False)
        set_effect(triggerIds=[605], visible=False)
        set_effect(triggerIds=[606], visible=False)
        set_effect(triggerIds=[607], visible=False)
        set_effect(triggerIds=[608], visible=False)
        set_effect(triggerIds=[609], visible=False)
        set_effect(triggerIds=[610], visible=False)
        set_effect(triggerIds=[611], visible=False)
        set_effect(triggerIds=[612], visible=False)
        set_effect(triggerIds=[613], visible=False)
        set_effect(triggerIds=[614], visible=False)
        set_effect(triggerIds=[615], visible=False)
        set_effect(triggerIds=[616], visible=False)
        set_effect(triggerIds=[617], visible=False)
        set_effect(triggerIds=[618], visible=False)
        set_effect(triggerIds=[619], visible=False)
        set_effect(triggerIds=[620], visible=False)
        set_effect(triggerIds=[621], visible=False)
        set_effect(triggerIds=[622], visible=False)
        set_effect(triggerIds=[623], visible=False)
        set_effect(triggerIds=[624], visible=False)
        set_effect(triggerIds=[625], visible=False)
        set_effect(triggerIds=[626], visible=False)
        set_effect(triggerIds=[627], visible=False)
        set_effect(triggerIds=[628], visible=False)
        set_effect(triggerIds=[629], visible=False)
        set_effect(triggerIds=[630], visible=False)
        set_effect(triggerIds=[631], visible=False)
        set_effect(triggerIds=[632], visible=False)
        set_effect(triggerIds=[633], visible=False)
        set_effect(triggerIds=[634], visible=False)
        set_effect(triggerIds=[635], visible=False)
        set_effect(triggerIds=[636], visible=False)
        set_effect(triggerIds=[637], visible=False)
        set_effect(triggerIds=[638], visible=False)
        set_effect(triggerIds=[639], visible=False)
        set_effect(triggerIds=[640], visible=False)
        set_effect(triggerIds=[641], visible=False)
        set_effect(triggerIds=[642], visible=False)
        set_effect(triggerIds=[643], visible=False)
        set_effect(triggerIds=[644], visible=False)
        set_effect(triggerIds=[645], visible=False)
        set_effect(triggerIds=[646], visible=False)
        set_effect(triggerIds=[647], visible=False)
        set_effect(triggerIds=[648], visible=False)
        set_effect(triggerIds=[649], visible=False)
        set_effect(triggerIds=[650], visible=False)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if monster_dead(boxIds=[101]):
            return 종료()


class 랜덤스킬작동(state.State):
    def on_tick(self) -> state.State:
        if random_condition(rate=2):
            return 번생성1()
        if random_condition(rate=2):
            return 번생성2()
        if random_condition(rate=2):
            return 번생성3()
        if random_condition(rate=2):
            return 번생성4()
        if random_condition(rate=2):
            return 번생성5()
        if random_condition(rate=2):
            return 번생성6()
        if random_condition(rate=2):
            return 번생성7()
        if random_condition(rate=2):
            return 번생성8()
        if random_condition(rate=2):
            return 번생성9()
        if random_condition(rate=2):
            return 번생성10()
        if random_condition(rate=2):
            return 번생성11()
        if random_condition(rate=2):
            return 번생성12()
        if random_condition(rate=2):
            return 번생성13()
        if random_condition(rate=2):
            return 번생성14()
        if random_condition(rate=2):
            return 번생성15()
        if random_condition(rate=2):
            return 번생성16()
        if random_condition(rate=2):
            return 번생성17()
        if random_condition(rate=2):
            return 번생성18()
        if random_condition(rate=2):
            return 번생성19()
        if random_condition(rate=2):
            return 번생성20()
        if random_condition(rate=2):
            return 번생성21()
        if random_condition(rate=2):
            return 번생성22()
        if random_condition(rate=2):
            return 번생성23()
        if random_condition(rate=2):
            return 번생성24()
        if random_condition(rate=2):
            return 번생성25()
        if random_condition(rate=2):
            return 번생성26()
        if random_condition(rate=2):
            return 번생성27()
        if random_condition(rate=2):
            return 번생성28()
        if random_condition(rate=2):
            return 번생성29()
        if random_condition(rate=2):
            return 번생성30()
        if random_condition(rate=2):
            return 번생성31()
        if random_condition(rate=2):
            return 번생성32()
        if random_condition(rate=2):
            return 번생성33()
        if random_condition(rate=2):
            return 번생성34()
        if random_condition(rate=2):
            return 번생성35()
        if random_condition(rate=2):
            return 번생성36()
        if random_condition(rate=2):
            return 번생성37()
        if random_condition(rate=2):
            return 번생성38()
        if random_condition(rate=2):
            return 번생성39()
        if random_condition(rate=2):
            return 번생성40()
        if random_condition(rate=2):
            return 번생성41()
        if random_condition(rate=2):
            return 번생성42()
        if random_condition(rate=2):
            return 번생성43()
        if random_condition(rate=2):
            return 번생성44()
        if random_condition(rate=2):
            return 번생성45()
        if random_condition(rate=2):
            return 번생성46()
        if random_condition(rate=2):
            return 번생성47()
        if random_condition(rate=2):
            return 번생성48()
        if random_condition(rate=2):
            return 번생성49()
        if random_condition(rate=2):
            return 번생성50()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()


class 번생성1(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7001], isEnable=True)
        set_effect(triggerIds=[601], visible=True)
        set_mesh(triggerIds=[3001], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성2(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7002], isEnable=True)
        set_effect(triggerIds=[602], visible=True)
        set_mesh(triggerIds=[3002], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성3(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7003], isEnable=True)
        set_effect(triggerIds=[603], visible=True)
        set_mesh(triggerIds=[3003], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성4(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7004], isEnable=True)
        set_effect(triggerIds=[604], visible=True)
        set_mesh(triggerIds=[3004], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성5(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7005], isEnable=True)
        set_effect(triggerIds=[605], visible=True)
        set_mesh(triggerIds=[3005], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성6(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7006], isEnable=True)
        set_effect(triggerIds=[606], visible=True)
        set_mesh(triggerIds=[3006], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성7(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7007], isEnable=True)
        set_effect(triggerIds=[607], visible=True)
        set_mesh(triggerIds=[3007], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성8(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7008], isEnable=True)
        set_effect(triggerIds=[608], visible=True)
        set_mesh(triggerIds=[3008], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성9(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7009], isEnable=True)
        set_effect(triggerIds=[609], visible=True)
        set_mesh(triggerIds=[3009], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성10(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7010], isEnable=True)
        set_effect(triggerIds=[610], visible=True)
        set_mesh(triggerIds=[3010], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성11(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7011], isEnable=True)
        set_effect(triggerIds=[611], visible=True)
        set_mesh(triggerIds=[3011], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성12(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7012], isEnable=True)
        set_effect(triggerIds=[612], visible=True)
        set_mesh(triggerIds=[3012], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성13(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7013], isEnable=True)
        set_effect(triggerIds=[613], visible=True)
        set_mesh(triggerIds=[3013], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성14(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7014], isEnable=True)
        set_effect(triggerIds=[614], visible=True)
        set_mesh(triggerIds=[3014], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성15(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7015], isEnable=True)
        set_effect(triggerIds=[615], visible=True)
        set_mesh(triggerIds=[3015], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성16(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7016], isEnable=True)
        set_effect(triggerIds=[616], visible=True)
        set_mesh(triggerIds=[3016], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성17(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7017], isEnable=True)
        set_effect(triggerIds=[617], visible=True)
        set_mesh(triggerIds=[3017], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성18(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7018], isEnable=True)
        set_effect(triggerIds=[618], visible=True)
        set_mesh(triggerIds=[3018], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성19(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7019], isEnable=True)
        set_effect(triggerIds=[619], visible=True)
        set_mesh(triggerIds=[3019], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성20(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7020], isEnable=True)
        set_effect(triggerIds=[620], visible=True)
        set_mesh(triggerIds=[3020], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성21(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7021], isEnable=True)
        set_effect(triggerIds=[621], visible=True)
        set_mesh(triggerIds=[3021], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성22(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7022], isEnable=True)
        set_effect(triggerIds=[622], visible=True)
        set_mesh(triggerIds=[3022], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성23(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7023], isEnable=True)
        set_effect(triggerIds=[623], visible=True)
        set_mesh(triggerIds=[3023], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성24(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7024], isEnable=True)
        set_effect(triggerIds=[624], visible=True)
        set_mesh(triggerIds=[3024], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성25(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7025], isEnable=True)
        set_effect(triggerIds=[625], visible=True)
        set_mesh(triggerIds=[3025], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성26(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7026], isEnable=True)
        set_effect(triggerIds=[626], visible=True)
        set_mesh(triggerIds=[3026], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성27(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7027], isEnable=True)
        set_effect(triggerIds=[627], visible=True)
        set_mesh(triggerIds=[3027], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성28(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7028], isEnable=True)
        set_effect(triggerIds=[628], visible=True)
        set_mesh(triggerIds=[3028], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성29(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7029], isEnable=True)
        set_effect(triggerIds=[629], visible=True)
        set_mesh(triggerIds=[3029], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성30(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7030], isEnable=True)
        set_effect(triggerIds=[630], visible=True)
        set_mesh(triggerIds=[3030], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성31(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7031], isEnable=True)
        set_effect(triggerIds=[631], visible=True)
        set_mesh(triggerIds=[3031], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성32(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7032], isEnable=True)
        set_effect(triggerIds=[632], visible=True)
        set_mesh(triggerIds=[3032], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성33(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7033], isEnable=True)
        set_effect(triggerIds=[633], visible=True)
        set_mesh(triggerIds=[3033], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성34(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7034], isEnable=True)
        set_effect(triggerIds=[634], visible=True)
        set_mesh(triggerIds=[3034], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성35(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7035], isEnable=True)
        set_effect(triggerIds=[635], visible=True)
        set_mesh(triggerIds=[3035], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성36(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7036], isEnable=True)
        set_effect(triggerIds=[636], visible=True)
        set_mesh(triggerIds=[3036], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성37(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7037], isEnable=True)
        set_effect(triggerIds=[637], visible=True)
        set_mesh(triggerIds=[3037], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성38(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7038], isEnable=True)
        set_effect(triggerIds=[638], visible=True)
        set_mesh(triggerIds=[3038], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성39(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7039], isEnable=True)
        set_effect(triggerIds=[639], visible=True)
        set_mesh(triggerIds=[3039], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성40(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7040], isEnable=True)
        set_effect(triggerIds=[640], visible=True)
        set_mesh(triggerIds=[3040], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성41(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7041], isEnable=True)
        set_effect(triggerIds=[641], visible=True)
        set_mesh(triggerIds=[3041], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성42(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7042], isEnable=True)
        set_effect(triggerIds=[642], visible=True)
        set_mesh(triggerIds=[3042], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성43(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7043], isEnable=True)
        set_effect(triggerIds=[643], visible=True)
        set_mesh(triggerIds=[3043], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성44(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7044], isEnable=True)
        set_effect(triggerIds=[644], visible=True)
        set_mesh(triggerIds=[3044], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성45(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7045], isEnable=True)
        set_effect(triggerIds=[645], visible=True)
        set_mesh(triggerIds=[3045], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성46(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7046], isEnable=True)
        set_effect(triggerIds=[646], visible=True)
        set_mesh(triggerIds=[3046], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성47(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7047], isEnable=True)
        set_effect(triggerIds=[647], visible=True)
        set_mesh(triggerIds=[3047], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성48(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7048], isEnable=True)
        set_effect(triggerIds=[648], visible=True)
        set_mesh(triggerIds=[3048], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성49(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7049], isEnable=True)
        set_effect(triggerIds=[649], visible=True)
        set_mesh(triggerIds=[3049], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 번생성50(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7050], isEnable=True)
        set_effect(triggerIds=[650], visible=True)
        set_mesh(triggerIds=[3050], visible=True, arg3=0, arg4=1)
        set_timer(timerId='3', seconds=3)

    def on_tick(self) -> state.State:
        if time_expired(timerId='3'):
            return 랜덤스킬작동()
        if object_interacted(interactIds=[10000804], arg2=0):
            return 시작()
        if monster_dead(boxIds=[101]):
            return 종료()


class 종료(state.State):
    def on_enter(self):
        set_skill(triggerIds=[7001], isEnable=False)
        set_skill(triggerIds=[7002], isEnable=False)
        set_skill(triggerIds=[7003], isEnable=False)
        set_skill(triggerIds=[7004], isEnable=False)
        set_skill(triggerIds=[7005], isEnable=False)
        set_skill(triggerIds=[7006], isEnable=False)
        set_skill(triggerIds=[7007], isEnable=False)
        set_skill(triggerIds=[7008], isEnable=False)
        set_skill(triggerIds=[7009], isEnable=False)
        set_skill(triggerIds=[7010], isEnable=False)
        set_skill(triggerIds=[7011], isEnable=False)
        set_skill(triggerIds=[7012], isEnable=False)
        set_skill(triggerIds=[7013], isEnable=False)
        set_skill(triggerIds=[7014], isEnable=False)
        set_skill(triggerIds=[7015], isEnable=False)
        set_skill(triggerIds=[7016], isEnable=False)
        set_skill(triggerIds=[7017], isEnable=False)
        set_skill(triggerIds=[7018], isEnable=False)
        set_skill(triggerIds=[7019], isEnable=False)
        set_skill(triggerIds=[7020], isEnable=False)
        set_skill(triggerIds=[7021], isEnable=False)
        set_skill(triggerIds=[7022], isEnable=False)
        set_skill(triggerIds=[7023], isEnable=False)
        set_skill(triggerIds=[7024], isEnable=False)
        set_skill(triggerIds=[7025], isEnable=False)
        set_skill(triggerIds=[7026], isEnable=False)
        set_skill(triggerIds=[7027], isEnable=False)
        set_skill(triggerIds=[7028], isEnable=False)
        set_skill(triggerIds=[7029], isEnable=False)
        set_skill(triggerIds=[7030], isEnable=False)
        set_skill(triggerIds=[7031], isEnable=False)
        set_skill(triggerIds=[7032], isEnable=False)
        set_skill(triggerIds=[7033], isEnable=False)
        set_skill(triggerIds=[7034], isEnable=False)
        set_skill(triggerIds=[7035], isEnable=False)
        set_skill(triggerIds=[7036], isEnable=False)
        set_skill(triggerIds=[7037], isEnable=False)
        set_skill(triggerIds=[7038], isEnable=False)
        set_skill(triggerIds=[7039], isEnable=False)
        set_skill(triggerIds=[7040], isEnable=False)
        set_skill(triggerIds=[7041], isEnable=False)
        set_skill(triggerIds=[7042], isEnable=False)
        set_skill(triggerIds=[7043], isEnable=False)
        set_skill(triggerIds=[7044], isEnable=False)
        set_skill(triggerIds=[7045], isEnable=False)
        set_skill(triggerIds=[7046], isEnable=False)
        set_skill(triggerIds=[7047], isEnable=False)
        set_skill(triggerIds=[7048], isEnable=False)
        set_skill(triggerIds=[7049], isEnable=False)
        set_skill(triggerIds=[7050], isEnable=False)
        set_effect(triggerIds=[601], visible=False)
        set_effect(triggerIds=[602], visible=False)
        set_effect(triggerIds=[603], visible=False)
        set_effect(triggerIds=[604], visible=False)
        set_effect(triggerIds=[605], visible=False)
        set_effect(triggerIds=[606], visible=False)
        set_effect(triggerIds=[607], visible=False)
        set_effect(triggerIds=[608], visible=False)
        set_effect(triggerIds=[609], visible=False)
        set_effect(triggerIds=[610], visible=False)
        set_effect(triggerIds=[611], visible=False)
        set_effect(triggerIds=[612], visible=False)
        set_effect(triggerIds=[613], visible=False)
        set_effect(triggerIds=[614], visible=False)
        set_effect(triggerIds=[615], visible=False)
        set_effect(triggerIds=[616], visible=False)
        set_effect(triggerIds=[617], visible=False)
        set_effect(triggerIds=[618], visible=False)
        set_effect(triggerIds=[619], visible=False)
        set_effect(triggerIds=[620], visible=False)
        set_effect(triggerIds=[621], visible=False)
        set_effect(triggerIds=[622], visible=False)
        set_effect(triggerIds=[623], visible=False)
        set_effect(triggerIds=[624], visible=False)
        set_effect(triggerIds=[625], visible=False)
        set_effect(triggerIds=[626], visible=False)
        set_effect(triggerIds=[627], visible=False)
        set_effect(triggerIds=[628], visible=False)
        set_effect(triggerIds=[629], visible=False)
        set_effect(triggerIds=[630], visible=False)
        set_effect(triggerIds=[631], visible=False)
        set_effect(triggerIds=[632], visible=False)
        set_effect(triggerIds=[633], visible=False)
        set_effect(triggerIds=[634], visible=False)
        set_effect(triggerIds=[635], visible=False)
        set_effect(triggerIds=[636], visible=False)
        set_effect(triggerIds=[637], visible=False)
        set_effect(triggerIds=[638], visible=False)
        set_effect(triggerIds=[639], visible=False)
        set_effect(triggerIds=[640], visible=False)
        set_effect(triggerIds=[641], visible=False)
        set_effect(triggerIds=[642], visible=False)
        set_effect(triggerIds=[643], visible=False)
        set_effect(triggerIds=[644], visible=False)
        set_effect(triggerIds=[645], visible=False)
        set_effect(triggerIds=[646], visible=False)
        set_effect(triggerIds=[647], visible=False)
        set_effect(triggerIds=[648], visible=False)
        set_effect(triggerIds=[649], visible=False)
        set_effect(triggerIds=[650], visible=False)


