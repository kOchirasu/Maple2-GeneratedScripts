using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000169: Mark
/// </summary>
public class _11000169 : NpcScript {
    internal _11000169(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 50;70
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0831180407000700$ 
                // - What seems to be the problem?
                return true;
            case 50:
                // $script:0831180407000704$ 
                // - $MyPCName$, do I look timid to you?
                switch (selection) {
                    // $script:0831180407000705$
                    // - Maybe... a little?
                    case 0:
                        Id = 51;
                        return false;
                    // $script:0831180407000706$
                    // - Not at all.
                    case 1:
                        Id = 52;
                        return false;
                }
                return true;
            case 51:
                // $script:0831180407000707$ 
                // - I do, huh? Ahh, no wonder! Miss $npcName:11000160[gender:1]$ said she doesn't like timid men. What should I do?
                return true;
            case 52:
                // $script:0831180407000708$ 
                // - Are you sure? I do hope Miss $npcName:11000160[gender:1]$ thinks the same of me, $MyPCName$. If that's the case, I might actually have a shot.
                return true;
            case 70:
                // $script:0831180407000709$ 
                // - It's not easy to stand in one spot all day guarding the arsenal, but someone has to do it. I'm proud of my job, too.
                return true;
            default:
                return true;
        }
    }
}
