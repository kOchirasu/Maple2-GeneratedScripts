using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11003112: Sproutlanders Guild Leader
/// </summary>
public class _11003112 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0119135307007875$
    // - Everything's so green!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0119135307007878$
                // - Hello, and welcome to this gathering of the Sproutlanders guild. We come together to garden and tend to the wonderful greenery of Maple World.
                switch (selection) {
                    // $script:0119135307007879$
                    // - I totally want to join your guild!
                    case 0:
                        return 31;
                    // $script:0119135307007880$
                    // - Not really my scene, but thanks.
                    case 1:
                        return 32;
                }
                return -1;
            case (31, 0):
                // $script:0119135307007881$
                // - I'm so sorry, but my guild is already full. You could always form your own guild for loving and caring for the natural world. I think everyone would benefit!
                return -1;
            case (32, 0):
                // $script:0119135307007882$
                // - Oh, I see. Well, to each their own, right? Just try not to harm any trees in your journeys. Or flowers. Or grass.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
