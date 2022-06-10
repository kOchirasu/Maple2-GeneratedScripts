using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004395: Marlene
/// </summary>
public class _11004395 : NpcScript {
    internal _11004395(INpcScriptContext context) : base(context) {
        // TODO: RandomPick 10;20
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0109181107012670$ 
                // - We stand for peace in Kritias.
                return true;
            case 10:
                // $script:0108212907012643$ 
                // - We stand for peace in Kritias.
                return true;
            case 20:
                // $script:0108212907012645$ 
                // - Captain $npcName:11004312[gender:1]$ told me she was sending reinforcements. I didn't realize she had meant you.
                // $script:0108212907012646$ 
                // - How are you? Things are going smoothly, I trust?
                switch (selection) {
                    // $script:0108212907012647$
                    // - Not exactly, but I'm getting by. There's a lot that needs doing these days.
                    case 0:
                        Id = 21;
                        return false;
                }
                return true;
            case 21:
                // $script:0108212907012648$ 
                // - Ah... Well, I'm afraid that my request isn't going to make things any easier...
                switch (selection) {
                    // $script:0108212907012649$
                    // - What is it?
                    case 0:
                        Id = 22;
                        return false;
                }
                return true;
            case 22:
                // $script:0108212907012650$ 
                // - There are resources nearby—resources Humanitas desperately needs. We'd been battling the Tairen for control of the area and making good ground, but then they received reinforcements from the capital...
                switch (selection) {
                    // $script:0108212907012651$
                    // - Were there many casualties?
                    case 0:
                        Id = 23;
                        return false;
                }
                return true;
            case 23:
                // $script:0108212907012652$ 
                // - We've only had some injuries, thank goodness. I'm more concerned about the ground we've lost; We need those supplies. Your mission is to secure $map:02020004$. Can I count on you?
                return true;
            default:
                return true;
        }
    }
}
