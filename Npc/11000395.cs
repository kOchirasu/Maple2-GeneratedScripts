using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000395: Yamoto
/// </summary>
public class _11000395 : NpcScript {
    internal _11000395(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407001603$ 
                // - Can I help you? 
                return true;
            case 20:
                // $script:0831180407001605$ 
                // - Everyone here works hard, including me, but we can't ever seem to get ahead. It's sad, and I've heard $map:02000100$'s mayor is responsible for keeping us all poor.  
                return true;
            default:
                return true;
        }
    }
}
