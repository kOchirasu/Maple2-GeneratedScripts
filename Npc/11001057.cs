using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001057: Stark
/// </summary>
public class _11001057 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003608$
    // - Oh, no... 
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003611$
                // - I look older than $npcName:11001028[gender:0]$. Well, thanks, I guess.
                return 30;
            case (30, 1):
                // $script:0831180407003612$
                // - $npcName:11001028[gender:0]$ looks young because he's bald, but he's the same age I am. Maybe I should shave my head, too. 
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
