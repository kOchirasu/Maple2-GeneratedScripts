using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003282: Einos
/// </summary>
public class _11003282 : NpcScript {
    internal _11003282(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0404102807008249$ 
                // - How may I help you?
                return true;
            case 30:
                // $script:0404102807008250$ 
                // - We must uncover the secret of darkness before it claims any more lives.
                return true;
            default:
                return true;
        }
    }
}
