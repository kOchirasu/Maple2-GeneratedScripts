using Maple2.Model.Enum;
using Maple2.Script.Npc;

/// <summary>
/// 11000305: Broh
/// </summary>
public class _11000305 : NpcScript {
    protected override int First() {
        return 20;
    }

    // Select 0:
    // $script:1121222006000817$
    // - How may I help you?
    protected override int Select() => 0;

    protected override int Execute(int selection) {
        switch (Id, Index++) {
            case (20, 0):
                // $script:1121222006000818$
                // - Pretty homes are nice to live in.
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
