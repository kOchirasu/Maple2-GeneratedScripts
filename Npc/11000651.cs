using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000651: Prisoner 170123
/// </summary>
public class _11000651 : NpcScript {
    internal _11000651(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002670$ 
                // - When can I get out of here? 
                return true;
            case 40:
                // $script:0831180407002674$ 
                // - I'm busy. Scram! 
                switch (selection) {
                    // $script:0831180407002675$
                    // - What are you doing?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407002676$ 
                // - Are you blind? I'm working! I have to pull a million weeds to have my sentence reduced. Ugh, I'll grow old before I can pull that many weeds. 
                return true;
            case 50:
                // $script:1210061907004923$ 
                // - I'm busy. Scram! 
                switch (selection) {
                    // $script:1210061907004924$
                    // - Do you know someone named $npcName:11001231[gender:0]$?
                    case 0:
                        Id = 51;
                        return false;
                }
                return true;
            case 51:
                // $script:1210061907004925$ 
                // - You want to talk? Fine. But first, what's the password? 
                switch (selection) {
                    // $script:1214233907004997$
                    // - What's the password?
                    case 0:
                        Id = 52;
                        return false;
                }
                return true;
            case 52:
                // $script:1214233907004998$ 
                // - Haw! You don't know the password? Then we got nothing to talk about. 
                return true;
            default:
                return true;
        }
    }
}
