using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000599: Lenty
/// </summary>
public class _11000599 : NpcScript {
    internal _11000599(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002398$ 
                // - What is it?
                return true;
            case 30:
                // $script:0831180407002401$ 
                // - There are treasure chests hidden all over the world, and they're highly sought after by adventurers.
                return true;
            default:
                return true;
        }
    }
}
