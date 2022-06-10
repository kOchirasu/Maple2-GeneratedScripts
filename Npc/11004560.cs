using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004560: Rovey
/// </summary>
public class _11004560 : NpcScript {
    internal _11004560(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0220211107014495$ 
                // - Hm. 
                return true;
            case 10:
                // $script:0220211107014496$ 
                // - And who might you be? 
                // $script:0220211107014497$ 
                // - I haven't seen you before, but you seem like a formidable opponent. 
                switch (selection) {
                    // $script:0220211107014498$
                    // - And you are?
                    case 0:
                        Id = 11;
                        return false;
                }
                return true;
            case 11:
                // $script:0220211107014499$ 
                // - Ahem! I am Rovey, drillmaster for the Royal Knights. 
                // $script:0220211107014500$ 
                // - I've trained many knights around your age. In fact, you remind me of one particular fool whom I once taught... 
                // $script:0220211107014501$ 
                // - Well, I shan't waste any more words on you. I will see you in the rumble. 
                return true;
            case 20:
                // $script:0220211107014502$ 
                // - !! 
                // $script:0220211107014503$ 
                // - You... 
                switch (selection) {
                    // $script:0220211107014504$
                    // - $npcName:11004560[gender:0]$?!
                    case 0:
                        Id = 21;
                        return false;
                }
                return true;
            case 21:
                // $script:0220211107014505$ 
                // - I'm surprised that foolish sense of justice hasn't gotten you killed. Why did you come here? 
                switch (selection) {
                    // $script:0220211107014506$
                    // - I'm here to fight.
                    case 0:
                        Id = 22;
                        return false;
                }
                return true;
            case 22:
                // $script:0220211107014507$ 
                // - It's been some time since we last sparred. I'm curious to see how you've grown. 
                return true;
            default:
                return true;
        }
    }
}
