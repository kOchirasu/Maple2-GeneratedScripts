using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000850: Akarka
/// </summary>
public class _11000850 : NpcScript {
    internal _11000850(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003111$ 
                // - I can think. I can assess. 
                return true;
            case 30:
                // $script:0831180407003114$ 
                // - Robots are no longer tools. We are capable of much more than our creators. 
                return true;
            default:
                return true;
        }
    }
}
