using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000645: Prisoner 160918
/// </summary>
public class _11000645 : NpcScript {
    internal _11000645(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002633$ 
                // - Get me out of here...  
                return true;
            case 40:
                // $script:0831180407002637$ 
                // - I know all the guards, and you ain't one of them. 
                switch (selection) {
                    // $script:0831180407002638$
                    // - How did you end up in here?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407002639$ 
                // - I used some swear words for my character's name. That's how I want to express myself! Why should I care about other people's feelings? 
                switch (selection) {
                    // $script:0831180407002640$
                    // - You've got a problem in how you think.
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:0831180407002641$ 
                // - Shut up!  I don't need your lecturing! Go away! 
                return true;
            case 50:
                // $script:1210061907004917$ 
                // - I know all the guards, and you ain't one of them. 
                switch (selection) {
                    // $script:1210061907004918$
                    // - Do you know someone named $npcName:11001231[gender:0]$?
                    case 0:
                        Id = 51;
                        return false;
                }
                return true;
            case 51:
                // $script:1210061907004919$ 
                // - No, I don't. And I don't wanna. 
                return true;
            default:
                return true;
        }
    }
}
