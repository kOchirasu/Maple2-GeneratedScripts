using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004488: Oranda
/// </summary>
public class _11004488 : NpcScript {
    protected override int First() {
        // TODO: RandomPick 10;12
    }

    // Select 0:
    // $script:1227192907012293$
    // - I'm so glad your here! I needed to share this with someone.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012294$
                // - I'm so glad your here! I needed to share this with someone.
                switch (selection) {
                    // $script:1227192907012295$
                    // - Oh? What is it?
                    case 0:
                        return 11;
                }
                return 10;
            case (10, 1):
                // $script:1227192907012296$
                // - Look at that structure up ahead. Really <i>look</i> at it. You can use my telescope if you like.
                switch (selection) {
                    // $script:1227192907012297$
                    // - Yeah, that's... um... something.
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1227192907012298$
                // - The whole thing is made of some kind of porous material, and it's soaked in aetherine like a sponge!
                return 12;
            case (12, 1):
                // $script:1227192907012299$
                // - The cylinder at the center looks like it draws aetherine directly from the ground. I think. I'm not exactly sure how it works...
                return 12;
            case (12, 2):
                // $script:1227192907012300$
                // - I think this terminal is connected somehow. I haven't managed to get it to do anything yet, though.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (10, 1) => NpcTalkButton.SelectableDistractor,
            (12, 0) => NpcTalkButton.Next,
            (12, 1) => NpcTalkButton.Next,
            (12, 2) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
