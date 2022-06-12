using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000342: Nomm
/// </summary>
public class _11000342 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407001372$
    // - May I... help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407001374$
                // - I can't believe this is happening to me... 
                switch (selection) {
                    // $script:0831180407001375$
                    // - What is it?
                    case 0:
                        return 21;
                }
                return -1;
            case (21, 0):
                // $script:0831180407001376$
                // - For years, I saved as much money as I could so that I could one day build a house of my own. And the day my dream finally becomes a reality, a giant mushroom comes and chases me away!
                return 21;
            case (21, 1):
                // $script:0831180407001377$
                // - Curse that $npcName:22000321$... What does a mushroom need with a house, anyway?
                return 21;
            case (21, 2):
                // $script:0831180407001378$
                // - I paid for that house and the land under it, it belongs to me! This is completely unfair!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.Next,
            (21, 1) => NpcTalkButton.Next,
            (21, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
