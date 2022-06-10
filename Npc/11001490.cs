using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001490: Ereve
/// </summary>
public class _11001490 : NpcScript {
    internal _11001490(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0114152507005802$ 
                // - $MyPCName$, what brings you to me? 
                return true;
            case 20:
                // $script:0114152507005804$ 
                // - It was no small task to recover the power of light. I pray it will never be overshadowed by darkness. 
                return true;
            default:
                return true;
        }
    }
}
