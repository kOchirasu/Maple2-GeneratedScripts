using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001302: Ereve
/// </summary>
public class _11001302 : NpcScript {
    internal _11001302(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1215203907005020$ 
                // - $MyPCName$, what brings you to me?
                return true;
            case 10:
                // $script:1215203907005021$ 
                // - $MyPCName$, please don't disappoint me. I know it's difficult, but keep up your efforts to save our world.
                return true;
            default:
                return true;
        }
    }
}
