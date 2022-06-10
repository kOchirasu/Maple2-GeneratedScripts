using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001451: Tasamia
/// </summary>
public class _11001451 : NpcScript {
    internal _11001451(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1121222006000863$ 
                // - Can I help you? 
                return true;
            case 10:
                // $script:1121222006000864$ 
                // - Can I help you? 
                return true;
            default:
                return true;
        }
    }
}
