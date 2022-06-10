using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000643: Prisoner 150125
/// </summary>
public class _11000643 : NpcScript {
    internal _11000643(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002624$ 
                // - Get me out of here... 
                return true;
            case 40:
                // $script:0831180407002628$ 
                // - Argh, this place is a sty! I hate prison! 
                return true;
            default:
                return true;
        }
    }
}
