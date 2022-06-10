using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000636: Prisoner 140919
/// </summary>
public class _11000636 : NpcScript {
    internal _11000636(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002589$ 
                // - I'm innocent!
                return true;
            case 40:
                // $script:0831180407002593$ 
                // - Another tourist? Come to see all the animals in their cages?
                switch (selection) {
                    // $script:0831180407002594$
                    // - How did you end up in here?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407002595$ 
                // - Argh, don't get me started. Why can't I change my own profile image to something I like? So what if the picture is a little bit... lewd?
                return true;
            case 50:
                // $script:1210061907004895$ 
                // - Another tourist? Come to see all the animals in their cages?
                switch (selection) {
                    // $script:1210061907004896$
                    // - Do you know someone named $npcName:11001231[gender:0]$?
                    case 0:
                        Id = 51;
                        return false;
                }
                return true;
            case 51:
                // $script:1210061907004897$ 
                // - ...You're one of <i>them</i>, aren't you?
                switch (selection) {
                    // $script:1210061907004898$
                    // - Uh... Sure I am. $npcName:11001231[gender:0]$ sent me.
                    case 0:
                        Id = 52;
                        return false;
                }
                return true;
            case 52:
                // $script:1210061907004899$ 
                // - Quiet, or the warden will hear you! You came to see how things are coming along, is that it?
                switch (selection) {
                    // $script:1210061907004900$
                    // - That's right.
                    case 0:
                        Id = 53;
                        return false;
                }
                return true;
            case 53:
                // $script:1210061907004901$ 
                // - Then talk to the supervisor. He's the one in charge here.
                switch (selection) {
                    // $script:1210061907004902$
                    // - Of course. And the supervisor is...?
                    case 0:
                        Id = 54;
                        return false;
                }
                return true;
            case 54:
                // $script:1210061907004903$ 
                // - $npcName:11000651[gender:0]$. You'll need the password, of course. We change it every three days to keep the guards off our trail.
                switch (selection) {
                    // $script:1210061907004904$
                    // - What's the latest password?
                    case 0:
                        Id = 55;
                        return false;
                }
                return true;
            case 55:
                // $script:1210061907004905$ 
                // - The latest password is... Shoot, what was it? Thick shadows... something. Ask one of the other guys.
                return true;
            default:
                return true;
        }
    }
}
