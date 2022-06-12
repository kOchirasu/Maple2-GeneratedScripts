using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11001021: Porte
/// </summary>
public class _11001021 : NpcScript {
    protected override int First() {
        return 30;
    }

    // Select 0:
    // $script:0831180407003468$
    // - Did the boss send you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (30, 0):
                // $script:0831180407003471$
                // - I don't have time for chitchat. I'm on a very important mission right now.
                return -1;
        }

        return default;
    }

    protected override NpcTalkButton Button() {
        return (Id, Index) switch {
            (30, 0) => NpcTalkButton.Close,
            _ => NpcTalkButton.None,
        };
    }
}
