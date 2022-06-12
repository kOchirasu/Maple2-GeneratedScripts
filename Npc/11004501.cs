using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004501: Drill Sergeant
/// </summary>
public class _11004501 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:1227192907012407$
    // - You here to enlist? Fall in line, Recruit!
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:1227192907012408$
                // - You here to enlist? Fall in line, Recruit!
                switch (selection) {
                    // $script:1227192907012409$
                    // - I'm not your recruit.
                    case 0:
                        return 11;
                }
                return -1;
            case (11, 0):
                // $script:1227192907012410$
                // - Is that so? Hmph. You have the look of a washed-up loser. Join my troop and I'll have you back on your feet in no time!
                return 11;
            case (11, 1):
                // $script:1227192907012411$
                // - We need all the help we can get to fight Tairen. We'll even take folks wearing... whatever that's supposed to be. You sure you don't want to sign on with us?
                switch (selection) {
                    // $script:1227192907012412$
                    // - I'll think about it...
                    case 0:
                        return 12;
                }
                return -1;
            case (12, 0):
                // $script:1227192907012413$
                // - Whenever and wherever, we're ready!
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
