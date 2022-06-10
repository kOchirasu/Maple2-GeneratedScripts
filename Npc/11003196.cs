using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003196: Katvan
/// </summary>
public class _11003196 : NpcScript {
    internal _11003196(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0404083307008224$ 
                // - $npcName:11003216[gender:0]$... That fool! 
                return true;
            case 10:
                // $script:0404083307008225$ 
                // - I won't give up until $npcName:11003216[gender:0]$ pays for his crimes. I just wish $npcName:11000069[gender:1]$ would understand that I'm doing this for her... 
                return true;
            case 20:
                // $script:0516084007008486$ 
                // - I told you! As long as $npcName:11003216[gender:0]$ is alive, $npcName:11000069[gender:1]$ isn't safe. 
                return true;
            default:
                return true;
        }
    }
}
