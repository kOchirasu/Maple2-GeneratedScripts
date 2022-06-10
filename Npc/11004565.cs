using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004565: Ophelia
/// </summary>
public class _11004565 : NpcScript {
    internal _11004565(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0220211107014536$ 
                // - Hm.
                return true;
            case 10:
                // $script:0220211107014537$ 
                // - No offense, but I'm not here on business, okay? You're gonna have to find someone else to enchant your gear.
                switch (selection) {
                    // $script:0220211107014538$
                    // - Relax. I'm just here to say hi.
                    case 0:
                        Id = 20;
                        return false;
                }
                return true;
            case 20:
                // $script:0220211107014539$ 
                // - Huh? You mean... You're not just talking to me because I'm a genius blacksmith?
                switch (selection) {
                    // $script:0220211107014540$
                    // - There's more to you than that.
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 30:
                // $script:0220211107014541$ 
                // - L-like what?
                switch (selection) {
                    // $script:0220211107014542$
                    // - Well, for example, your... Never mind.
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:0220211107014543$ 
                // - I know you're trying to cheer me up, but I feel oddly insulted...
                return true;
            default:
                return true;
        }
    }
}
