using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001143: Valgor
/// </summary>
public class _11001143 : NpcScript {
    internal _11001143(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0915171007003945$ 
                // - Hello!
                return true;
            case 30:
                // $script:0915171007003948$ 
                // - Plenty of archaeologists would kill for the chance to see Ellin Ruins with their own eyes. Are you here to see the ruins yourself?
                switch (selection) {
                    // $script:0915171007003949$
                    // - I'm not that interested in this old junk.
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0915171007003950$
                    // - Oh yeah, I'm super into this stuff.
                    case 1:
                        Id = 32;
                        return false;
                    // $script:0915171007003951$
                    // - Not really. I was just wandering aimlessly.
                    case 2:
                        Id = 33;
                        return false;
                }
                return true;
            case 31:
                // $script:0915171007003952$ 
                // - Really? Not interested in all this history? Oh... Then maybe you've come to hunt monsters? Just look around, this place is teeming with them.
                return true;
            case 32:
                // $script:0915171007003953$ 
                // - Really? You don't look like an archaeologist. Well, it's just nice to see someone interested in history. Stay as long as you like!
                return true;
            case 33:
                // $script:0915171007003954$ 
                // - Ah! A classic case of wanderlust, have we? Well, regardless, please be careful not to damage the ruins... And also, try not to get horribly mauled by monsters.
                return true;
            default:
                return true;
        }
    }
}
