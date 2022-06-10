using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004367: Mia
/// </summary>
public class _11004367 : NpcScript {
    internal _11004367(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1109213607011779$ 
                // - You know how hard I work, but even I need a break. 
                return true;
            case 10:
                // $script:1109213607011780$ 
                // - Working is intensely satisfying. And it also makes my rest hours that much sweeter. 
                // $script:1120173007011854$ 
                // - $MyPCName$, take care of yourself this season. Happy holidays! 
                return true;
            default:
                return true;
        }
    }
}
