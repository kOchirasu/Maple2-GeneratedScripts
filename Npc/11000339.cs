using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000339: Maccachi
/// </summary>
public class _11000339 : NpcScript {
    internal _11000339(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001358$ 
                // - Can I help you? 
                return true;
            case 10:
                // $script:0831180407001359$ 
                // - Ah, I want to be a great hotelier someday! 
                return true;
            default:
                return true;
        }
    }
}
