using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000634: Prisoner 140917
/// </summary>
public class _11000634 : NpcScript {
    internal _11000634(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 40;50
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407002575$ 
                // - Get me out of here...  
                return true;
            case 40:
                // $script:0831180407002579$ 
                // - Get me out of here, would ya? I've got a stash on the outside. A million mesos for my freedom. What'cha say? 
                switch (selection) {
                    // $script:0831180407002580$
                    // - No way, you're in for fraud! That's the worst!
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:0831180407002581$ 
                // - Bah, how did you know I'm in here for fraud? Did the warden tell you? If you're not going to get me out of here, then scram! 
                return true;
            case 50:
                // $script:1210061907004888$ 
                // - Get me out of here, would ya? I've got a stash on the outside. A million mesos for my freedom. What'cha say? 
                switch (selection) {
                    // $script:1210061907004889$
                    // - Do you know someone named $npcName:11001231[gender:0]$?
                    case 0:
                        Id = 51;
                        return false;
                }
                return true;
            case 51:
                // $script:1210061907004890$ 
                // - Sure I do, sure! Just help me break out, and I'll tell you all about it. 
                switch (selection) {
                    // $script:1210061907004891$
                    // - What does she look like?
                    case 0:
                        Id = 52;
                        return false;
                }
                return true;
            case 52:
                // $script:1210061907004892$ 
                // - She's got... hair. A real smart-looking gal. And really pretty, too. 
                switch (selection) {
                    // $script:1210061907004893$
                    // - $npcName:11001231[gender:0]$ is a man.
                    case 0:
                        Id = 53;
                        return false;
                }
                return true;
            case 53:
                // $script:1210061907004894$ 
                // - You were testing me? Get outta here, you rat! If you ain't gonna help me, just leave me alone! 
                return true;
            default:
                return true;
        }
    }
}
