using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001477: Blackstar Gangster
/// </summary>
public class _11001477 : NpcScript {
    internal _11001477(INpcScriptContext context) : base(context) {
        Id = 20;
        // TODO: RandomPick 20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1228113207005717$ 
                // - What brings you here?
                return true;
            case 20:
                // $script:1228113207005719$ 
                // - Those weren't ordinary train robbers.
                return true;
            default:
                return true;
        }
    }
}
