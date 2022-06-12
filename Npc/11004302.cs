using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004302: Ghost
/// </summary>
public class _11004302 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:1002141907011418$
    // - I'mma scratch <i>everything!</i>
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:1002141907011422$
                // - Now I'mma ghost, I can talk to people! How fun!
                return 30;
            case (30, 1):
                // $script:1002141907011423$
                // - 'Cause I'm inna good mood, I'mma tell you a secret! Watch the floors around here, or you're gonna fall!
                switch (selection) {
                    // $script:1002141907011424$
                    // - What's that supposed to mean?
                    case 0:
                        return 31;
                }
                return -1;
            case (31, 0):
                // $script:1002141907011425$
                // - Your foot's gonna fall! Watch the floors! Got it?
                return -1;
        }
        
        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Next,
            (30, 1) => NpcTalkButton.SelectableDistractor,
            (31, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
