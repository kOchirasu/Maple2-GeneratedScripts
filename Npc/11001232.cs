using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001232: Eupheria
/// </summary>
public class _11001232 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1125194807004474$
    // - Even with the draft in effect, we still don't have enough soldiers.
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1125194807004477$
                // - $MyPCName$, if I'm not mistaken? You're that reckless student of $npc:11001244[gender:0]$'s I've heard so much about.
                switch (selection) {
                    // $script:1205185107004721$
                    // - Where did you hear that?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1205185107004722$
                // - You'll be hard-pressed to find a Runeblade within Terrun Calibre that hasn't heard of you. Though lately, your name has been cropping up more and more.
                switch (selection) {
                    // $script:1205185107004723$
                    // - What do you mean by that?
                    case 0:
                        return 32;
                }
                return -1;
            case (32, 0):
                // $script:1205185107004724$
                // - You don't know? Your teacher, $npc:11001246[gender:0]$, is one of the Eight Blades, the most magnificent warriors in all of Terrun Calibre. Learning from him is an honor, yet your approach to your studies have been a bit... unconventional. It's no wonder why there are many Runeblades who are jealous and resentful of you.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.SelectableDistractor,
            (32, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
