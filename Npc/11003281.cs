using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003281: Asimov
/// </summary>
public class _11003281 : NpcScript {
    internal _11003281(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0404102807008247$ 
                // - How may I help you? 
                return true;
            case 30:
                // $script:0404102807008248$ 
                // - I've been waiting for you.  
                return true;
            default:
                return true;
        }
    }
}
