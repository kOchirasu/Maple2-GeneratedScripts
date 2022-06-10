using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000596: Ting
/// </summary>
public class _11000596 : NpcScript {
    internal _11000596(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002392$ 
                // - I'm busy, so busy!
                return true;
            case 30:
                // $script:0831180407002395$ 
                // - I have to do homework, and I have to study... 
                return true;
            default:
                return true;
        }
    }
}
