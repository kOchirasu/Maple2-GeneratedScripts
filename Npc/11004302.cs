using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004302: Ghost
/// </summary>
public class _11004302 : NpcScript {
    internal _11004302(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1002141907011418$ 
                // - I'mma scratch <i>everything!</i>
                return true;
            case 30:
                // $script:1002141907011422$ 
                // - Now I'mma ghost, I can talk to people! How fun!
                // $script:1002141907011423$ 
                // - 'Cause I'm inna good mood, I'mma tell you a secret! Watch the floors around here, or you're gonna fall!
                switch (selection) {
                    // $script:1002141907011424$
                    // - What's that supposed to mean?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1002141907011425$ 
                // - Your foot's gonna fall! Watch the floors! Got it?
                return true;
            default:
                return true;
        }
    }
}
