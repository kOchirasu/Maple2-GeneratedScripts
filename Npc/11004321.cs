using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004321: Tara
/// </summary>
public class _11004321 : NpcScript {
    internal _11004321(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;30
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1102172107011625$ 
                // - This won't do...
                return true;
            case 20:
                // $script:1010140307011458$ 
                // - This won't do...
                return true;
            case 10:
                // $script:1102172107011626$ 
                // - It's hard to get my bearings in a weird place like this.
                return true;
            case 30:
                // $script:1010140307011459$ 
                // - Huh?
                // $script:1010140307011460$ 
                // - Ah! It's you! How have you been?
                switch (selection) {
                    // $script:1010140307011461$
                    // - I'm doing pretty well, thanks.
                    case 0:
                        Id = 40;
                        return false;
                }
                return true;
            case 40:
                // $script:1010140307011462$ 
                // - That's good to hear. So what brings you here?
                switch (selection) {
                    // $script:1010140307011463$
                    // - I came here on an investigation.
                    case 0:
                        Id = 50;
                        return false;
                }
                return true;
            case 50:
                // $script:1010140307011464$ 
                // - I see, you too... Sigh.
                // $script:1010140307011465$ 
                // - We're here researching the dark dragons that Biset used to talk about.
                switch (selection) {
                    // $script:1010140307011466$
                    // - How did you get here?
                    case 0:
                        Id = 60;
                        return false;
                }
                return true;
            case 60:
                // $script:1010140307011467$ 
                // - $npcName:11004319[gender:1]$ brought us here with her dragon power. It seems she's come a long way.
                // $script:1010140307011468$ 
                // - So far this new land seems like an amazing place, but some of us are having a harder time adjusting than others. $npcName:11004320[gender:0]$'s not acting like himself. Do you think you could offer him some words of encouragement?
                switch (selection) {
                    // $script:1010140307011469$
                    // - I'll see what I can do.
                    case 0:
                        Id = 70;
                        return false;
                }
                return true;
            case 70:
                // $script:1010140307011470$ 
                // - Thanks! I'm counting on you!
                return true;
            default:
                return true;
        }
    }
}
