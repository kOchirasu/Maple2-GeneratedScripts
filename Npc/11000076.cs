using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000076: Allon
/// </summary>
public class _11000076 : NpcScript {
    internal _11000076(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000354$ 
                // - How may I help you?
                return true;
            case 40:
                // $script:0831180407000358$ 
                // - I command the Royal Knights of Empress $npcName:11000075[gender:1]$. Our sacred duty is to keep her safe. 
                // $script:0831180407000359$ 
                // - But after that shadow gate to the Land of Darkness appeared, the empress sent us here to guard the border between worlds.
                // $script:0831180407000360$ 
                // - The minister is with the empress, but that doesn't reassure me much. I've been here for too long. I want this battle done and over with so I can go back to her.
                return true;
            case 50:
                // $script:0831180407000361$ 
                // - I lead the Lumiknights, the defenders of the empress, and yet I was completely oblivious of $npcName:11000044[gender:0]$'s true nature. It's disgraceful.
                return true;
            default:
                return true;
        }
    }
}
