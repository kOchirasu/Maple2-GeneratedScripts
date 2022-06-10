using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004492: Pantanal
/// </summary>
public class _11004492 : NpcScript {
    internal _11004492(INpcScriptContext context) : base(context) {
        Id = 10;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1227192907012337$ 
                // - Ah, $MyPCName$! I'm here researching the plants of Kritias.
                return true;
            case 10:
                // $script:1227192907012338$ 
                // - Ah, $MyPCName$! I'm here researching the plants of Kritias.
                switch (selection) {
                    // $script:1227192907012339$
                    // - What have you learned?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:1227192907012340$ 
                // - So much! All of the plants in Kritias have at least a little bit of aetherine in them.
                // $script:1227192907012341$ 
                // - And the plants react to each other's aetherine. It seems like they use the aetherine to communicate with each other!
                switch (selection) {
                    // $script:1227192907012342$
                    // - So what... talking plants?
                    case 0:
                        Id = 12;
                        return false;
                }
                return true;
            case 12:
                // $script:1227192907012343$ 
                // - Not precisely, but the idea of plants being able to communicate with each other isn't exactly new. The ecosystem in Kritias may be the most concrete evidence we've ever seen.
                // $script:1227192907012344$ 
                // - The plants are all giving off the same aetherine wavelength. It's almost as if they're singing a chorus!
                switch (selection) {
                    // $script:0114164007012721$
                    // - Incredible!
                    case 0:
                        Id = 13;
                        return false;
                }
                return true;
            case 13:
                // $script:0114164007012722$ 
                // - Astonishing, too!
                return true;
            default:
                return true;
        }
    }
}
