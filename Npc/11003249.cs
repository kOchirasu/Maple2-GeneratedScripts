using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003249: Einos
/// </summary>
public class _11003249 : NpcScript {
    internal _11003249(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0403155707008165$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0403155707008166$ 
                // - We must uncover the secret of darkness before it claims any more lives.
                return true;
            default:
                return true;
        }
    }
}
