using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000476: Goldus's Secretary
/// </summary>
public class _11000476 : NpcScript {
    internal _11000476(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002075$ 
                // - May I help you?
                return true;
            case 30:
                // $script:0831180407002077$ 
                // - $map:02000100$ would never have been developed without the help of $npcName:11000252[gender:0]$!
                return true;
            default:
                return true;
        }
    }
}
