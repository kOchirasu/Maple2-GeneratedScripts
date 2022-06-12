using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004483: Cabomba
/// </summary>
public class _11004483 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012249$
    // - Hello! I'll be helping you explore Kritias. Nice to meet you.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012250$
                // - Hello! I'll be helping you explore Kritias. Nice to meet you.
                switch (selection) {
                    // $script:1227192907012251$
                    // - When do you start?
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012252$
                // - St-st-st-start? Soon! Really soon! Yeah...
                return 11;
            case (11, 1):
                // $script:1227192907012253$
                // - There's lots and lots of preparation to do. So that's what I'm doing... Preparing! Yep. Gotta prepare before you can go out into the wilderness...
                switch (selection) {
                    // $script:1227192907012254$
                    // - It's okay to be scared.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1227192907012255$
                // - I'm not scared! I'm c-cautious, okay? This is an important j-j-j-job. I'm <i>definitely</i> not stalling!
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
