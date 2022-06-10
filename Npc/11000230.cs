using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000230: Jacklin
/// </summary>
public class _11000230 : NpcScript {
    internal _11000230(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000803$ 
                // - What is it?
                return true;
            case 10:
                // $script:1121222006000804$ 
                // - Isn't there some kind of cure-all for my brother?
                return true;
            default:
                return true;
        }
    }
}
