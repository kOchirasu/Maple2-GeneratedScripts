using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000077: Taru
/// </summary>
public class _11000077 : NpcScript {
    internal _11000077(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000362$ 
                // - What seems to be the problem?
                return true;
            case 30:
                // $script:0831180407000365$ 
                // - How are your journeys treating you? Deployments can be exciting, but I get homesick if I'm away for too long.
                return true;
            default:
                return true;
        }
    }
}
