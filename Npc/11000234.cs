using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000234: Cindy
/// </summary>
public class _11000234 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 20;30
    }

    // Select 0:
    // $script:0831180407000993$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407000995$
                // - Did you come from the rich neighborhood? What are you doing here?
                switch (selection) {
                    // $script:0831180407000996$
                    // - Do you know $npcName:11000064[gender:0]$?
                    case 0:
                        return 21;
                }
                return -1;
            case (21, 0):
                // $script:0831180407000997$
                // - $npcName:11000064[gender:0]$? Who's that? Is he famous?
                return -1;
            case (30, 0):
                // $script:0831180407000998$
                // - The people living in the rich neighborhood think we're smelly and dirty. But Mr. $npcName:11000006[gender:0]$ said they're smellier and dirtier on the inside for thinking that.
                return 30;
            case (30, 1):
                // $script:0831180407000999$
                // - Mr. $npcName:11000006[gender:0]$ said he'd change the world, so everyone could be equal and happy together.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.SelectableDistractor,
            (21, 0) => NpcTalkButton.Close,
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
