using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001453: Turazi
/// </summary>
public class _11001453 : NpcScript {
    internal _11001453(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000869$ 
                // - What is it?
                return true;
            case 10:
                // $script:1121222006000870$ 
                // - What is it?
                return true;
            default:
                return true;
        }
    }
}
