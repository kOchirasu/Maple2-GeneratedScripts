using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001495: Startz
/// </summary>
public class _11001495 : NpcScript {
    internal _11001495(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0118150907005816$ 
                // - Do you need more food?
                return true;
            case 30:
                // $script:0118150907005819$ 
                // - I've got a bad feeling... like something bad's about to happen.
                return true;
            default:
                return true;
        }
    }
}
