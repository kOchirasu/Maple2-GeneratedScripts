using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001112: Bella's Soul
/// </summary>
public class _11001112 : NpcScript {
    internal _11001112(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0908154107003738$ 
                // - Do you know me?
                return true;
            case 30:
                // $script:0908154107003739$ 
                // - I... I can't go back like this... No... 
                return true;
            default:
                return true;
        }
    }
}
