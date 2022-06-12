using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004134: Ishura
/// </summary>
public class _11004134 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;100
    }

    // Select 0:
    // $script:0730132107010529$
    // - ...
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0730132107010530$
                // - Huh?
                return -1;
            case (100, 0):
                // $script:0730132107010531$
                // - Huh?
                switch (selection) {
                    // $script:0730132107010532$
                    // - I was worried about you. Let's get out of here.
                    case 0:
                        return 101;
                }
                return -1;
            case (101, 0):
                // $script:0730132107010533$
                // - Nonsense.
                return 101;
            case (101, 1):
                // $script:0730132107010534$
                // - There's nothing more to talk about.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Close,
            (100, 0) => NpcTalkButton.SelectableDistractor,
            (101, 0) => NpcTalkButton.Next,
            (101, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
