using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001084: Dodo
/// </summary>
public class _11001084 : NpcScript {
    internal _11001084(INpcScriptContext context) : base(context) {
        Id = 40;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1216233107005214$ 
                // - Ah! A human!
                return true;
            case 40:
                // $script:1216233107005218$ 
                // - We're not supposed to talk to strangers without the captain's approval.
                switch (selection) {
                    // $script:1216233107005219$
                    // - I'm not a stranger. I'm just a friend you haven't met.
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1216233107005220$ 
                // - I'm not falling for that. Shoo!
                return true;
            default:
                return true;
        }
    }
}
