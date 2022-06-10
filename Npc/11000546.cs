using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000546: Ebby
/// </summary>
public class _11000546 : NpcScript {
    internal _11000546(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002318$ 
                // - What seems to be the problem?
                return true;
            case 10:
                // $script:0831180407002319$ 
                // - Want to see what I've got inside this bundle? Then show me your wallet first! Ha, just kidding...
                return true;
            default:
                return true;
        }
    }
}
