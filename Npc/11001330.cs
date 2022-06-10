using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001330: Mr. Arthur
/// </summary>
public class _11001330 : NpcScript {
    internal _11001330(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217012607005239$ 
                // - It's getting late already.
                return true;
            case 40:
                // $script:1217012607005243$ 
                // - She's been shopping all day. You'd think all that running around would be decent exercise...
                return true;
            default:
                return true;
        }
    }
}
