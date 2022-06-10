using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001032: Herman
/// </summary>
public class _11001032 : NpcScript {
    internal _11001032(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003529$ 
                // - This is bad, really bad! 
                return true;
            case 30:
                // $script:0831180407003532$ 
                // - I'm the head of this robot development center, and even I don't know how to get these robots under control. What should I do to contain this problem? 
                return true;
            default:
                return true;
        }
    }
}
