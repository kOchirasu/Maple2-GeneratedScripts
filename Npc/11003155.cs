using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003155: Rumi
/// </summary>
public class _11003155 : NpcScript {
    internal _11003155(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0306155707008043$ 
                // - Can I help you? 
                return true;
            case 30:
                // $script:0306155707008046$ 
                // - My sisters say I'm prettier than any flower. I agree. 
                return true;
            default:
                return true;
        }
    }
}
