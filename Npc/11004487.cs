using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004487: Diversi
/// </summary>
public class _11004487 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012284$
    // - Ah, the hero of Sky Fortress! You have many fans, you know.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012285$
                // - Ah, the hero of Sky Fortress! You have many fans, you know.
                switch (selection) {
                    // $script:1227192907012286$
                    // - Stop. You're making me blush.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012287$
                // - Don't let it get to your head. You'll get sloppy.
                return 11;
            case (11, 1):
                // $script:1227192907012288$
                // - Anyway, this looks to be some kind of aetherine mine. There must be a huge deposit of the stuff under here.
                return 11;
            case (11, 2):
                // $script:1227192907012289$
                // - That would explain why there are so many enemy forces marshaled here. They want the aetherine.
                return 11;
            case (11, 3):
                // $script:1227192907012290$
                // - I think <i>we</i> ought to put our hat in the ring, so I sent a request for reinforcements. I'm trying to estimate the size of the aetherine deposit before they get here...
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.SelectableDistractor,
            (11, 0) => NpcTalkButton.Next,
            (11, 1) => NpcTalkButton.Next,
            (11, 2) => NpcTalkButton.Next,
            (11, 3) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
