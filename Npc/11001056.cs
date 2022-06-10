using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001056: Intertimer
/// </summary>
public class _11001056 : NpcScript {
    internal _11001056(INpcScriptContext context) : base(context) {
        // TODO: Job 1
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180610001152$ 
                // - This teleportation device is on a test run.
                return true;
            case 1:
                // $script:0831180610001153$ 
                // - Do you want to use this experimental teleportation device?
                //   Destination: $map:02000259$
                //   Cost: 5,000 mesos
                return true;
            case 10:
                // $script:0831180610001154$ 
                // - The testing period of this teleportation device has ended.
                return true;
            case 20:
                // $script:0831180610001155$ 
                // - You do not have enough money to use this experimental teleportation device. It costs 5,000 mesos to use.
                return true;
            default:
                return true;
        }
    }
}
