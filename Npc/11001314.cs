using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001314: Temorro
/// </summary>
public class _11001314 : NpcScript {
    internal _11001314(INpcScriptContext context) : base(context) {
        Id = 40;
        // TODO: RandomPick 40
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:1215203907005033$ 
                // - I've answered plenty of your questions already.
                return true;
            case 40:
                // $script:1227194507005683$ 
                // - I'm sick of the constant questions! Even if I told them the answers, they wouldn't remember them, the dopes!
                switch (selection) {
                    // $script:1227194507005684$
                    // - It sounds like you don't actually know the answers.
                    case 0:
                        Id = 41;
                        return false;
                }
                return true;
            case 41:
                // $script:1227194507005685$ 
                // - Why you! It'll take more than that to shake their faith in me. Do I look like an easy mark to you?
                switch (selection) {
                    // $script:1227194507005686$
                    // - No.
                    case 0:
                        Id = 42;
                        return false;
                }
                return true;
            case 42:
                // $script:1227194507005687$ 
                // - Maybe you don't know how this works, but you're supposed to trade intel with me, not question my credibility. Well, forget you!
                return true;
            default:
                return true;
        }
    }
}
