using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000520: Poron
/// </summary>
public class _11000520 : NpcScript {
    internal _11000520(INpcScriptContext context) : base(context) {
        Id = 20;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002227$ 
                // - If you're not here for the job, please leave.
                return true;
            case 20:
                // $script:0831180407002229$ 
                // - Industrialization, urban development... I don't know who'll really benefit from all that.
                return true;
            default:
                return true;
        }
    }
}
