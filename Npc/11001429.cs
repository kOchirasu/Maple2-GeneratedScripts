using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001429: 
/// </summary>
public class _11001429 : NpcScript {
    internal _11001429(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0211204406000704$ 
                // - I've got everything you need. 
                return true;
            case 40:
                // $script:0809170706000907$ 
                // - Confused? 
                return true;
            default:
                return true;
        }
    }
}
