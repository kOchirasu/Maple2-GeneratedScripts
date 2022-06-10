using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001891: Blackeye
/// </summary>
public class _11001891 : NpcScript {
    internal _11001891(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1101100307007368$ 
                // - Hm... 
                return true;
            case 10:
                // $script:1101100307007369$ 
                // - Thank you for coming here.
                return true;
            default:
                return true;
        }
    }
}
