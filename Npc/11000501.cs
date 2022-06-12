using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000501: Balboa
/// </summary>
public class _11000501 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:0831180407002179$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:0831180407002181$
                // - As long as you know who you are and what you believe, what others think of you doesn't matter. That's the way we Boroboros live.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (20, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
