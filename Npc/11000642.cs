using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000642: Prisoner 150124
/// </summary>
public class _11000642 : NpcScript {
    internal _11000642(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002617$ 
                // - Did you call me? 
                return true;
            case 40:
                // $script:0831180407002621$ 
                // - I know all the guards, and you ain't one of them. 
                switch (selection) {
                    // $script:0831180407002622$
                    // - How did you end up in here?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407002623$ 
                // - I made a T-shirt with a sexy picture on it, so what? That's not a crime! 
                return true;
            case 50:
                // $script:1210061907004906$ 
                // - I know all the guards, and you ain't one of them. 
                switch (selection) {
                    // $script:1210061907004907$
                    // - Do you know someone named $npcName:11001231[gender:0]$?
                    case 0:
                        Id = 51;
                        return false;
                }
                return true;
            case 51:
                // $script:1210061907004908$ 
                // - What's it to you?
<font color="#909090">(He narrows his eyes at you.)</font> 
                switch (selection) {
                    // $script:1210061907004909$
                    // - I'm working with him.
                    case 0:
                        Id = 52;
                        return false;
                }
                return true;
            case 52:
                // $script:1210061907004910$ 
                // - Hm... Yeah, you don't look like no ordinary tourist. Tell him not to worry. Everything's right on schedule. 
                switch (selection) {
                    // $script:1210061907004911$
                    // - I need to see the supervisor.
                    case 0:
                        Id = 53;
                        return false;
                }
                return true;
            case 53:
                // $script:1210061907004912$ 
                // - Yeah, yeah, sure. That's $npcName:11000651[gender:0]$. But he won't talk to you unless you know the password. 
                switch (selection) {
                    // $script:1210061907004913$
                    // - What's the password?
                    case 0:
                        Id = 54;
                        return false;
                }
                return true;
            case 54:
                // $script:1210061907004914$ 
                // - Hold your horses. I wrote it down somewhere... 
                // $script:1210061907004915$ 
                // - Here we go. "Thick shadows have been cast..." ...something something... "...illuminate light..." Dang, who smudged up the password? 
                // $script:1210061907004916$ 
                // - Sorry, $male:buddy,female:lady$. You got to get the rest from someone else. 
                switch (selection) {
                    // $script:1214232607004979$
                    // - Why can't I just talk to the supervisor?
                    case 0:
                        Id = 55;
                        return false;
                }
                return true;
            case 55:
                // $script:1214232607004980$ 
                // - Listen, the supervisor won't even talk to <i>me</i> without the password. You don't stand a chance without it. 
                return true;
            default:
                return true;
        }
    }
}
