using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004059: Beatrice
/// </summary>
public class _11004059 : NpcScript {
    internal _11004059(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0614185307010091$ 
                // - The Alemani family will devote all of their resources to aid in the recovery effort.
                return true;
            case 10:
                // $script:0614185307010092$ 
                // - My other half... You have forged a blood oath. I expect you to aid me til the very end.
                return true;
            default:
                return true;
        }
    }
}
