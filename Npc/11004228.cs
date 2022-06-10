using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004228: Dortov
/// </summary>
public class _11004228 : NpcScript {
    internal _11004228(INpcScriptContext context) : base(context) {
        Id = 10;
        // TODO: RandomPick 10
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0806222707010807$ 
                // - Hmm...
                return true;
            case 10:
                // $script:0806222707010808$ 
                // - I despise the noise and brutishness that permeates society. On this topic, it seems that I and this vision of elegance are of one mind.
                return true;
            default:
                return true;
        }
    }
}
