using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004193: Landevian
/// </summary>
public class _11004193 : NpcScript {
    internal _11004193(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0813101707010954$ 
                // - What...?
                return true;
            case 10:
                // $script:0813101707010955$ 
                // - What happened? I'm having trouble remembering.
                return true;
            default:
                return true;
        }
    }
}
