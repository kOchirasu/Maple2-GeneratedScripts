using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003153: Rudy
/// </summary>
public class _11003153 : NpcScript {
    internal _11003153(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0306155707008035$ 
                // - How may I help you? 
                return true;
            case 30:
                // $script:0306155707008038$ 
                // - $MyPCName$, did you come to enjoy the flowers? So did I! 
                return true;
            default:
                return true;
        }
    }
}
