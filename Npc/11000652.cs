using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000652: Prisoner 170124
/// </summary>
public class _11000652 : NpcScript {
    internal _11000652(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002677$ 
                // - When can I get out of here? 
                return true;
            case 40:
                // $script:0831180407002681$ 
                // - Nine thousand nine hundred fifty-five... Nine thousand nine hundred fifty-six... 
                switch (selection) {
                    // $script:0831180407002682$
                    // - What are you doing?
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407002683$ 
                // - Are you blind? I'm working! I have to pull a million weeds to have my sentence reduced. Argh, and now you've made me lose count! 
                return true;
            case 50:
                // $script:1210061907004926$ 
                // - Nine thousand nine hundred fifty-five... Nine thousand nine hundred fifty-six... 
                switch (selection) {
                    // $script:1210061907004927$
                    // - Do you know someone named $npcName:11001231[gender:0]$?
                    case 0:
                        Id = 51;
                        return false;
                }
                return true;
            case 51:
                // $script:1210061907004928$ 
                // - ...Nine thousand nine hundred six... Drat! You made me lose count! 
                return true;
            default:
                return true;
        }
    }
}
