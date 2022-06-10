using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000664: Deke
/// </summary>
public class _11000664 : NpcScript {
    internal _11000664(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002699$ 
                // - What is it?
                return true;
            case 30:
                // $script:0831180407002701$ 
                // - Do you believe in love at first sight? I do. I fell in love with $npcName:11000151[gender:1]$...
                return true;
            default:
                return true;
        }
    }
}
