using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003441: Pathos
/// </summary>
public class _11003441 : NpcScript {
    internal _11003441(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0721140007008689$ 
                // - It's you. 
                return true;
            case 10:
                // $script:0721142007008707$ 
                // - It's you. 
                return true;
            default:
                return true;
        }
    }
}
