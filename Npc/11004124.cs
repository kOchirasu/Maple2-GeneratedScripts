using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004124: Dark Wind Agent
/// </summary>
public class _11004124 : NpcScript {
    internal _11004124(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0720125407010491$ 
                // - The road to victory is paved with good intel.
                return true;
            case 10:
                // $script:0720125407010492$ 
                // - I've never seen anything so spooky.
                return true;
            default:
                return true;
        }
    }
}
