using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000653: Prisoner 170125
/// </summary>
public class _11000653 : NpcScript {
    internal _11000653(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002684$ 
                // - When can I get out of here? 
                return true;
            case 40:
                // $script:0831180407002688$ 
                // - I'm busy. Scram! 
                switch (selection) {
                    // $script:0831180407002689$
                    // - What are you doing?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407002690$ 
                // - Can't you see? I'm working! If I were you, I would've stayed home napping instead of coming to see a horrible place like this. 
                return true;
            case 50:
                // $script:1210061907004929$ 
                // - I'm busy. Scram! 
                switch (selection) {
                    // $script:1210061907004930$
                    // - Do you know someone named $npcName:11001231[gender:0]$?
                    case 0:
                        Id = 51;
                        return false;
                }
                return true;
            case 51:
                // $script:1210061907004931$ 
                // - Keep your voice down. We're being watched. You're in the know? 
                switch (selection) {
                    // $script:1210061907004932$
                    // - Uh... Sure I am. $npcName:11001231[gender:0]$ sent me.
                    case 0:
                        Id = 52;
                        return false;
                }
                return true;
            case 52:
                // $script:1214232707004989$ 
                // - We call $npcName:11000651[gender:0]$ the supervisor. He's the one you oughtta be talking to, not me. But good luck getting a peep outta him without the password... 
                switch (selection) {
                    // $script:1214232707004990$
                    // - What's the password?
                    case 0:
                        Id = 53;
                        return false;
                }
                return true;
            case 53:
                // $script:1214232707004991$ 
                // - Haw! Like I'm gonna trust <i>you</i> with that info! If you don't even know the password, how can I trust you? Stoopid! 
                switch (selection) {
                    // $script:1214232707004992$
                    // - I'll be sure to mention you when I see $npcName:11001231[gender:0]$.
                    case 0:
                        Id = 54;
                        return false;
                }
                return true;
            case 54:
                // $script:1214232707004993$ 
                // - Bah! <b>Fine!</b> The password is... I forget. They change the dang thing every three days, y'know? 
                switch (selection) {
                    // $script:1214232707004994$
                    // - Do you remember any part of it?
                    case 0:
                        Id = 55;
                        return false;
                }
                return true;
            case 55:
                // $script:1214232707004995$ 
                // - How'd it go? Um... "Enlighten the light," I think. That's all I remember, honest! 
                // $script:1214232707004996$ 
                // - Now get outta here, before the warden notices we been talking. 
                return true;
            default:
                return true;
        }
    }
}
