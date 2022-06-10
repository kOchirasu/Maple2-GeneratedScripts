using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001052: Alicia
/// </summary>
public class _11001052 : NpcScript {
    internal _11001052(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407003592$ 
                // - Wah... I messed it up!
                return true;
            case 30:
                // $script:0831180407003595$ 
                // - No one can imagine how exciting time travel is without trying it.
                return true;
            default:
                return true;
        }
    }
}
