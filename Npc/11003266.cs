using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003266: Eks
/// </summary>
public class _11003266 : NpcScript {
    internal _11003266(INpcScriptContext context) : base(context) {
        Id = 30;
        // TODO: RandomPick 30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008212$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0403155707008213$ 
                // - My head is throbbing. Shoulder, knees, and toes, too. Mark my words, there's a storm brewing. 
                return true;
            default:
                return true;
        }
    }
}
