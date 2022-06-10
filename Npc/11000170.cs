using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000170: Leta
/// </summary>
public class _11000170 : NpcScript {
    internal _11000170(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 20;30;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000710$ 
                // - What seems to be the problem?
                return true;
            case 20:
                // $script:0831180407000712$ 
                // - $npcName:11000174[gender:1]$ and I grew up together in the same neighborhood. I started to notice my heart racing and my mood brightening whenever I thought about $npcName:11000174[gender:1]$. I've honestly never felt like this about anyone else before.
                return true;
            case 30:
                // $script:0831180407000713$ 
                // - $npcName:11000174[gender:1]$ and I grew up together in the same neighborhood. I started to notice my heart racing and my mood brightening whenever I thought about $npcName:11000174[gender:1]$. I've honestly never felt like this about anyone else before.
                return true;
            case 40:
                // $script:0317164707008110$ 
                // - How may I help you?
                switch (selection) {
                    // $script:0317164707008111$
                    // - Have you seen anyone in a mask go through here?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0317164707008112$ 
                // - I sure did! Hard not to notice someone that odd. He ran off toward the Kerning Interchange.
                return true;
            default:
                return true;
        }
    }
}
