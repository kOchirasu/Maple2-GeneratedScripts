using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000483: Bunny Gal
/// </summary>
public class _11000483 : NpcScript {
    internal _11000483(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 50;60
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002119$ 
                // - Welcome, $MyPCName$!
                return true;
            case 50:
                // $script:0831180407002124$ 
                // - You're amazing!
                return true;
            case 60:
                // $script:0831180407002125$ 
                // - You did it! Good job!
                return true;
            default:
                return true;
        }
    }
}
