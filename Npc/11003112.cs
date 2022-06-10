using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003112: Sproutlanders Guild Leader
/// </summary>
public class _11003112 : NpcScript {
    internal _11003112(INpcScriptContext context) : base(context) {
        Id = 30;
    }

    public override bool Next(int selection = 0) {
        switch (Id) {
            case 0:
                // $script:0119135307007875$ 
                // - Everything's so green!
                return true;
            case 30:
                // $script:0119135307007878$ 
                // - Hello, and welcome to this gathering of the Sproutlanders guild. We come together to garden and tend to the wonderful greenery of Maple World.
                switch (selection) {
                    // $script:0119135307007879$
                    // - I totally want to join your guild!
                    case 0:
                        Id = 31;
                        return false;
                    // $script:0119135307007880$
                    // - Not really my scene, but thanks.
                    case 1:
                        Id = 32;
                        return false;
                }
                return true;
            case 31:
                // $script:0119135307007881$ 
                // - I'm so sorry, but my guild is already full. You could always form your own guild for loving and caring for the natural world. I think everyone would benefit!
                return true;
            case 32:
                // $script:0119135307007882$ 
                // - Oh, I see. Well, to each their own, right? Just try not to harm any trees in your journeys. Or flowers. Or grass.
                return true;
            default:
                return true;
        }
    }
}
