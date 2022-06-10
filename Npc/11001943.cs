using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001943: Gichak
/// </summary>
public class _11001943 : NpcScript {
    internal _11001943(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1123165007007489$ 
                // - Can I help you?
                return true;
            case 10:
                // $script:1208184307007527$ 
                // - Lazy designers! These are the exact same clothes they had here yesterday. Where are the new designs?
                return true;
            default:
                return true;
        }
    }
}
