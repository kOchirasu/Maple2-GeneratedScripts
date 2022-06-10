using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004075: Chee the Caterpillar
/// </summary>
public class _11004075 : NpcScript {
    internal _11004075(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0619202207010200$ 
                // - Uh... Um...
                return true;
            case 10:
                // $script:0619202207010201$ 
                // - Uh... Um...
                // $script:0619202207010202$ 
                // - Okay, I'm just gonna do it. I'm going to ask. Hey, human! Tell me something...
                switch (selection) {
                    // $script:0619202207010203$
                    // - Know what?
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0619202207010204$ 
                // - What am I? I mean, what do you think I'm gonna be when I grow up?
                switch (selection) {
                    // $script:0619202207010205$
                    // - What do you mean?
                    case 0:
                        Id = 32;
                        return false;
                }
                return true;
            case 32:
                // $script:0619202207010206$ 
                // - Am I gonna be a moth? A butterfly? Maybe a beetle?
                switch (selection) {
                    // $script:0619202207010207$
                    // - You're a beetle, for sure.
                    case 0:
                        Id = 40;
                        return false;
                    // $script:0619202207010208$
                    // - Oh, you're definitely a moth.
                    case 1:
                        Id = 41;
                        return false;
                    // $script:0619202207010209$
                    // - Hmm. Maybe a butterfly?
                    case 2:
                        Id = 42;
                        return false;
                }
                return true;
            case 40:
                // $script:0619202207010210$ 
                // - R-really? I guess beetles are pretty cool...
                return true;
            case 41:
                // $script:0619202207010211$ 
                // - Wow... A moth? So the butterflies were telling the truth... I might as well just end it now. Sniff...
                return true;
            case 42:
                // $script:0619202207010212$ 
                // - That's a relief! The butterflies said I was a moth, but I want to become a beautiful butterfly!
                return true;
            default:
                return true;
        }
    }
}
