using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000644: Prisoner 160917
/// </summary>
public class _11000644 : NpcScript {
    internal _11000644(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002629$ 
                // - Get me out of here... 
                return true;
            case 30:
                // $script:0831180407002632$ 
                // - Ah... I'm bored...
                return true;
            default:
                return true;
        }
    }
}
