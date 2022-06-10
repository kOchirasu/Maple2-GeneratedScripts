using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001390: Yul
/// </summary>
public class _11001390 : NpcScript {
    internal _11001390(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1217193307005390$ 
                // - Sigh... 
                return true;
            case 30:
                // $script:1223165107005568$ 
                // - My daughter, $npcName:11001396[gender:1]$, is always lost in thought. What could keep her so preoccupied all day long? 
                switch (selection) {
                    // $script:1226235907005589$
                    // - Tell me about her.
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:1223165107005569$ 
                // - She used to be such a clever girl. Even the people in $map:02010002$ heard about her genius. 
                // $script:1223165107005570$ 
                // - But instead of going out and making something of herself, she came back to this small town. I'm happy to have her here, but I can't help but feel that she's wasting her talent... 
                return true;
            default:
                return true;
        }
    }
}
