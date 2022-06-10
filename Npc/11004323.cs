using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004323: Eve
/// </summary>
public class _11004323 : NpcScript {
    internal _11004323(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1010140307011481$ 
                // - ...
                return true;
            case 10:
                // $script:1010140307011482$ 
                // - You...
                // $script:1010140307011483$ 
                // - What are you doing here? Have you come to try and convince me to go home too?
                switch (selection) {
                    // $script:1010140307011484$
                    // - Nothing like that.
                    case 0:
                        Id = 20;
                        return false;
                }
                return true;
            case 20:
                // $script:1010140307011485$ 
                // - ...Really?
                switch (selection) {
                    // $script:1010140307011486$
                    // - You don't look well. Are you feeling all right?
                    case 0:
                        Id = 30;
                        return false;
                }
                return true;
            case 30:
                // $script:1010140307011487$ 
                // - You're not the first person to say that.
                // $script:1010140307011488$ 
                // - Something $npcName:11000044[gender:0]$ said was bothering me. I came here hoping to find answers.
                // $script:1010140307011489$ 
                // - Somehow $npcName:11004324[gender:0]$ figured out where I was going and came after me.
                // $script:1010140307011490$ 
                // - All he's done since is nag, sigh.
                // $script:1010140307011491$ 
                // - I'm not going to let anyone stop me from finding out what $npcName:11000044[gender:0]$ told me was true.
                switch (selection) {
                    // $script:0111232407012691$
                    // - Good for you!
                    case 0:
                        Id = 31;
                        return false;
                }
                return true;
            case 31:
                // $script:0111232407012692$ 
                // - Thanks! I appreciate your support.
                return true;
            case 40:
                // $script:0109125407012657$ 
                // - Sigh...
                // $script:0109125407012658$ 
                // - $npcName:11004324[gender:0]$ is sweet, but sometimes I just need to be by myself.
                return true;
            default:
                return true;
        }
    }
}
