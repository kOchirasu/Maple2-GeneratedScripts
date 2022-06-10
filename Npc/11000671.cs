using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000671: Misplaced Book
/// </summary>
public class _11000671 : NpcScript {
    internal _11000671(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002735$ 
                // - Yes, here! 
                return true;
            case 10:
                // $script:0831180407002736$ 
                // - It's locked! You need a key! 
                return true;
            case 20:
                // $script:0831180407002737$ 
                // - Make sure to return books to where they belong! 
                return true;
            default:
                return true;
        }
    }
}
