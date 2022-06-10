using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000182: Junkyard Worker
/// </summary>
public class _11000182 : NpcScript {
    internal _11000182(INpcScriptContext context) : base(context) {
        Id = 50;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000762$ 
                // - What? 
                return true;
            case 50:
                // $script:0831180407000767$ 
                // - Scram, I got work to do. 
                return true;
            default:
                return true;
        }
    }
}
