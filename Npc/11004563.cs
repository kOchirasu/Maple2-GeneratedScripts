using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004563: Allon
/// </summary>
public class _11004563 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0220211107014520$
    // - Hm?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0220211107014521$
                // - Hm?
                return 10;
            case (10, 1):
                // $script:0220211107014522$
                // - I had a feeling I'd see you here.
                switch (selection) {
                    // $script:0220211107014523$
                    // - I didn't think you were into this kind of thing.
                    case 0:
                        return 20;
                }
                return -1;
            case (20, 0):
                // $script:0220211107014524$
                // - Come now. I wouldn't pass up the chance to fight the hero of Tria.
                return 20;
            case (20, 1):
                // $script:0220211107014525$
                // - I look forward to our match.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (20, 0) => NpcTalkButton.Next,
            (20, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
