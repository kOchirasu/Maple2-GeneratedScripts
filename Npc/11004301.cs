using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004301: Ghost
/// </summary>
public class _11004301 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1002141907011409$
    // - Ooh la la!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1002141907011412$
                // - Beautiful. Stunning. A gift from the goddess!
                switch (selection) {
                    // $script:1002141907011413$
                    // - What are you going on about?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1002141907011414$
                // - I can't get the woman in purple out of my head! I love a woman with pep.
                switch (selection) {
                    // $script:1002141907011415$
                    // - You mean $npc:11004289[gender:1]$?
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:1002141907011416$
                // - That's the one! You'd be head-over-heels if you saw her, too. So lithe. And those executive management skills? Ooh la la!
                return 32;
            case (32, 1):
                // $script:1002141907011417$
                // - The other ghosts say she's mean, but I think she's better than the empress herself! A woman like that makes a guy wish he'd died young, so he'd have a handsomer ghost.
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Next,
            (32, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
