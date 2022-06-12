using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000601: Luanna
/// </summary>
public class _11000601 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 30;40
    }

    // Select 0:
    // $script:0831180407002468$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407002473$
                // - The world is relying on your strength. May the empress's blessing be with you.
                return -1;
            case (40, 0):
                // $script:1215105907009721$
                // - Empress's blessings, $MyPCName$! What brings you here?
                switch (selection) {
                    // $script:1215105907009722$
                    // - I've heard a lot of rumors circulating through town.
                    case 0:
                        return 41;
                }
                return -1;
            case (41, 0):
                // $script:1215105907009723$
                // - Ah, yes, as have we. A dark aura begins to spread over Maple World once more.
                switch (selection) {
                    // $script:1215105907009724$
                    // - Tell me what you know.
                    case 0:
                        return 42;
                }
                return -1;
            case (42, 0):
                // $script:1215105907009725$
                // - I'm afraid I have no more information than anyone else. However... I sense that the strange occurrences of late are harbingers of a greater darkness. A threat unlike any we have faced.
                return 42;
            case (42, 1):
                // $script:1215105907009726$
                // - Please... be careful.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            (40, 0) => NpcTalkButton.SelectableDistractor,
            (41, 0) => NpcTalkButton.SelectableDistractor,
            (42, 0) => NpcTalkButton.Next,
            (42, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
