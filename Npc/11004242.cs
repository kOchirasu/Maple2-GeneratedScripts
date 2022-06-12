using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11004242: Eupheria
/// </summary>
public class _11004242 : NpcScript {
    protected override int First() {
        return 10;
    }

    // Select 0:
    // $script:0809223207010947$
    // - How can I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (10, 0):
                // $script:0809223207010948$
                // - I feel like I'm still in a dream.
                return 10;
            case (10, 1):
                // $script:0809223207010949$
                // - I'm so confused. My memories are all jumbled. I think I need some time.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (10, 0) => NpcTalkButton.Next,
            (10, 1) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
