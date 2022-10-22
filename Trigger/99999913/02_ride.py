""" trigger/99999913/02_ride.xml """
from common import *
import state


class Wait(state.State):
    def on_enter(self):
        set_user_value(key='SetRide', value=0)
        set_user_value(key='StartPatrol', value=0)

    def on_tick(self) -> state.State:
        if user_value(key='SetRide', value=1):
            return Ride01_Ready()
        if user_value(key='SetRide', value=2):
            return Ride02_Ready()
        if user_value(key='SetRide', value=3):
            return Ride03_Ready()
        if user_value(key='SetRide', value=4):
            return Ride04_Ready()
        if user_value(key='SetRide', value=5):
            return Ride05_Ready()
        if user_value(key='SetRide', value=6):
            return Ride06_Ready()
        if user_value(key='SetRide', value=7):
            return Ride07_Ready()
        if user_value(key='SetRide', value=8):
            return Ride08_Ready()


#  North_To_South 
class Ride01_Ready(state.State):
    def on_enter(self):
        create_monster(spawnIds=[110], arg2=False) # North_To_South
        write_log(logName='Survival', arg3='bus_01') # 서바이벌 버스 로그

    def on_tick(self) -> state.State:
        if user_value(key='StartPatrol', value=1):
            return Ride01_StartPatrolDelay()


class Ride01_StartPatrolDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Ride01_StartPatrol()


class Ride01_StartPatrol(state.State):
    def on_enter(self):
        move_npc(spawnId=110, patrolName='MS2PatrolData_110') # North_To_South

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=36000):
            return Quit()


#  South_To_North 
class Ride02_Ready(state.State):
    def on_enter(self):
        create_monster(spawnIds=[120], arg2=False) # South_To_North
        write_log(logName='Survival', arg3='bus_02') # 서바이벌 버스 로그

    def on_tick(self) -> state.State:
        if user_value(key='StartPatrol', value=1):
            return Ride02_StartPatrolDelay()


class Ride02_StartPatrolDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Ride02_StartPatrol()


class Ride02_StartPatrol(state.State):
    def on_enter(self):
        move_npc(spawnId=120, patrolName='MS2PatrolData_120') # South_To_North

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=36000):
            return Quit()


#  East_To_West 
class Ride03_Ready(state.State):
    def on_enter(self):
        create_monster(spawnIds=[130], arg2=False) # East_To_West
        write_log(logName='Survival', arg3='bus_03') # 서바이벌 버스 로그

    def on_tick(self) -> state.State:
        if user_value(key='StartPatrol', value=1):
            return Ride03_StartPatrolDelay()


class Ride03_StartPatrolDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Ride03_StartPatrol()


class Ride03_StartPatrol(state.State):
    def on_enter(self):
        move_npc(spawnId=130, patrolName='MS2PatrolData_130') # East_To_West

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=36000):
            return Quit()


#  West_To_East 
class Ride04_Ready(state.State):
    def on_enter(self):
        create_monster(spawnIds=[140], arg2=False) # West_To_East
        write_log(logName='Survival', arg3='bus_04') # 서바이벌 버스 로그

    def on_tick(self) -> state.State:
        if user_value(key='StartPatrol', value=1):
            return Ride04_StartPatrolDelay()


class Ride04_StartPatrolDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Ride04_StartPatrol()


class Ride04_StartPatrol(state.State):
    def on_enter(self):
        move_npc(spawnId=140, patrolName='MS2PatrolData_140') # North_To_South

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=36000):
            return Quit()


#  West_To_East 
class Ride05_Ready(state.State):
    def on_enter(self):
        create_monster(spawnIds=[150], arg2=False) # NorthWest_To_SouthEast
        write_log(logName='Survival', arg3='bus_05') # 서바이벌 버스 로그

    def on_tick(self) -> state.State:
        if user_value(key='StartPatrol', value=1):
            return Ride05_StartPatrolDelay()


class Ride05_StartPatrolDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Ride05_StartPatrol()


class Ride05_StartPatrol(state.State):
    def on_enter(self):
        move_npc(spawnId=150, patrolName='MS2PatrolData_150') # NorthWest_To_SouthEast

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=36000):
            return Quit()


#  NorthEast_To_SouthWest 
class Ride06_Ready(state.State):
    def on_enter(self):
        create_monster(spawnIds=[160], arg2=False) # NorthEast_To_SouthWest
        write_log(logName='Survival', arg3='bus_06') # 서바이벌 버스 로그

    def on_tick(self) -> state.State:
        if user_value(key='StartPatrol', value=1):
            return Ride06_StartPatrolDelay()


class Ride06_StartPatrolDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Ride06_StartPatrol()


class Ride06_StartPatrol(state.State):
    def on_enter(self):
        move_npc(spawnId=160, patrolName='MS2PatrolData_160') # NorthEast_To_SouthWest

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=36000):
            return Quit()


#  SouthWest_To_NorthEast 
class Ride07_Ready(state.State):
    def on_enter(self):
        create_monster(spawnIds=[170], arg2=False) # SouthWest_To_NorthEast
        write_log(logName='Survival', arg3='bus_07') # 서바이벌 버스 로그

    def on_tick(self) -> state.State:
        if user_value(key='StartPatrol', value=1):
            return Ride07_StartPatrolDelay()


class Ride07_StartPatrolDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Ride07_StartPatrol()


class Ride07_StartPatrol(state.State):
    def on_enter(self):
        move_npc(spawnId=170, patrolName='MS2PatrolData_170') # SouthWest_To_NorthEast

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=36000):
            return Quit()


#  SouthEast_To_NorthWest 
class Ride08_Ready(state.State):
    def on_enter(self):
        create_monster(spawnIds=[180], arg2=False) # SouthEast_To_NorthWest
        write_log(logName='Survival', arg3='bus_08') # 서바이벌 버스 로그

    def on_tick(self) -> state.State:
        if user_value(key='StartPatrol', value=1):
            return Ride08_StartPatrolDelay()


class Ride08_StartPatrolDelay(state.State):
    def on_tick(self) -> state.State:
        if wait_tick(waitTick=2000):
            return Ride08_StartPatrol()


class Ride08_StartPatrol(state.State):
    def on_enter(self):
        move_npc(spawnId=180, patrolName='MS2PatrolData_180') # SouthEast_To_NorthWest

    def on_tick(self) -> state.State:
        if wait_tick(waitTick=36000):
            return Quit()


class Quit(state.State):
    def on_enter(self):
        destroy_monster(spawnIds=[110,120,130,140,150,160,170,180])
        write_log(logName='Survival', arg3='bus_end') # 서바이벌 버스 로그


